import PyPDF2

pdf_file_path = r"C:\Users\FREDDY.MEIJER\Downloads\Merged_PDF.pdf"

with open(pdf_file_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    extracted_text = ''

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        page_text = page.extract_text()

        extracted_text += page_text

lines = extracted_text.splitlines()

#NAHEFFINGSAANSLAGEN PRODUCT 02
with open('output.csv', 'w' , encoding='utf-8') as file:
    for i in range(len(lines)):
        if "Retouradres: Postbus 495, 2300 AL Leiden" in lines[i]:
            kenteken = lines[i+30]
            kenteken = kenteken[17:].split(' ',1)
            kenteken = kenteken[0]
            adres = kenteken + ";" + lines[i+1] + ";" + lines[i+2] + ";" + lines[i+3]
            adres = adres[:-27] + "\n"
            file.write(adres)