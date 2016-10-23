from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import Sale

class Pago(View):
    def get(self, request):
        template_name = 'pago.html'
        return render(request, template_name)

    def post(self, request):
        print('gfsdgfgfgggsgddg')
        print(request.POST["conektaTokenId"])
        token_id = request.POST["conektaTokenId"]
        sale = Sale()
        if token_id: #Prevents send empty token
            return HttpResponse(sale.charge(300, token_id))
