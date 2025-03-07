#Divicion

num3 = int(input("Escriba el primer número: "))
num4 = int(input("Escriba el segundo número: "))

if num4 == 0:
    print("No se puede dividir por cero")
else:
    div = num3 / num4
    print(f"División: {num3}/{num4} = {div}")