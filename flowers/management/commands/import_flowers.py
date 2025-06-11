import csv
from django.core.management.base import BaseCommand
from flowers.models import Flower, Category

class Command(BaseCommand):
    help = 'Importuje kwiaty z pliku CSV'

    def handle(self, *args, **kwargs):
        with open('kwiaty.csv', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name'].strip()
                meaning = row['meaning'].strip()
                category_names = [cat.strip() for cat in row['categories'].split(';')]

                flower = Flower.objects.create(name=name, meaning=meaning)

                for cat_name in category_names:
                    category, _ = Category.objects.get_or_create(name=cat_name)
                    flower.categories.add(category)

                self.stdout.write(self.style.SUCCESS(f'Dodano kwiat: {name}'))