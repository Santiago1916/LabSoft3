from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template , Context

def saludo(request):
    doc_externo=open("C:/Users/usuario/Dropbox/My PC (DESKTOP-23VV5U8)/Documents/GitHub/LabSoft3/HM_Cocktails/HM_Cocktails/templates/inicio.html")
    ptl = Template(doc_externo.read)
    doc_externo.close
    ctx = Context()
    documento = ptl.render(ctx)
    return HttpResponse(documento)

def login(request):
    doc_externo=open("C:/Users/usuario/Dropbox/My PC (DESKTOP-23VV5U8)/Documents/GitHub/LabSoft3/HM_Cocktails/HM_Cocktails/templates/login.html")
    ptl = Template(doc_externo.read)
    doc_externo.close
    ctx = Context()
    documento = ptl.render(ctx)
    return HttpResponse(documento)
# Create your views here.
