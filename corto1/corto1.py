# #  Ultimos digitos de mi carnet (201318571) hasta donde llegar la secuencia
numero = 571

# # Ciclo que despliega desde el numero indicado has llegar a un valor de 1 respetando las sentencias de si el numero es par o impar 
while numero != 1:
    if numero % 2 == 0:
        print("%d," % (numero), end = "")
        numero = numero / 2
    else:
        print("%d," % (numero), end = "")
        numero = (numero * 3) + 1

    if numero == 1:
        print("1")