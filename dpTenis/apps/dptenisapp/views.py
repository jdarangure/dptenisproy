import datetime
import re

from django.contrib import messages
from django.shortcuts import redirect, render

from .models import *

# Función para limpieza de texto

def limpiaTexto(texto):
    
    # Se crea un diccionaro don se mapea los numeros correspondientes a cada letra de abecedario similar a ese número
    dic_num2let = {"0" : "o" , "1": "i", "3": "e", "4": "a", "5": "s", "6": "g", "7": "t"}

    # Lista de vocales para evitar vocales repetidas juntas
    list_vocals = {'a', 'e', 'i', 'o', 'u'}

    # Lista para validar que el texto solo contenga letras
    list_validate = re.compile("[A-Za-z]")

    txt = texto.split(' ') #se separa el texto por palabras para realizar el limpiado por cada una

    res = [] # declaración de una variable tipo lista donde se guardará el resultado de la limpieza

    # ciclo para recorrer cada palabra en la lista txt
    for el in txt:
      list_txt = [] #declaración de una variable tipo lista donde se guardará cada una de las letras que conforma la palabra ya limpia
      a = '' #declaración de una variable para guardar la letra anterior y validad que no sea un duplicado
      
      # ciclo para recorrer cada letra de la palabra
      for idx, l in enumerate(el):
          try: #buscamos la letra en el diccionario dic_num2let y en caso de encontrarla, guarda la letra correspondiente en una variable
            x = dic_num2let[l]
          except: #en caso de que el elemento buscado no se encuentre en el diccionario, es decir, que no sea un número, se guarda la letra en minúsculas
            x = l.lower()
            
          if idx == 0: #se valida si el el elemento es la primera letra de la palabra para convertirla en mayúscula
            x = x.upper()
              
          if list_validate.fullmatch(x): #se valida que el elemento sea una letra
            if x.lower() != a.lower() or (x.lower() not in list_vocals): #se valida que el elemento actual (x) no sea igual al elemento anterior (a), además, se valida que no sea una vocal.
              list_txt.append(x) #agregamos la letra a la lista
              a = x #se guarda el elemento actual (x) en una variable (a) para compararle en la siguiente iteración
      
      res.append(''.join(list_txt)) #agregamos la palabra ya limpia en la lista para formar la palabra completa
    
    return (' '.join(res)) #retornamos la palabra completa separa por espacios para mostrarla en el template

# Create your views here.
def home(request):
    
    # se obtiene la información de todos los modelos(tablas)
    _distributor=distributor.objects.all()
    _persons=persons.objects.all()
    _addresses=addresses.objects.all()
    _phone_numbers=phone_numbers.objects.all()

    _distrOptimize = [] #variable tipo lista para guardar la información a la cual se le aplicó la limpieza de datos
    _distComplete = [] #varia tipo lista para guardar la información real que se encuentra en las tablas

    #ciclo para iterar sobre cada uno de los registros de la tabla distributor para obtener la información para cada Id
    for d in _distributor:
        
        # se busca el id de distribuido de cada una de las tablas para obtener su información
        _persons=persons.objects.get(id_dist=d.id_dist)
        _addresses=addresses.objects.get(id_dist=d.id_dist)
        _phone_numbers=phone_numbers.objects.get(id_dist=d.id_dist)
        
        #se guarda la información en la lista optimizada, aplicando limpieza a cada uno de los campos de texto con la función limpiaTexto()
        _distrOptimize.append(
            {
              "id_dist" : d.id_dist,
              "nombre_completo": limpiaTexto(_persons.nombre) + " " + limpiaTexto(_persons.apellido_paterno) + " " + limpiaTexto(_persons.apellido_materno),
              "direccion" : "Calle: " + limpiaTexto(_addresses.calle) + ", #" + str(_addresses.numero_casa) + ", Colonia: " + limpiaTexto(_addresses.colonia),
              "telefono" : _phone_numbers.numero_telefono
            }
        )

        #se guarda la información real de cada tabla para regresar un listado único que pueda ser facimelte consumido por el template.
        _distComplete.append(
            {
              "id_dist" : d.id_dist,
              "nombre": _persons.nombre,
              "apellido_paterno" : _persons.apellido_paterno,
              "apellido_materno" : _persons.apellido_materno,
              "calle" : _addresses.calle,
              "numero_casa" : _addresses.numero_casa,
              "colonia" : _addresses.colonia,
              "numero_telefono" : _phone_numbers.numero_telefono
            }
        )

    #retornamos el renderizado del template principal, y le mandamos las listas creadas
    return render(request, "dpteniscrud.html", {"distributor" : _distrOptimize, "distComplete" : _distComplete})

