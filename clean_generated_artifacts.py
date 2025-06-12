#!/usr/bin/env python3
"""
Enhanced cleanup script for generated artifacts
Provides robust cleanup with better error handling, logging, and user experience
"""

import os
import shutil
import sys
from pathlib import Path
from typing import List, Dict, Set
import platform
import logging
from datetime import datetime


class ArtifactCleaner:
    """Enhanced artifact cleaner with improved functionality"""
    
    def __init__(self):
        self.home = Path.home()
        self.system = platform.system().lower()
        self.cleaned_count = 0
        self.failed_count = 0
        self.skipped_count = 0
        self.total_size_freed = 0
        
        # Setup logging
        self._setup_logging()
        
        # Define artifact categories
        self.artifact_categories = {
            'SSH Keys': self._get_ssh_paths,
            'API Keys': self._get_api_paths,
            'Generated Documents': self._get_document_paths,
            'Generated Logs': self._get_log_paths,
            'Source Code': self._get_source_code_paths,
            'Browser History Backups': self._get_browser_backup_paths
        }
    
    def _setup_logging(self):
        """Setup logging configuration"""
        log_dir = self.home / "cleanup_logs"
        log_dir.mkdir(exist_ok=True)
        
        log_file = log_dir / f"cleanup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"Cleanup session started - System: {platform.system()}")
    
    def _get_ssh_paths(self) -> List[Path]:
        """Get SSH-related paths"""
        ssh_dir = self.home / ".ssh"
        paths = []
        
        # Standard SSH key files
        ssh_files = ["id_rsa", "id_rsa.pub", "id_ed25519", "id_ed25519.pub", 
                    "id_ecdsa", "id_ecdsa.pub", "id_dsa", "id_dsa.pub"]
        
        for fname in ssh_files:
            fpath = ssh_dir / fname
            if fpath.exists():
                paths.append(fpath)
        
        return paths
    
    def _get_api_paths(self) -> List[Path]:
        """Get API key related paths"""
        paths = []
        api_dirs = [
            self.home / ".api_keys",
            self.home / "api_keys",
            self.home / ".config" / "api_keys"
        ]
        
        for api_dir in api_dirs:
            if api_dir.exists():
                paths.append(api_dir)
        
        return paths
    
    def _get_document_paths(self) -> List[Path]:
        """Get generated document paths"""
        paths = []
        doc_dirs = [
            self.home / "Generated_Documents",
            self.home / "Documents" / "Generated",
            self.home / "generated_docs"
        ]
        
        for doc_dir in doc_dirs:
            if doc_dir.exists():
                paths.append(doc_dir)
        
        return paths
    
    def _get_log_paths(self) -> List[Path]:
        """Get generated log paths"""
        paths = []
        log_dirs = [
            self.home / "Generated_Logs",
            self.home / "logs" / "generated",
            self.home / "generated_logs"
        ]
        
        for log_dir in log_dirs:
            if log_dir.exists():
                paths.append(log_dir)
        
        return paths
    
    def _get_source_code_paths(self) -> List[Path]:
        """Get generated source code paths"""
        paths = []
        code_dirs = [
            self.home / "Code_Source",
            self.home / "generated_code",
            self.home / "source_generated"
        ]
        
        for code_dir in code_dirs:
            if code_dir.exists():
                paths.append(code_dir)
        
        return paths
    
    def _get_browser_backup_paths(self) -> List[Path]:
        """Get browser history backup paths"""
        paths = []
        
        # Windows browser paths
        if self.system == 'windows':
            browser_bases = [
                self.home / 'AppData/Local/Google/Chrome/User Data',
                self.home / 'AppData/Local/Microsoft/Edge/User Data',
                self.home / 'AppData/Local/BraveSoftware/Brave-Browser/User Data',
                self.home / 'AppData/Local/Chromium/User Data',
                self.home / 'AppData/Roaming/Mozilla/Firefox/Profiles'
            ]
        else:  # Linux/Unix
            browser_bases = [
                self.home / '.config/google-chrome',
                self.home / '.config/chromium',
                self.home / '.config/BraveSoftware/Brave-Browser',
                self.home / '.config/microsoft-edge',
                self.home / '.mozilla/firefox'
            ]
        
        # Find backup files
        backup_extensions = ['.backup', '.sqlite.backup', '.bak']
        
        for base_path in browser_bases:
            if not base_path.exists():
                continue
                
            # Handle direct backup files
            for ext in backup_extensions:
                for backup_file in base_path.rglob(f"*{ext}"):
                    if backup_file.is_file():
                        paths.append(backup_file)
        
        return paths
    
    def _get_file_size(self, path: Path) -> int:
        """Get size of file or directory in bytes"""
        try:
            if path.is_file():
                return path.stat().st_size
            elif path.is_dir():
                total_size = 0
                for file_path in path.rglob('*'):
                    if file_path.is_file():
                        try:
                            total_size += file_path.stat().st_size
                        except (OSError, PermissionError):
                            continue
                return total_size
        except (OSError, PermissionError):
            pass
        return 0
    
    def _format_size(self, size_bytes: int) -> str:
        """Format bytes to human readable format"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} TB"
    
    def find_all_artifacts(self) -> Dict[str, List[Path]]:
        """Find all artifacts organized by category"""
        artifacts = {}
        
        for category, path_getter in self.artifact_categories.items():
            try:
                paths = path_getter()
                if paths:
                    artifacts[category] = paths
                    self.logger.info(f"Found {len(paths)} items in category: {category}")
            except Exception as e:
                self.logger.error(f"Error finding {category}: {e}")
        
        return artifacts
    
    def _safe_remove(self, path: Path) -> bool:
        """Safely remove a file or directory with proper error handling"""
        try:
            # Get size before deletion for reporting
            size = self._get_file_size(path)
            
            if path.is_file():
                path.unlink()
                self.logger.info(f"Deleted file: {path}")
            elif path.is_dir():
                shutil.rmtree(path)
                self.logger.info(f"Deleted directory: {path}")
            else:
                self.logger.warning(f"Path does not exist or is not a file/directory: {path}")
                self.skipped_count += 1
                return False
            
            self.cleaned_count += 1
            self.total_size_freed += size
            return True
            
        except PermissionError:
            self.logger.error(f"Permission denied: {path}")
            self.failed_count += 1
            return False
        except FileNotFoundError:
            self.logger.warning(f"File not found (may have been deleted): {path}")
            self.skipped_count += 1
            return False
        except Exception as e:
            self.logger.error(f"Failed to delete {path}: {e}")
            self.failed_count += 1
            return False
    
    def preview_cleanup(self) -> Dict[str, List[Path]]:
        """Preview what will be cleaned without actually deleting"""
        artifacts = self.find_all_artifacts()
        
        if not artifacts:
            print("No generated artifacts found to clean!")
            return artifacts
        
        print("\n" + "="*70)
        print("CLEANUP PREVIEW")
        print("="*70)
        
        total_items = 0
        total_size = 0
        
        for category, paths in artifacts.items():
            print(f"\n📁 {category}:")
            print("-" * 40)
            
            category_items = 0
            category_size = 0
            
            for path in paths:
                size = self._get_file_size(path)
                size_str = self._format_size(size)
                path_type = "📁" if path.is_dir() else "📄"
                
                print(f"  {path_type} {path} ({size_str})")
                category_items += 1
                category_size += size
            
            print(f"  └── Total: {category_items} items, {self._format_size(category_size)}")
            total_items += category_items
            total_size += category_size
        
        print("\n" + "="*70)
        print(f"SUMMARY: {total_items} items, {self._format_size(total_size)} total")
        print("="*70)
        
        return artifacts
    
    def clean_artifacts(self, artifacts: Dict[str, List[Path]], 
                       categories: Set[str] = None) -> bool:
        """Clean the specified artifacts"""
        if not artifacts:
            return True
        
        # Filter by categories if specified
        if categories:
            artifacts = {k: v for k, v in artifacts.items() if k in categories}
        
        print("\n" + "="*70)
        print("STARTING CLEANUP")
        print("="*70)
        
        for category, paths in artifacts.items():
            print(f"\n Cleaning {category}...")
            
            for path in paths:
                self._safe_remove(path)
        
        self._print_cleanup_summary()
        return self.failed_count == 0
    
    def _print_cleanup_summary(self):
        """Print cleanup summary"""
        print("\n" + "="*70)
        print("CLEANUP SUMMARY")
        print("="*70)
        
        print(f"✅ Successfully cleaned: {self.cleaned_count} items")
        print(f"❌ Failed to clean: {self.failed_count} items")
        print(f"Skipped: {self.skipped_count} items")
        print(f"Total space freed: {self._format_size(self.total_size_freed)}")
        
        if self.failed_count == 0:
            print("\n Cleanup completed successfully!")
        elif self.cleaned_count > self.failed_count:
            print("\n⚠️  Cleanup mostly successful. Check logs for details.")
        else:
            print("\n❌ Cleanup had significant issues. Check logs for details.")
    
    def interactive_cleanup(self):
        """Interactive cleanup with user choices"""
        artifacts = self.preview_cleanup()
        
        if not artifacts:
            return True
        
        print("\nChoose cleanup options:")
        print("1. Clean all artifacts")
        print("2. Choose specific categories")
        print("3. Cancel cleanup")
        
        while True:
            try:
                choice = input("\nEnter your choice (1-3): ").strip()
                
                if choice == '1':
                    # Confirm before cleaning all
                    confirm = input(f"\n⚠️  This will permanently delete all {sum(len(p) for p in artifacts.values())} items. Type 'YES' to confirm: ").strip()
                    if confirm == 'YES':
                        return self.clean_artifacts(artifacts)
                    else:
                        print("Cleanup cancelled.")
                        return False
                
                elif choice == '2':
                    print("\nAvailable categories:")
                    categories = list(artifacts.keys())
                    for i, category in enumerate(categories, 1):
                        item_count = len(artifacts[category])
                        print(f"{i}. {category} ({item_count} items)")
                    
                    while True:
                        try:
                            selection = input(f"\nEnter category numbers (1-{len(categories)}, separated by spaces): ").strip()
                            if not selection:
                                continue
                            
                            selected_indices = [int(x) - 1 for x in selection.split()]
                            selected_categories = set()
                            
                            for idx in selected_indices:
                                if 0 <= idx < len(categories):
                                    selected_categories.add(categories[idx])
                                else:
                                    print(f"Invalid selection: {idx + 1}")
                                    break
                            else:
                                if selected_categories:
                                    selected_artifacts = {k: v for k, v in artifacts.items() if k in selected_categories}
                                    total_items = sum(len(p) for p in selected_artifacts.values())
                                    
                                    confirm = input(f"\n⚠️  This will delete {total_items} items from selected categories. Type 'YES' to confirm: ").strip()
                                    if confirm == 'YES':
                                        return self.clean_artifacts(artifacts, selected_categories)
                                    else:
                                        print("Cleanup cancelled.")
                                        return False
                                else:
                                    print("No valid categories selected.")
                        except ValueError:
                            print("Invalid input. Please enter numbers only.")
                        except KeyboardInterrupt:
                            print("\nCleanup cancelled by user.")
                            return False
                
                elif choice == '3':
                    print("Cleanup cancelled.")
                    return False
                
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
                    
            except KeyboardInterrupt:
                print("\nCleanup cancelled by user.")
                return False
    
    def force_cleanup(self):
        """Force cleanup without prompts (for automation)"""
        artifacts = self.find_all_artifacts()
        return self.clean_artifacts(artifacts)


def main():
    """Main entry point"""
    print("Enhanced Artifact Cleanup Tool")
    print("=" * 50)
    
    cleaner = ArtifactCleaner()
    
    # Check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] in ['--force', '-f']:
            print("Running in force mode (no prompts)...")
            success = cleaner.force_cleanup()
        elif sys.argv[1] in ['--preview', '-p']:
            print("Preview mode - no files will be deleted.")
            cleaner.preview_cleanup()
            return
        elif sys.argv[1] in ['--help', '-h']:
            print("Usage:")
            print("  python clean_generated_artifacts.py           # Interactive mode")
            print("  python clean_generated_artifacts.py --force   # Force cleanup")
            print("  python clean_generated_artifacts.py --preview # Preview only")
            print("  python clean_generated_artifacts.py --help    # Show this help")
            return
        else:
            print(f"Unknown argument: {sys.argv[1]}")
            print("Use --help for usage information.")
            return
    else:
        # Interactive mode
        success = cleaner.interactive_cleanup()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()