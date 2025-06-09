#!/usr/bin/env python3
"""
Main application module
Contains the Application class that orchestrates the SSH key generation and web history injection
"""

import sys
from pathlib import Path
from os_detector import OSDetector
from sshkeygenerator.factory import SSHKeyGeneratorFactory
from webhistory.history_factory import WebHistoryInjectorFactory


class Application:
    """Main application class"""
    
    def __init__(self):
        self.detector = OSDetector()
        self.ssh_generator = None
        self.history_injector = None
    
    def _display_system_info(self):
        """Display information about the detected system"""
        system_name = self.detector.get_system_name()
        ssh_dir = Path.home() / '.ssh'
        
        print(f"Detected operating system: {system_name}")
        print(f"SSH directory will be: {ssh_dir}")
        print(f"Supported browsers: {', '.join(WebHistoryInjectorFactory.get_supported_browsers())}")
        print("-" * 70)
    
    def _display_menu(self):
        """Display the main menu options"""
        print("\nSelect operation:")
        print("1. Generate SSH Keys")
        print("2. Inject Web History")
        print("3. Execute Both (SSH Keys + Web History)")
        print("4. Exit")
        print("-" * 50)
        
        while True:
            try:
                choice = input("Enter your choice (1-4): ").strip()
                if choice in ['1', '2', '3', '4']:
                    return int(choice)
                else:
                    print("Invalid choice. Please enter 1, 2, 3, or 4.")
            except (ValueError, KeyboardInterrupt):
                print("\nInvalid input. Please try again.")
    
    def _execute_ssh_generator(self):
        """Execute the SSH key generator"""
        print("\n" + "="*50)
        print("EXECUTING SSH KEY GENERATION")
        print("="*50)
        
        if self.detector.is_linux():
            print("Executing Linux bash script...")
        elif self.detector.is_windows():
            print("Executing Windows PowerShell script...")
        
        result = self.ssh_generator.generate_keys()
        return result
    
    def _execute_history_injector(self):
        """Execute the web history injector"""
        print("\n" + "="*50)
        print("EXECUTING WEB HISTORY INJECTION")
        print("="*50)
        
        if self.detector.is_linux():
            print("Executing Linux web history injection...")
        elif self.detector.is_windows():
            print("Executing Windows web history injection...")
        
        result = self.history_injector.inject_history()
        return result
    
    def _display_results(self, operation_name, result):
        """Display the execution results"""
        print(f"\n{operation_name} Results:")
        print("-" * 30)
        
        if result.returncode == 0:
            print(f"✓ {operation_name} executed successfully!")
            if result.stdout:
                print("\nOutput:")
                print(result.stdout)
        else:
            print(f"✗ {operation_name} execution failed!")
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
    
    def _execute_ssh_keys(self):
        """Execute SSH key generation"""
        try:
            # Create SSH generator if not already created
            if not self.ssh_generator:
                self.ssh_generator = SSHKeyGeneratorFactory.create_generator()
            
            # Execute the generator
            result = self._execute_ssh_generator()
            
            # Display results
            return self._display_results("SSH Key Generation", result)
            
        except Exception as e:
            print(f"Error during SSH key generation: {e}")
            return False
    
    def _execute_web_history(self):
        """Execute web history injection"""
        try:
            # Create history injector if not already created
            if not self.history_injector:
                self.history_injector = WebHistoryInjectorFactory.create_injector()
            
            # Execute the injector
            result = self._execute_history_injector()
            
            # Display results
            return self._display_results("Web History Injection", result)
            
        except Exception as e:
            print(f"Error during web history injection: {e}")
            return False
    
    def _execute_both(self):
        """Execute both SSH key generation and web history injection"""
        print("\n" + "="*70)
        print("EXECUTING BOTH OPERATIONS")
        print("="*70)
        
        success_count = 0
        
        # Execute SSH keys
        if self._execute_ssh_keys():
            success_count += 1
        
        # Execute web history
        if self._execute_web_history():
            success_count += 1
        
        # Summary
        print("\n" + "="*50)
        print("EXECUTION SUMMARY")
        print("="*50)
        print(f"Successfully completed: {success_count}/2 operations")
        
        if success_count == 2:
            print("✅ All operations completed successfully!")
            return True
        elif success_count == 1:
            print("⚠ Some operations failed. Check the output above.")
            return False
        else:
            print("❌ All operations failed.")
            return False
    
    def run(self):
        """Main application entry point"""
        try:
            # Check if OS is supported
            if not self._check_system_support():
                sys.exit(1)
            
            # Display system information
            self._display_system_info()
            
            # Main application loop
            while True:
                choice = self._display_menu()
                
                if choice == 1:
                    success = self._execute_ssh_keys()
                elif choice == 2:
                    success = self._execute_web_history()
                elif choice == 3:
                    success = self._execute_both()
                elif choice == 4:
                    print("\nExiting application. Goodbye!")
                    sys.exit(0)
                
                # Ask if user wants to continue
                if choice in [1, 2, 3]:
                    print("\n" + "="*50)
                    continue_choice = input("Do you want to perform another operation? (y/n): ").strip().lower()
                    if continue_choice not in ['y', 'yes']:
                        print("\nExiting application. Goodbye!")
                        break
                
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user. Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            sys.exit(1)

def main():
    """Entry point function"""
    app = Application()
    app.run()


if __name__ == "__main__":
    main()