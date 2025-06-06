# Copied from https://github.com/fusionbox/django-betterforms/blob/master/betterforms/multiform.py
#
# From https://github.com/fusionbox/django-betterforms/blob/master/LICENSE
#
# Copyright (c) 2013, Fusionbox, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# - Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# - Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
from __future__ import annotations

from collections import OrderedDict
from functools import reduce
from itertools import chain
from operator import add

from django.core.exceptions import NON_FIELD_ERRORS
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe


class MultiForm:
    """A container that allows you to treat multiple forms as one form.  This is
    great for using more than one form on a page that share the same submit
    button.  MultiForm imitates the Form API so that it is invisible to anybody
    else that you are using a MultiForm.
    """

    form_classes = {}

    def __init__(self, data=None, files=None, *args, **kwargs) -> None:
        # Some things, such as the WizardView expect these to exist.
        self.data, self.files = data, files
        kwargs.update(
            data=data,
            files=files,
        )

        self.initials = kwargs.pop("initial", None)
        if self.initials is None:
            self.initials = {}
        self.forms = OrderedDict()
        self.crossform_errors = []

        for key, form_class in self.form_classes.items():
            fargs, fkwargs = self.get_form_args_kwargs(key, args, kwargs)
            self.forms[key] = form_class(*fargs, **fkwargs)

    def get_form_args_kwargs(self, key, args, kwargs):
        """Returns the args and kwargs for initializing one of our form children."""
        fkwargs = kwargs.copy()
        prefix = kwargs.get("prefix")
        prefix = key if prefix is None else f"{key}__{prefix}"
        fkwargs.update(
            initial=self.initials.get(key),
            prefix=prefix,
        )
        return args, fkwargs

    def __str__(self) -> str:
        return self.as_table()

    def __getitem__(self, key):
        return self.forms[key]

    @property
    def errors(self):
        errors = {}
        for form_name in self.forms:
            form = self.forms[form_name]
            for field_name in form.errors:
                errors[form.add_prefix(field_name)] = form.errors[field_name]
        if self.crossform_errors:
            errors[NON_FIELD_ERRORS] = self.crossform_errors
        return errors

    @property
    def fields(self):
        fields = []
        for form_name in self.forms:
            form = self.forms[form_name]
            for field_name in form.fields:
                fields += [form.add_prefix(field_name)]
        return fields

    def __iter__(self):
        # TODO: Should the order of the fields be controllable from here?
        return chain.from_iterable(self.forms.values())

    @property
    def is_bound(self):
        return any(form.is_bound for form in self.forms.values())

    def clean(self):
        """Raises any ValidationErrors required for cross form validation. Should
        return a dict of cleaned_data objects for any forms whose data should
        be overridden.
        """
        return self.cleaned_data

    def add_crossform_error(self, e) -> None:
        self.crossform_errors.append(e)

    def is_valid(self):
        forms_valid = all(form.is_valid() for form in self.forms.values())
        try:
            self.cleaned_data = self.clean()
        except ValidationError as e:
            self.add_crossform_error(e)
        return forms_valid and not self.crossform_errors

    def non_field_errors(self):
        form_errors = (form.non_field_errors() for form in self.forms.values() if hasattr(form, "non_field_errors"))
        return ErrorList(chain(self.crossform_errors, *form_errors))

    def as_table(self):
        return mark_safe("".join(form.as_table() for form in self.forms.values()))

    def as_ul(self):
        return mark_safe("".join(form.as_ul() for form in self.forms.values()))

    def as_p(self):
        return mark_safe("".join(form.as_p() for form in self.forms.values()))

    def is_multipart(self):
        return any(form.is_multipart() for form in self.forms.values())

    @property
    def media(self):
        return reduce(add, (form.media for form in self.forms.values()))

    def hidden_fields(self):
        # copy implementation instead of delegating in case we ever
        # want to override the field ordering.
        return [field for field in self if field.is_hidden]

    def visible_fields(self):
        return [field for field in self if not field.is_hidden]

    @property
    def cleaned_data(self):
        return OrderedDict((key, form.cleaned_data) for key, form in self.forms.items() if form.is_valid())

    @cleaned_data.setter
    def cleaned_data(self, data) -> None:
        for key, value in data.items():
            child_form = self[key]
            if hasattr(child_form, "forms"):
                for formlet, formlet_data in zip(child_form.forms, value, strict=False):
                    formlet.cleaned_data = formlet_data
            else:
                child_form.cleaned_data = value


class MultiModelForm(MultiForm):
    """MultiModelForm adds ModelForm support on top of MultiForm.  That simply
    means that it includes support for the instance parameter in initialization
    and adds a save method.
    """

    def __init__(self, *args, **kwargs) -> None:
        self.instances = kwargs.pop("instance", None)
        if self.instances is None:
            self.instances = {}
        super().__init__(*args, **kwargs)

    def get_form_args_kwargs(self, key, args, kwargs):
        fargs, fkwargs = super().get_form_args_kwargs(
            key,
            args,
            kwargs,
        )
        try:
            # If we only pass instance when there was one specified, we make it
            # possible to use non-ModelForms together with ModelForms.
            fkwargs["instance"] = self.instances[key]
        except KeyError:
            pass
        return fargs, fkwargs

    def save(self, commit=True):
        objects = OrderedDict((key, form.save(commit)) for key, form in self.forms.items())

        if any(hasattr(form, "save_m2m") for form in self.forms.values()):

            def save_m2m() -> None:
                for form in self.forms.values():
                    if hasattr(form, "save_m2m"):
                        form.save_m2m()

            self.save_m2m = save_m2m

        return objects
