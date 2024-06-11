from django.apps import apps


def get_custom_model_name():
    default_models = ["LogEntry", "Permission", "Group", "User", "ContentType", "Session", "UploadModel"]
    custom_model_list = []

    for custom_model in apps.get_models():
        if custom_model.__name__ not in default_models:
            custom_model_list.append(custom_model.__name__)
    
    return custom_model_list

        
        
    