bitcoin_amount= float(input("Introduzca su cantidad de Bitcoin que presenta: ")) 
bitcoin_value_euros= 25000
def bitcoin_to_euros(bitcoin_amount, bitcoin_value_euros):
    euros_value= bitcoin_amount * bitcoin_value_euros
    return euros_value
euros_value= bitcoin_to_euros(bitcoin_amount, bitcoin_value_euros)
if euros_value <= 30000:
    print("Su inversión es inferior a 30.000€")
if euros_value > 30000:
    print("Su inversión es mayor a 30.000€")