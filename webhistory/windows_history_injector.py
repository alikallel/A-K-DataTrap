#!/usr/bin/env python3
"""
Windows Web History Injector module
Handles web history injection for Windows systems
"""


import sqlite3
import subprocess
import os
import shutil
from pathlib import Path
from datetime import datetime, timedelta
import time
import random
from webhistory.web_history_injector import WebHistoryInjector


class WindowsWebHistoryInjector(WebHistoryInjector):
    """Real web history injector for Windows systems using Python SQLite"""
    
    def __init__(self):
        super().__init__()
        self.chrome_time_epoch = datetime(1601, 1, 1)  # Chrome's epoch

    def _convert_to_chrome_time(self, dt):
        """Convert datetime to Chrome's microsecond timestamp format"""
        delta = dt - self.chrome_time_epoch
        return int(delta.total_seconds() * 1000000)
    
    def _kill_browser_processes(self):
        """Kill browser processes to unlock databases"""
        browsers = ['chrome.exe', 'msedge.exe', 'brave.exe', 'firefox.exe', 'opera.exe']
        killed = []
        
        for browser in browsers:
            try:
                result = subprocess.run(['taskkill', '/F', '/IM', browser], 
                                      capture_output=True, text=True)
                if result.returncode == 0:
                    killed.append(browser)
            except:
                pass
        
        if killed:
            print(f"Killed browser processes: {', '.join(killed)}")
            time.sleep(2)  # Wait for processes to fully terminate
        
        return killed
    
    def _get_table_columns(self, conn, table_name):
        """Return a list of column names for a given table"""
        cursor = conn.execute(f"PRAGMA table_info({table_name})")
        return [row[1] for row in cursor.fetchall()]

    def _insert_url_entry(self, cursor, table_columns, url_id, url, title, visit_count, last_visit_time):
        """Dynamically insert into urls table based on available columns"""
        data = {
            "id": url_id,
            "url": url,
            "title": title,
            "visit_count": visit_count,
            "typed_count": 1,
            "last_visit_time": last_visit_time,
            "hidden": 0
        }
        if "favicon_id" in table_columns:
            data["favicon_id"] = 0
        columns = ", ".join(data.keys())
        placeholders = ", ".join("?" for _ in data)
        sql = f"INSERT OR REPLACE INTO urls ({columns}) VALUES ({placeholders})"
        cursor.execute(sql, tuple(data.values()))

    def _insert_visit_entry(self, cursor, table_columns, url_id, visit_time):
        """Dynamically insert into visits table based on available columns"""
        data = {
            "url": url_id,
            "visit_time": visit_time,
            "from_visit": 0,
            "transition": 805306368,  # PAGE_TRANSITION_TYPED
            "segment_id": 0
        }
        if "visit_duration" in table_columns:
            data["visit_duration"] = random.randint(30000, 300000)
        if "is_indexed" in table_columns:
            data["is_indexed"] = 0
        columns = ", ".join(data.keys())
        placeholders = ", ".join("?" for _ in data)
        sql = f"INSERT INTO visits ({columns}) VALUES ({placeholders})"
        cursor.execute(sql, tuple(data.values()))

    def _inject_chromium_history(self, db_path, browser_name):
        """Inject history into Chromium-based browsers (Chrome, Edge, Brave)"""
        if not db_path.exists():
            print(f"{browser_name} database not found: {db_path}")
            return False
        
        # Create backup
        backup_path = db_path.with_suffix('.backup')
        try:
            shutil.copy2(db_path, backup_path)
            print(f"✓ Backup created: {backup_path}")
        except Exception as e:
            print(f"Warning: Could not create backup: {e}")
        
        try:
            # Connect to database
            conn = sqlite3.connect(str(db_path))
            cursor = conn.cursor()
            
            # Check if tables exist
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='urls';")
            if not cursor.fetchone():
                print(f"URLs table not found in {browser_name} database")
                conn.close()
                return False

            # Dynamically get columns for urls and visits tables
            url_columns = self._get_table_columns(conn, "urls")
            visit_columns = self._get_table_columns(conn, "visits")

            # Get current max URL ID
            cursor.execute("SELECT MAX(id) FROM urls")
            max_id = cursor.fetchone()[0] or 0
            
            # Prepare fake data
            base_time = datetime.now()
            fake_sites = [
                {"url": "https://www.google.com", "title": "Google", "visits": 15},
                {"url": "https://www.youtube.com", "title": "YouTube", "visits": 8},
                {"url": "https://www.facebook.com", "title": "Facebook", "visits": 5},
                {"url": "https://www.amazon.com", "title": "Amazon.com: Online Shopping", "visits": 3},
                {"url": "https://www.wikipedia.org", "title": "Wikipedia", "visits": 4},
                {"url": "https://www.reddit.com", "title": "Reddit - Dive into anything", "visits": 6},
                {"url": "https://www.twitter.com", "title": "Twitter", "visits": 4},
                {"url": "https://www.linkedin.com", "title": "LinkedIn", "visits": 2},
                {"url": "https://www.stackoverflow.com", "title": "Stack Overflow", "visits": 3},
                {"url": "https://www.github.com", "title": "GitHub", "visits": 5},
                {"url": "https://www.netflix.com", "title": "Netflix", "visits": 2},
                {"url": "https://www.spotify.com", "title": "Spotify", "visits": 4},
                {"url": "https://www.instagram.com", "title": "Instagram", "visits": 3},
                {"url": "https://www.tiktok.com", "title": "TikTok", "visits": 2},
                {"url": "https://www.twitch.tv", "title": "Twitch", "visits": 1}
            ]
            
            # Insert URLs and visits dynamically
            url_id = max_id + 1
            for site in fake_sites:
                # Random last visit time (within last 30 days)
                days_ago = random.randint(1, 30)
                hours_ago = random.randint(0, 23)
                last_visit = base_time - timedelta(days=days_ago, hours=hours_ago)
                chrome_time = self._convert_to_chrome_time(last_visit)
                
                self._insert_url_entry(cursor, url_columns, url_id, site['url'], site['title'], site['visits'], chrome_time)
                
                # Insert visits
                for i in range(site['visits']):
                    visit_days_ago = random.randint(1, 30)
                    visit_hours_ago = random.randint(0, 23)
                    visit_time = base_time - timedelta(days=visit_days_ago, hours=visit_hours_ago)
                    visit_chrome_time = self._convert_to_chrome_time(visit_time)
                    self._insert_visit_entry(cursor, visit_columns, url_id, visit_chrome_time)
                
                url_id += 1
            
            # Commit changes
            conn.commit()
            conn.close()
            
            print(f"✅ Successfully injected {len(fake_sites)} URLs into {browser_name}")
            return True
            
        except sqlite3.Error as e:
            print(f"❌ SQLite error for {browser_name}: {e}")
            return False
        except Exception as e:
            print(f"❌ Error injecting {browser_name} history: {e}")
            return False
    
    def _inject_firefox_history(self, db_path):
        """Inject history into Firefox places.sqlite"""
        if not db_path or not db_path.exists():
            print("Firefox database not found")
            return False
        
        # Create backup
        backup_path = db_path.with_suffix('.sqlite.backup')
        try:
            shutil.copy2(db_path, backup_path)
            print(f"✓ Firefox backup created: {backup_path}")
        except Exception as e:
            print(f"Warning: Could not create Firefox backup: {e}")
        
        try:
            conn = sqlite3.connect(str(db_path))
            cursor = conn.cursor()
            
            # Check if tables exist
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='moz_places';")
            if not cursor.fetchone():
                print("Firefox moz_places table not found")
                conn.close()
                return False
            
            # Get current max place ID
            cursor.execute("SELECT MAX(id) FROM moz_places")
            max_id = cursor.fetchone()[0] or 0
            
            # Firefox uses microseconds since Unix epoch
            base_time = datetime.now()
            
            fake_sites = [
                {"url": "https://www.google.com", "title": "Google"},
                {"url": "https://www.youtube.com", "title": "YouTube"},
                {"url": "https://www.facebook.com", "title": "Facebook"},
                {"url": "https://www.amazon.com", "title": "Amazon"},
                {"url": "https://www.wikipedia.org", "title": "Wikipedia"}
            ]
            
            place_id = max_id + 1
            for site in fake_sites:
                days_ago = random.randint(1, 30)
                visit_time = base_time - timedelta(days=days_ago)
                firefox_time = int(visit_time.timestamp() * 1000000)  # Microseconds
                
                # Insert into moz_places
                cursor.execute("""
                    INSERT OR REPLACE INTO moz_places 
                    (id, url, title, visit_count, last_visit_date, guid)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (place_id, site['url'], site['title'], random.randint(1, 10), firefox_time, f"fake_{place_id}"))
                
                # Insert into moz_historyvisits
                cursor.execute("""
                    INSERT INTO moz_historyvisits 
                    (place_id, visit_date, visit_type, session)
                    VALUES (?, ?, 1, 0)
                """, (place_id, firefox_time))
                
                place_id += 1
            
            conn.commit()
            conn.close()
            
            print(f"✅ Successfully injected {len(fake_sites)} URLs into Firefox")
            return True
            
        except sqlite3.Error as e:
            print(f"❌ Firefox SQLite error: {e}")
            return False
        except Exception as e:
            print(f"❌ Error injecting Firefox history: {e}")
            return False
    
    def inject_history(self):
        """Execute real history injection on Windows"""
        print("🔄 Starting real web history injection...")
        print("⚠️  WARNING: This will close all browser windows!")
        
        # Ask for confirmation
        response = input("Continue? (y/N): ").strip().lower()
        if response not in ['y', 'yes']:
            print("Operation cancelled.")
            return type('Result', (), {'returncode': 1, 'stdout': '', 'stderr': 'Cancelled by user'})()
        
        # Kill browser processes
        killed_browsers = self._kill_browser_processes()
        
        success_count = 0
        total_browsers = 0
        results = []
        
        # Chrome
        chrome_path = Path.home() / 'AppData/Local/Google/Chrome/User Data/Default/History'
        if chrome_path.exists():
            total_browsers += 1
            if self._inject_chromium_history(chrome_path, 'Chrome'):
                success_count += 1
                results.append("✅ Chrome: Success")
            else:
                results.append("❌ Chrome: Failed")
        
        # Edge
        edge_path = Path.home() / 'AppData/Local/Microsoft/Edge/User Data/Default/History'
        if edge_path.exists():
            total_browsers += 1
            if self._inject_chromium_history(edge_path, 'Edge'):
                success_count += 1
                results.append("✅ Edge: Success")
            else:
                results.append("❌ Edge: Failed")
        
        # Brave
        brave_path = Path.home() / 'AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/History'
        if brave_path.exists():
            total_browsers += 1
            if self._inject_chromium_history(brave_path, 'Brave'):
                success_count += 1
                results.append("✅ Brave: Success")
            else:
                results.append("❌ Brave: Failed")
        
        # Firefox
        firefox_profiles = Path.home() / 'AppData/Roaming/Mozilla/Firefox/Profiles'
        if firefox_profiles.exists():
            for profile_dir in firefox_profiles.iterdir():
                places_db = profile_dir / 'places.sqlite'
                if places_db.exists():
                    total_browsers += 1
                    if self._inject_firefox_history(places_db):
                        success_count += 1
                        results.append("✅ Firefox: Success")
                    else:
                        results.append("❌ Firefox: Failed")
                    break  # Only process first profile found
        
        # Create result object
        stdout_msg = f"""
Real Web History Injection Results:
===================================
Browsers processed: {total_browsers}
Successful injections: {success_count}
Failed injections: {total_browsers - success_count}

Details:
{chr(10).join(results)}

⚠️  Important: 
- Restart your browsers to see the changes
- Check browser history with Ctrl+H
- Backup files were created automatically
"""
        
        if killed_browsers:
            stdout_msg += f"\n Killed browser processes: {', '.join(killed_browsers)}"
            stdout_msg += "\n You can now restart your browsers safely"
        
        return_code = 0 if success_count > 0 else 1
        
        return type('Result', (), {
            'returncode': return_code, 
            'stdout': stdout_msg, 
            'stderr': '' if success_count > 0 else 'No browsers were successfully processed'
        })()