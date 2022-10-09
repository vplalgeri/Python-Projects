from importlib.resources import path
import os
from PyPDF2 import PdfFileMerger
path = input ("Enter the path:")
os.chdir(path)
merger=PdfFileMerger()
for item in os.listdir(path):
    if item.endswith('pdf'):
        merger.append(item)
merger.write('output.pdf')
file_name= input("Enter the file Name:")
oldname= ('output.pdf')
os.rename(oldname, file_name)
merger.close()