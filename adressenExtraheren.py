import PyPDF2
import tkinter as tk
from tkinter import filedialog

def selectFile():
    File=filedialog.askopenfilename(
        title="Selecteer PDF bestand",
        filetypes=[("PDF Bestanden","*.pdf"),("Alle bestanden","*.*")]
    )
    if File:
        return File

def adressenExtraheren(bestand):

    while True:
        product = input("Typ het producttype (alleen 02 op dit moment)") #04, 08, 09, 21, 22, 30 of 51): ")
        try:
            if product in ["02"]: #,"04","08","09","21","22","30","51"]:
                break
        except ValueError:
            print("Onjuist product gekozen.")

    with open(bestand, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        extracted_text = ""

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()

            extracted_text += page_text

    lines = extracted_text.splitlines()

    if product == "02":
        with open("output.csv", "w", encoding="utf-8") as file:
            file.write("KENTEKEN;NAAM;ADRES;POSTCODE\n")
            for i in range(len(lines)):
                if "Retouradres: Postbus 495, 2300 AL Leiden" in lines[i]:
                    uniekkenmerk = lines[i + 30]
                    uniekkenmerk = uniekkenmerk[17:].split(" ", 1)
                    uniekkenmerk = uniekkenmerk[0]
                    adres = (
                        uniekkenmerk
                        + ";"
                        + lines[i + 1]
                        + ";"
                        + lines[i + 2]
                        + ";"
                        + lines[i + 3]
                    )
                    adres = adres[:-27] + "\n"
                    file.write(adres)

adressenExtraheren(selectFile())