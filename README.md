# pdfThumb

Install the dependencies:

```shell
pip install -r requirements.txt
```

To run the serve, use:

```shell
python index.py
```

## Example of request

```shell
https://pdf-thumb-eight.vercel.app/get?pdf=YOUR_PDF_URL
```

## Queries Parameters

* `width`: Set the with of thumbnail
* `height`: Set the height of thumbnail
* `page_number`: Set the page number of file for generate thumbnail

## Dependencies

* Flask
* PyMuPDF
* request
* Pillow
