from django.test import TestCase
from django.contrib import admin

from .admin import HitterAdmin
from .models import Hitter

class HittersTest(TestCase):
  def test_hitter_modal_shold_have_email_field(self):
    hitter = Hitter.objects.create(
      email='shine@prontomarketing.com'
    )
    self.assertEqual(hitter.email, 'shine@prontomarketing.com')

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
