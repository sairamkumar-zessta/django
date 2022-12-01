from django.urls import path
from finance.views import feeDueReport
from finance.views import feeCollection
from finance.views import feeCollectedReport

urlpatterns = [
    path('rep/', feeCollectedReport),
    path('coll/', feeCollection),
    path('due/',feeDueReport),
]
