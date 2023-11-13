import requests
import fitz  # PyMuPDF
from PIL import Image
from io import BytesIO

DEFAULT_COVER = 'https://i.imgur.com/CvdZqTL.png'

class PDFThumb:
    
    @classmethod
    def generate_pdf_thumbnail(self, url, page_number = 0, size = (300, 400)):
        response = requests.get(url)

        if response.status_code == 200:
            pdf_document = fitz.open(stream=response.content, filetype = 'pdf')
            page = pdf_document[page_number]
            pix = page.get_pixmap()
            img = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
            img.thumbnail(size)
            thumbnail_buffer = BytesIO()
            img.save(thumbnail_buffer, format = 'png')
            pdf_document.close()
            return thumbnail_buffer
        else:
            return None
        
    @classmethod
    def get_default_thumbnail():
        default_image_url = DEFAULT_COVER
        response = requests.get(default_image_url)

        if response.status_code == 200:
            thumbnail_buffer = BytesIO(response.content)
            return thumbnail_buffer
        else:
            return None
