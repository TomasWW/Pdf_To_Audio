import tkinter as tk
from tkinter import filedialog

from PyPDF2 import PdfReader
from gtts import gTTS


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.msg = None
        self.body = None
        self.text = ""
        self.file_name = None
        self.title("Pdf to Audio")
        self.geometry("300x200")
        self.create_widget()
        self.language = "en"
        self.accent = None

    def create_widget(self):
        self.input_text()
        self.search_btn()
        self.convert_button()
        self.en_button()
        self.es_button()

    def search_btn(self):
        self.brw_btn = tk.Button(self, text="Browser",command=self.open_file_name)
        self.brw_btn.pack()

    def convert_button(self):
        self.convert_btn = tk.Button(self,text="Convert",command=self.text_to_audio)
        self.convert_btn.pack()
    def en_button(self):
        self.en_btn = tk.Button(self,text="En",command=self.en_btn_func)
        self.en_btn.pack()
    def es_button(self):
        self.es_btn = tk.Button(self,text="Es",command=self.es_btn_func)
        self.es_btn.pack()

    def en_btn_func(self):
        self.language = "en"
        self.accent = "us"
    def es_btn_func(self):
        self.language = "es"
        self.accent = "es"
    def open_file_name(self):
        self.file_name = filedialog.askopenfilename(initialdir="/", title="Select A File")
        self.body.configure(text=self.file_name)
        self.pdf_to_text()


    def input_text(self):
        self.body = tk.Label(self, height=1, width=200)
        self.body.pack()


    def pdf_to_text(self):
        reader = PdfReader(self.file_name)

        for i in range(len(reader.pages)):
            page = reader.pages[i]
            self.text += page.extract_text()




    def text_to_audio(self):

        tts = gTTS(self.text,lang=self.language,  tld=self.accent)

        mp3_file = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        tts.save(mp3_file)
        if tts.save:
            self.msg = tk.Label(text="Saved")
            self.msg.pack()
            print("saved")





if __name__ == "__main__":
    app = App()
    app.mainloop()
