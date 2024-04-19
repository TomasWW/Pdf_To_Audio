from flask import Flask

from routes import pdf_to_audio

app = Flask(__name__)
app.secret_key = "Some_Other_secret_key"
app.register_blueprint(pdf_to_audio)

if __name__ == "__main__":
    app.run(port=8080, debug=True)

