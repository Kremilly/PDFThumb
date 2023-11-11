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

@app.route('/get', methods=['GET'])
def generate_thumbnail():
    pdf_url = request.args.get('pdf')

    if pdf_url:
        thumbnail_buffer = generate_pdf_thumbnail(pdf_url)
        if thumbnail_buffer:
            thumbnail_buffer.seek(0)
            return send_file(thumbnail_buffer, mimetype='image/png')
        else:
            return "Error downloading the PDF file", 500
    else:
        return "Parameter 'pdf' missing", 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
