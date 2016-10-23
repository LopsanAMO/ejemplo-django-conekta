from django.conf.urls import url
from .views import Pago

urlpatterns = [
    url(r'^pago', Pago.as_view(), name='pago_prro'),
]
