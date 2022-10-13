#PRIMERA CLASE

#1
nombre = input("Ingrese su nombre: ")
print('Hola ' + nombre + ', bienvenido al modulo')
#print(type(nombre))

#2
from math import pi
radio = float(input('Ingrese el radio del círculo en metros: '))
area = pi*(radio**2)
print(f"El area de la circunferencia es: {area}" + ' m2')

#3
number = input("Ingrese numero que desea invertir: ")
print(int(number)//100) #Extrae primer digito
print((int(number)%100)//10) #Extrae segundo digito
print((int(number)%100)%10) #Extrae tercer digito

#Como numero:
print("El numero invertido es: ", str((int(number)%100)%10)+str((int(number)%100)//10)+str(int(number)//100))
#Como texto:
print("El numero invertido es: ", number[2]+number[1]+number[0])

#4
cent = float(input("Ingrese longitud en centimetros: "))
pulgadas = float(cent/2.54)
print("Longitud en pulgadas: ", pulgadas)
print(f"{cent} centimetros son {round(pulgadas,2)} pulgadas")

#5
far = float(input("Ingrese temp en farenheit: "))
celcius = int((far-32)*(5/9))
print("La temp en grados celcius es: ", celcius)

#6
a, b, c = list(map(int, input("Ingrese longitud de lados del triangulo: ").split("|")))
s = (a+b+c)/2 #Semiperimetro
area = pow(abs(float(s*(s-a)*(s-b)*(s-c))),0.5)
print(f"El semiperimetro es: {s} [m] y el area es: {area} [m2]")
print("Area: ",area)
print("Semiperimetro: ",s)

#7
temp = int(input('Ingrese temperatura: '))
if temp == 30:
    print("Hola")


#8
grades = list(map(float, input("Ingrese notas en el curso: ").split()))
avg = sum(grades)/len(grades)
print("El promedio de las notas obtenidas en el curso es: ", avg)
if avg > 55:
    print("Usted aprobó con ", avg)
else:
    print("Usted reprobó con ", avg)

#9
#Repeat three times the function using "for":
#for i in range(0,3):
#    temp_2 = float(input("Ingrese temperatura de caldera: "))
#    if temp_2 >= 60:
#        print("Too hot")
#    elif temp_2 < 60 and temp_2 >= 40:
#        print("Well")
#    elif temp_2 < 40 and temp_2 >= 20:
#        print("Enough")
#    else:
#        print("Nah")

#10
#a, b, c = list(map(int, input("Ingrese las tres notas: ").split()))
#prom = float((a+b+c)/3)
#print('Su promedio aritmetico es: ', prom)
#prom_2 = float(pow((a*b*c),1/3))
#print('Su promedio geometrico es: ', prom_2)

#if prom>=80:
#    print("Excelente")
#elif prom >= 55 and prom < 80:
#    print("Aceptable")
#elif prom >= 30  and prom < 55:
#    print("Ok")
#else:
#    print("Pésimo")

#11
import random
Usando randint:
if random.randint(1,2) == 1:
    print("Cara")
else:
    print("Sello")

Usando choice:
options = ["CARA", "SELLO"]
rand = random.choice(options)
print(rand)

#12
a, b = input("Ingrese dos palabras a continuación: ").split()
words = [a, b]
highest = max(words, key=len)
lowest = min(words, key=len)
print(highest)
print(lowest)

diff = abs(len(highest) - len(lowest))
if diff != 0:
    print(f"La palabra {highest}" + f" es mas largo que {lowest}" + f" por {diff} letras")
else:
    print("Both words are same length")

#13
height, weight, y_old = list(map(float, input("A continuación ingrese su estatura, peso y edad separados por '|': ").split("|")))
IMC = weight / (height**2)
print(IMC)
if y_old >= 45 and IMC >= 22.0:
    print("Condición de riesgo alto")
elif y_old >= 45 and IMC < 22.0:
    print("Condición de riesgo medio")
elif y_old < 45 and IMC >= 22.0:
    print("Condición de riesgo medio")
else:
    print("Condición de riesgo bajo")

#14
#To enter five times the salary and obtain the corresponding tax to pay:
#for j in range(0,5):
#    salary = int(input("Ingrese su sueldo: "))
#    print(salary)

#    def tax_payment(tax, salary):
#        return salary*(tax/100)

#    if salary < 1000:
#        tax = 0.0
#        z = tax_payment(tax, salary)
#        print(f"Usted pagará {z} de impuesto")

#    elif salary >= 1000 and salary <2000:
#        tax = 5.0
#        z = tax_payment(tax, salary)
#        print(f"Usted pagará {z} de impuesto")

#    elif salary >= 2000 and salary <4000:
#        tax = 10.0
#        z = tax_payment(tax, salary)
#        print(f"Usted pagará {z} de impuesto")

#    else:
#        tax = 12.0
#        z = tax_payment(tax, salary)
#        print(f"Usted pagará {z} de impuesto")

#15
first = int(input("Ingrese primer numero: "))
print("Primer numero: ", first)
second = int(input("Ingrese segundo numero: "))
third = int(input("Ingrese tercer numero: "))
fourth = int(input("Ingrese cuarto numero: "))
fifth = int(input("Ingrese quinto numero: "))

others = [second, third, fourth, fifth]
diff = []
for i in range(0, len(others)):
    y = others[i]-first
    diff.append(abs(y))

#Usando if:
if diff[0]>diff[1] and diff[0]>diff[2] and diff[0]>diff[3]:
    print(f"El número mas lejano al primero es {second} y la diferencia es {diff[0]}")
elif diff[1]>diff[0] and diff[1]>diff[2] and diff[1]>diff[3]:
    print(f"El número mas lejano al primero es {third} y la diferencia es {diff[1]}")
elif diff[2]>diff[0] and diff[2]>diff[1] and diff[2]>diff[3]:
    print(f"El número mas lejano al primero es {fourth} y la diferencia es {diff[2]}")
else:
    print(f"El número mas lejano al primero es {fifth} y la diferencia es {diff[3]}")

#Usando funciones max e index:
print(diff)
print(max(diff))
print("The index with highest difference", diff.index(max(diff)))
print(f"El número mas lejano al primero es el {others[diff.index(max(diff))]} y la diferencia es igual a {max(diff)}")