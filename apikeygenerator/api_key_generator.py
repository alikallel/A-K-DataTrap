#!/usr/bin/env python3
"""
Base API Key Generator module
Contains the abstract base class for API key generation
"""

from pathlib import Path


class APIKeyGenerator:
    """Base class for API key generation"""
    
    def __init__(self):
        self.api_dir = self._get_api_directory()
    
    def _get_api_directory(self):
        """Get the default API keys directory path for the current OS"""
        home = Path.home()
        return home / '.api_keys'
    
    def generate_keys(self):
        """Abstract method to be implemented by subclasses"""
        raise NotImplementedError("Subclasses must implement generate_keys method")