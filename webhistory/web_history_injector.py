#!/usr/bin/env python3
"""
Base Web History Injector module
Contains the abstract base class for web history injection
"""

from pathlib import Path
import json
from datetime import datetime, timedelta
import random


class WebHistoryData:
    """Class to manage fake web history data"""
    
    @staticmethod
    def get_fake_history():
        """Generate fake browsing history data"""
        base_time = datetime.now()
        history_entries = []
        
        # Sample websites with realistic visit patterns
        websites = [
            {"url": "https://www.google.com", "title": "Google", "visits": 15},
            {"url": "https://www.youtube.com", "title": "YouTube", "visits": 8},
            {"url": "https://www.facebook.com", "title": "Facebook", "visits": 5},
            {"url": "https://www.amazon.com", "title": "Amazon", "visits": 3},
            {"url": "https://www.wikipedia.org", "title": "Wikipedia", "visits": 4},
            {"url": "https://www.reddit.com", "title": "Reddit", "visits": 6},
            {"url": "https://www.twitter.com", "title": "Twitter", "visits": 4},
            {"url": "https://www.linkedin.com", "title": "LinkedIn", "visits": 2},
            {"url": "https://www.stackoverflow.com", "title": "Stack Overflow", "visits": 3},
            {"url": "https://www.github.com", "title": "GitHub", "visits": 5},
            {"url": "https://www.news.ycombinator.com", "title": "Hacker News", "visits": 2},
            {"url": "https://www.medium.com", "title": "Medium", "visits": 3},
            {"url": "https://www.netflix.com", "title": "Netflix", "visits": 2},
            {"url": "https://www.spotify.com", "title": "Spotify", "visits": 4},
            {"url": "https://www.gmail.com", "title": "Gmail", "visits": 10},
        ]
        
        # Generate entries for the past 30 days
        for site in websites:
            for i in range(site["visits"]):
                # Random time within the last 30 days
                days_ago = random.randint(0, 30)
                hours_ago = random.randint(0, 23)
                minutes_ago = random.randint(0, 59)
                
                visit_time = base_time - timedelta(
                    days=days_ago, 
                    hours=hours_ago, 
                    minutes=minutes_ago
                )
                
                history_entries.append({
                    "url": site["url"],
                    "title": site["title"],
                    "visit_time": visit_time,
                    "visit_count": random.randint(1, 5)
                })
        
        # Sort by visit time (most recent first)
        history_entries.sort(key=lambda x: x["visit_time"], reverse=True)
        return history_entries


class WebHistoryInjector:
    """Base class for web history injection"""
    
    def __init__(self):
        self.history_data = WebHistoryData.get_fake_history()
    
    def get_browser_paths(self):
        """Abstract method to get browser database paths"""
        raise NotImplementedError("Subclasses must implement get_browser_paths method")
    
    def inject_history(self):
        """Abstract method to inject history into browsers"""
        raise NotImplementedError("Subclasses must implement inject_history method")
    
    def backup_existing_history(self, db_path):
        """Create backup of existing browser history"""
        if db_path.exists():
            backup_path = db_path.with_suffix(f"{db_path.suffix}.backup")
            try:
                import shutil
                shutil.copy2(db_path, backup_path)
                return backup_path
            except Exception as e:
                print(f"Warning: Could not backup {db_path}: {e}")
        return None