import csv

from django.core.management.base import BaseCommand

from reviews.models import Category


class Command(BaseCommand):
    help = "import data from category.csv"

    def handle(self, *args, **kwargs):
        with open("static/data/category.csv", encoding="utf8") as f:
            dr = csv.DictReader(f, delimiter=",")
            for row in dr:
                obj = Category(
                    id=row["id"],
                    name=row["name"],
                    slug=row["slug"],
                )
                obj.save()
