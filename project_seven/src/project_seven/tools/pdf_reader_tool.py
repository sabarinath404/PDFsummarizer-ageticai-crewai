from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import PyPDF2

class PDFReaderInput(BaseModel):
    """Input schema for the PDF reader tool."""
    file_path: str = Field(..., description="Full path to the PDF file to read")

class PDFReaderTool(BaseTool):
    name: str = "PDF Reader Tool"
    description: str = "Reads and extracts text from a PDF file"
    args_schema: Type[BaseModel] = PDFReaderInput

    def _run(self, file_path: str) -> str:
        try:
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
            return text.strip() if text else "No text found in the PDF."
        except Exception as e:
            return f"Error reading PDF: {str(e)}"
