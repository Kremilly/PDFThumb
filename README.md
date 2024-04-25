# pdfThumb

Generate as PDF Thumbnail for remote document

## Example of request

```shell
https://api.kremilly.com/pdfthumb?pdf=YOUR_PDF_URL
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
