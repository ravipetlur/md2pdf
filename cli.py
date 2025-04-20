#!/usr/bin/env python3
import argparse
import sys
from app import convert_to_pdf, convert_to_docx

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown files to PDF or DOCX')
    parser.add_argument('input_file', help='Path to the input Markdown file')
    parser.add_argument('output_file', help='Path to save the output file')
    parser.add_argument('--format', choices=['pdf', 'docx'], default='pdf',
                      help='Output format (default: pdf)')
    
    args = parser.parse_args()
    
    try:
        # Read the markdown file
        with open(args.input_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Convert based on format
        if args.format == 'pdf':
            pdf_file = convert_to_pdf(markdown_content)
            with open(args.output_file, 'wb') as f:
                f.write(pdf_file.getvalue())
        else:
            docx_file = convert_to_docx(markdown_content)
            with open(args.output_file, 'wb') as f:
                f.write(docx_file.getvalue())
        
        print(f"Successfully converted {args.input_file} to {args.output_file}")
        
    except FileNotFoundError:
        print(f"Error: Input file '{args.input_file}' not found", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main() 