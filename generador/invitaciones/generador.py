
datos_correctos = False

while datos_correctos == False:    

    with open('../invitados.txt') as invitadostxt:
        invitados = invitadostxt.read().split("\n")
        print("\n\n\nla lista de invitados es: -> " + str(invitados))
        invitadostxt.close()

    with open('../projectname.txt') as proyectotxt:
        proyecto = proyectotxt.read()
        print("\nel nombre de el proyecto es: -> " + str(proyecto))
        proyectotxt.close()

    with open('../time-date.txt') as time_datetxt:
        time_date = time_datetxt.read().split("\n")
        print("\nla hora y fecha del proyecto es: -> " + str(time_date))
        time_datetxt.close()
        
    with open('../urlmaps.txt') as urlmapstxt:
        urlmaps = urlmapstxt.read()
        print("\nel codigo url de la ubicacion es: -> " + str(urlmaps))
        urlmapstxt.close()
        
    print("\n\nlos datos son correctos? si=1 no=0")
    aux =  int(input("-> "))
    if aux == 0:
        datos_correctos = False
    else:
        datos_correctos = True

n=0

with open('../code.txt', encoding="utf8") as codetxt:
        code = codetxt.read()
        codetxt.close()

for i in invitados:
    print(invitados[n])
    doc_name = invitados[n] + ".html"
    
    #se tiene que modificar el code
    
    print(code)
    with open(doc_name, "w", encoding="utf8") as invitacion:
        invitacion.write(code)
    
    n += 1