# pdfThumb

Install the dependencies:

```shell
pip install -r requirements.txt
```

To run the serve, use:

```shell
python app.py
```

## Example of request

```shell
https://pdf-thumb-ijp59ght7-thesilvaemily.vercel.app/get?pdf=https://olacesar.com/e-books/biblia.pdf
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
