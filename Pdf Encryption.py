from tkinter import *
from PyPDF2 import PdfFileReader,PdfFileWriter
from tkinter.filedialog import *
from tkinter import messagebox
import getpass

root = Tk()
root.update()

in_path=askopenfilename()
if '.pdf' not in in_path:
    messagebox.showwarning("Invalid file extension", "Please select a pdf file")
root.withdraw()
file_pdf=PdfFileReader(in_path)
### Object for pdf writer
out_pdf=PdfFileWriter()

for i in range(file_pdf.numPages):
    page_details=file_pdf.getPage(i)
    ### Add to the output page
    out_pdf.addPage(page_details)
    
password=getpass.getpass(prompt="Enter password to encrypt pdf :") 
out_pdf.encrypt(password)

out_path=asksaveasfilename()
if '.pdf' not in out_path:
    messagebox.showwarning("Invalid file extension", "Please save the file as .pdf")
    out_path=asksaveasfilename()

with open(out_path,"wb") as filename:
    out_pdf.write(filename)
root.destroy()