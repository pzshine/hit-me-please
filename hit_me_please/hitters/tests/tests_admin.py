from django.test import TestCase
from django.contrib import admin

from ..admin import HitterAdmin
from ..models import Hitter

class HittersAdminTest(TestCase):
  def test_hitter_should_be_registed_to_admin(self):
    self.assertIsInstance(
      admin.site._registry[Hitter],
      HitterAdmin
    )

  def test_hitter_admin_should_set_list_display(self):
    expected = (
      'email',
    )
    self.assertEqual(HitterAdmin.list_display, expected)


# Create your tests here.
