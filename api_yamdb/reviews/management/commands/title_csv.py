import csv

from django.core.management.base import BaseCommand

from reviews.models import Category, Title


class Command(BaseCommand):
    help = "import data from titles.csv"

    def handle(self, *args, **kwargs):
        with open("static/data/titles.csv", encoding="utf8") as f:
            dr = csv.DictReader(f, delimiter=",")
            for row in dr:
                obj = Title(
                    id=row["id"],
                    name=row["name"],
                    year=row["year"],
                    category=Category(pk=row["category"]),
                )
                obj.save()
