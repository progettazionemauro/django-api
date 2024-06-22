import pdf2image
import pytesseract

# Convert PDF to image
def pdf_to_image(input_file):
    images = pdf2image.convert_from_path(input_file)
    return images

# Use OCR to convert images into text.
def image_to_text(image):
    text = pytesseract.image_to_string(image)
    return text

# Save the text to a file
def save_text_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

# Extract text from PDF.
def extract_text_from_pdf(input_file, output_file):
    # Convert PDF to image
    images = pdf_to_image(input_file)
    
    extracted_text = ""
    
    # Extract text from each image.
    for image in images:
        text = image_to_text(image)
        extracted_text += text + "\n"
    
    # Save the extracted text to a file.
    save_text_to_file(extracted_text, output_file)

# Extract text from scanned PDF.
extract_text_from_pdf('scanned_document.pdf', 'extracted_text.txt')

print("OCR (Optical Character Recognition) magic completed! Now you can convert scanned PDF documents into editable text!")