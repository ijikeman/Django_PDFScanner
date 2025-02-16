import pytesseract
from pdf2image import convert_from_path

class PDFExtractor:
    @staticmethod
    def extract_text(pdf_path):
        text = ""
        try:
            with open(pdf_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text() or ""

            # OCR処理（画像PDF用）
            if not text.strip():  # もしテキストが取れなかったらOCRを試す
                images = convert_from_path(pdf_path)
                for image in images:
                    text += pytesseract.image_to_string(image, lang='jpn')  # 日本語OCR
        except Exception as e:
            text = f"エラー: {str(e)}"
        return text
