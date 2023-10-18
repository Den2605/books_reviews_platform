import csv

from django.core.management.base import BaseCommand

from reviews.models import Genre


class Command(BaseCommand):
    help = "import data from genre.csv"

    def handle(self, *args, **kwargs):
        with open("static/data/genre.csv", encoding="utf8") as f:
            dr = csv.DictReader(f, delimiter=",")
            for row in dr:
                obj = Genre(
                    id=row["id"],
                    name=row["name"],
                    slug=row["slug"],
                )
                obj.save()
