from PIL import Image
from pdf2image import convert_from_path
from pathlib import Path
import os
import OdhaleniHranic

#nahrani pdfka
# cesta_pdfka = Path('../../a.pdf')
# cesta_pdfka = Path("C:\Users\Admin\Desktop\CropMasteikova\Ocni_terapeuticke_systemy_-_podklady_k_prednasce.pdf")
cesta_pdfka = Path(input("Přetáhněte sem pdf_soubor(tím se sem nahraje jeho cesta) a potvrďte Enterem:\n\t"))
print("\nNyní prosím čekejte, pdf se nahrává a zpracovává.")
pages = convert_from_path(cesta_pdfka, 600)

testpage = pages[0]
print("Nyní se zjišťuje rozložení slidů na strance.")
X0, Y0, sirka, vyska, pocet = OdhaleniHranic.Recognize(testpage)

print(f"Jedna stránka obsahuje {pocet} slajdů.")

(X0, Y0, X0 + sirka, Y0 + vyska)

kombinace = []
for x in X0:
    for y in Y0:
        kombinace.append([x, y, x + sirka, y+vyska])

print("PDF nahráno. Nyní se budou extrahovat slidy.")
slidy = []
for each_page in pages:
    for rez in kombinace:
        cropped_img = each_page.crop(rez).resize((1850,1308))
        # cropped_img.show()
        slidy.append(cropped_img)
        # break
    # break


im_blank = Image.open("./source/blank.jpg")
out_pdfko = str(cesta_pdfka.absolute().parent) + "/" + cesta_pdfka.stem + "_slides.pdf"
im_blank.save(out_pdfko, "PDF" ,resolution=100.0, save_all=True, append_images=slidy)

print(f"\nVe slozce původniho PDF byl vytvoren soubor se slidy.\nPozor! Nové PDF obsahuje bílé stránky!!!\n\nCesta nového souboru je:\n\t{out_pdfko}\n\nKonec programu")


os.system("echo K zavreni prikazove radky stisknete enter")
os.system("pause > nul")
# os.system("exit 0")

