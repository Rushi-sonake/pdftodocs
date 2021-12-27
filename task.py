"""Template robot with Python."""
import pikepdf
from pdf2docx import parse
def File_decrypt():
    My_doc=pikepdf.open('PDF_PP_text.pdf', password='Propero$234')
    My_doc.save('unlocked.pdf')

def convert_docs():
    pdf='unlocked.pdf'
    docs= 'extracted.docx'
    parse(pdf, docs, start=0, end=None)

def minimal_task():
    print("Done.")


if __name__ == "__main__":
    minimal_task()
    File_decrypt()
    convert_docs()