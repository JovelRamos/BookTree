#!/usr/bin/env python3
"""
Barebones EPUB Reader - Skeleton
A simple command-line EPUB reader that extracts and displays text content.
"""

import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
import sys
import re


class EPUBReader:
    def __init__(self, epub_path):
        self.epub_path = Path(epub_path)
        self.namespaces = {
            'n': 'urn:oasis:names:tc:opendocument:xmlns:container',
            'opf': 'http://www.idpf.org/2007/opf',
            'xhtml': 'http://www.w3.org/1999/xhtml'
        }
        
    def read(self):
        """Extract and return the EPUB content"""
        # TODO: Check if file exists
        
        # TODO: Open EPUB as ZIP file
        
        # TODO: Read META-INF/container.xml to find content.opf location
        
        # TODO: Parse content.opf file
        
        # TODO: Extract spine (reading order) and manifest (file mappings)
        
        # TODO: Loop through spine items and extract text from each chapter
        
        # TODO: Return list of chapters
        
        pass
    
    def _extract_text(self, html_content):
        """Extract text from HTML/XHTML content"""
        # Remove script and style tags
        html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
        html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
        
        # Remove all HTML tags
        text = re.sub(r'<[^>]+>', '', html_content)
        
        # Decode HTML entities
        text = text.replace('&nbsp;', ' ')
        text = text.replace('&lt;', '<')
        text = text.replace('&gt;', '>')
        text = text.replace('&amp;', '&')
        text = text.replace('&quot;', '"')
        text = text.replace('&#39;', "'")
        
        # Clean up whitespace
        text = re.sub(r'\n\s*\n', '\n\n', text)
        text = re.sub(r' +', ' ', text)
        
        return text.strip()
    
    def get_metadata(self):
        """Extract metadata from the EPUB"""
        with zipfile.ZipFile(self.epub_path, 'r') as epub:
            # Read container.xml to find content.opf location
            container = epub.read('META-INF/container.xml')
            container_root = ET.fromstring(container)
            opf_path = container_root.find('.//n:rootfile', self.namespaces).get('full-path')
            
            # Parse content.opf file
            opf_content = epub.read(opf_path)
            opf_root = ET.fromstring(opf_content)
            
            # Extract title and author from Dublin Core metadata
            metadata = {}
            dc_ns = '{http://purl.org/dc/elements/1.1/}'
            
            title = opf_root.find(f'.//{dc_ns}title')
            metadata['title'] = title.text if title is not None else 'Unknown'
            
            creator = opf_root.find(f'.//{dc_ns}creator')
            metadata['author'] = creator.text if creator is not None else 'Unknown'
            
            return metadata


def main():
    # Check command line arguments
    if len(sys.argv) < 2:
        print("Usage: python epub_reader.py <path_to_epub_file>")
        sys.exit(1)
    
    epub_path = sys.argv[1]
    
    try:
        # Create EPUBReader instance
        reader = EPUBReader(epub_path)
        
        # Get and display metadata
        metadata = reader.get_metadata()
        print("=" * 60)
        print(f"Title: {metadata['title']}")
        print(f"Author: {metadata['author']}")
        print("=" * 60)
        
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading EPUB: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()