#!/usr/bin/env python3
"""
Operating System Detection module
Provides utilities for detecting and validating the current operating system
"""

import platform


class OSDetector:
    """Class responsible for detecting the operating system"""
    
    @staticmethod
    def get_system():
        """Get the current operating system"""
        return platform.system().lower()
    
    @staticmethod
    def is_linux():
        """Check if the current system is Linux"""
        return OSDetector.get_system() == 'linux'
    
    @staticmethod
    def is_windows():
        """Check if the current system is Windows"""
        return OSDetector.get_system() == 'windows'
    
    @staticmethod
    def is_supported():
        """Check if the current system is supported"""
        return OSDetector.is_linux() or OSDetector.is_windows()
    
    @staticmethod
    def get_system_name():
        """Get a human-readable system name"""
        system = OSDetector.get_system()
        if system == 'linux':
            return 'Linux'
        elif system == 'windows':
            return 'Windows'
        else:
            return system.capitalize()