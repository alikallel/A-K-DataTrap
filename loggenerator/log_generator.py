#!/usr/bin/env python3
"""
Base Log Generator module
Contains the abstract base class for log file generation
"""

from pathlib import Path
import datetime


class LogGenerator:
    """Base class for log file generation"""
    
    def __init__(self):
        self.logs_dir = self._get_logs_directory()
    
    def _get_logs_directory(self):
        """Get the default logs directory path for the current OS"""
        home = Path.home()
        return home / 'Generated_Logs'
    
    def _get_current_timestamp(self):
        """Get current timestamp in various formats"""
        now = datetime.datetime.now()
        return {
            'iso': now.isoformat(),
            'syslog': now.strftime('%b %d %H:%M:%S'),
            'apache': now.strftime('%d/%b/%Y:%H:%M:%S %z'),
            'nginx': now.strftime('%d/%b/%Y:%H:%M:%S %z'),
            'windows': now.strftime('%m/%d/%Y %I:%M:%S %p'),
            'epoch': int(now.timestamp())
        }
    
    def generate_logs(self):
        """Abstract method to be implemented by subclasses"""
        raise NotImplementedError("Subclasses must implement generate_logs method")
    