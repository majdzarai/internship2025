# extract_text_Majd_Zarai.py

"""
Main script to extract text from documents (.pdf, .docx, .xlsx).
- PDF: uses PyMuPDF with OCR fallback (pytesseract)
- DOCX: extracts paragraphs, tables, and metadata
- XLSX: parses each sheet with optional empty row control

Output is saved as: majd_zarai_<filename>_cleaned.txt
"""

import os
import logging

# Import enhanced extractors
from Majd_Zarai_text_extractor.pdf_handler import extract_text_from_pdf_enhanced
from Majd_Zarai_text_extractor.pdf_handler import  extract_images_from_pdf
from Majd_Zarai_text_extractor.docx_handler import extract_text_from_docx_enhanced
from Majd_Zarai_text_extractor.excel_handler import extract_text_from_excel_enhanced



# Define folders
INPUT_DIR = "uploads"
OUTPUT_DIR = "extracted_texts"

# Logger configuration
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)


def save_text(original_filename: str, content: str):
    """
    Save extracted text to the output directory with custom naming:
    majd_zarai_<filename>_cleaned.txt

    Args:
        original_filename (str): Base name of the file (without extension).
        content (str): Text content to be saved.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_filename = f"majd_zarai_{original_filename}_cleaned.txt"
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        logger.info(f"[✓] Output saved to: {output_path}")
    except Exception as e:
        logger.error(f"[✗] Failed to write output file: {output_path} – {e}")


def extract_all_files():
    """
    Process all supported files in the uploads directory:
    - Dispatches to correct handler based on file extension
    - Logs activity and results
    - Skips unsupported file types
    """
    # Check input folder exists
    if not os.path.exists(INPUT_DIR):
        logger.error(f"[!] Input directory '{INPUT_DIR}' does not exist.")
        return

    files = os.listdir(INPUT_DIR)
    if not files:
        logger.warning("[!] No files found in the uploads directory.")
        return

    # Process each file
    for file in files:
        file_path = os.path.join(INPUT_DIR, file)
        filename, ext = os.path.splitext(file.lower())

        logger.info(f"[~] Processing: {file}")

        try:
            # Match by file extension
            if ext == ".pdf":
                text = extract_text_from_pdf_enhanced(file_path)
                extract_images_from_pdf(file_path) # ← image extraction call
            elif ext == ".docx":
                text = extract_text_from_docx_enhanced(file_path, include_metadata=True)
            elif ext == ".xlsx":
                text = extract_text_from_excel_enhanced(file_path, include_empty=False)
            else:
                logger.warning(f"[!] Unsupported file type: {ext} — Skipping '{file}'")
                continue

            # Save cleaned output
            if text:
                save_text(filename, text)
            else:
                logger.warning(f"[!] No content extracted from: {file}")

        except Exception as e:
            logger.error(f"[✗] Exception while processing '{file}': {e}")


# ─────────────────────────────
# ▶ Entrypoint
# ─────────────────────────────

if __name__ == "__main__":
    logger.info(" Starting document extraction...")
    extract_all_files()
    logger.info(" All files processed. Output saved to 'extracted_texts/'.")
