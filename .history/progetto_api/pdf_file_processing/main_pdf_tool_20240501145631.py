# Import the pdf_to_image function from pdf_conversion.py
from pdf_conversion import pdf_to_image

# Specify the input PDF file and the output text file
input_pdf = './SOPRALLUOGHI DIC23_MAR24.pdf'
output_text = 'extracted_text.txt'

# Call the pdf_to_image function to convert the input PDF file into images
pdf_to_image(input_pdf, output_text)

# Print a message indicating the completion of PDF to image conversion
print("PDF to image conversion completed!")

# Call the extract_text_from_pdf function to perform OCR
# Uncomment the following line once you have defined the extract_text_from_pdf function
# extract_text_from_pdf(input_pdf, output_text)

# Print a message indicating the completion of OCR
# Uncomment the following line once you have defined the extract_text_from_pdf function
# print("OCR (Optical Character Recognition) magic completed! Now you can convert scanned PDF documents into editable text!")
