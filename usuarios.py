
usuarios = {}
dia=""
catv=150
cats=180
def comprar_entrada(usuarios,catv,cats):
    while True:
        n=input("Ingrese el nombre del usuario. ")
        try:  
            if n not in usuarios:
                while True:
           
                    o=int(input("1. Función Día Viernes\n2. Función Día Sábado."))
                    try:
                            if o==1:
                                if cats<=0:
                                    print("No quedan más entradas.")
                                else:
                                    catv=catv-1
                                    print(f"Entrada registrada en función 1! Stock restantes:\nFunción 1 (Viernes): {catv} \nFunción 2 (Sábado): {cats}")
                                    dia="viernes"
                                    return catv
                            if o==2:
                                if cats<=0:
                                    print("No quedan más entradas.")
                                if cats>=1:
                                    cats=cats-1
                                    dia="sabado"
                                    print(f"Entrada registrada en función 1! Stock restantes:\nFunción 1 (Viernes): {catv} \nFunción 2 (Sábado): {cats}") 
                                    return cats        
                            else:
                                print("Ingresa una opción válida.\n")
                    except ValueError:
                        print("Ingrese un valor válido. ")
                    usuarios[n] =[dia]
                    break
            if n in usuarios:
                print("Nombre ya en uso. Intentelo otra vez.")
        except ValueError:
            print("Ingrese un valor válido.")
        break   
   

def cambio_funcion(usuarios,cats,catv):
    cam=input("Ingrese el nombre del usuario. ")
    while True:
        if cam in usuarios:
            if usuarios[cam][0] == "viernes":
                catv=catv+1
                cats=cats-1 
                usuarios[cam][0] = "sabado"
                break
            if usuarios[cam][0] == "sabado":    
                catv=catv-1
                cats=cats+1
                usuarios[cam][0] = "Viernes"
                break   
            return usuarios[cam] [0]
                
        if cam not in usuarios:
            print("Usuario no encontrado. ")
            break
   
    
def mostrar_s(catv,cats):
    print(f"-- Stock de Funciones --\nFunción 1 (Viernes): Disponibles {catv}, Vendidas {150-catv}\nFunción 2 (Sábado): Disponibles {cats}, Vendidas {180-cats}")
    





while True:
    try:
        mo=int(input("TOTEM AUTOATENCIÓN CAFECONLECHE\n1.- Comprar entrada a Cats.\n2.- Cambio de función.\n3.- Mostrar stock de funciones.\n4.- Salir."))
        if mo==4:
            print("\nPrograma terminado...")
            break
        if mo==1:
            comprar_entrada(usuarios,catv,cats)
            
        if mo==2:
            cambio_funcion(usuarios,catv,cats)
        if mo==3:
            mostrar_s(catv,cats)
        else:
            print("Ingrese una opción válida. ")
        

    except ValueError:
        print("Ingresa un valor válido")

