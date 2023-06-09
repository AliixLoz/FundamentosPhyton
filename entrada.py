# fuction input --> retorna string 
name= input('Cómo te llamas?\n')
age= int(input ('Cúantos años tienes?\n'))
future= int(input('cuantos años más?\n'))

print("Hola"+name)
print("En" + str(future)+ "años tendrás" + str(age+future))

#Format Strings
"""
     Hola Aliix, en 3 años tendrás 21 años
"""

text_complete= "Hola {}, en {} años tendrás {} años"
print(text_complete.format(name, future, age + future))
print(f"Hola {name}, en {future} años tendrás {age + future} años")

