import random
import time
import socketio

# Conectar ao servidor Flask
sio = socketio.Client()

# Defina as coordenadas de Brasília como ponto inicial
latitude = -15.7801
longitude = -47.9292

# Função para simular o movimento (com variação aleatória)
def generate_gps_data():
    global latitude, longitude
    # Simulando um movimento mais restrito em torno de Brasília
    latitude += random.uniform(-0.00001, 0.00001)  # Movendo com menos variação
    longitude += random.uniform(-0.00001, 0.00001)  # Movendo com menos variação
    return {
        'latitude': latitude,
        'longitude': longitude,
        'timestamp': time.time()
    }

# Enviar dados de GPS para o servidor
def send_gps_data():
    data = generate_gps_data()
    sio.emit('gps_data', data)
    print(f"Enviando dados: {data}")

# Conectar ao servidor Flask
sio.connect('http://localhost:5000')

# Enviar dados de GPS a cada 1 segundo
while True:
    send_gps_data()
    time.sleep(1)  # A cada segundo, a posição será atualizada
