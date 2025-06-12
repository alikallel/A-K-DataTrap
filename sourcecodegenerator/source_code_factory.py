#!/usr/bin/env python3
"""
Factory module for creating Source Code Generators
Implements the Factory pattern to create appropriate generators based on OS
"""

from os_detector import OSDetector
from sourcecodegenerator.linux_code_generator import LinuxSourceCodeGenerator
from sourcecodegenerator.windows_code_generator import WindowsSourceCodeGenerator


class SourceCodeGeneratorFactory:
    """Factory class to create appropriate source code generator based on OS"""
    
    @staticmethod
    def create_generator():
        """Create and return the appropriate source code generator"""
        if OSDetector.is_linux():
            return LinuxSourceCodeGenerator()
        elif OSDetector.is_windows():
            return WindowsSourceCodeGenerator()
        else:
            raise OSError(f"Unsupported operating system: {OSDetector.get_system()}")
    
    @staticmethod
    def get_supported_systems():
        """Return a list of supported operating systems"""
        return ['Linux', 'Windows']
    
    @staticmethod
    def get_supported_languages():
        """Return a list of supported programming languages"""
        return ['Python', 'JavaScript', 'Java', 'C++', 'C', 'Bash/PowerShell', 'C#']