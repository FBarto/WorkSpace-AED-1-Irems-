class Auto:

    def __init__ (self,marca,modelo,año,precio_por_kilometro,seguro_alquiler,dni_cliente,nombre_del_arrendatario,kilometros_recorridos):
        self.marca = marca
        self.modelo= modelo
        self.año=año
        self.precio_por_kilometro=precio_por_kilometro
        self.seguro_alquiler=seguro_alquiler
        self.dni_cliente=dni_cliente
        self.nombre_del_arrendatario=nombre_del_arrendatario
        self.kilometros_recorridos=kilometros_recorridos


    def mostrarDatos(self):
        print(f"El señor {self.nombre_del_arrendatario} Dni:{self.dni_cliente}. Alquilo el auto {self.marca} {self.modelo} año: {self.año}")
        print(f"Acordando del pago de {self.precio_por_kilometro} y recorrio {self.kilometros_recorridos} incluyendo el seguro de {self.seguro_alquiler}")
        print(f"El precio total a pagar es de {str((self.kilometros_recorridos * self.precio_por_kilometro) + self.seguro_alquiler)}")

