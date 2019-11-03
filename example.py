from weasyprint import HTML
pdf = HTML('http://www.google.com').write_pdf()