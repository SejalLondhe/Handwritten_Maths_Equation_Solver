from flask import Flask, request, jsonify, send_from_directory

import os
import base64

app = Flask(__name__, static_folder="static")

@app.route('/')
def index():
    return send_from_directory('', 'login.html')

@app.route('/<page>')
def serve_page(page):
    if page in ["login.html", "index.html"]:
        return send_from_directory('', page)
    return "Page not found", 404

@app.route('/save_image', methods=['POST'])
def save_image():
    data = request.json['image']
    image_data = data.split(',')[1]
    image_bytes = base64.b64decode(image_data)

    image_path = os.path.join('static', 'canvas_image.jpg')
    with open(image_path, 'wb') as f:
        f.write(image_bytes)

    return jsonify({'message': 'Image saved successfully!', 'path': image_path})

if __name__ == '__main__':
    app.run(debug=True)
