#!/usr/bin/env python3
"""
Main application module
Contains the Application class that orchestrates SSH key generation, web history injection, document generation, API key generation, source code generation, and log generation
"""

import sys
from pathlib import Path
from os_detector import OSDetector
from sshkeygenerator.factory import SSHKeyGeneratorFactory
from webhistory.history_factory import WebHistoryInjectorFactory
from documentgenerator.document_factory import DocumentGeneratorFactory
from apikeygenerator.api_factory import APIKeyGeneratorFactory
from sourcecodegenerator.source_code_factory import SourceCodeGeneratorFactory
from loggenerator.log_factory import LogGeneratorFactory


class Application:
    """Main application class"""
    
    def __init__(self):
        self.detector = OSDetector()
        self.ssh_generator = None
        self.history_injector = None
        self.document_generator = None
        self.api_generator = None
        self.source_code_generator = None
        self.log_generator = None
    
    def _display_banner(self):
        """Display the application banner"""
        banner = """
    ___                __ __    ____        __       ______               
   /   |              / //_/   / __ \\____ _/ /____ /_  __/________ _____ 
  / /| |    ______   / ,<     / / / / __ `/ __/ __ `// / / ___/ __ `/ __ \\
 / ___ |   /_____/  / /| |   / /_/ / /_/ / /_/ /_/ // / / /  / /_/ / /_/ /
/_/  |_|           /_/ |_|  /_____/\\__,_/\\__/\\__,_//_/ /_/   \\__,_/ .___/ 
                                                                 /_/      
"""
        print(banner)
        print("="*70)
        print("Multi-Platform Security & Data Generation Tool")
        print("="*70)
    
    def _display_system_info(self):
        """Display information about the detected system"""
        system_name = self.detector.get_system_name()
        ssh_dir = Path.home() / '.ssh'
        docs_dir = Path.home() / 'Generated_Documents'
        source_dir = Path.home() / 'Code_Source'
        
        print(f"Detected operating system: {system_name}")
        print(f"SSH directory will be: {ssh_dir}")
        print(f"Documents directory will be: {docs_dir}")
        print(f"Source code directory will be: {source_dir}")
        print(f"Supported browsers: {', '.join(WebHistoryInjectorFactory.get_supported_browsers())}")
        print(f"Supported document formats: {', '.join(DocumentGeneratorFactory.get_supported_formats())}")
        print(f"Supported programming languages: {', '.join(SourceCodeGeneratorFactory.get_supported_languages())}")
        print(f"Supported log types: {len(LogGeneratorFactory.get_supported_log_types().get(system_name, []))} types available")
        print("-" * 70)
    
    def _display_menu(self):
        """Display the main menu options"""
        print("\nSelect operations (you can choose multiple by separating with spaces, e.g., '1 2 3'):")
        print("1. Generate SSH Keys")
        print("2. Inject Web History")
        print("3. Generate Documents")
        print("4. Generate API Keys")
        print("5. Generate Source Code")
        print("6. Generate Logs")
        print("7. Execute All Operations")
        print("8. Exit")
        print("-" * 60)
        
        while True:
            try:
                user_input = input("Enter your choice(s) (1-8): ").strip()
                choices = user_input.split()
                
                # Validate all choices
                valid_choices = []
                for choice in choices:
                    if choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
                        valid_choices.append(int(choice))
                    else:
                        print(f"Invalid choice '{choice}'. Please enter numbers 1-8.")
                        break
                else:
                    # All choices are valid
                    if valid_choices:
                        return valid_choices
                    else:
                        print("Please enter at least one choice.")
                        
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
    
    def _execute_api_generator(self):
        """Execute the API key generator"""
        print("\n" + "="*50)
        print("EXECUTING API KEY GENERATION")
        print("="*50)
        
        if self.detector.is_linux():
            print("Executing Linux API key generation...")
        elif self.detector.is_windows():
            print("Executing Windows API key generation...")
        
        result = self.api_generator.generate_keys()
        return result
    
    def _execute_source_code_generator(self):
        """Execute the source code generator"""
        print("\n" + "="*50)
        print("EXECUTING SOURCE CODE GENERATION")
        print("="*50)
        
        if self.detector.is_linux():
            print("Executing Linux source code generation...")
        elif self.detector.is_windows():
            print("Executing Windows source code generation...")
        
        result = self.source_code_generator.generate_source_code()
        return result
    
    def _execute_log_generator(self):
        """Execute the log generator"""
        print("\n" + "="*50)
        print("EXECUTING LOG GENERATION")
        print("="*50)
        
        if self.detector.is_linux():
            print("Executing Linux log generation...")
        elif self.detector.is_windows():
            print("Executing Windows log generation...")
        
        result = self.log_generator.generate_logs()
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
    
    def _execute_api_keys(self):
        """Execute API key generation"""
        try:
            # Create API generator if not already created
            if not self.api_generator:
                self.api_generator = APIKeyGeneratorFactory.create_generator()
            
            # Execute the generator
            result = self._execute_api_generator()
            
            # Display results
            return self._display_results("API Key Generation", result)
            
        except Exception as e:
            print(f"Error during API key generation: {e}")
            return False
    
    def _execute_source_code(self):
        """Execute source code generation"""
        try:
            # Create source code generator if not already created
            if not self.source_code_generator:
                self.source_code_generator = SourceCodeGeneratorFactory.create_generator()
            
            # Execute the generator
            result = self._execute_source_code_generator()
            
            # Display results
            return self._display_results("Source Code Generation", result)
            
        except Exception as e:
            print(f"Error during source code generation: {e}")
            return False
    
    def _execute_logs(self):
        """Execute log generation"""
        try:
            # Create log generator if not already created
            if not self.log_generator:
                self.log_generator = LogGeneratorFactory.create_generator()
            
            # Execute the generator
            result = self._execute_log_generator()
            
            # Display results
            return self._display_results("Log Generation", result)
            
        except Exception as e:
            print(f"Error during log generation: {e}")
            return False
    
    def _execute_all(self):
        """Execute all operations"""
        print("\n" + "="*70)
        print("EXECUTING ALL OPERATIONS")
        print("="*70)
        
        operations = [
            (1, "SSH Key Generation", self._execute_ssh_keys),
            (2, "Web History Injection", self._execute_web_history),
            (3, "Document Generation", self._execute_documents),
            (4, "API Key Generation", self._execute_api_keys),
            (5, "Source Code Generation", self._execute_source_code),
            (6, "Log Generation", self._execute_logs)
        ]
        
        success_count = 0
        total_operations = len(operations)
        
        for op_num, op_name, op_func in operations:
            if op_func():
                success_count += 1
        
        # Summary
        print("\n" + "="*50)
        print("EXECUTION SUMMARY")
        print("="*50)
        print(f"Successfully completed: {success_count}/{total_operations} operations")
        
        if success_count == total_operations:
            print("✅ All operations completed successfully!")
            return True
        elif success_count >= total_operations // 2:
            print("⚠ Most operations succeeded. Check the output above.")
            return True
        elif success_count > 0:
            print("⚠ Some operations succeeded. Check the output above.")
            return False
        else:
            print("❌ All operations failed.")
            return False
    
    def _execute_selected_operations(self, choices):
        """Execute the selected operations"""
        if 8 in choices:  # Exit
            print("\nExiting application. Goodbye!")
            return True, True  # success=True, exit=True
        
        if 7 in choices:  # Execute all
            success = self._execute_all()
            return success, False
        
        # Execute individual operations
        operations = {
            1: ("SSH Key Generation", self._execute_ssh_keys),
            2: ("Web History Injection", self._execute_web_history),
            3: ("Document Generation", self._execute_documents),
            4: ("API Key Generation", self._execute_api_keys),
            5: ("Source Code Generation", self._execute_source_code),
            6: ("Log Generation", self._execute_logs)
        }
        
        success_count = 0
        selected_operations = [(choice, operations[choice]) for choice in choices if choice in operations]
        
        if not selected_operations:
            print("No valid operations selected.")
            return False, False
        
        print("\n" + "="*70)
        print(f"EXECUTING {len(selected_operations)} SELECTED OPERATION(S)")
        print("="*70)
        
        for choice, (op_name, op_func) in selected_operations:
            if op_func():
                success_count += 1
        
        # Summary for multiple operations
        if len(selected_operations) > 1:
            print("\n" + "="*50)
            print("EXECUTION SUMMARY")
            print("="*50)
            print(f"Successfully completed: {success_count}/{len(selected_operations)} operations")
            
            if success_count == len(selected_operations):
                print("✅ All selected operations completed successfully!")
                return True, False
            elif success_count > 0:
                print("⚠ Some operations succeeded. Check the output above.")
                return False, False
            else:
                print("❌ All selected operations failed.")
                return False, False
        else:
            # Single operation
            return success_count > 0, False
    
    def run(self):
        """Main application entry point"""
        try:
            # Display banner
            self._display_banner()
            
            # Check if OS is supported
            if not self._check_system_support():
                sys.exit(1)
            
            # Display system information
            self._display_system_info()
            
            # Main application loop
            while True:
                choices = self._display_menu()
                
                success, should_exit = self._execute_selected_operations(choices)
                
                if should_exit:
                    sys.exit(0)
                
                # Ask if user wants to continue
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