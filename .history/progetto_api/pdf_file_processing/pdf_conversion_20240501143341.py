# converto to image:
from pdf2image import convert_from_path

def pdf_to_image(input_file, output_file):
    images = convert_from_path(input_file)
    for i, image in enumerate(images):
        image.save(f'{output_file}_{i}.jpg', 'JPEG')

pdf_to_image('input.pdf', 'output_image')

""" Ubuntu/Debian：

Install Poppler. Run the following command:

sudo apt-get install poppler-utils
After installation is complete, please restart your Python environment and try running the pdf_to_image function again. This way, you will be able to successfully convert PDF to images.

 """
# converto to html:

from PyPDF2 import PdfReader

def pdf_to_html(input_file, output_file):
    with open(input_file, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        
        # Extract text content page by page
        for page in reader.pages:
            text += page.extract_text()
        
        # Save as HTML file
        with open(output_file, 'w') as html_file:
            html_file.write(f"<html><body>{text}</body></html>")

pdf_to_html('input.pdf', 'output.html')

# converto to plain text:
""" Install dependencies: Use the pdfminer.six library

pip install pdfminer.six
     """
     
# converto to plain text:
from pdfminer.high_level import extract_text_to_fp

def pdf_to_text(input_file, output_file):
    with open(output_file, 'w') as text_file:
        with open(input_file, 'rb') as file:
            extract_text_to_fp(file, text_file)

pdf_to_text('input.pdf', 'output.txt')

# converto to word:

Install dependencies:

pip install python-docx PyPDF2

from docx import Document
from PyPDF2 import PdfReader

def pdf_to_word(input_file, output_file):
    with open(input_file, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        
        # Extract text content page by page
        for page in reader.pages:
            text += page.extract_text()
        
        # Create Word document
        doc = Document()
        doc.add_paragraph(text)
        
        # Save as Word document
        doc.save(output_file)

pdf_to_word('input.pdf', 'output.docx')