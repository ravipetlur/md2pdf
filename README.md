# Markdown to PDF/DOCX Converter

A simple web application that converts Markdown files to PDF or DOCX format while preserving formatting.

## Setup

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open your web browser and navigate to `http://localhost:5000`

## Features

- Convert Markdown files to PDF or DOCX
- Preserves basic formatting
- Supports tables and code blocks
- Uses standard fonts (Arial, sans-serif)
- Simple and intuitive interface

## Usage

1. Click the "Choose File" button and select your Markdown file
2. Select the desired output format (PDF or DOCX)
3. Click "Convert" to download the converted file

## Testing

The project includes comprehensive test cases. To run the tests:

1. Make sure all dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

2. Run all tests:
   ```bash
   pytest
   ```

3. For more detailed output:
   ```bash
   pytest -v
   ```

4. To see test coverage:
   ```bash
   pytest --cov=app tests/
   ```

The test suite includes:
- Basic functionality tests
- File upload tests
- PDF conversion tests
- DOCX conversion tests
- Special character handling
- Error case handling

## Note

Make sure you have all the dependencies installed properly. WeasyPrint might require additional system dependencies depending on your operating system.

### System Dependencies

On macOS:
```bash
brew install cairo pango gdk-pixbuf libffi
```

On Ubuntu/Debian:
```bash
sudo apt-get install python3-cffi python3-brotli libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0
```
