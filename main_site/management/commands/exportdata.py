from django.core.management.base import BaseCommand
from django.apps import apps
import datetime
import csv


class Command(BaseCommand):

    help = "export data from database with provided model"

    # taking argument
    def add_arguments(self, parser):
        parser.add_argument("model_name", type=str, help='provide the model name')


    def handle(self, *args, **options):
        provided_model = options["model_name"]

        # getting app & model name
        found_model = None
        for app_data in apps.get_app_configs():
            try:
                found_model = apps.get_model(app_data.label, provided_model)
                break
            except LookupError:
                continue

        # create a file name
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d')
        file_name = f"from_{found_model.__name__}_at_{timestamp}.csv"

        # open and write file

        if found_model is not None:
            
            with open(file_name, 'w', newline='') as file:
                
                csv_writer = csv.writer(file)
                csv_writer.writerow(field_header.name for field_header in found_model._meta.get_fields() if field_header.name != "id")
                model_object = found_model.objects.all()
                for data in model_object:
                    csv_writer.writerow([getattr(data, value.name) for value in found_model._meta.fields if value.name != "id"])
                
                self.stdout.write(self.style.SUCCESS("Data Exported Successfully !"))

        else:
            self.stderr.write("Something went wrong !!")





