from PIL import Image
from pdf2image import convert_from_path
from pathlib import Path
import os

#nahrani pdfka
# cesta_pdfka = Path('./a.pdf')
cesta_pdfka = Path(input("Pretahnete sem pdf_soubor (tim se sem nahraje jeho cesta): \t"))
print("\nNyní prosím čekejte, pdf se nahrává a zpracovává.")
pages = convert_from_path(cesta_pdfka, 600)

#hranice
leva = 317
prava = 4200
horni = 686
dolni = 5890

sinis =2169
dext = 2353

first = 2074
second = 2596
third = 3978
fourth =4504

#list slidu
hranice = [
    (leva, horni, sinis, first),
    (dext, horni, prava, first),
    (leva, second, sinis, third),
    (dext, second, prava, third),
    (leva, fourth, sinis, dolni),
    (dext, fourth, prava, dolni)
]

print("PDF nahrano. Nyni se budou extrahovat slidy.")
slidy = []
for each_page in pages:
    for rez in hranice:
        cropped_img = each_page.crop(rez)
        # cropped_img.show()
        slidy.append(cropped_img)
        # break
    # break


im_blank = Image.open("blank.jpg")
out_pdfko = str(cesta_pdfka.absolute().parent) + "/" + cesta_pdfka.stem + "_slides.pdf"
im_blank.save(out_pdfko, "PDF" ,resolution=100.0, save_all=True, append_images=slidy)

print(f"\nVe slozce původniho PDF byl vytvoren soubor se slidy.\nPozor! Nové PDF obsahuje bílé stránky!!!\n\nCesta nového souboru je:\n\t{out_pdfko}\n\nKonec programu")

os.system("echo K zavreni prikazove radky stisknete enter")
os.system("pause > nul")

