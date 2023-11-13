import os
from flask import Flask, request, send_file
import requests
import fitz  # PyMuPDF
from PIL import Image
from io import BytesIO

app = Flask(__name__)

def generate_pdf_thumbnail(url, page_number=0, size=(300, 400)):
    response = requests.get(url)

    if response.status_code == 200:
        pdf_document = fitz.open(stream=response.content, filetype="pdf")
        page = pdf_document[page_number]
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img.thumbnail(size)
        thumbnail_buffer = BytesIO()
        img.save(thumbnail_buffer, format="PNG")
        pdf_document.close()
        return thumbnail_buffer
    else:
        return None

def get_default_thumbnail():
    default_image_url = 'https://i.imgur.com/CvdZqTL.png'
    response = requests.get(default_image_url)

    if response.status_code == 200:
        thumbnail_buffer = BytesIO(response.content)
        return thumbnail_buffer
    else:
        return None

@app.route('/get', methods=['GET'])
def generate_thumbnail():
    pdf_url = request.args.get('pdf')
    width = request.args.get('width') if request.args.get('width') else 300
    height = request.args.get('height') if request.args.get('height') else 400
    page_number = request.args.get('page_number') if request.args.get('page_number') else 0

    if pdf_url:
        thumbnail_buffer = generate_pdf_thumbnail(pdf_url, page_number=int(page_number), size=(int(width), int(height)))
        if thumbnail_buffer:
            thumbnail_buffer.seek(0)
            return send_file(thumbnail_buffer, mimetype='image/png')
        else:
            default_thumbnail = get_default_thumbnail()
            if default_thumbnail:
                default_thumbnail.seek(0)
                return send_file(default_thumbnail, mimetype='image/png')
            else:
                return "Error loading default image", 500
    else:
        return "Parameter 'pdf' missing", 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
