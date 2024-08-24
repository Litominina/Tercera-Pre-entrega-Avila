from django.http import HttpResponse
from datetime import date
from django.template import Template, Context



def saludo(request):
	return HttpResponse("Holis! esta es Litóbar saludando.")

def otra_vista(request):
	return HttpResponse("<h1>Este título dice que Lito es belli❤️</h1><p>Y este es un párrafo dice que es inteligente.</p>")

def dia_de_hoy(request):
	hoy= date.today()
	return HttpResponse(f"Hoy es {hoy}")

def muestra_nombre(self, nombre):
	return HttpResponse(f"Buenos días {nombre}, biendenida por estos lados.")


def probando_template(request):

    miHtml = open("C:/Users/lavilaga/Desktop/Curso Python/Actividades/Tercera pre-entrega Avila/proyecto_litobar/plantillas/template1.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)
