
apto=[1,2,3,4,5]
bd={}
class edificio():
    def __init__(self, nombre,numero_de_pisos,calle , ciudad , codigo_postal, apartamentos ) :
        self.nombre=nombre
        self.numero_de_pisos=numero_de_pisos
        self.calle=calle
        self.ciudad=ciudad
        self.codigo_postal=codigo_postal
        self.apartamentos= apto

    def constructor(self):
        self.nombre=input('Ingrese el nombre')
        self.numero_de_pisos=input('Ingrese le numero de pisos:')
        self.ciudad=input('Ingrese ciudad:')
        self.codigo_postal=input('Ingrese el codigo postal:')
        self.apartamento=input ("Ingrese el numero de apartamentos:" )
        bd.update(objeto1)
    
    def mostar_direccion(self):
        nombre_edificio=input
        print('i')

    def mostrar_edificio(self):
        return f'El nombre del edificio es: {self.nombre} | Numero de pisos:{self.numero_de_pisos} |La Calle es:{self.calle}|La ciudad es :{self.ciudad}|El codigo postal es {self.codigo_postal}|Los apartamentos son:{self.apartamentos}'

objeto1=edificio()