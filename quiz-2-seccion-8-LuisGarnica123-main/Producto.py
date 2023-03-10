class producto():
    def __init__(self, nombre,tipo,stock,precio):
        self.nombre=nombre
        self.tipo=tipo
        self.stock=stock
        self.precio=precio
    def __str__(self):
        self.nombre=input('Ingrese el nombre del producto:')
        self.tipo=input('Ingrese le tipo:')
        self.stock=int(input('Ingrese el Stock:'))
        self.precio=(input('Ingrese el precio:'))
    def mostrar(self):
        return f'Nombre:{self.nombre}| el tipo:{self.tipo} |El stock:{self.stock}| El precio:{self.precio}'
    