
from django.urls import path
from main_site import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('import/', views.import_view, name="import"),
    path('export/', views.export_view, name="export"),
] 