import streamlit as st
import os 
from PIL import Image
from pillow_heif import register_heif_opener

from flask import Flask 
from flask import Flask, jsonify, request

app = Flask(__name__) 

# Pass the required route to the decorator. 
@app.route("/hello") 
def hello(): 
	return "Salo"

@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    register_heif_opener()
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            # image.save(image.filename) 

            file_name = image.filename.lower()
            
            if file_name.endswith('.heic'):
                with Image.open(image) as heif_file:
                    
                    new_file_name = os.path.basename(file_name).replace('.heic','.jpg')
                    
                    new_file_path = os.path.abspath(os.path.join('converted_images', new_file_name))
                    heif_file.save(new_file_path, format='JPEG')

            return jsonify({
                "image": "/converted_images/"+new_file_name,
                })
    return "Qaytadan urinib ko'ring!"

if __name__ == "__main__": 
	app.run(debug=True) 






