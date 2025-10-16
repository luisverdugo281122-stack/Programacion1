import random
while True:
 input("¿haz una pregunta?")

 dado= random.randint(1,20)
 
 if dado == 1:
  print("si")

 elif dado == 2:
  print ("no")
 elif dado == 3:
  print ("tal vez")
 elif dado == 4:
  print ("probablemente si")
 elif dado == 5:
  print ("probablemente no")
 elif dado == 6:
  print ("pregunta en otro momento")
 elif dado == 7:
  print ("es muy poco probable")
 elif dado == 8:
  print ("es muy probable")
 elif dado == 9:
  print ("creo")
 elif dado == 10:
  print ("no debes saber")
 elif dado == 11:
  print ("sabras otro dia")
 elif dado == 12:
  print ("que te importa")
 elif dado == 13:
  print ("nunca sabras")
 elif dado == 14:
  print ("si tienes suerte puede ser")
 elif dado == 15:
  print ("alguien mas te lo dira")
 elif dado == 16:
  print ("dios no cumple caprichos")
 elif dado == 17:
  print ("necesitas un milagro")
 elif dado == 18:
  print ("creo")
 elif dado == 19:
  print ("nada seguro")
 elif dado == 20:
  print ("imposible")

 pregunta= input ("quieres otra pregunta")
 
 if pregunta== "no":
   break

