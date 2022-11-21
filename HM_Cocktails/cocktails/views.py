from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template , Context , loader

def saludo(request):
    list=[
        "¿Cree que para el año 2022 el SMMLV es suficiente para solventar las necesidades basicas del diario vivir?",
        "¿Esta de acuerdo con el incremento de año para recibir la pension (65 años para hombres y 62 para mujeres)?",
        "¿Esta de acuerdo con la reforma tributaria propuesta por el gobierno?",
        "¿Cree que la educacion debe ser 100% publica y gratuita?",
        "¿Cree que la atencion medica y medicamentos deben ser 100% publicos y gratuitos?",
        "¿Esta de acuerdo con el porte legal de armas?",
        "¿Esta de acuerdo con que se pague el trabajo por horas?",
        "¿Esta de acuerdo con el incremento a los productos de la canasta familiar?",
        "¿Esta de acuerdo con la cantidad de peajes en el territorio nacional (168)?",
        "¿Esta de acuerdo con la dosis personal de consumo de Marihuana?",
        "¿Esta de acuerdo con la legalizacion del suicidio asistido?",
        "¿Cree que las escuelas deben proporcionar alimentacion gratuita a sus estudiantes?"]
    template=loader.get_template("inicio.html")
    return render(request,'inicio.html',{"list":list})
    

def login(request):
    template=loader.get_template("login.html")
    return HttpResponse(template.render())
# Create your views here.
