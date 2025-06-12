#!/usr/bin/env python3
"""
Base Source Code Generator module
Contains the abstract base class for source code generation
"""

from pathlib import Path


class SourceCodeGenerator:
    """Base class for source code generation"""
    
    def __init__(self):
        self.output_dir = self._get_output_directory()
    
    def _get_output_directory(self):
        """Get the default output directory path for generated source code"""
        home = Path.home()
        return home / 'Code_Source'
    
    def generate_source_code(self):
        """Abstract method to be implemented by subclasses"""
        raise NotImplementedError("Subclasses must implement generate_source_code method")