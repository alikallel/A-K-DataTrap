#!/usr/bin/env python3
"""
Main application module
Contains the Application class that orchestrates the SSH key generation process
"""

import sys
from pathlib import Path
from os_detector import OSDetector
from sshkeygenerator.factory import SSHKeyGeneratorFactory


class Application:
    """Main application class"""
    
    def __init__(self):
        self.detector = OSDetector()
        self.generator = None
    
    def _display_system_info(self):
        """Display information about the detected system"""
        system_name = self.detector.get_system_name()
        ssh_dir = Path.home() / '.ssh'
        
        print(f"Detected operating system: {system_name}")
        print(f"SSH directory will be: {ssh_dir}")
        print("-" * 50)
    
    def _execute_generator(self):
        """Execute the SSH key generator"""
        if self.detector.is_linux():
            print("Executing Linux bash script...")
        elif self.detector.is_windows():
            print("Executing Windows PowerShell script...")
        
        result = self.generator.generate_keys()
        return result
    
    def _display_results(self, result):
        """Display the execution results"""
        if result.returncode == 0:
            print("✓ Script executed successfully!")
            if result.stdout:
                print("\nOutput:")
                print(result.stdout)
        else:
            print("✗ Script execution failed!")
            if result.stderr:
                print("\nError:")
                print(result.stderr)
            return False
        return True
    
    def _check_system_support(self):
        """Check if the current system is supported"""
        if not self.detector.is_supported():
            supported_systems = SSHKeyGeneratorFactory.get_supported_systems()
            print(f"Unsupported operating system: {self.detector.get_system_name()}")
            print(f"This script supports: {', '.join(supported_systems)}")
            return False
        return True
    
    def run(self):
        """Main application entry point"""
        try:
            # Check if OS is supported
            if not self._check_system_support():
                sys.exit(1)
            
            # Display system information
            self._display_system_info()
            
            # Create appropriate generator
            self.generator = SSHKeyGeneratorFactory.create_generator()
            
            # Execute the generator
            result = self._execute_generator()
            
            # Display results
            success = self._display_results(result)
            
            if not success:
                sys.exit(1)
                
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)


def main():
    """Entry point function"""
    app = Application()
    app.run()


if __name__ == "__main__":
    main()