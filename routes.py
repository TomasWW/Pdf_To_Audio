import os
import tempfile

from PyPDF2 import PdfReader
from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash, send_file
from gtts import gTTS

pdf_to_audio = Blueprint("home", __name__)


@pdf_to_audio.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@pdf_to_audio.route("/text_to_pdf", methods=["GET", "POST"])
def pdf_to_text():
    pdf_file = request.files['pdfFile']
    language = request.form['language']

    if pdf_file.filename.split(".")[1] != "pdf":
        flash('Please Select a PDF format')
    else:

        pdf_file = request.files['pdfFile']
        language = request.form['language']

        if pdf_file.filename.split(".")[1] != "pdf":
            flash('Please select a PDF file')
            return redirect(url_for('home.home'))

        text = ""

        reader = PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text()

        if language == "es":
            tts = gTTS(text, lang="es", tld="es")
        elif language == "en":
            tts = gTTS(text, lang="en", tld="us")
        else:
            flash("Invalid language selection")
            return redirect(url_for('home.home'))

        mp3_file_name = f'{pdf_file.filename.split(".")[0]}.mp3'

        temp_file_path = os.path.join(tempfile.gettempdir(), mp3_file_name)
        tts.save(temp_file_path)

        return send_file(temp_file_path, as_attachment=True)
