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
        # TODO: Remove script and style tags
        
        # TODO: Remove all HTML tags
        
        # TODO: Decode HTML entities (&nbsp;, &lt;, &gt;, etc.)
        
        # TODO: Clean up whitespace
        
        # TODO: Return cleaned text
        
        pass
    
    def get_metadata(self):
        """Extract metadata from the EPUB"""
        # TODO: Open EPUB as ZIP file
        
        # TODO: Read META-INF/container.xml to find content.opf location
        
        # TODO: Parse content.opf file
        
        # TODO: Extract title and author from Dublin Core metadata
        
        # TODO: Return metadata dictionary
        
        pass


def main():
    # TODO: Check command line arguments
    
    # TODO: Create EPUBReader instance
    
    # TODO: Get and display metadata
    
    # TODO: Read and display chapters
    
    # TODO: Add pause between chapters for user interaction
    
    # TODO: Handle errors appropriately
    
    pass


if __name__ == "__main__":
    main()