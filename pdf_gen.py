
from io import BytesIO
from flask import render_template
from xhtml2pdf import pisa

def generate_pdf_with_data(context):
    
    if context is None:
        context = [
                { 
                    "status": True,
                    "title": "Untitles",
                    "authors" : "John & Jane Doe",
                    "publish_date" : "1 Jan, 1977",
                    "keywords" : "article",
                    "summary" : "Lorem ipsum",
                    "url": "http://en.wikipdia.org"
            }
        ]
        
    html = render_template('pdf-template.html', articles=context)
    
    pdf_file = BytesIO()
    
    pisa_status = pisa.CreatePDF(html, dest=pdf_file)
    
    if pisa_status.err:
        return { 'status' : False, 'error': 'PDF generation failed!' }
    
    pdf_content = pdf_file.getvalue()
    
    return { 'status' : True, 'content': pdf_content }
