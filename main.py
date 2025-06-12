#!/usr/bin/env python3
"""
Main application module
Contains the Application class that orchestrates SSH key generation, web history injection, and document generation
"""

import sys
from pathlib import Path
from os_detector import OSDetector
from sshkeygenerator.factory import SSHKeyGeneratorFactory
from webhistory.history_factory import WebHistoryInjectorFactory
from documentgenerator.document_factory import DocumentGeneratorFactory


class Application:
    """Main application class"""
    
    def __init__(self):
        self.detector = OSDetector()
        self.ssh_generator = None
        self.history_injector = None
        self.document_generator = None
    
    def _display_system_info(self):
        """Display information about the detected system"""
        system_name = self.detector.get_system_name()
        ssh_dir = Path.home() / '.ssh'
        docs_dir = Path.home() / 'Generated_Documents'
        
        print(f"Detected operating system: {system_name}")
        print(f"SSH directory will be: {ssh_dir}")
        print(f"Documents directory will be: {docs_dir}")
        print(f"Supported browsers: {', '.join(WebHistoryInjectorFactory.get_supported_browsers())}")
        print(f"Supported document formats: {', '.join(DocumentGeneratorFactory.get_supported_formats())}")
        print("-" * 70)
    
    def _display_menu(self):
        """Display the main menu options"""
        print("\nSelect operation:")
        print("1. Generate SSH Keys")
        print("2. Inject Web History")
        print("3. Generate Documents")
        print("4. Execute SSH Keys + Web History")
        print("5. Execute SSH Keys + Documents")
        print("6. Execute Web History + Documents")
        print("7. Execute All (SSH Keys + Web History + Documents)")
        print("8. Exit")
        print("-" * 60)
        
        while True:
            try:
                choice = input("Enter your choice (1-8): ").strip()
                if choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
                    return int(choice)
                else:
                    print("Invalid choice. Please enter 1-8.")
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
    
    def _execute_document_generator(self):
        """Execute the document generator"""
        print("\n" + "="*50)
        print("EXECUTING DOCUMENT GENERATION")
        print("="*50)
        
        if self.detector.is_linux():
            print("Executing Linux document generation...")
        elif self.detector.is_windows():
            print("Executing Windows document generation...")
        
        result = self.document_generator.generate_documents()
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
    
    def _execute_documents(self):
        """Execute document generation"""
        try:
            # Create document generator if not already created
            if not self.document_generator:
                self.document_generator = DocumentGeneratorFactory.create_generator()
            
            # Execute the generator
            result = self._execute_document_generator()
            
            # Display results
            return self._display_results("Document Generation", result)
            
        except Exception as e:
            print(f"Error during document generation: {e}")
            return False
    
    def _execute_ssh_and_history(self):
        """Execute both SSH key generation and web history injection"""
        print("\n" + "="*70)
        print("EXECUTING SSH KEYS + WEB HISTORY")
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
    
    def _execute_ssh_and_documents(self):
        """Execute SSH key generation and document generation"""
        print("\n" + "="*70)
        print("EXECUTING SSH KEYS + DOCUMENTS")
        print("="*70)
        
        success_count = 0
        
        # Execute SSH keys
        if self._execute_ssh_keys():
            success_count += 1
        
        # Execute documents
        if self._execute_documents():
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
    
    def _execute_history_and_documents(self):
        """Execute web history injection and document generation"""
        print("\n" + "="*70)
        print("EXECUTING WEB HISTORY + DOCUMENTS")
        print("="*70)
        
        success_count = 0
        
        # Execute web history
        if self._execute_web_history():
            success_count += 1
        
        # Execute documents
        if self._execute_documents():
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
    
    def _execute_all(self):
        """Execute all operations: SSH keys, web history, and documents"""
        print("\n" + "="*70)
        print("EXECUTING ALL OPERATIONS")
        print("="*70)
        
        success_count = 0
        
        # Execute SSH keys
        if self._execute_ssh_keys():
            success_count += 1
        
        # Execute web history
        if self._execute_web_history():
            success_count += 1
        
        # Execute documents
        if self._execute_documents():
            success_count += 1
        
        # Summary
        print("\n" + "="*50)
        print("EXECUTION SUMMARY")
        print("="*50)
        print(f"Successfully completed: {success_count}/3 operations")
        
        if success_count == 3:
            print("✅ All operations completed successfully!")
            return True
        elif success_count >= 2:
            print("⚠ Most operations succeeded. Check the output above.")
            return True
        elif success_count == 1:
            print("⚠ Only one operation succeeded. Check the output above.")
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
                    success = self._execute_documents()
                elif choice == 4:
                    success = self._execute_ssh_and_history()
                elif choice == 5:
                    success = self._execute_ssh_and_documents()
                elif choice == 6:
                    success = self._execute_history_and_documents()
                elif choice == 7:
                    success = self._execute_all()
                elif choice == 8:
                    print("\nExiting application. Goodbye!")
                    sys.exit(0)
                
                # Ask if user wants to continue
                if choice in [1, 2, 3, 4, 5, 6, 7]:
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