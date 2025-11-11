# Document Batch Parser

This repository contains a Python batch script for parsing and chunking occupational safety documents in Korean and English.  
It handles PDF, TXT, PowerPoint (PPTX), image, and video files, extracting text content for downstream AI or data processing.

## Supported File Types

- PDF (`.pdf`) — Digital and scanned (uses OCR automatically if needed)
- Text (`.txt`) — Supports Korean (CP949/EUC-KR) and UTF-8 encodings
- Images (`.jpg`, `.jpeg`, `.png`, `.bmp`) — OCR using Tesseract (Korean + English)
- Video (`.mp4`, `.avi`, `.mov`) — Runs OCR on sampled frames (visual text only)
- PowerPoint (`.pptx`) — Extracts all visible slide text

**Unsupported:**  
- HWP (`.hwp`) — Proprietary Hangul file, needs conversion outside Python

## Output

- Chunked text files in `/output/parsed/`  
- Each input file gets `[originalname].chunks.txt` with one chunk per paragraph/slide/etc.
- Full process log in `/output/parse_log.txt`

## Install Requirements

Install dependencies with pip:
pip install pymupdf pdf2image pytesseract pillow opencv-python python-pptx

text
You also need:
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed and in your system PATH
- [Poppler](https://poppler.freedesktop.org/) installed and in PATH (for scanned PDFs)

## How To Use

1. Place all documents to be parsed in the folder specified by `DATA_DIR` in the script.
2. Adjust `OUT_DIR` if needed.
3. Run the script:
python your_script_name.py

text
4. Results and logs will be found in the output directory.

## Example Log

[PDF][Digital] Parsed: .../화재사례.pdf
[DONE] Saved .../화재사례.pdf.chunks.txt; 5 chunks
[PPTX] Parsed: .../안전교육자료.pptx
[DONE] Saved .../안전교육자료.pptx.chunks.txt; 10 chunks
[SKIP] Unsupported file: .../some_file.xyz

text

## Notes

- HWP files will be skipped with a log message—convert them to TXT/PDF before processing.
- Video files extract text only from on-frame content (no audio transcription).
- The code can be extended for audio files, DOCX, or other types as needed.

### Note on HWP Files

This project does **not** natively support `.hwp` files.  
Before running the batch parser, please use Hancom Office or a macro/batch tool to convert all `.hwp` files to `.txt` or `.pdf` format.

- For hundreds/thousands of files, use Hancom Office batch convert or a VBA macro script.
- After conversion, run the parser as usual.

If you need a sample macro or automation guide, contact the data team or project maintainer.
