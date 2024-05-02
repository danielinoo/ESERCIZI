#Pietropaolo Daniele
#2/5/24

#scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e viceversa a seconda del parametro to_fahrenheit. Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit.



def convert_temperature(temperature : float,to_fahrenheit = True) -> float:

    if to_fahrenheit == True:
        temperature : float = (temperature * 9/5) + 32
        return temperature

    else:
        temperature = (temperature - 32) /1.8
        return temperature




print(convert_temperature(4))
print(convert_temperature(56,to_fahrenheit=False))

