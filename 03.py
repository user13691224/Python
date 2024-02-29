cadena1= "probando"
cadena2="probando 2"
cadena_reemplazando=cadena1.replace("pro","hola como estas")
print(cadena_reemplazando)
lista=[1,2,6,3,"hola"]
lista.insert(0,0)
print(lista)
# extend
lista.extend([False,2023])
lista.pop(0)
print(lista)
lista.remove(3)
print(lista)
lista.remove("hola")
lista.sort(reverse=True)
lista.reverse()
print(lista)