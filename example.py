from weasyprint import HTML
pdf = HTML('http://example.net/hello/').write_pdf()