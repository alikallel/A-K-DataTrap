#!/usr/bin/env python3
"""
Factory module for creating SSH Key Generators
Implements the Factory pattern to create appropriate generators based on OS
"""

from os_detector import OSDetector
from sshkeygenerator.linux_generator import LinuxSSHKeyGenerator
from sshkeygenerator.windows_generator import WindowsSSHKeyGenerator


class SSHKeyGeneratorFactory:
    """Factory class to create appropriate SSH key generator based on OS"""
    
    @staticmethod
    def create_generator():
        """Create and return the appropriate SSH key generator"""
        if OSDetector.is_linux():
            return LinuxSSHKeyGenerator()
        elif OSDetector.is_windows():
            return WindowsSSHKeyGenerator()
        else:
            raise OSError(f"Unsupported operating system: {OSDetector.get_system()}")
    
    @staticmethod
    def get_supported_systems():
        """Return a list of supported operating systems"""
        return ['Linux', 'Windows']