from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

# Evento que recebe os dados de GPS
@socketio.on('gps_data')
def handle_gps_data(data):
    print(f"📍 Dados recebidos: {data}")
    # Emite os dados para todos os clientes conectados
    emit('update_map', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5000)
