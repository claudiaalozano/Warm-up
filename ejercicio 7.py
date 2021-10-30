for i in range(51):
    print(i) 
dinero= 2000
import random
precio_helado= 100
porcentaje= 1.2
edad=random.randint(0,50)
hambre=edad
if edad>= 85: 
    print("Estas satisfecho")
elif edad<0:
    print("Error")
else:
    helado_1= precio_helado 
    helado_2= precio_helado * porcentaje
    helado_3= precio_helado * (porcentaje ** 2)
    helado_4= precio_helado * (porcentaje ** 3)
    helado_5= precio_helado * (porcentaje ** 4)
    helado_6= precio_helado * (porcentaje ** 5)
    helado_7= precio_helado * (porcentaje ** 6)
    helado_8= precio_helado * (porcentaje ** 7)
    print(edad)
    if helado_1 <= dinero and hambre < 85:
        hambre= edad * 2
        dinero= dinero - helado_1
        if hambre > 100:
            hambre= 100
        print ("Se come un helado")
    if helado_2 <= dinero and hambre < 85:
        hambre= edad * 3
        dinero= dinero - helado_2
        if hambre > 100:
            hambre= 100
        print ("Se come dos helados")
    if helado_3 <= dinero and hambre < 85:
        hambre= edad * 4
        dinero= dinero - helado_3
        if hambre > 100:
            hambre= 100
        print ("Se come tres helados")
    if helado_4 <= dinero and hambre < 85:
        hambre= edad * 5
        dinero= dinero - helado_4
        if hambre > 100:
            hambre= 100
        print ("Se come cuatro helados")
    if helado_5 <= dinero and hambre < 85:
        hambre= edad * 6
        dinero= dinero - helado_5
        if hambre > 100:
            hambre= 100
        print ("Se come cinco helados")
    if helado_6 <= dinero and hambre < 85:
        hambre= edad * 7
        dinero= dinero - helado_6
        if hambre > 100:
            hambre= 100
        print ("Se come seis helados")
    if helado_7 <= dinero and hambre < 85:
        hambre= edad * 8
        dinero= dinero - helado_7
        if hambre > 100:
            hambre= 100
        print ("Se come siete helados")
    if helado_8 <= dinero and hambre < 85:
        hambre= edad * 9
        dinero= dinero - helado_8
        if hambre > 100:
            hambre= 100
        print ("Se come ocho helados")
    print("Tiene " + str(dinero) + "€" + " y de hambre presenta " + str(hambre) + "%")