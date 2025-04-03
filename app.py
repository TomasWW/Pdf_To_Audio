import tkinter as tk
from tkinter import filedialog

from PyPDF2 import PdfReader
from gtts import gTTS


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Initialize variables
        self.msg = None
        self.body = None
        self.text = ""
        self.file_name = None
        self.language = "en"
        self.accent = None
        
        # Configure window properties
        self.title("Pdf to Audio")
        self.geometry("300x200")
        
        # Create UI elements
        self.create_widget()


    def create_widget(self):
        """Create all UI elements."""        
        self.input_text()
        self.search_btn()
        self.convert_button()
        self.en_button()
        self.es_button()

   def search_btn(self):
        """Create a button to browse for a PDF file."""
        self.brw_btn = tk.Button(self, text="Browse", command=self.open_file_name)
        self.brw_btn.pack()
       
    def convert_button(self):
        """Create a button to convert the extracted text into an audio file."""
        self.convert_btn = tk.Button(self, text="Convert", command=self.text_to_audio)
        self.convert_btn.pack()
        
    def en_button(self):
        """Button to select English as the language for speech conversion."""
        self.en_btn = tk.Button(self, text="En", command=self.en_btn_func)
        self.en_btn.pack()
        
    def en_button(self):
        """Button to select English as the language for speech conversion."""
        self.en_btn = tk.Button(self, text="En", command=self.en_btn_func)
        self.en_btn.pack()

    def en_btn_func(self):
        """Set language to English with a US accent."""
        self.language = "en"
        self.accent = "us"
        
    def es_btn_func(self):
        """Set language to Spanish."""
        self.language = "es"
        self.accent = "es"
        
    def open_file_name(self):
        """Open a file dialog to select a PDF file and extract its text."""
        self.file_name = filedialog.askopenfilename(
            initialdir="/", title="Select A File", filetypes=[("PDF Files", "*.pdf")]
        )

        if self.file_name:  # Check if a file was actually selected
            self.body.configure(text=self.file_name)
            self.pdf_to_text()


    def input_text(self):
        """Create a label to display the selected file name."""
        self.body = tk.Label(self, height=1, width=200)
        self.body.pack()

   def pdf_to_text(self):
        """Extract text from the selected PDF file."""
        try:
            reader = PdfReader(self.file_name)
            self.text = ""  # Reset text before extracting

            for page in reader.pages:
                extracted_text = page.extract_text()
                if extracted_text:
                    self.text += extracted_text + "\n"
        except Exception as e:
            print(f"Error reading PDF: {e}")




    def text_to_audio(self):
        """Convert extracted text to an MP3 audio file."""
        if not self.text.strip():
            print("No text extracted. Please select a valid PDF.")
            return

        try:
            tts = gTTS(self.text, lang=self.language, tld=self.accent)

            # Ask user for the save location
            mp3_file = filedialog.asksaveasfilename(
                defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")]
            )

            if mp3_file:
                tts.save(mp3_file)
                self.msg = tk.Label(text="Saved")
                self.msg.pack()
                print("File saved successfully.")
        except Exception as e:
            print(f"Error converting text to audio: {e}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
