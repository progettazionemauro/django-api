# Import the functions from ocr.py
# from ocr import extract_text_from_pdf

# Import the pdf_to_image function from pdf_image_conversion.py
from pdf_conversion import pdf_to_image

# Specify the input PDF file and the output text file
input_pdf = 'SOPRALLUOGHI DIC23_MAR24.pdf'
output_text = 'extracted_text.txt'



# Call the extract_text_from_pdf function to perform OCR
extract_text_from_pdf(input_pdf, output_text)

# Print a message indicating the completion of OCR
print("OCR (Optical Character Recognition) magic completed! Now you can convert scanned PDF documents into editable text!")
