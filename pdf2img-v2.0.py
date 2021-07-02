#!/usr/bin/env python
from pdf2image import convert_from_path
import os
mode = 0o666
a = 'y'
print("PDF TO IMAGE CONVERTER 2.0\n\n")
print('***Write PDF file name with full directory if it is not in the same directory of this application')
print('***write only file name name if both are in same folder')
print('***Image will be downloaded in the same directory of the application, not PDF')
while a == 'y' or a == 'Y':
    pdf = input("\nPDF file name: ")
    dr = pdf.replace('.pdf', '')
    images = convert_from_path(pdf)
    os.mkdir(dr, mode)
    for i in range(len(images)):
        images[i].save(dr+'\\'+'page'+str(i)+'.jpg','JPEG')
    a = input('do you want to convirt another? y/n\n>>> ')
input('press any key to exit')
