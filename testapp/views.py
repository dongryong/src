from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.decorators.http import require_http_methods


class Pong(View):
    """ respond to ping requests"""
    def get(self, request):
        return HttpResponse('pong')

@require_http_methods(['GET','HEAD','OPTIONS'])
def pong(request):
    if request.method in ["GET","HEAD"]:
        return HttpResponse("pong")
    else:
        reponse = HttpResponse()
        reponse["Allow"] = ', '.join(
            ["GET","HEAD","OPTIONS"]
        )
        return reponse