from django.urls import path

from . import views

urlpatterns = [

    path(
        '',
        views.quotation_create,
        name='quotation'
    ),

]
