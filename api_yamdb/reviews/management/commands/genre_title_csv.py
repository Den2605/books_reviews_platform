import csv

from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404

from reviews.models import Genre, Title


class Command(BaseCommand):
    help = "import data from titles.csv"

    def handle(self, *args, **kwargs):
        with open("static/data/genre_title.csv", encoding="utf8") as f:
            dr = csv.DictReader(f, delimiter=",")
            for row in dr:
                title = get_object_or_404(Title, id=row["title_id"])
                genre = get_object_or_404(Genre, id=row["genre_id"])
                title.save()
                title.genre.add(genre)
