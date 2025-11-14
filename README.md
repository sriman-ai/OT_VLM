**_Document Batch Parser:**_
This repository contains a Python batch script for parsing and chunking occupational safety documents in Korean and English.
It handles PDF, TXT, PowerPoint (PPTX), image, and video files, extracting text content and generating both classic (paragraph-based) and semantic chunks for downstream AI or data processing.

**__Supported File Types:**__
PDF (.pdf) — Digital and scanned; performs OCR if text extraction fails

Text (.txt) — Supports Korean (CP949/EUC-KR) and UTF-8 encodings

Images (.jpg, .jpeg, .png, .bmp) — OCR via Tesseract (Korean + English)

Video (.mp4, .avi, .mov) — OCR on sampled frames (visual text only)

PowerPoint (.pptx) — Extracts all visible slide text

**_Unsupported:**_

HWP (.hwp) — Proprietary Hangul format, requires conversion outside Python

**_Output_**
Chunked results in /output/parsed/
Each input file generates:

[originalname].chunks.txt — Classic chunks (one per paragraph/slide/etc.)

[originalname].semantic_chunks.txt — Semantic chunks (context-based grouping; see code for tunable threshold)

Full log in /output/parse_log.txt

Tracks parsing status, errors, and chunk counts for all files

**_Install Requirements**_
Install Python dependencies:

bash:
pip install pymupdf pdf2image pytesseract pillow opencv-python python-pptx sentence-transformers nltk
You also need:

Tesseract OCR (in your system PATH)

Poppler (in PATH, for scanned PDFs)

**_How To Use**_
Place all documents to be parsed in data/sample/샘플 (or adjust DATA_DIR in the script).

Adjust OUT_DIR as needed (default is output/parsed/).

**_Run the script:**_

bash
python scripts/batch_parse.py

**_Outputs:**_

See chunked results in output/parsed/

All logs in output/parse_log.txt

**_Example Output/Log**_

[PDF][Digital] Parsed: .../화재사례.pdf
[DONE] Saved .../화재사례.pdf.chunks.txt; 5 chunks
[DONE][Semantic] Saved .../화재사례.pdf.semantic_chunks.txt; 18 semantic chunks
[PPTX] Parsed: .../안전교육자료.pptx
[DONE] Saved .../안전교육자료.pptx.chunks.txt; 10 chunks
[SKIP] Unsupported file: .../some_file.hwp
Open any .semantic_chunks.txt and .chunks.txt in /output/parsed/ for chunked text output.

**_Notes_**
.hwp files are skipped: convert them to TXT or PDF before parsing.

Video files extract only visible frame text (no audio transcript).

Script can be extended for DOCX, audio, or new formats if desired.

Semantic chunking is controlled by a threshold parameter (default 0.75). Lower for finer chunks, raise for coarser grouping.

**_Note on HWP Files**_
This project does not natively support .hwp.
Before running the batch parser, convert all .hwp files to .txt or .pdf using Hancom Office batch, VBA script, or any other tool. After conversion, process as usual.