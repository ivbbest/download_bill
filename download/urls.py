from .views import *
from django.urls import path


urlpatterns = [
    path('client_org/', ClientOrgUploadView.as_view()),
    path('bills/', BillUploadView.as_view()),
    path('clients/', ClientAPIList.as_view()),
    path('invoices/', BillAPIList.as_view())
]
