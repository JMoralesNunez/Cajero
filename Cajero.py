Menu = True
saldo = 0
historial = {}
movimiento = len(historial)

while Menu:
    print("="*50)
    print("Bienvenido a tu cajero!")
    print("1. Ver saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Ver historial de movimiento")
    print("5. Salir del programa")
    print("="*50)
    option = input("Selecciona una opción: 1/2/3/4/5: ")
    if option == "1":
        print(f"Tu saldo actual es de ${saldo} pesetas")
    if option == "2":
        while True:
            retirar = int(input("Ingresa cuanto saldo deseas retirar: "))
            if retirar == 0:
                print("No has retirado nada")
                break            
            saldo -= retirar
            if saldo >= 0:
                retiro = (f"Se retiró ${str(retirar)}")
                movimiento += 1
                historial.update({movimiento:retiro})
                print("Saldo retirado exitosamente")
                break
            else:
                print("Saldo insuficiente")
                saldo = 0
                break
    if option == "3":
        while True:
            depositar = int(input("Ingresa cuanto saldo deseas depositar: "))
            if depositar == 0:
                print("No has depositado nada")
                break
            else:
                saldo += depositar
                deposito = (f"Se depositó ${str(depositar)}")
                movimiento += 1
                historial.update({movimiento:deposito})
                print("Deposito exitoso")
                break
    if option == "4":
        if not historial:
            print("No hay movimientos por ahora")
        for key, value in historial.items():
            print(f"{key}...................{value}")
    if option == "5":
        print("Gracias, vuelva pronto")
        Menu = False