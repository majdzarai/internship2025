# 🧠 Majd Zarai – DYDON AI Internship 2025 Submission

Welcome to my submission for the **DYDON AI Summer Internship 2025**.

I’ve developed a complete and extensible solution to extract structured content from `.pdf`, `.docx`, and `.xlsx` files — with enhancements including OCR fallback, image extraction from PDFs, and a professional-grade Streamlit front-end for evaluation and demo purposes.

---

## 🚀 Project Overview

This project addresses all required objectives and adds several bonus capabilities:

| Capability                                      | Included |
|------------------------------------------------|----------|
| ✅ Text extraction from `.pdf`                 | ✔️       |
| ✅ OCR fallback for scanned PDFs               | ✔️       |
| ✅ DOCX parsing (paragraphs + tables)          | ✔️       |
| ✅ XLSX parsing (all sheets + formatting)      | ✔️       |
| ✅ Embedded image extraction from PDFs         | ✔️       |
| ✅ Modular architecture per file type          | ✔️       |
| ✅ CLI script and web frontend                 | ✔️       |
| ✅ Gradient-styled UI with previews            | ✔️       |

---

## 🗂️ Project Structure

.
├── Majd_Zarai_text_extractor/ # Modular extractors (PDF, DOCX, XLSX)
│ ├── pdf_handler.py
│ ├── docx_handler.py
│ └── excel_handler.py

├── uploads/ # Input documents
├── extracted_texts/ # Output text + images
│ ├── majd_zarai_<filename>_cleaned.txt
│ └── majd_extracted_images_from_pdf/
│ └── <pdf_name>_images/
│ ├── page1_img1.png
│ └── ...

├── extract_text_Majd_Zarai.py # Main CLI pipeline
├── majd_front.py # Streamlit frontend
├── DEV_LOG_Majd_Zarai.md # Dev notes + justification
├── requirements.txt # Minimal used packages
├── Majd_assets/ # UI screenshots
└── README.md # Project summary (this file)




---

## 💡 My Enhancements & Bonus Contributions

### 🧠 OCR Fallback for PDFs  
If a page has no extractable text, we fallback to OCR using Tesseract — rendered with 300 DPI for high accuracy.

### 🖼️ PDF Image Extraction  
Automatically extracts embedded images in PDFs and organizes them per page, under `extracted_texts/majd_extracted_images_from_pdf`.

### 🌐 Streamlit UI  
Includes a fully polished interface for:
- Drag-and-drop document upload
- Gradient red-white background theme
- Interactive preview of text
- **Button to view extracted images per page**
- Download support for `.txt` result

---

## ⚙️ How to Run

### ▶️ CLI Mode

To process everything in `uploads/`:

```bash
python extract_text_Majd_Zarai.py


This will save results inside extracted_texts/.


🌐 Streamlit Web Frontend

streamlit run majd_front.py
Upload a file via browser, and:

View extracted text instantly

Show/hide image previews (PDFs only)

Download .txt result with 1 click


🎨 Front-End Preview
Upload Panel
Drag and drop .pdf, .docx, or .xlsx documents into the browser.

Text Output
Extracted text appears beautifully styled in a large viewer:


📦 Requirements
Install cleanly via:
pip install -r requirements.txt

🙏 Thank You
This was built with passion, attention to detail, and care for extensibility. I believe this reflects my capability to work with real-world AI/NLP pipelines.

Thank you for the opportunity to contribute!

— Majd Zarai


