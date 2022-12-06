#Variables

my_variable= "My string variable"
print(my_variable)

my_int_variable=5
print(my_int_variable)

my_bool_variable= False
print(my_bool_variable)

#concatenation of variables
print(my_variable, my_int_variable,my_bool_variable)
print(type(print(my_variable, my_int_variable,my_bool_variable)))

#Some System functions
print(len(my_variable))

#Variables at one line, no abusar
name, surname, alias,age = "Anthony", "Chela", "Tony", 25
print("Me Llamo: ",name, surname, "Mi edad es:",age, "Mi alias:", alias)

#Imputs y redefinir las variables name and age
name=input('Cual es tu nombre? ')
age=input('Cual es tu edad? ')
print(name)
print(age)

#forzamos el tipo
address: str = "Mi direccion"
address = True
address = 32
address=1.2
print(type(address))


#built in functions in python documentation (funciones integradas)

# str to int or float
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

