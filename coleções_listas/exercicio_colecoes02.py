#Criando uma "tupla" 
#Convertendo ela para lista, adicionando um elemento a ela
#E convertendo novamente para tupla.

#Tuple feita com marcas de carros
car_brands = ('Honda', 'Mustang', 'McLaren', 'Subaru')
#input para o schema de escolhas. 
bchoice_cars = str(input(f'Type the brand you are looking for: '))
#Schema de escolhas com objetivo de realizar os requisitos do exercicio; 
if bchoice_cars == 'Subaru' and 'Subaru' in car_brands:
    print("Subaru in stock")
else:
    print("Subaru is not in stock!")

print(car_brands)    
#Segunda parte do exercicio. Adicionando elementos a uma tupla convertendo ela para lista e convertendo novamente para lista.
list_car = list(car_brands)
print(list_car)

list_car.append("Chevrolet")
list_car.append("Fiat")
list_car.append("Ferrari")
list_car.append("Lamborghini")
print(tuple(list_car))