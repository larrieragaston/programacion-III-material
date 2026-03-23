import pytesseract
from pdf2image import convert_from_path
import sys

pdf_path = sys.argv[1] if len(sys.argv) > 1 else "/Users/glarriera/Downloads/Introducción - Presentación.pdf"

images = convert_from_path(pdf_path, dpi=300)

for i, img in enumerate(images, 1):
    text = pytesseract.image_to_string(img, lang="spa")
    print(f"=== SLIDE {i} of {len(images)} ===")
    print(text.strip())
    print()
