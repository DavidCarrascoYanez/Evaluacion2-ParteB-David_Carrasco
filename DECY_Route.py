import urllib.parse
import requests

api_principal = "https://www.mapquestapi.com/directions/v2/route?"
llave_de_sol = "XAU4NgulmewtdiLSXpfNjyyLOZyhN0d0"
while True:
   partida = input("Escriba su ubicacion inicial: ")
   if partida == "salir" or partida == "s":
        break
   llegada = input("Elija el destino al cual desea llegar: ")
   if llegada == "salir" or llegada == "s":
        break
   
   enlace = api_principal + urllib.parse.urlencode({"key" :llave_de_sol, "from" :partida, "to" :llegada})
   json_datitos = requests.get(enlace).json()
   print(json_datitos)
   print("URL: " + (enlace))
   
   json_estadazo = json_datitos ["info"] ["statuscode"]
   if json_estadazo == 0:
    print("Estado de la API: " + str(json_estadazo) + "= Se ha establecido conexion con su destino.\n")
    print("=============================================")
    print("Direcciones desde " + (partida) + " hacia " + (llegada))
    print("Duración de todo su trayecto:   " + (json_datitos["route"]["formattedTime"]))
    print("Kilómetros totales:      " + str("{:.2f}".format((json_datitos["route"]["distance"])*1.61)))
    print("=============================================")
    for each in json_datitos["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
        
   elif json_estadazo == 402:
        print("**********************************************")
        print("Estado actual del código actual: " + str(json_estadazo) + "; Entrada no válida para una o ambas ubicaciones.")
        print("**********************************************\n")
   elif json_estadazo == 611:
        print("**********************************************")
        print("Estado actual del código: " + str(json_estadazo) + "; Falta una entrada o ambas ubicaciones.")
        print("**********************************************\n")
   
    





