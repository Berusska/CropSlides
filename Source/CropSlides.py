from PIL import Image
from pdf2image import convert_from_path
from pathlib import Path
import OdhaleniHranic

#nahrani pdfka
# cesta_pdfka = Path('../../a.pdf')
# cesta_pdfka = Path("C:\Users\Admin\Desktop\CropMasteikova\Ocni_terapeuticke_systemy_-_podklady_k_prednasce.pdf")
cesta_pdfka = input("Přetáhněte sem pdf_soubor(tím se sem nahraje jeho cesta) a potvrďte Enterem:\n\t")
if cesta_pdfka == "":
    print("\nZadaná cesta je prázdná, nejspíš jste stiskli v předstihu omylem klávesu Enter.\nSpusťte program znovu ...\n")
    quit()
elif Path(cesta_pdfka).is_file() and Path(cesta_pdfka).suffix == ".pdf":
    cesta_pdfka = Path(cesta_pdfka)
    print("\nNyní prosím čekejte, pdf se nahrává a zpracovává.")
else:
    print("Nebyl načten žádný soubor.\n\tmožné důvody:\n\t\t-stisknutí klavesy enter před vložením cesty souboru\n\t\t-soubor neexistuje\n\t\t-cesta je nevalidní\n\nSpusťte program znovu ...\n")
    exit()
    
pages = convert_from_path(cesta_pdfka, 400)

testpage = pages[0]
print("Nyní se zjišťuje rozložení slidů na strance.")
X0, Y0, sirka, vyska, pocet = OdhaleniHranic.Recognize(testpage)

print(f"Jedna stránka obsahuje {pocet} slajdů.")


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

im_blank = Image.open("./Source/blank.jpg")
out_pdfko = str(cesta_pdfka.absolute().parent) + "\\" + cesta_pdfka.stem + "_slides.pdf"
im_blank.save(out_pdfko, "PDF" ,resolution=100.0, save_all=True, append_images=slidy)

print(f"\nVe slozce původniho PDF byl vytvoren soubor se slidy.\nPozor! Nové PDF obsahuje bílé stránky!!!\n\nCesta nového souboru je:\n\t{out_pdfko}\n\nKonec programu")


