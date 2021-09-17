from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from core.models import Category, Currency


class Command(BaseCommand):
    help = "Fill some test currencies and transactions"

    def add_arguments(self, parser):
        parser.add_argument(
            "user", type=str,
            help="The username of the owner of the transaction"
        )

    def _fill_currencies(self):
        currencies = [
            Currency(
                code="",
                name="",
            ),
            Currency(
                code="",
                name="",
            ),
            Currency(
                code="",
                name="",
            ),
            Currency(
                code="",
                name="",
            ),
            Currency(
                code="",
                name="",
            ),
        ]
        try:
            Currency.objects.bulk_create(currencies)
        except Exception as ex:
            self.stdout.write(self.style.ERROR(f"An error has occurred: {ex}"))
        else:
            self.stdout.write(self.style.SUCCESS(
                f"Successfully created {len(currencies)} currencies"
            ))

    def _fill_categories(self, user):
        categories = [
            Category(
                user=user,
                name="",
            ),
            Category(
                user=user,
                name="",
            ),
            Category(
                user=user,
                name="",
            ),
            Category(
                user=user,
                name="",
            ),
            Category(
                user=user,
                name="",
            ),
        ]
        try:
            Category.objects.bulk_create(categories)
        except Exception as ex:
            self.stdout.write(self.style.ERROR(f"An error has occurred: {ex}"))
        else:
            self.stdout.write(self.style.SUCCESS(
                f"Successfully created {len(categories)} categories"
            ))

    def handle(self, *args, **kwargs):
        try:
            user = User.objects.filter(username=kwargs.get("user")).first()
            self._fill_currencies()
            self._fill_categories(user=user)
        except Exception as ex:
            self.stdout.write(self.style.ERROR(f"An error has occurred: {ex}"))
