# By this way we can create a python file in python.
# (wb) is stand for "write-binary" file.
# (w) is stand for "write" file
# (r) is stand for "read" file.
f = open("new_file.py", "w")
# By this way we can write anything we want in that python file we created.
f.write('print("Hello")')
# And make sure the file is closed.
f.close()

# By this way we execute the file which we created before.
with open("new_file.py", "r") as f:
    x = f.read()

print(x)

# By this way we can convert an html file into pdf.
# Here we just create a custom HTML file.
# (xhtml2pdf) this one is a library. There are many others as well.
from xhtml2pdf import pisa

def convert_html_to_pdf(html_string, pdf_path):
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)

    return not pisa_status.err

# HTML content
html_content = '''
<!DOCTYPE html>
<html>
<head>
    <title>PDF Example</title>
</head>
<body>
    <h1>Hello, world!</h1>
</body>
</html>
'''

# Generate PDF
pdf_path = "example.pdf"
if convert_html_to_pdf(html_content, pdf_path):
    print(f"PDF generated and saved at {pdf_path}")
else:
    print("PDF generation failed")













