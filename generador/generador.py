with open('invitados.txt') as invitadostxt:
    invitados = invitadostxt.read().split("\n")
    print(invitados)

n=0

for i in invitados:
    print(invitados[n])
    
    
    
    n += 1