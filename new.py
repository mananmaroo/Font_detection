import fitz  # PyMuPDF
import re
file_path = r'/Users/mananmaroo/Desktop/FontDetector/Manan Maroo.pdf'

def detect_font_changes(pdf_path):
    doc = fitz.open(pdf_path)
    font_changes = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]

        prev_font = None

        for b in blocks:
            for line in b["lines"]:
                for span in line["spans"]:
                    text = re.sub(r'[^a-zA-Z0-9\s]', '', span["text"]).strip()
                    if text:
                        if prev_font is None or span["font"] != prev_font:
                            font_changes.append((page_num + 1, line["bbox"][3], text, span["font"]))
                        prev_font = span["font"]

    doc.close()
    return font_changes

# Example usage:
pdf_path = 'path_to_your_pdf.pdf'  # Replace with your actual PDF file path

font_changes = detect_font_changes(file_path)

print("Font changes detected:")
for page_num, _, text, font in font_changes:
    print(f"Page {page_num}, Font: {font}, Text: '{text}'")