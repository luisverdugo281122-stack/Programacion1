dia= input ("dime el dia de la semana")
clima= input ("dime el clima (soleado,lluvioso nublado):")

match dia:
 case "lunes": 
    if clima == "soleado":
     print ("es lunes y esta soleado sal a caminar")
    elif clima == "lluvioso":
     print(" es lunes y llueve quedate en casa")
    else: 
     print ("es lunes y esta nublado haz tus tareas")
case "martes": # type: ignore
if clima == "soleado":
     print ("es martes y esta soleado sal a la playa")
elif clima == "lluvioso":
    print(" es martes y llueve quedate en casa y has ejercicio")
else:
    print ("es martes y esta nublado lava tu carro")

     case "miercoles": # type: ignore
if clima == "soleado":
     print ("es miercoles y esta soleado riega tus plantas")
elif clima == "lluvioso":
    print(" es miercoles y llueve quedate en casa y ve a dormir")
else:
    print ("es miercoles y esta nublado cocina algo")

     case "jueves": # type: ignore
if clima == "soleado":
     print ("es jueves y esta soleado sal con tu familia")
elif clima == "lluvioso":
    print(" es jueves y llueve quedate en casa y juega video juegos")
else:
    print ("es jueves y esta nublado lee un libro")

    case "viernes": # type: ignore
if clima == "soleado":
     print ("es viernes y esta soleado sal con tus amigos")
elif clima == "lluvioso":
    print(" es viernes y llueve quedate en casa y ve una pelicula")
else:
    print ("es viernes y esta nublado pasea tu mascota")