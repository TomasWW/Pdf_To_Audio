# PDF to Audio Converter

This Python application converts text from PDF files to audio files in MP3 format. It utilizes the tkinter library for the graphical user interface, PyPDF2 for PDF processing, and gTTS (Google Text-to-Speech) for converting text to speech.

## Installation

Clone this repository to your local machine:
git clone https://github.com/your_username/pdf-to-audio-converter.git

pip install PyPDF2 gtts

## Usage

Upon launching the application, you'll see a window with a "Browser" button.

1. Click the "Browser" button to select a PDF file from your system.
2. After selecting the file, its path will be displayed in the window.
3. Choose the desired language by clicking the "En" button for English or the "Es" button for Spanish. By default, the language is set to English.
4. Click the "Convert" button to start the conversion process. The text from the PDF will be converted to audio in the selected language.
5. Once the conversion is complete, you will be prompted to save the generated MP3 file. Choose a location and file name for the audio file and click "Save".
6. A confirmation message will be displayed in the application window, indicating that the audio file has been saved successfully.

## Notes

- This application supports PDF files with text content only. It may not work properly with scanned documents or images.
- Ensure that you have an active internet connection during the conversion process, as gTTS requires internet access to generate speech.
- For best results, make sure the PDF file's text is formatted correctly to avoid any issues with text extraction.
