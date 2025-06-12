#!/usr/bin/env python3
"""
Factory module for creating Document Generators
Implements the Factory pattern to create appropriate generators based on OS
"""

from os_detector import OSDetector
from documentgenerator.linux_document_generator import LinuxDocumentGenerator
from documentgenerator.windows_document_generator import WindowsDocumentGenerator


class DocumentGeneratorFactory:
    """Factory class to create appropriate document generator based on OS"""
    
    @staticmethod
    def create_generator():
        """Create and return the appropriate document generator"""
        if OSDetector.is_linux():
            return LinuxDocumentGenerator()
        elif OSDetector.is_windows():
            return WindowsDocumentGenerator()
        else:
            raise OSError(f"Unsupported operating system: {OSDetector.get_system()}")
    
    @staticmethod
    def get_supported_systems():
        """Return a list of supported operating systems"""
        return ['Linux', 'Windows']
    
    @staticmethod
    def get_supported_formats():
        """Return a list of supported document formats"""
        return ['txt', 'csv', 'json', 'html', 'md', 'log', 'ps1', 'sh']