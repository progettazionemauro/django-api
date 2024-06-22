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