#función para agregar un registro a las tablas
def registraDist(request):
    
    list_validate = re.compile("[A-Za-z0-9]+")
    
    #validamos si el id existe en la tabla distributors
    if not(list_validate.fullmatch(request.POST['txtIdDist'])): #en caso de que exista regresa un mensaje al front por la duplicidad
       messages.success(request, 'El id del distribuidor solo debe contener números y letras')
       return redirect('/')

    #optenemos la información de los inputs del formulario y los guardamos en variables que hacen referencia a cada campo de las tablas
    _id_dist=request.POST['txtIdDist']
    _nombre=request.POST['txtNombre']
    _apellido_paterno=request.POST['txtApPaterno']
    _apellido_materno=request.POST['txtApMaterno']
    _calle=request.POST['txtCalle']
    _numero_casa=request.POST['txtNumeroCasa']
    _colonia=request.POST['txtColonia']
    _numero_telefono=request.POST['txtTelefono']

    try: #se guarda la información en las tablas
      _distributor = distributor.objects.create(
          id_dist=_id_dist,
          fecha = datetime.datetime.now()
      )
      _persons = persons.objects.create(
          id_dist=_id_dist,
          nombre=_nombre,
          apellido_paterno=_apellido_paterno,
          apellido_materno=_apellido_materno
      )
      _addresses = addresses.objects.create(
          id_dist=_id_dist,
          calle=_calle,
          numero_casa=_numero_casa,
          colonia=_colonia
      )
      _phone_numbers = phone_numbers.objects.create(
          id_dist=_id_dist,
          numero_telefono=_numero_telefono,
          activo=True
      )

      messages.success(request, '¡Distribuidor registrado!')

      return redirect('/')
    except: #en caso de el proceso de guardado arroje un error, manda un mensaje al front
      messages.success(request, '¡El id del distribuidor ya se encuentra registrado!')

      return redirect('/')


#función para mostrar la información a editar del registro seleccionado en la tabla del template principal
def editarDist(request, _id_dist):
    
    #optenemos la información de cada tabla buscada por medio del id
    _distributor=distributor.objects.get(id_dist=_id_dist)
    _persons=persons.objects.get(id_dist=_id_dist)
    _addresses=addresses.objects.get(id_dist=_id_dist)
    _phone_numbers=phone_numbers.objects.get(id_dist=_id_dist)

    #guardamos la información en una variable tipo diccionario para ser consumida facilmente por el template de edición
    _distrComplete = {
        "id_dist" : _distributor.id_dist,
        "nombre": _persons.nombre,
        "apellido_paterno" : _persons.apellido_paterno,
        "apellido_materno" : _persons.apellido_materno,
        "calle" : _addresses.calle,
        "numero_casa" : _addresses.numero_casa,
        "colonia" : _addresses.colonia,
        "numero_telefono" : _phone_numbers.numero_telefono
      }

    return render(request, "editardist.html", {"distributor": _distrComplete})

#función para guardar la el registro editado
def editDist(request):
    
    #optenemos la información de los inputs del formulario y los guardamos en variables que hacen referencia a cada campo de las tablas
    _id_dist=request.POST['txtIdDist']
    _nombre=request.POST['txtNombre']
    _apellido_paterno=request.POST['txtApPaterno']
    _apellido_materno=request.POST['txtApMaterno']
    _calle=request.POST['txtCalle']
    _numero_casa=request.POST['txtNumeroCasa']
    _colonia=request.POST['txtColonia']
    _numero_telefono=request.POST['txtTelefono']

    #optenemos la información a editar de cada tabla buscada por medio del id
    _distributor=distributor.objects.get(id_dist=_id_dist)
    _persons=persons.objects.get(id_dist=_id_dist)
    _addresses=addresses.objects.get(id_dist=_id_dist)
    _phone_numbers=phone_numbers.objects.get(id_dist=_id_dist)

    #se actualiza la información de cada campo en la tabla correspondiente
    _distributor.fecha = datetime.datetime.now()
    
    _persons.nombre = _nombre
    _persons.apellido_paterno = _apellido_paterno
    _persons.apellido_materno = _apellido_materno

    _addresses.calle = _calle
    _addresses.numero_casa = _numero_casa
    _addresses.colonia = _colonia

    _phone_numbers.numero_telefono = _numero_telefono

    #guarda los cambios en cada tabla
    _distributor.save()
    _persons.save()
    _addresses.save()
    _phone_numbers.save()

    messages.success(request, '¡Registro Modificado!')

    return redirect('/')

# función para borrar un registro
def borraDist(request, _id_dist):
    #obtenemos el registro de cada tabla por medio del Id y aplicamos el borrado de ese registro
    _distributor=distributor.objects.get(id_dist=_id_dist)
    _distributor.delete()
    _persons=persons.objects.get(id_dist=_id_dist)
    _persons.delete()
    _addresses=addresses.objects.get(id_dist=_id_dist)
    _addresses.delete()
    _phone_numbers=phone_numbers.objects.get(id_dist=_id_dist)
    _phone_numbers.delete()

    messages.success(request, '¡Registro Eliminado!')

    return redirect('/')