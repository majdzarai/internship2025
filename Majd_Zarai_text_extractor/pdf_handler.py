import fitz  # PyMuPDF for reading PDFs
import pytesseract  # OCR engine for scanned documents
from pdf2image import convert_from_path  # Converts PDF pages to images
import tempfile  # For creating temporary directories
import os 

# ─────────────────────────────────────────────────────────────
#  ORIGINAL FUNCTION — Core working solution (no changes)
# ─────────────────────────────────────────────────────────────

def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file. If the file has no machine-readable text,
    OCR is automatically applied using pytesseract.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        str: The extracted text (machine or OCR).
    """
    try:
        doc = fitz.open(file_path)
        full_text = ""
        requires_ocr = True  # Assume OCR is needed unless we find extractable text

        for page_number, page in enumerate(doc):
            text = page.get_text()
            if text.strip():
                full_text += text + "\n"
                requires_ocr = False  # Found extractable text
            else:
                print(f"[INFO] No extractable text on page {page_number + 1}, may fallback to OCR...")

        # If none of the pages had extractable text, fallback to OCR
        if requires_ocr:
            print(f"[INFO] Applying OCR on scanned PDF: {file_path}")
            with tempfile.TemporaryDirectory() as temp_dir:
                images = convert_from_path(file_path, dpi=300, fmt='png', output_folder=temp_dir)
                for i, image in enumerate(images):
                    ocr_text = pytesseract.image_to_string(image, lang='eng')
                    full_text += f"\n[OCR - Page {i + 1}]\n{ocr_text}"

        return full_text.strip()

    except Exception as e:
        print(f"[ERROR] Failed to extract PDF: {file_path} – {e}")
        return ""

# ─────────────────────────────────────────────────────────────
#  BONUS FUNCTION — Enhanced, production-grade version
# ─────────────────────────────────────────────────────────────

import logging

try:
    from tqdm import tqdm  #  progress bar for multi-page PDFs
    USE_TQDM = True
except ImportError:
    USE_TQDM = False  # Fallback if tqdm isn't available

# Configure a basic logger for this module
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def extract_text_from_pdf_enhanced(file_path, lang='eng'):
    """
    Enhanced version of PDF extraction with per-page OCR, logging, and progress tracking.

    Features:
    - Attempts to extract machine-readable text with PyMuPDF.
    - Falls back to Tesseract OCR per page if text is not available.
    - Logs detailed statistics and handles errors gracefully.
    - Optional: shows a progress bar if tqdm is installed.

    Args:
        file_path (str): Path to the input PDF file.
        lang (str): Language code for OCR (default: 'eng').

    Returns:
        str: The extracted and concatenated full text from the PDF.
    """
    try:
        doc = fitz.open(file_path)
        total_pages = len(doc)
        full_text = []
        ocr_pages = 0
        native_pages = 0

        # Use tqdm to show progress if installed
        iterator = tqdm(enumerate(doc), total=total_pages, desc="Processing PDF") if USE_TQDM else enumerate(doc)

        for page_number, page in iterator:
            # Attempt to extract machine-readable text
            text = page.get_text()
            if text.strip():
                full_text.append(text)
                native_pages += 1
            else:
                # Log and fallback to OCR for this page
                logger.info(f"Page {page_number + 1} has no extractable text. Applying OCR.")
                with tempfile.TemporaryDirectory() as temp_dir:
                    image = convert_from_path(
                        file_path,
                        dpi=300,
                        fmt='png',
                        output_folder=temp_dir,
                        first_page=page_number + 1,
                        last_page=page_number + 1
                    )[0]
                    ocr_text = pytesseract.image_to_string(image, lang=lang)
                    full_text.append(f"\n[OCR - Page {page_number + 1}]\n{ocr_text.strip()}")
                    ocr_pages += 1

        # Summary log
        logger.info(f"Extraction complete: {native_pages} native pages, {ocr_pages} OCR pages.")

        return "\n".join(full_text).strip()

    except Exception as e:
        logger.error(f"Enhanced PDF extraction failed for {file_path}: {e}")
        return ""
    



# ─────────────────────────────────────────────────────────────
#  BONUS FUNCTION — extract images from pdf
# ─────────────────────────────────────────────────────────────

def extract_images_from_pdf(file_path, output_root_dir='extracted_texts/majd_extracted_images_from_pdf'):
    """
    Extracts and saves all embedded images from a PDF using PyMuPDF.
    
    Args:
        file_path (str): Full path to the input PDF file.
        output_root_dir (str): Root folder where images will be stored.
    
    Returns:
        int: Number of images extracted.
    """
    try:
        doc = fitz.open(file_path)
        pdf_name = os.path.splitext(os.path.basename(file_path))[0]
        
        # Create per-document image folder
        image_dir = os.path.join(output_root_dir, f"{pdf_name}_images")
        os.makedirs(image_dir, exist_ok=True)

        image_count = 0

        for page_index in range(len(doc)):
            images = doc.get_page_images(page_index)

            for img_index, img in enumerate(images):
                xref = img[0]  # reference to the image
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                image_filename = f"page{page_index+1}_img{img_index+1}.{image_ext}"

                image_path = os.path.join(image_dir, image_filename)
                with open(image_path, "wb") as f:
                    f.write(image_bytes)

                image_count += 1

        logger.info(f"[✓] Extracted {image_count} image(s) from '{pdf_name}.pdf' into: {image_dir}")
        return image_count

    except Exception as e:
        logger.error(f"[✗] Failed to extract images from PDF '{file_path}': {e}")
        return 0




