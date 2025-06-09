#!/usr/bin/env python3
"""
Factory module for creating Web History Injectors
Implements the Factory pattern to create appropriate injectors based on OS
"""

from os_detector import OSDetector
from webhistory.linux_history_injector import LinuxWebHistoryInjector
from webhistory.windows_history_injector import WindowsWebHistoryInjector


class WebHistoryInjectorFactory:
    """Factory class to create appropriate web history injector based on OS"""
    
    @staticmethod
    def create_injector():
        """Create and return the appropriate web history injector"""
        if OSDetector.is_linux():
            return LinuxWebHistoryInjector()
        elif OSDetector.is_windows():
            return WindowsWebHistoryInjector()
        else:
            raise OSError(f"Unsupported operating system: {OSDetector.get_system()}")
    
    @staticmethod
    def get_supported_systems():
        """Return a list of supported operating systems"""
        return ['Linux', 'Windows']
    
    @staticmethod
    def get_supported_browsers():
        """Return a list of supported browsers"""
        return ['Chrome', 'Firefox', 'Edge', 'Brave', 'Opera', 'Internet Explorer']