#  Majd Zarai – DYDON AI Internship 2025 Submission

Welcome to my submission for the **DYDON AI Summer Internship 2025**.

I’ve developed a robust and extensible solution to extract structured content from `.pdf`, `.docx`, and `.xlsx` files — with enhancements like OCR fallback for scanned PDFs, image extraction, and a Streamlit-powered web interface.

---

##  Project Overview

This solution fulfills all required tasks and includes several bonus features for better performance, usability, and extensibility:

| Capability                                      | Status   |
|------------------------------------------------|----------|
|  Text extraction from `.pdf`                 | ✔️       |
|  OCR fallback for scanned PDFs               | ✔️       |
|  `.docx` parsing (paragraphs & tables)       | ✔️       |
|  `.xlsx` parsing (multi-sheet, formatting)   | ✔️       |
|  Embedded image extraction from PDFs         | ✔️       |
|  Modular architecture (clean file separation)| ✔️       |
|  CLI script & web UI                         | ✔️       |
|  Frontend: gradient design + image viewer    | ✔️       |

---

## 📂 Project Structure

<details>
  <summary><strong>📁 Click to view structure</strong></summary>

```text
.
├── Majd_Zarai_text_extractor/      # Modular extractors
│   ├── pdf_handler.py              # PDF reader, OCR fallback, image extractor
│   ├── docx_handler.py             # DOCX paragraph + table extraction
│   └── excel_handler.py            # XLSX parser (multi-sheet)
│
├── uploads/                        # Input documents
├── extracted_texts/               # Extracted outputs
│   ├── majd_zarai_<filename>_cleaned.txt
│   └── majd_extracted_images_from_pdf/
│       └── <pdf_name>_images/
│           ├── page1_img1.png
│           └── ...
│
├── extract_text_Majd_Zarai.py     # Main CLI processing script
├── majd_front.py                  # Streamlit frontend app
├── Majd_assets/                   # UI screenshots for README
├── DEV_LOG_Majd_Zarai.md          # Development log
├── requirements.txt               # Project dependencies
└── README.md                      # You're here!
</details> ```








