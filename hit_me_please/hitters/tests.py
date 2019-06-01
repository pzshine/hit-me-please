from django.test import TestCase
from .models import Hitter
class HittersTest(TestCase):
  def test_hitter_modal_shold_have_email_field(self):
    hitter = Hitter.objects.create(
      email='shine@prontomarketing.com'
    )
    self.assertEqual(hitter.email, 'shine@prontomarketing.com')

# Create your tests here.
