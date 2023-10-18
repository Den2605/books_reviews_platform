import csv

from django.core.management.base import BaseCommand

from users.models import CustomUser as User


class Command(BaseCommand):
    help = "import data from titles.csv"

    def handle(self, *args, **kwargs):
        with open("static/data/users.csv", encoding="utf8") as f:
            dr = csv.DictReader(f, delimiter=",")
            for row in dr:
                obj = User(
                    id=row["id"],
                    username=row["username"],
                    email=row["email"],
                    role=row["role"],
                    bio=row["bio"],
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                )
                obj.save()
