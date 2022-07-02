from .views import *
from django.urls import path


urlpatterns = [
    path('client_org/', ClientOrgUploadView.as_view()),
    path('bills/', BillUploadView.as_view()),
    path('clients/', BillUploadView.as_view()),
    path('invoices/', BillUploadView.as_view()),

    # path('item/<int:pk>', ItemView.as_view()),
]