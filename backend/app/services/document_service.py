import shutil
from app.services.pdf_service import PDFService
from pathlib import Path
from sqlalchemy.orm import Session
from app.utils import BASE_DIR


UPLOAD_DIR = Path(BASE_DIR) / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)


class DocumentService:

    @staticmethod
    async def upload_document(db: Session,file, user_name):

        # Validate PDF signature
        header = await file.read(5)

        if header != b"%PDF-":
            raise ValueError("Not a valid PDF Document.")

        await file.seek(0)

        # Read file
        content = await file.read()

        MAX_SIZE = 10 * 1024 * 1024

        if len(content) > MAX_SIZE:
            raise ValueError("PDF File exceeds size limit.")

        await file.seek(0)      

        document_folder = UPLOAD_DIR / str(user_name)
        document_folder.mkdir(parents=True, exist_ok=True)
        file_path = document_folder / file.filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        text_content = PDFService.extract_text(file_path)

        return (file_path, text_content)

