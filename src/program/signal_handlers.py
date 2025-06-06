from __future__ import annotations

import logging

from django.core.exceptions import ValidationError

logger = logging.getLogger(f"bornhack.{__name__}")


def check_speaker_event_camp_consistency(sender, instance, **kwargs) -> None:
    if kwargs["action"] == "pre_add":
        from program.models import Event
        from program.models import Speaker

        if isinstance(instance, Event):
            # loop over speakers being added to this event
            for pk in kwargs["pk_set"]:
                # check if this speaker belongs to a different Camp than the event does
                speaker = Speaker.objects.get(id=pk)
                if speaker.camp != instance.camp:
                    raise ValidationError(
                        {
                            "speakers": f"The speaker ({speaker}) belongs to a different camp ({speaker.camp}) than the event does ({instance.camp})",
                        },
                    )
        elif isinstance(instance, Speaker):
            # loop over events being added to this speaker
            for pk in kwargs["pk_set"]:
                # check if this event belongs to a different Camp than the speaker does
                event = Event.objects.get(id=pk)
                if event.camp != instance.camp:
                    raise ValidationError(
                        {
                            "events": f"The event ({event}) belongs to a different camp ({event.camp}) than the speaker does ({instance.camp})",
                        },
                    )


def event_session_post_save(sender, instance, created, **kwargs) -> None:
    """Make sure we have the number of EventSlots we need to have, adjust if not."""
    instance.fixup_event_slots()
