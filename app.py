from flask import Flask, render_template, request, redirect
from imgurpython import ImgurClient
import os

# Replace with your Imgur Client ID and Client Secret
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'

client = ImgurClient(CLIENT_ID, CLIENT_SECRET)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    # Save the uploaded file to a temporary location
    upload_folder = 'uploads'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)

    # Upload file to Imgur
    upload = client.upload_from_path(file_path, config=None, anon=True)
    imgur_link = upload['link']

    # Delete the temporary file after upload
    os.remove(file_path)

    return render_template('upload.html', imgur_link=imgur_link)

if __name__ == '__main__':
    app.run(debug=True)
