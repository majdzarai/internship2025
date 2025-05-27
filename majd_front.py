import streamlit as st
import os
import tempfile
from Majd_Zarai_text_extractor.pdf_handler import extract_text_from_pdf_enhanced, extract_images_from_pdf
from Majd_Zarai_text_extractor.docx_handler import extract_text_from_docx_enhanced
from Majd_Zarai_text_extractor.excel_handler import extract_text_from_excel_enhanced

st.set_page_config(page_title="Majd Zarai - Document Intelligence", layout="wide")

# ────────────────────────────────
# Custom Styling
# ────────────────────────────────
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to bottom right, #ff0000, #ffffff);
            padding: 2rem;
            font-family: 'Segoe UI', sans-serif;
        }

        #MainMenu, header, footer {
            visibility: hidden;
        }

        h1, h2, h3 {
            color: #000000 !important;
        }

        .css-13sdm1p {
            background-color: #bbd4de !important;
            border-radius: 12px;
            padding: 1rem;
            border: 2px dashed #ff4d4d;
        }

        .stTextArea textarea {
            background-color: #bbd4de;
            color: #333;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            border-radius: 8px;
            border: 1px solid #ccc;
            padding: 1rem;
        }

        .stButton > button {
            background: linear-gradient(to right, #bbd4de, #ff9999);
            border: none;
            color: white;
            font-weight: 600;
            border-radius: 10px;
            padding: 0.6em 1.5em;
            margin-top: 0.5rem;
        }

        .stDownloadButton > button {
            background: #000000;
            color: white;
            font-weight: bold;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────
# App Title & Upload
# ────────────────────────────────
st.markdown("""
<div style='text-align: center; color: black; padding: 1rem 0;'>
    <h1 style="font-size: 3em;"> Intelligent Document Extractor by Majd Zarai</h1>
    <p style="font-size: 1.2em;">
        Upload <code>.pdf</code>, <code>.docx</code>, or <code>.xlsx</code> files to extract and view structured content and images (if available).
    </p>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload your document", type=["pdf", "docx", "xlsx"])

if uploaded_file:
    filetype = uploaded_file.type
    filename = uploaded_file.name
    base_filename = os.path.splitext(filename)[0].replace(" ", "_")

    with tempfile.NamedTemporaryFile(delete=False, suffix=filename) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    with st.spinner("🔍 Processing your document..."):
        text = ""
        image_dir = None

        try:
            if filetype == "application/pdf":
                text = extract_text_from_pdf_enhanced(tmp_path)
                extract_images_from_pdf(tmp_path)
                image_dir = f"extracted_texts/majd_extracted_images_from_pdf/{base_filename}_images"

            elif filetype == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                text = extract_text_from_docx_enhanced(tmp_path)

            elif filetype == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                text = extract_text_from_excel_enhanced(tmp_path)

            else:
                st.error("Unsupported file type.")
        except Exception as e:
            st.error(f" Error processing file: {e}")

    # ────────────────────────────────
    # Show Extracted Text
    # ────────────────────────────────
    if text:
        st.success(" Text extracted successfully!")
        st.subheader(" Extracted Text")
        st.text_area(label="", value=text, height=400)

        # Download
        cleaned_filename = f"majd_zarai_{base_filename}_cleaned.txt"
        st.download_button(" Download Extracted Text", data=text, file_name=cleaned_filename)

    