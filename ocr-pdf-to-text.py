import ocrmypdf
import pdfplumber
import os

def ocr_pdf(input_path, output_path):
    try:
        ocrmypdf.ocr(input_path, output_path, deskew=True)
        print(f"OCR completed. Searchable PDF saved to {output_path}")
    except Exception as e:
        print(f"An error occurred during OCR: {str(e)}")
        return False
    return True

def extract_text_from_pdf(pdf_path, txt_output_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
                text += "\n"  # Add a newline after each page
            
            if not text.strip():
                print(f"Warning: No text could be extracted from {pdf_path}.")
                return False
            
            with open(txt_output_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text)
            
            print(f"Text extraction complete. Extracted {len(text)} characters.")
            return True
            
    except Exception as e:
        print(f"An error occurred while processing the PDF: {str(e)}")
        return False

def main():
    # Specify the paths
    pdf_folder = "dataset"
    pdf_filename = "FP.pdf"
    pdf_path = os.path.join(pdf_folder, pdf_filename)
    ocr_pdf_path = os.path.join(pdf_folder, "FP_ocr.pdf")
    txt_output_path = os.path.join(pdf_folder, "FP_text.txt")

    # Apply OCR to the PDF
    if ocr_pdf(pdf_path, ocr_pdf_path):
        # Extract text from the OCR-processed PDF
        extract_text_from_pdf(ocr_pdf_path, txt_output_path)

    print(f"Process completed. Please check {txt_output_path} for the extracted text.")

if __name__ == "__main__":
    main()
