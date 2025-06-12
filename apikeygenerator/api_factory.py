#!/usr/bin/env python3
"""
Factory module for creating API Key Generators
Implements the Factory pattern to create appropriate generators based on OS
"""

from os_detector import OSDetector
from apikeygenerator.linux_generator import LinuxAPIKeyGenerator
from apikeygenerator.windows_generator import WindowsAPIKeyGenerator


class APIKeyGeneratorFactory:
    """Factory class to create appropriate API key generator based on OS"""
    
    @staticmethod
    def create_generator():
        """Create and return the appropriate API key generator"""
        if OSDetector.is_linux():
            return LinuxAPIKeyGenerator()
        elif OSDetector.is_windows():
            return WindowsAPIKeyGenerator()
        else:
            raise OSError(f"Unsupported operating system: {OSDetector.get_system()}")
    
    @staticmethod
    def get_supported_systems():
        """Return a list of supported operating systems"""
        return ['Linux', 'Windows']