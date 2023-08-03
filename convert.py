# Converts PDF to images. Poppler and Tesseract need to be installed. You should install poppler within the conda env.
# Make sure to replace the path names with the appropriate paths.

from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader
from PIL import Image
from tqdm import tqdm  # tqdm is for showing a progress bar
import time
from borb.pdf import Document
from borb.pdf import PDF
from pathlib import Path
import typing
import os
import subprocess

        

def fix_pdf(in_path: Path, out_path: Path) -> None:
   doc: typing.Optional[Document] = None
   with open(in_path, "rb") as fh:
       doc = PDF.loads(fh)
   with open(out_path, "wb") as fh:
       PDF.dumps(fh, doc)
       
       
def ocr_and_save_to_txt(input_folder, output_folder):
    # Get a list of all files in the input folder
    file_list = os.listdir(input_folder)

    # Iterate through the list of file names
    for filename in file_list:
        # Construct the input image file path
        input_image_path = os.path.join(input_folder, filename)

        # Get the base name of the file without the extension
        file_basename = os.path.splitext(filename)[0]

        # Construct the output text file path
        output_text_path = os.path.join(output_folder, f"{file_basename}")

        # Execute the Tesseract command using subprocess
        command = f"tesseract {input_image_path} {output_text_path}"
        subprocess.run(command, shell=True)

Image.MAX_IMAGE_PIXELS = 2**40

# Path to the PDF file
pdf_path = "C:\\Users\\your_username\\PDF.pdf"
pdf_path_fixed = "C:\\Users\\your_username\\PDFFixed.pdf"

fix_pdf(pdf_path, pdf_path_fixed)


# Convert the PDF to images. Slow for large files. Just let it be unless you get an error.
images = convert_from_path(pdf_path_fixed, poppler_path="C:\\Users\\your_username\\anaconda3\\envs\\YourENVWorkspace\\Library\\bin")

# Save images
for i, image in enumerate(tqdm(images, desc="Saving images", unit="image", ncols=100)):
    image.save('C:\\Users\\your_username\\Documents\\PDFTitle\\output_page_{}.png'.format(i), 'PNG')


ocr_and_save_to_txt("C:\\Users\\your_username\\Documents\\PDFTitle", "C:\\Users\\your_username\\Documents\\PDFTitleText")
