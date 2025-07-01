from __future__ import annotations

import datetime

from django.test import TestCase
from django.urls import reverse

from tickets.models import PrizeTicket, ShopTicket, SponsorTicket
from utils.tests import BornhackTestBase


class CampMenuTest(TestCase):
    def test_this_year_shown_on_homepage(self):
        """By March, the current year's camp should be on the homepage."""
        response = self.client.get(
            "/news/",
        )  # The tests don't work with / because of the camp dispatcher.
        year = (datetime.date.today() - datetime.timedelta(days=59)).year
        href = reverse("camp_detail", kwargs={"camp_slug": f"bornhack-{year}"})
        assert href in response.content.decode("utf-8")


class TestCampModel(BornhackTestBase):
    """Tests for the Camp model"""

    def test_todays_checked_in_adults(self) -> None:
        """Test the return value of todays checked in adults"""
        print(ShopTicket.objects.filter(ticket_type__camp=self.camp))
        print(SponsorTicket.objects.filter(ticket_type__camp=self.camp))
        print(PrizeTicket.objects.filter(ticket_type__camp=self.camp))
        assert self.camp.checked_in_full_week_adults == 1

