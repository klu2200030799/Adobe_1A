
import os
import json
import fitz  # PyMuPDF

def extract_headings_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    title = None
    outline = []
    seen_titles = set()

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                for line in b["lines"]:
                    line_text = "".join(span["text"] for span in line["spans"]).strip()
                    if not line_text or line_text in seen_titles:
                        continue

                    seen_titles.add(line_text)
                    font_size = max(span["size"] for span in line["spans"])
                    bold_count = sum(1 for span in line["spans"] if "bold" in span.get("font", "").lower())
                    
                    if font_size > 16 and not title:
                        title = line_text
                    elif font_size > 14:
                        outline.append({"level": "H1", "text": line_text, "page": page_num})
                    elif font_size > 12:
                        outline.append({"level": "H2", "text": line_text, "page": page_num})
                    elif font_size > 10:
                        outline.append({"level": "H3", "text": line_text, "page": page_num})

    doc.close()
    return {
        "title": title or "Untitled Document",
        "outline": outline
    }

input_dir = '/app/input'
output_dir = '/app/output'

for filename in os.listdir(input_dir):
    if filename.endswith('.pdf'):
        file_path = os.path.join(input_dir, filename)
        result = extract_headings_from_pdf(file_path)
        output_filename = os.path.splitext(filename)[0] + '.json'
        output_path = os.path.join(output_dir, output_filename)
        with open(output_path, 'w') as f:
            json.dump(result, f, indent=2)
