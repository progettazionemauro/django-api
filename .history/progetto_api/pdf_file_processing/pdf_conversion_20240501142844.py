# converto to image:
from pdf2image import convert_from_path

def pdf_to_image(input_file, output_file):
    images = convert_from_path(input_file)
    for i, image in enumerate(images):
        image.save(f'{output_file}_{i}.jpg', 'JPEG')

pdf_to_image('input.pdf', 'output_image')