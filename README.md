# 🖼️ Simple Imgur Uploader

A lightweight web application that allows users to easily upload images to Imgur using Python (Flask) and HTML.

<img src="https://imgur.com/78jE0Cj.png" alt="YouTube Downloader" width="500" style="border-radius: 15px;">

<img src="https://imgur.com/2fSPXEw.png" alt="YouTube Downloader" width="500" style="border-radius: 15px;">

## ✨ Features

- Simple and intuitive user interface
- Direct upload to Imgur
- Copy-to-clipboard functionality for uploaded image links

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+
- Flask
- imgurpython

## 🚀 Installation

1. Clone the repository:
   ```
   git clone https://github.com/TaahDev/Imgur-Image-Uploader.git
   cd Imgur-Image-Uploader
   ```

2. Install the required packages:
   ```
   pip install flask imgurpython
   ```

3. Set up your Imgur API credentials:
   - Go to [Imgur API](https://api.imgur.com/oauth2/addclient)
   - Select "Anonymous usage without user authorization" for the Authorization type
   - Type in `https://api.imgur.com/` for the Authorization callback URL
   - Replace `CLIENT_ID` and `CLIENT_SECRET` in `app.py` with your Imgur API credentials

## 🖱️ Usage

1. Run the application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Select an image file and click "Upload"

4. After successful upload, you'll see the Imgur link. Click to copy or Ctrl+Click to open in a new tab.

## 📁 Project Structure

- `app.py`: Main Flask application
- `templates/`: HTML templates
  - `index.html`: Home page with upload form
  - `upload.html`: Success page with Imgur link
- `static/`: CSS stylesheets and other static files

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License 

This project is open source and available under the [CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/) license.

## 🙏 Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [imgurpython](https://github.com/Imgur/imgurpython)
- [Imgur API](https://apidocs.imgur.com/)
