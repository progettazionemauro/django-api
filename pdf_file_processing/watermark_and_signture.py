from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
import io

# Add watermark to PDF
def add_watermark(input_file, output_file, watermark_text):
    reader = PdfReader(input_file)
    writer = PdfWriter()

    watermark_buffer = io.BytesIO()

    # Create a PDF with watermark.
    c = canvas.Canvas(watermark_buffer)
    c.setFont("Helvetica", 48) # Pay attention to the choice of font.
    c.rotate(45)
    c.translate(-500, -500)
    c.setFillAlpha(0.3)
    c.drawString(400, 400, watermark_text)
    c.save()

    watermark_buffer.seek(0)
    watermark_pdf = PdfReader(watermark_buffer)

    # Traverse each page.
    for i, page in enumerate(reader.pages, start=1):
        watermark_page = watermark_pdf.pages[0]

        # Add watermark to the page
        page.merge_page(watermark_page)
        writer.add_page(page)

    # Save the file with watermark.
    with open(output_file, 'wb') as file:
        writer.write(file)

# Add digital signature to PDF
def add_signature(input_file, output_file, signature_image):
    reader = PdfReader(input_file)
    writer = PdfWriter()

    # Traverse each page.
    for i, page in enumerate(reader.pages, start=1):
        # Add a signature image to the bottom right corner of the page.
        page.merge_page(signature_image)
        writer.add_page(page)

    # Save the document with a signature.
    with open(output_file, 'wb') as file:
        writer.write(file)

# Use the functions add_watermark() and add_signature() to add watermark and signature.
watermark_text = "Confidential document, do not disclose."
signature_image = PdfReader("signature.pdf").pages[0]

add_watermark('part_21-30.pdf', 'document_with_watermark.pdf', watermark_text)
add_signature('document_with_watermark.pdf', 'document_with_watermark_and_signature.pdf', signature_image)

print("Watermark and signature magic completed! You can now make your PDF files more secure and professional!")