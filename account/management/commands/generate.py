import random

from django.core.management import BaseCommand
from account.models import Workers


class Command(BaseCommand):
    help = "Create slug for all Workers model"

    def handle(self, *args, **options):
        print("Started ................>>>>")
        workers = Workers.objects.all()

        for worker in workers:
            worker.salary = random.randint(500,1500)
            worker.save()
            print("{}".format(worker.slug))

        print("Complate [OK]")
