import os
from core.pdf_thumb import PDFThumb
from flask import Flask, request, send_file, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        'index.html', 
        title='PDFThumb - Home', 
        header='PDFThumb'
    )

@app.route('/get', methods=['GET'])
def generate_thumbnail():
    pdf_url = request.args.get('pdf')
    width = request.args.get('width') if request.args.get('width') else 300
    height = request.args.get('height') if request.args.get('height') else 400
    page_number = request.args.get('page_number') if request.args.get('page_number') else 0

    if pdf_url:
        thumbnail_buffer = PDFThumb.generate_pdf_thumbnail(
            url = pdf_url, 
            page_number = int(page_number), 
            size = (
                int(width), int(height)
            )
        )
        
        if thumbnail_buffer:
            thumbnail_buffer.seek(0)
            return send_file(thumbnail_buffer, mimetype='image/png')
        else:
            default_thumbnail = PDFThumb.get_default_thumbnail()
            
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
