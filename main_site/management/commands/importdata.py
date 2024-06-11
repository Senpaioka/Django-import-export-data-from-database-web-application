from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv



class Command(BaseCommand):

    help = "Import data to the database"

    # command arguments
    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="file path link")
        parser.add_argument("model_name", type=str, help="model name")

    def handle(self, *args, **options):
        # getting argument values
        file_link = options["file_path"]     
        provided_model = options["model_name"]

        # find the model
        model_found = None

        for app_details in apps.get_app_configs():
            
            try:
                model_found = apps.get_model(app_details.label, provided_model)
                break

            except LookupError:
                continue

        # open csv file
    
        if not model_found:
            raise CommandError(f"model {provided_model} is not authorized to access !!!")

        else:
            with open(file_link , 'r') as file:
                csv_reader = csv.DictReader(file)
                
                # check model name and upload file column name match
                model_column_name = [field_name.name for field_name in model_found._meta.get_fields() if field_name.name != "id"] 
                file_column_name = csv_reader.fieldnames 
                
                # upload data from file to database
                if model_column_name == file_column_name:

                    for data in csv_reader:
                              
                        model_found.objects.create(**data)

                else:
                    raise ValueError("file and model does not match. ")

            self.stdout.write(self.style.SUCCESS("Importing completed !!"))

        
        
   