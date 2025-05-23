import fitz  # PyMuPDF
import os

# Full path to your PDF
pdf_path = r"C:\Users\HP\OneDrive\Desktop\dataset for project consumer protection\New folder\datasets for cases\Vishnu_Agencies_Pvt_Ltd_Etc_vs_Commercial_Tax_Officer_Ors_Etc_on_16_December_1977.PDF"
output_folder = "extracted_txt"
os.makedirs(output_folder, exist_ok=True)

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

# Extract text from the PDF
extracted_text = extract_text_from_pdf(pdf_path)

# Create a txt filename based on the PDF filename
pdf_filename = os.path.basename(pdf_path)
txt_filename = pdf_filename.replace(".PDF", ".txt").replace(".pdf", ".txt")
txt_path = os.path.join(output_folder, txt_filename)

# Save extracted text to the txt file
with open(txt_path, "w", encoding="utf-8") as f:
    f.write(extracted_text)

print(f"Text extracted and saved to: {txt_path}")
