import random
from decimal import Decimal

from django.utils import timezone
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from core.models import Category, Currency, Transaction


class Command(BaseCommand):
    help = "Generates a given number of transactions"

    def add_arguments(self, parser):
        parser.add_argument(
            "total", type=int,
            help="Indicates the number of transactions to be created"
        )
        parser.add_argument(
            "user", type=str,
            help="The username of the owner of the transaction"
        )

    def handle(self, *args, **kwargs):
        total = kwargs.get("total", 0)
        user = User.objects.filter(username=kwargs.get("user")).first()
        currencies = list(Currency.objects.all())
        categories = list(Category.objects.all())
        txs = []

        try:
            for i in range(total):
                tx = Transaction(
                    user=user,
                    amount=random.randrange(Decimal(1), Decimal(1000)),
                    currency=random.choice(currencies),
                    description="",
                    date=timezone.now() - timezone.timedelta(
                        days=random.randint(1, 365)
                    ),
                    category=random.choice(categories)
                )
                txs.append(tx)

            Transaction.objects.bulk_create(txs, batch_size=500)
        except Exception as ex:
            self.stdout.write(self.style.ERROR(f"An error has occurred: {ex}"))
        else:
            self.stdout.write(self.style.SUCCESS(
                f"Successfully created {total} transactions"
            ))
