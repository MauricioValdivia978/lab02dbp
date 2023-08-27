from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de animes de ejemplo
animes = [
    {
        'id': 1,
        'titulo': 'Mi Anime Favorito',
        'poster': 'https://ejemplo.com/poster.jpg',
        'categoria': 'Aventura',
        'rating': 9.5,
        'reviews': 100,
        'season': '2023 Verano',
        'tipo': 'TV'
    }
]

# Ruta de inicio
@app.route('/')
def index():
    return '¡Hola, mundo! Esta es mi primera API con Flask.'

# Ruta para obtener la lista de animes
@app.route('/anime', methods=['GET'])
def get_animes():
    return jsonify({'animes': animes})

# Ruta para crear un nuevo anime
@app.route('/anime', methods=['POST'])
def create_anime():
    new_anime = request.get_json()
    animes.append(new_anime)
    return jsonify({'message': 'Anime creado exitosamente'})

# Ruta para obtener detalles de un anime por ID
@app.route('/anime/<int:anime_id>', methods=['GET'])
def get_anime(anime_id):
    anime = next((anime for anime in animes if anime['id'] == anime_id), None)
    if anime:
        return jsonify({'anime': anime})
    return jsonify({'message': 'Anime no encontrado'}), 404

# Ruta para eliminar un anime por ID
@app.route('/anime/<int:anime_id>', methods=['DELETE'])
def delete_anime(anime_id):
    anime = next((anime for anime in animes if anime['id'] == anime_id), None)
    if anime:
        animes.remove(anime)
        return jsonify({'message': 'Anime eliminado exitosamente'})
    return jsonify({'message': 'Anime no encontrado'}), 404

# Ruta para actualizar un anime por ID
@app.route('/anime/<int:anime_id>', methods=['PUT'])
def update_anime(anime_id):
    updated_anime = request.get_json()
    anime = next((anime for anime in animes if anime['id'] == anime_id), None)
    if anime:
        anime.update(updated_anime)
        return jsonify({'message': 'Anime actualizado exitosamente'})
    return jsonify({'message': 'Anime no encontrado'}), 404

# Ruta para actualizar parcialmente un anime por ID
@app.route('/anime/<int:anime_id>', methods=['PATCH'])
def partial_update_anime(anime_id):
    partial_updates = request.get_json()
    anime = next((anime for anime in animes if anime['id'] == anime_id), None)
    if anime:
        anime.update(partial_updates)
        return jsonify({'message': 'Anime actualizado parcialmente exitosamente'})
    return jsonify({'message': 'Anime no encontrado'}), 404

if __name__ == '__main__':
    app.run()