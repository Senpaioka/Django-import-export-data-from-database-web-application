from django.shortcuts import render
from common_codes.models_name import get_custom_model_name
from django.core.management import call_command
from main_site.models import UploadModel
from site_settings import settings
from django.contrib import messages



# Create your views here.


def home_view(request):
    return render(request, 'home.html')








def import_view(request):
    
    # get the file path
    try :

        relative_path = ""

        if request.method == 'POST':
             # file name
            file_name_value = request.FILES.get('fileUpload')
            model_name = request.POST.get('model_name')
                
            # save file to the database

            save_file = UploadModel.objects.create(
            file_name = file_name_value
             )  

            relative_path = save_file.file_name.url
            save_file.save()

            base_url = str(settings.BASE_DIR)
            full_path = base_url+relative_path

            #trigger the custom management command function
            call_command('importdata', full_path , model_name)

            # showing success message
            messages.success(request, "Data Import Successful !")

    except ValueError as err:
        
        messages.error(request, err)
    

    # get list of models for frontend
    all_custom_model = get_custom_model_name()


    context = {
        "custom_models" : all_custom_model,
    }
    
    return render(request, 'import.html', context)









def export_view(request):

    # backend functionality

    try:
        # get the model name from frontend
        if request.method == 'POST' :
            selected_model_name = request.POST.get('model_name')
            
            # trigger the custom management command functionality
            call_command('exportdata', selected_model_name)

    except:
        pass

    # get list of models for frontend
    all_custom_model = get_custom_model_name()

    context = {
        "custom_models" : all_custom_model,
    }

    return render(request, 'export.html', context)