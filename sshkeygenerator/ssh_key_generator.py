#!/usr/bin/env python3
"""
Base SSH Key Generator module
Contains the abstract base class for SSH key generation
"""

from pathlib import Path


class SSHKeyGenerator:
    """Base class for SSH key generation"""
    
    def __init__(self):
        self.ssh_dir = self._get_ssh_directory()
    
    def _get_ssh_directory(self):
        """Get the default SSH directory path for the current OS"""
        home = Path.home()
        return home / '.ssh'
    
    def generate_keys(self):
        """Abstract method to be implemented by subclasses"""
        raise NotImplementedError("Subclasses must implement generate_keys method")