print('BIENVENIDO AL PROGRAMA')
contraseña='123'
us=input('introduzca el usuario ')
ingreso=input('introduzca la contraseña')
while ingreso != contraseña: 
    print('la contraseña es incorrecta')
    ingreso=input('vuelva a intentarlo')
print('la contraseña es correcta')
a=float(input('ingrese el primer numero a operar'))
b=float(input('ingrese el segundo numero a operar'))
print('*********seleccione la operacion a realizar con los numeros introducidos*********')
print('    1:division   ')
print('    2:divisor    ')
print('    3:numero capicua')
print('    4:cambio de base')
print('    5:salir del programa')
e=input(' elije una opcion:   ')
if (e==1):
    n=0
    for i in range (n,a,b):
        print(n)

elif (e==5):
    print('usted saldra del programada')
    breakpoint