from django.shortcuts import render
from django.views.generic import View

class Pago(View):
    def get(self, request):
        template_name = 'pago.html'
        return render(request, template_name)
