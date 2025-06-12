#!/usr/bin/env python3
"""
Log Factory module for creating Log Generators
Implements the Factory pattern to create appropriate generators based on OS
"""

from os_detector import OSDetector
from loggenerator.linux_generator import LinuxLogGenerator
from loggenerator.windows_generator import WindowsLogGenerator


class LogGeneratorFactory:
    """Factory class to create appropriate log generator based on OS"""
    
    @staticmethod
    def create_generator():
        """Create and return the appropriate log generator"""
        if OSDetector.is_linux():
            return LinuxLogGenerator()
        elif OSDetector.is_windows():
            return WindowsLogGenerator()
        else:
            raise OSError(f"Unsupported operating system: {OSDetector.get_system()}")
    
    @staticmethod
    def get_supported_systems():
        """Return a list of supported operating systems"""
        return ['Linux', 'Windows']
    
    @staticmethod
    def get_supported_log_types():
        """Return a list of supported log types"""
        return {
            'Linux': [
                'Apache Access Log',
                'System Log (syslog)',
                'Authentication Log',
                'Nginx Error Log',
                'Application Log',
                'Kernel Log'
            ],
            'Windows': [
                'IIS Access Log',
                'Windows Event Log',
                'PowerShell Execution Log',
                'SQL Server Error Log',
                'Application Log',
                'Performance CSV'
            ]
        }