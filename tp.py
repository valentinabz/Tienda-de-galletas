#mostrar menu
#funcines definidas
def mostrar_menu(sabores):
    print("Bienvenido a la tienda de galletas!")
    print("Estos son los sabores disponibles:")
    for i, sabor in enumerate(sabores):
        print(f"{i + 1}. {sabor}")

#condicionales
#elegir sabores
def elegir_sabores(sabores):
    eleccion = []
    while len(eleccion) < 6:
        try:
            opcion = int(input("Elige un número del menú para seleccionar un sabor: "))
            if 1 <= opcion <= len(sabores) and sabores[opcion - 1] not in eleccion:
                eleccion.append(sabores[opcion - 1])
            else:
                print("Opción inválida o sabor ya elegido. Intenta de nuevo.")
        except :
            print("Por favor, ingresa un número válido.")
    return eleccion

#bucles
#mostrar los sabores

def mostrar_seleccion(seleccion):
    print("Has elegido los siguientes sabores:")
    for sabor in seleccion:
        print(f"- {sabor}")
#modiicar o quitar algun sabor
def modificar_seleccion(seleccion, sabores):
    while True:
        opcion = input("¿Quieres quitar algún sabor? (s/n): ").lower()
        if opcion == 's':
            sabor_quitar = input("Ingresa el sabor que deseas quitar: ")
            if sabor_quitar in seleccion:
                seleccion.remove(sabor_quitar)
                nuevo_sabor = elegir_nuevo_sabor(sabores, seleccion)
                seleccion.append(nuevo_sabor)
            else:
                print("El sabor no está en la selección. Intenta de nuevo.")
        elif opcion == 'n':
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
    return seleccion
#funcion para elegir los sabores
def elegir_nuevo_sabor(sabores, seleccion):
    while True:
        try:
            opcion = int(input("Elige un número del menú para seleccionar un nuevo sabor: "))
            if 1 <= opcion <= len(sabores) and sabores[opcion - 1] not in seleccion:
                return sabores[opcion - 1]
            else:
                print("Opción inválida o sabor ya elegido. Intenta de nuevo.")
        except :
            print("Por favor, ingresa un número válido.")
#finalizar la compra
def finalizar_compra(seleccion):
    print("Gracias por tu compra! Has elegido los siguientes sabores de galletas:")
    for sabor in seleccion:
        print(f"- {sabor}")
    print("Gracias,¡Que disfrutes tus galletas!")
#lista

#sabores
def main():
    sabores = [
        "Chocolate", "Chocoalmendra", "Red velvet", "Limon", "Coco", "m&m", 
        "Avellana", "Nutella", "Kinder", "dulce de leche", "Manzana", "Arándano"
    ]
    mostrar_menu(sabores)
    seleccion = elegir_sabores(sabores)
    mostrar_seleccion(seleccion)
    seleccion = modificar_seleccion(seleccion, sabores)
    finalizar_compra(seleccion)

if __name__ == "__main__":
    main()
