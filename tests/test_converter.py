import pytest
from app import app
import io
from docx import Document
from PyPDF2 import PdfReader

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def sample_markdown():
    return """# Test Heading

This is a paragraph with **bold** and *italic* text.

## Code Block
```python
def hello():
    print("Hello, World!")
```

## List
- Item 1
- Item 2
  - Nested Item

## Table
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
"""

def test_index_page(client):
    """Test if the index page loads correctly"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Markdown to PDF/DOCX Converter' in response.data

def test_no_file_upload(client):
    """Test the response when no file is uploaded"""
    response = client.post('/')
    assert response.status_code == 400
    assert b'No file uploaded' in response.data

def test_empty_file_selection(client):
    """Test the response when no file is selected"""
    response = client.post('/', data={
        'file': (io.BytesIO(b''), ''),
        'format': 'pdf'
    })
    assert response.status_code == 400
    assert b'No file selected' in response.data

def test_pdf_conversion(client, sample_markdown):
    """Test PDF conversion with various Markdown elements"""
    response = client.post('/', data={
        'file': (io.BytesIO(sample_markdown.encode()), 'test.md'),
        'format': 'pdf'
    }, content_type='multipart/form-data')
    
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/pdf'
    
    # Verify PDF content
    pdf_content = io.BytesIO(response.data)
    pdf_reader = PdfReader(pdf_content)
    text = pdf_reader.pages[0].extract_text()
    
    assert 'Test Heading' in text
    assert 'This is a paragraph' in text
    assert 'Item 1' in text
    assert 'Header 1' in text

def test_docx_conversion(client, sample_markdown):
    """Test DOCX conversion with various Markdown elements"""
    response = client.post('/', data={
        'file': (io.BytesIO(sample_markdown.encode()), 'test.md'),
        'format': 'docx'
    }, content_type='multipart/form-data')
    
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    
    # Verify DOCX content
    docx_content = io.BytesIO(response.data)
    doc = Document(docx_content)
    
    # Extract text from the document
    full_text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    
    assert 'Test Heading' in full_text
    assert 'This is a paragraph' in full_text
    assert 'Item 1' in full_text

def test_invalid_markdown(client):
    """Test conversion with invalid Markdown content"""
    invalid_content = "```\nUnclosed code block"
    
    response = client.post('/', data={
        'file': (io.BytesIO(invalid_content.encode()), 'invalid.md'),
        'format': 'pdf'
    }, content_type='multipart/form-data')
    
    assert response.status_code == 200  # Should still produce output

def test_large_file(client):
    """Test conversion of a large Markdown file"""
    large_content = "# " + "Very long heading\n\n" * 1000
    
    response = client.post('/', data={
        'file': (io.BytesIO(large_content.encode()), 'large.md'),
        'format': 'pdf'
    }, content_type='multipart/form-data')
    
    assert response.status_code == 200 