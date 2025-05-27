#  DEV_LOG_Majd_Zarai.md  
DYDON AI – Internship 2025 Submission

This development log outlines the architecture, design rationale, implementation process, and key technologies behind my solution for the DYDON AI Internship 2025 challenge.

---

##  Objective

Design and implement a Python-based system that:
- Extracts text from `.pdf`, `.docx`, and `.xlsx` documents
- Applies OCR to scanned PDFs
- Is modular, readable, and production-ready
- Includes logging, error handling, and extensibility
- Optionally includes a frontend for user interaction

---

##  Solution Architecture

I structured the project around a **modular pipeline**, where each file type is handled by a dedicated extractor script under the `Majd_Zarai_text_extractor/` directory:

### 1. `pdf_handler.py`
- ✅ Extracts text from PDFs using `PyMuPDF` (fitz)
- ✅ If no machine-readable text exists, applies `pytesseract` OCR on each page using `pdf2image`
- ✅ Extracts embedded images using `fitz.get_page_images()` and stores them by page in a dedicated folder

### 2. `docx_handler.py`
- ✅ Parses paragraphs and tables using `python-docx`
- ✅ Ensures empty text is filtered out
- ✅ Optional support prepared for reading DOCX metadata

### 3. `excel_handler.py`
- ✅ Uses `openpyxl` to parse all sheets
- ✅ Cleans and formats rows with tab delimiters
- ✅ Skips empty rows for concise output

### 4. `extract_text_Majd_Zarai.py`
- ✅ CLI pipeline that:
  - Iterates over files in the `uploads/` folder
  - Delegates to the correct handler
  - Saves output `.txt` files with my name in the filename
  - Logs all actions and errors

---

##  Front-End – `majd_front.py`

To complement the CLI, I developed a clean and intuitive **Streamlit front-end** for real-time interaction.

### Features:
-  Drag-and-drop file upload
-  Live preview of extracted text
-  Button to toggle and preview images (per-page thumbnails)
-  Download button for extracted `.txt` results
-  Custom gradient background (red-to-white) and modern card styling
-  Fully responsive layout and optimized UX

---

##  Design Considerations

- **Modularity**: Each file type is handled in isolation for maintainability and testability.
- **Clarity**: All functions include docstrings and inline comments.
- **Logging**: All major actions and exceptions are logged to inform the user.
- **Extensibility**: New formats or NLP processing steps could be added with minimal changes.
- **Naming conventions**: Output files are saved as `majd_zarai_<filename>_cleaned.txt` per DYDON requirements.

---

##  Dependencies Used

All packages are listed in `requirements.txt`. Core dependencies:

| Library         | Purpose                                   |
|-----------------|--------------------------------------------|
| `PyMuPDF`       | PDF parsing (text and image)              |
| `pytesseract`   | OCR for scanned PDFs                      |
| `pdf2image`     | Convert PDF pages to images for OCR       |
| `openpyxl`      | Excel file parsing                        |
| `python-docx`   | DOCX file parsing                         |
| `Pillow`        | Image manipulation                        |
| `streamlit`     | Front-end UI                              |
| `tqdm`          | Optional progress bar for CLI             |

---

##  Folder Output Example

When a user uploads a file named `invoice.pdf`, this is what the output structure looks like:

```text
extracted_texts/
├── majd_zarai_invoice_cleaned.txt
└── majd_extracted_images_from_pdf/
└── invoice_images/
├── page1_img1.png
├── page2_img2.png
└── ...
```

---

##  Testing and Validation

I validated the system using:
- Native PDFs with machine-readable text
- Scanned PDFs to confirm OCR fallback
- DOCX files containing both text and tables
- Multi-sheet Excel files with mixed content
- PDFs with embedded figures/images

---

##  Bonus Features Implemented

| Feature                        | Description |
|-------------------------------|-------------|
| ✅ OCR fallback               | If no text, fallback to high-res OCR (300 DPI) |
| ✅ Image extraction           | All PDF images saved and previewed in UI |
| ✅ Front-end interface        | Gradient UI with upload + preview |
| ✅ User-friendly logging      | Structured logs for success and failure |
| ✅ Output consistency         | All filenames include my full name and are organized cleanly |

---

##  Final Notes

This project reflects my ability to:
- Write modular, clear, and production-grade Python
- Integrate OCR and file I/O workflows
- Design user-friendly front-end UIs
- Follow instructions and go above expectations

Thank you for the opportunity to apply to DYDON AI.  
I hope this project demonstrates both my technical capability and attention to real-world usability.

— **Majd Zarai**


