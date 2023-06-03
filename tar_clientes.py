import random  # Importamos el módulo random para generar números aleatorios
import queue  # Importamos el módulo queue para usar una cola de prioridad
import time  # Importamos el módulo time para simular el paso del tiempo

# Definimos la clase Cliente para representar a un cliente
class Cliente:
    def __init__(self, tipo, subtipo):
        self.tipo = tipo
        self.subtipo = subtipo

# Definimos la clase Ventanilla para representar una ventanilla de atención
class Ventanilla:
    def __init__(self):
        self.ocupada = False  # Indica si la ventanilla está ocupada atendiendo a un cliente
        self.tiempo_restante = 0  # Tiempo restante de atención para el cliente actual

# Creamos una lista de ventanillas
N = 5  # Número de ventanillas
ventanillas = [Ventanilla() for _ in range(N)]  # Creamos N instancias de la clase Ventanilla y las almacenamos en una lista

# Creamos una cola de clientes con prioridad
cola_de_clientes = queue.PriorityQueue()

# Definimos las prioridades para los tipos de clientes
prioridades = {
    'con tarjeta': 3,
    'sin tarjeta': 2,
    'preferencial': 1
}

# Definimos los tipos y subtipos de clientes
tipos_de_clientes = ['con tarjeta', 'sin tarjeta', 'preferencial']
subtipos_de_clientes = {
    'con tarjeta': ['comunes', 'personas naturales VIP', 'personas jurídicas comunes', 'personas jurídicas VIP'],
    'sin tarjeta': [None],
    'preferencial': ['mayores de 60 años', 'con deficiencia física', 'con necesidades especiales']
}

# Simulamos el funcionamiento de las ventanillas para atender a los clientes
def atender_clientes(ventanillas, cola_de_clientes):
    for ventanilla in ventanillas:
        if not ventanilla.ocupada:  # Si la ventanilla está libre
            if not cola_de_clientes.empty():  # Si hay clientes en la cola
                _, cliente = cola_de_clientes.get()  # Obtenemos el cliente de mayor prioridad de la cola
                print(f"Atendiendo a cliente {cliente.tipo} {cliente.subtipo if cliente.subtipo else ''} en ventanilla {ventanillas.index(ventanilla)+1}")
                ventanilla.ocupada = True  # Marcamos la ventanilla como ocupada
                ventanilla.tiempo_restante = random.randint(5, 15)  # Generamos un tiempo aleatorio de atención para el cliente
        else:
            ventanilla.tiempo_restante -= 1  # Decrementamos el tiempo restante de atención
            if ventanilla.tiempo_restante == 0:  # Si el tiempo de atención ha terminado
                ventanilla.ocupada = False  # Marcamos la ventanilla como libre
                print(f"Ventanilla {ventanillas.index(ventanilla)+1} libre")

# Simulamos el escenario en el que una ventanilla deja de atender
def pausa_ventanilla(ventanillas):
    ventanilla = random.choice(ventanillas)
    if ventanilla.ocupada:
        print(f"Ventanilla {ventanillas.index(ventanilla)+1} deja de atender por un momento")
        ventanilla.ocupada = False
        ventanilla.tiempo_restante = 0

# Simulamos el paso del tiempo
for t in range(200):  # Simulamos 200 unidades de tiempo
    # Simulamos la llegada de clientes
    if random.random() < 0.1:  # 10% de probabilidad de que llegue un cliente en cada unidad de tiempo
        tipo = random.choice(tipos_de_clientes)
        subtipo = random.choice(subtipos_de_clientes[tipo])
        cliente = Cliente(tipo, subtipo)
        cola_de_clientes.put((prioridades[tipo], cliente))
        print(f"Llega cliente {cliente.tipo} {cliente.subtipo if cliente.subtipo else ''} en tiempo {t}")

    atender_clientes(ventanillas, cola_de_clientes)
    if random.random() < 0.05:  # 5% de probabilidad de que una ventanilla deje de atender
        pausa_ventanilla(ventanillas)

    time.sleep(0.1)