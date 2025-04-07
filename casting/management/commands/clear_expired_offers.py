from django.core.management.base import BaseCommand
from django.utils import timezone
from casting.models import CastingOffer

class Command(BaseCommand):
    help = 'Usuwa oferty, których termin (offer_date) już minął.'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        expired_offers = CastingOffer.objects.filter(offer_date__lt=today)
        count = expired_offers.count()
        expired_offers.delete()
        self.stdout.write(self.style.SUCCESS(f'Usunięto {count} ofert, których termin minął.'))