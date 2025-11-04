import random
palabras = ("playa","libro","abril","actor","acero","abeto")

while True:
    palabra = palabras[random.randint(0,len(palabras)-1)]
    wordle = list(palabra)#"a","b","j","0"
    print("""\033[1;31;43]
          ===============================WORDLE=======================================
          bienvenido ya he elegido la palavra secreta tienes 5 intentos para adivinarla
          =============================================================================
          /033[0;30;47]""",wordle)
    
    for i in range(5):
        intento = input("ingrese una palabra de 5 letras sin acento").lower()[:5]
        indice = 0
        correctas = 0
        resultado = ""
    for letra in intento:   
        if letra == wordle[indice]:
            resultado += "\033[1;32m" +letra+"\033[0;35m"
        elif letra in wordle:
             resultado += "\033[1;32m" +letra+"\033[0;35m"
        else:
             resultado += "\033[1;32m" +letra+"\033[0;35m"
        indice += 1
        print(resultado)
        if correctas == 5:
         break
        if correctas == 5:
                print ("felicidades la palabra era \033[1;32m{palabra}\033[0;30m has acertado")
        else:
                print ("lo siento has fallado la palabra era: \033[1;32m{palabra}\033[0;30m")
    opcion = input("desas jugar otra vez si/no").lowe()
    if opcion == "no":
        break
