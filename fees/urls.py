from django.conf.urls import url
from .views import fees_pay

urlpatterns = [
    url(r'^$', fees_pay, "fees_pay")
]
