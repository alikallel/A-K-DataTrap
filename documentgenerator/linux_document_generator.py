#!/usr/bin/env python3
"""
Linux Document Generator module
Handles document generation for Linux systems using native tools and libraries
"""

import os
import subprocess
import json
import csv
from pathlib import Path
from datetime import datetime, timedelta
import random
from documentgenerator.document_generator import DocumentGenerator


class LinuxDocumentGenerator(DocumentGenerator):
    """Document generator for Linux systems"""
    
    def _create_bash_script(self):
        """Create the bash script content for document generation"""
        return '''#!/bin/bash

# Document Generation Script for Linux
# This script creates various types of fake documents

DOCS_DIR="$HOME/Generated_Documents"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Create documents directory
mkdir -p "$DOCS_DIR"

echo "Creating fake documents in: $DOCS_DIR"

# Create text documents
cat > "$DOCS_DIR/Meeting_Notes_${TIMESTAMP}.txt" << 'EOF'
Meeting Notes - Project Alpha
Date: $(date +"%B %d, %Y")
Attendees: John Smith, Sarah Johnson, Mike Wilson

Key Points:
- Q4 targets exceeded by 15%
- New client onboarding scheduled for January
- Budget allocation for next quarter approved
- Team expansion plans discussed

Action Items:
- Prepare quarterly report (Due: Dec 20)
- Schedule client meeting (Due: Dec 18)
- Review hiring requirements (Due: Dec 22)

Next Meeting: December 22, 2024
EOF

cat > "$DOCS_DIR/Project_Requirements_${TIMESTAMP}.txt" << 'EOF'
Project Requirements Document
Version: 1.2
Last Updated: $(date +"%B %d, %Y")

Project Overview:
The goal is to develop a comprehensive system that meets the following requirements:

Functional Requirements:
1. User authentication and authorization
2. Data processing and storage
3. Real-time notifications
4. Reporting and analytics
5. Mobile compatibility

Technical Requirements:
- Database: PostgreSQL 13+
- Backend: Python 3.9+
- Frontend: React 18+
- Cloud: AWS/Azure
- Security: OAuth 2.0, SSL/TLS

Performance Requirements:
- Response time: <200ms
- Uptime: 99.9%
- Concurrent users: 1000+
- Data retention: 7 years

Timeline:
Phase 1: January 2025
Phase 2: March 2025
Phase 3: May 2025
EOF

# Create CSV file
cat > "$DOCS_DIR/Budget_Analysis_${TIMESTAMP}.csv" << 'EOF'
Department,Allocated,Spent,Remaining,Percentage
Engineering,500000,485000,15000,97%
Marketing,300000,275000,25000,92%
Sales,400000,390000,10000,98%
Operations,250000,235000,15000,94%
HR,150000,145000,5000,97%
EOF

# Create JSON configuration file
cat > "$DOCS_DIR/System_Config_${TIMESTAMP}.json" << 'EOF'
{
  "application": {
    "name": "Enterprise System",
    "version": "2.1.0",
    "environment": "production"
  },
  "database": {
    "host": "db.company.com",
    "port": 5432,
    "name": "enterprise_db",
    "ssl": true
  },
  "features": {
    "authentication": true,
    "logging": true,
    "monitoring": true,
    "caching": true
  },
  "limits": {
    "max_users": 1000,
    "max_connections": 100,
    "request_timeout": 30
  }
}
EOF

# Create HTML report
cat > "$DOCS_DIR/System_Report_${TIMESTAMP}.html" << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>System Performance Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .metric { background-color: #e8f5e8; }
    </style>
</head>
<body>
    <h1>System Performance Report</h1>
    <p>Generated on: $(date)</p>
    
    <h2>Performance Metrics</h2>
    <table>
        <tr>
            <th>Metric</th>
            <th>Value</th>
            <th>Status</th>
        </tr>
        <tr>
            <td>CPU Usage</td>
            <td>65%</td>
            <td class="metric">Normal</td>
        </tr>
        <tr>
            <td>Memory Usage</td>
            <td>72%</td>
            <td class="metric">Normal</td>
        </tr>
        <tr>
            <td>Disk Usage</td>
            <td>45%</td>
            <td class="metric">Good</td>
        </tr>
        <tr>
            <td>Network Latency</td>
            <td>23ms</td>
            <td class="metric">Excellent</td>
        </tr>
    </table>
    
    <h2>Recent Activities</h2>
    <ul>
        <li>System backup completed successfully</li>
        <li>Database optimization performed</li>
        <li>Security updates installed</li>
        <li>User accounts synchronized</li>
    </ul>
</body>
</html>
EOF

# Create Markdown documentation
cat > "$DOCS_DIR/API_Documentation_${TIMESTAMP}.md" << 'EOF'
# API Documentation

## Overview
This document describes the REST API endpoints for the Enterprise System.

## Authentication
All API requests require authentication using Bearer tokens.

```
Authorization: Bearer <your-token>
```

## Endpoints

### Users

#### GET /api/users
Returns a list of all users.

**Response:**
```json
{
  "users": [
    {
      "id": 1,
      "username": "john.doe",
      "email": "john@company.com",
      "status": "active"
    }
  ]
}
```

#### POST /api/users
Creates a new user.

**Request Body:**
```json
{
  "username": "jane.doe",
  "email": "jane@company.com",
  "password": "secure_password"
}
```

### Projects

#### GET /api/projects
Returns a list of all projects.

#### POST /api/projects
Creates a new project.

## Error Codes

| Code | Description |
|------|-------------|
| 200  | Success |
| 400  | Bad Request |
| 401  | Unauthorized |
| 404  | Not Found |
| 500  | Internal Server Error |

## Rate Limiting
API requests are limited to 1000 requests per hour per user.
EOF

# Create shell script
cat > "$DOCS_DIR/deploy_script_${TIMESTAMP}.sh" << 'EOF'
#!/bin/bash
# Deployment Script
# Version: 1.0

set -e

echo "Starting deployment process..."

# Configuration
APP_NAME="enterprise-app"
DEPLOY_DIR="/opt/applications"
BACKUP_DIR="/opt/backups"

# Create backup
echo "Creating backup..."
tar -czf "${BACKUP_DIR}/${APP_NAME}_backup_$(date +%Y%m%d_%H%M%S).tar.gz" "${DEPLOY_DIR}/${APP_NAME}"

# Stop application
echo "Stopping application..."
systemctl stop ${APP_NAME}

# Deploy new version
echo "Deploying new version..."
cp -r ./build/* "${DEPLOY_DIR}/${APP_NAME}/"

# Update permissions
chown -R app:app "${DEPLOY_DIR}/${APP_NAME}"
chmod +x "${DEPLOY_DIR}/${APP_NAME}/bin/*"

# Start application
echo "Starting application..."
systemctl start ${APP_NAME}

# Verify deployment
sleep 5
if systemctl is-active --quiet ${APP_NAME}; then
    echo "✅ Deployment successful!"
else
    echo "❌ Deployment failed!"
    exit 1
fi

echo "Deployment completed at $(date)"
EOF

chmod +x "$DOCS_DIR/deploy_script_${TIMESTAMP}.sh"

# Create log file
cat > "$DOCS_DIR/application_log_${TIMESTAMP}.log" << 'EOF'
[2024-12-12 10:00:01] INFO: Application started
[2024-12-12 10:00:02] INFO: Database connection established
[2024-12-12 10:00:03] INFO: Cache initialized
[2024-12-12 10:15:23] INFO: User login: john.doe
[2024-12-12 10:16:45] INFO: API request: GET /api/users
[2024-12-12 10:17:12] INFO: Database query executed in 23ms
[2024-12-12 10:30:45] WARN: High memory usage detected: 85%
[2024-12-12 10:31:02] INFO: Memory usage normalized: 72%
[2024-12-12 11:00:00] INFO: Scheduled backup started
[2024-12-12 11:05:30] INFO: Backup completed successfully
[2024-12-12 11:15:45] ERROR: Connection timeout to external service
[2024-12-12 11:16:00] INFO: Retry successful
[2024-12-12 12:00:00] INFO: Daily statistics generated
EOF

echo "✅ Document generation completed!"
echo "Generated files:"
find "$DOCS_DIR" -name "*${TIMESTAMP}*" -type f
echo ""
echo "Total files created: $(find "$DOCS_DIR" -name "*${TIMESTAMP}*" -type f | wc -l)"
'''
    
    def _generate_python_documents(self):
        """Generate documents using Python libraries"""
        try:
            # Ensure output directory exists
            if not self._create_output_directory():
                return False
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Generate JSON configuration
            config_data = {
                "application": {
                    "name": "Enterprise System",
                    "version": "2.1.0",
                    "environment": "production",
                    "created": datetime.now().isoformat()
                },
                "database": {
                    "host": "db.company.com",
                    "port": 5432,
                    "name": "enterprise_db",
                    "ssl": True
                },
                "features": {
                    "authentication": True,
                    "logging": True,
                    "monitoring": True,
                    "caching": True
                },
                "performance": {
                    "max_users": 1000,
                    "max_connections": 100,
                    "request_timeout": 30,
                    "cpu_usage": f"{random.randint(50, 80)}%",
                    "memory_usage": f"{random.randint(60, 85)}%"
                }
            }
            
            json_file = self.output_dir / f"system_config_{timestamp}.json"
            with open(json_file, 'w') as f:
                json.dump(config_data, f, indent=2)
            
            # Generate CSV budget data
            csv_file = self.output_dir / f"budget_analysis_{timestamp}.csv"
            with open(csv_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Department', 'Allocated', 'Spent', 'Remaining', 'Percentage'])
                
                departments = [
                    ['Engineering', 500000, 485000, 15000, '97%'],
                    ['Marketing', 300000, 275000, 25000, '92%'],
                    ['Sales', 400000, 390000, 10000, '98%'],
                    ['Operations', 250000, 235000, 15000, '94%'],
                    ['HR', 150000, 145000, 5000, '97%']
                ]
                
                for dept in departments:
                    writer.writerow(dept)
            
            # Generate text documents
            for doc in self.document_data['text_documents']:
                filename = f"{doc['name'].replace('.txt', '')}_{timestamp}.txt"
                filepath = self.output_dir / filename
                with open(filepath, 'w') as f:
                    f.write(doc['content'])
            
            return True
            
        except Exception as e:
            print(f"Error generating Python documents: {e}")
            return False
    
    def generate_documents(self):
        """Execute document generation on Linux"""
        print("Generating documents using Linux native tools...")
        
        # First, try to generate using bash script
        script_content = self._create_bash_script()
        script_path = '/tmp/generate_documents.sh'
        
        try:
            # Write script to file
            with open(script_path, 'w') as f:
                f.write(script_content)
            
            # Make script executable
            os.chmod(script_path, 0o755)
            
            # Execute script
            result = subprocess.run(['bash', script_path], capture_output=True, text=True)
            
            # Also generate documents using Python for additional formats
            python_success = self._generate_python_documents()
            
            # Combine results
            if result.returncode == 0 or python_success:
                combined_stdout = result.stdout
                if python_success:
                    combined_stdout += "\n✅ Additional Python-generated documents created successfully!"
                
                return type('Result', (), {
                    'returncode': 0,
                    'stdout': combined_stdout,
                    'stderr': result.stderr
                })()
            else:
                return result
            
        except Exception as e:
            # Fallback to Python-only generation
            print(f"Bash script failed, falling back to Python generation: {e}")
            if self._generate_python_documents():
                return type('Result', (), {
                    'returncode': 0,
                    'stdout': f"✅ Documents generated successfully using Python fallback!\nOutput directory: {self.output_dir}",
                    'stderr': ''
                })()
            else:
                return type('Result', (), {
                    'returncode': 1,
                    'stdout': '',
                    'stderr': f'Document generation failed: {e}'
                })()
        
        finally:
            # Clean up script file if it exists
            if os.path.exists(script_path):
                os.remove(script_path)