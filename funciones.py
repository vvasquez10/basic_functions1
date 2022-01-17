#1
def number_of_food_groups():
    return 5
print(number_of_food_groups()) #Se mostrará 5


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches()) #error, ya que la primera función no está definida


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold()) #Se mostrará 5, ignora todo despúes del primer return

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers()) #Se mostrará 5, ignora todo despúes del primer return


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x) #Se mostrará "5" solo 1 vez, x no es igual a , ya que la funcion no retorna nada


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3)) # se miestra 3 y 5, que es el resultado de llamar a ambas funciones, pero el imprimir las 2 funciones concatenadas no resultará


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5)) #Devolverá "25"




#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b) 
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents()) #Se imprime 100 y luego 10 ya que se cumple el else.


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) # se imprime 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))# se imprime 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # se imprime 21, se interpreta como suma



#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5)) #devuelve 8


#11
b = 500
print(b) #devuelve 500
def foobar():
    b = 300
    print(b)
print(b)#devuelve 500
foobar() #devuelve 300
print(b)#devuelve 500


#12
b = 500
print(b) #imprime 500
def foobar():
    b = 300
    print(b)
    return b
print(b) #imprime 500
foobar() #imprime 300
print(b) #imprime 500



#13
b = 500 
print(b) #imprime 500
def foobar():
    b = 300
    print(b)
    return b
print(b) #imprime 500
b=foobar() #imprime 300 y devuelve b=300
print(b) #imprime 300



#14
def foo():
    print(1) 
    bar() 
    print(2)
def bar():
    print(3)
foo() #prints 1 and then 3, then 2


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo() #prints 1, 3, 5 and returns 10
print(y)  #prints 10