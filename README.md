# pdfThumb

Clone this respository:

```shell
git clone https://github.com/kremilly/pdfThumb
```

Install the dependencies:

```shell
pip install -r requirements.txt
```

To run the server, use:

```shell
python index.py
```

## Example of request

```shell
https://pdfthumb.kremilly.com/get?pdf=YOUR_PDF_URL
```

## Queries Parameters

* `pdf`: Set the PDF file URL
* `width`: Set the with of thumbnail
* `height`: Set the height of thumbnail
* `page`: Set the page number of file for generate thumbnail

## Dependencies

* Flask
* PyMuPDF
* requests
* Pillow
