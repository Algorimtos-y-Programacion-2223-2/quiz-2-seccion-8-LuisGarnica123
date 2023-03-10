from Producto import producto as pro

products = [
{ "id": 1, "name": "Nevera", "type": "Hogar", "stock": 753, "price": 800 },
{ "id": 2, "name": "Cama", "type": "Hogar", "stock": 327, "price": 600  },
{ "id": 3, "name": "Suéter", "type": "Ropa", "stock": 260, "price": 25 },
{ "id": 4, "name": "Zapatos", "type": "Ropa", "stock": 593, "price": 5 },
{ "id": 5, "name": "Laptop Gamer", "type": "Gaming", "stock": 11, "price": 2500 },
{ "id": 6, "name": "Nintendo Switch OLED", "type": "Gaming", "stock": 25, "price": 400 },
]




def agregar():
    nuevo_producto=pro()
    products.update(nuevo_producto)

    print("Se ha actualizado exitosamente el inventario!!!")

def mostrar_inventario():
    for i in products:
        print(i)
        
def main():
    print("--Bienvenido--")
    eleccion=input('Que desea hacer?\n 1.Agregar al inventario \n2. Ver inventario \n>>>>')
    if eleccion == '1':
        agregar()
        main()

    if eleccion == '2' :
        mostrar_inventario()
        main()

main()
    