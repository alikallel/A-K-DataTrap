#!/usr/bin/env python3
"""
Windows Document Generator module
Handles document generation for Windows systems using PowerShell and Python libraries
"""

import subprocess
import json
import csv
import os
from pathlib import Path
from datetime import datetime, timedelta
import random
from documentgenerator.document_generator import DocumentGenerator


class WindowsDocumentGenerator(DocumentGenerator):
    """Document generator for Windows systems"""
    
    def _create_powershell_script(self):
        """Create the PowerShell script content for document generation"""
        return '''# Document Generation Script for Windows
# This script creates various types of fake documents

$DocsDir = Join-Path $env:USERPROFILE "Generated_Documents"
$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"

# Create documents directory
if (-not (Test-Path $DocsDir)) {
    New-Item -ItemType Directory -Path $DocsDir -Force | Out-Null
}

Write-Host "Creating fake documents in: $DocsDir"

# Create text documents
$MeetingNotes = @"
Meeting Notes - Project Alpha
Date: $(Get-Date -Format "MMMM dd, yyyy")
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
"@

$ProjectRequirements = @"
Project Requirements Document
Version: 1.2
Last Updated: $(Get-Date -Format "MMMM dd, yyyy")

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
"@

# Write text files
$MeetingNotes | Out-File -FilePath "$DocsDir\\Meeting_Notes_$Timestamp.txt" -Encoding UTF8
$ProjectRequirements | Out-File -FilePath "$DocsDir\\Project_Requirements_$Timestamp.txt" -Encoding UTF8

# Create CSV file
$CsvContent = @"
Department,Allocated,Spent,Remaining,Percentage
Engineering,500000,485000,15000,97%
Marketing,300000,275000,25000,92%
Sales,400000,390000,10000,98%
Operations,250000,235000,15000,94%
HR,150000,145000,5000,97%
"@

$CsvContent | Out-File -FilePath "$DocsDir\\Budget_Analysis_$Timestamp.csv" -Encoding UTF8

# Create JSON configuration file
$JsonConfig = @{
    application = @{
        name = "Enterprise System"
        version = "2.1.0"
        environment = "production"
        created = (Get-Date -Format "yyyy-MM-ddTHH:mm:ss")
    }
    database = @{
        host = "db.company.com"
        port = 5432
        name = "enterprise_db"
        ssl = $true
    }
    features = @{
        authentication = $true
        logging = $true
        monitoring = $true
        caching = $true
    }
    limits = @{
        max_users = 1000
        max_connections = 100
        request_timeout = 30
    }
}

$JsonConfig | ConvertTo-Json -Depth 3 | Out-File -FilePath "$DocsDir\\System_Config_$Timestamp.json" -Encoding UTF8

# Create HTML report
$HtmlReport = @"
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
    <p>Generated on: $(Get-Date)</p>
    
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
"@

$HtmlReport | Out-File -FilePath "$DocsDir\\System_Report_$Timestamp.html" -Encoding UTF8

# Create Markdown documentation
$MarkdownDoc = @"
# API Documentation

## Overview
This document describes the REST API endpoints for the Enterprise System.

## Authentication
All API requests require authentication using Bearer tokens.

``````
Authorization: Bearer <your-token>
``````

## Endpoints

### Users

#### GET /api/users
Returns a list of all users.

**Response:**
``````json
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
``````

#### POST /api/users
Creates a new user.

**Request Body:**
``````json
{
  "username": "jane.doe",
  "email": "jane@company.com",
  "password": "secure_password"
}
``````

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
"@

$MarkdownDoc | Out-File -FilePath "$DocsDir\\API_Documentation_$Timestamp.md" -Encoding UTF8

# Create PowerShell deployment script
$DeployScript = @"
# Deployment Script for Windows
# Version: 1.0

param(
    [string]`$AppName = "enterprise-app",
    [string]`$DeployDir = "C:\\Applications",
    [string]`$BackupDir = "C:\\Backups"
)

Write-Host "Starting deployment process..." -ForegroundColor Green

# Create directories if they don't exist
if (-not (Test-Path `$DeployDir)) {
    New-Item -ItemType Directory -Path `$DeployDir -Force | Out-Null
}
if (-not (Test-Path `$BackupDir)) {
    New-Item -ItemType Directory -Path `$BackupDir -Force | Out-Null
}

# Create backup
`$BackupFile = Join-Path `$BackupDir ("{0}_backup_{1}.zip" -f `$AppName, (Get-Date -Format "yyyyMMdd_HHmmss"))
if (Test-Path (Join-Path `$DeployDir `$AppName)) {
    Write-Host "Creating backup..." -ForegroundColor Yellow
    Compress-Archive -Path (Join-Path `$DeployDir `$AppName) -DestinationPath `$BackupFile -Force
}

# Stop application service (if running)
`$ServiceName = `$AppName
if (Get-Service `$ServiceName -ErrorAction SilentlyContinue) {
    Write-Host "Stopping service: `$ServiceName" -ForegroundColor Yellow
    Stop-Service `$ServiceName -Force
}

# Deploy application
Write-Host "Deploying application..." -ForegroundColor Yellow
`$AppPath = Join-Path `$DeployDir `$AppName
if (Test-Path `$AppPath) {
    Remove-Item `$AppPath -Recurse -Force
}

# Simulate deployment (copy from build directory)
New-Item -ItemType Directory -Path `$AppPath -Force | Out-Null
Write-Host "Application deployed to: `$AppPath" -ForegroundColor Green

# Start service
if (Get-Service `$ServiceName -ErrorAction SilentlyContinue) {
    Write-Host "Starting service: `$ServiceName" -ForegroundColor Green
    Start-Service `$ServiceName
}

Write-Host "Deployment completed at $(Get-Date)" -ForegroundColor Green
"@

$DeployScript | Out-File -FilePath "$DocsDir\\deploy_script_$Timestamp.ps1" -Encoding UTF8

# Create log file
$LogContent = @"
[$(Get-Date -Format "yyyy-MM-dd HH:mm:ss")] INFO: Application started
[$(Get-Date -Format "yyyy-MM-dd HH:mm:ss")] INFO: Database connection established
[$(Get-Date -Format "yyyy-MM-dd HH:mm:ss")] INFO: Cache initialized
[$(Get-Date -Format "yyyy-MM-dd HH:mm:ss")] INFO: User login: john.doe
[$(Get-Date -Format "yyyy-MM-dd HH:mm:ss")] INFO: API request: GET /api/users
[$(Get-Date -Format "yyyy-MM-dd HH:mm:ss")] INFO: Database query executed in 23ms
[$(Get-Date -Format "yyyy-MM-dd HH:mm:ss")] WARN: High memory usage detected: 85%
[$(Get-Date -Format "yyyy-MM-dd HH:mm:ss")] INFO: Memory usage normalized: 72%
[$(Get-Date -Format "yyyy-MM-dd HH:mm:ss")] INFO: Scheduled backup started
[$(Get-Date -Format "yyyy-MM-dd HH:mm:ss")] INFO: Backup completed successfully
[$(Get-Date -Format "yyyy-MM-dd HH:mm:ss")] ERROR: Connection timeout to external service
[$(Get-Date -Format "yyyy-MM-dd HH:mm:ss")] INFO: Retry successful
[$(Get-Date -Format "yyyy-MM-dd HH:mm:ss")] INFO: Daily statistics generated
"@

$LogContent | Out-File -FilePath "$DocsDir\\application_log_$Timestamp.log" -Encoding UTF8

Write-Host ""
Write-Host "✅ Document generation completed!" -ForegroundColor Green
Write-Host "Generated files:" -ForegroundColor Cyan
Get-ChildItem -Path "$DocsDir" -Filter "*$Timestamp*" | ForEach-Object { Write-Host "  - $($_.Name)" }
Write-Host ""
Write-Host "Total files created: $((Get-ChildItem -Path "$DocsDir" -Filter "*$Timestamp*").Count)" -ForegroundColor Green
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
                    "created": datetime.now().isoformat(),
                    "platform": "Windows"
                },
                "database": {
                    "host": "db.company.com",
                    "port": 5432,
                    "name": "enterprise_db",
                    "ssl": True,
                    "connection_pool": 50
                },
                "features": {
                    "authentication": True,
                    "logging": True,
                    "monitoring": True,
                    "caching": True,
                    "analytics": True
                },
                "performance": {
                    "max_users": 1000,
                    "max_connections": 100,
                    "request_timeout": 30,
                    "cpu_usage": f"{random.randint(50, 80)}%",
                    "memory_usage": f"{random.randint(60, 85)}%",
                    "disk_usage": f"{random.randint(30, 70)}%"
                },
                "security": {
                    "encryption": "AES-256",
                    "ssl_version": "TLS 1.3",
                    "auth_method": "OAuth 2.0",
                    "session_timeout": 3600
                }
            }
            
            json_file = self.output_dir / f"system_config_{timestamp}.json"
            with open(json_file, 'w') as f:
                json.dump(config_data, f, indent=2)
            
            # Generate CSV budget data
            csv_file = self.output_dir / f"budget_analysis_{timestamp}.csv"
            with open(csv_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Department', 'Allocated', 'Spent', 'Remaining', 'Percentage', 'Status'])
                
                departments = [
                    ['Engineering', 500000, 485000, 15000, '97%', 'On Track'],
                    ['Marketing', 300000, 275000, 25000, '92%', 'Under Budget'],
                    ['Sales', 400000, 390000, 10000, '98%', 'On Track'],
                    ['Operations', 250000, 235000, 15000, '94%', 'Under Budget'],
                    ['HR', 150000, 145000, 5000, '97%', 'On Track'],
                    ['IT', 200000, 195000, 5000, '98%', 'On Track'],
                    ['Finance', 100000, 92000, 8000, '92%', 'Under Budget']
                ]
                
                for dept in departments:
                    writer.writerow(dept)
            
            # Generate employee data CSV
            employee_csv = self.output_dir / f"employee_data_{timestamp}.csv"
            with open(employee_csv, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['ID', 'Name', 'Department', 'Position', 'Salary', 'Start_Date', 'Status'])
                
                employees = [
                    [1001, 'John Smith', 'Engineering', 'Senior Developer', 95000, '2022-03-15', 'Active'],
                    [1002, 'Sarah Johnson', 'Marketing', 'Marketing Manager', 75000, '2021-08-20', 'Active'],
                    [1003, 'Mike Wilson', 'Sales', 'Sales Representative', 65000, '2023-01-10', 'Active'],
                    [1004, 'Emily Davis', 'HR', 'HR Specialist', 55000, '2022-11-05', 'Active'],
                    [1005, 'David Brown', 'Engineering', 'Lead Developer', 110000, '2020-06-12', 'Active'],
                    [1006, 'Lisa Garcia', 'Operations', 'Operations Manager', 80000, '2021-09-30', 'Active'],
                    [1007, 'Robert Taylor', 'Finance', 'Financial Analyst', 70000, '2022-04-18', 'Active']
                ]
                
                for emp in employees:
                    writer.writerow(emp)
            
            # Generate text documents
            for doc in self.document_data['text_documents']:
                filename = f"{doc['name'].replace('.txt', '')}_{timestamp}.txt"
                filepath = self.output_dir / filename
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(doc['content'])
            
            # Generate project status report
            project_report = self.output_dir / f"project_status_{timestamp}.txt"
            with open(project_report, 'w', encoding='utf-8') as f:
                f.write(f'''Project Status Report
Generated: {datetime.now().strftime("%B %d, %Y at %I:%M %p")}

=== ACTIVE PROJECTS ===

Project Alpha (ID: PRJ-2024-001)
Status: In Progress (85% Complete)
Team Lead: John Smith
Budget: $150,000 (Used: $127,500)
Expected Completion: January 15, 2025
Last Update: Critical milestone achieved - API integration complete

Project Beta (ID: PRJ-2024-002)
Status: Testing Phase (95% Complete)
Team Lead: Sarah Johnson
Budget: $200,000 (Used: $190,000)
Expected Completion: December 30, 2024
Last Update: User acceptance testing in progress

Project Gamma (ID: PRJ-2024-003)
Status: Planning (20% Complete)
Team Lead: Mike Wilson
Budget: $300,000 (Used: $60,000)
Expected Completion: May 30, 2025
Last Update: Requirements gathering phase initiated

=== COMPLETED PROJECTS ===

Project Omega - Completed December 1, 2024
- Final budget: $180,000 (10% under budget)
- Delivered 2 weeks early
- Client satisfaction: 95%

=== KEY METRICS ===

- Total Active Projects: 3
- Total Budget Allocated: $650,000
- Total Budget Used: $377,500
- Average Project Completion: 67%
- On-Time Delivery Rate: 90%

=== UPCOMING MILESTONES ===

December 20, 2024: Project Beta - Final deployment
January 15, 2025: Project Alpha - Phase 1 completion
February 1, 2025: Project Gamma - Design review
''')
            
            return True
            
        except Exception as e:
            print(f"Error generating Python documents: {e}")
            return False
    
    def generate_documents(self):
        """Execute document generation on Windows"""
        print("Generating documents using Windows PowerShell and Python...")
        
        # First, try to generate using PowerShell script
        script_content = self._create_powershell_script()
        script_path = os.path.join(os.environ.get('TEMP', '.'), 'generate_documents.ps1')
        
        try:
            # Write script to file
            with open(script_path, 'w', encoding='utf-8') as f:
                f.write(script_content)
            
            # Execute PowerShell script
            result = subprocess.run([
                'powershell.exe', 
                '-ExecutionPolicy', 'Bypass',
                '-File', script_path
            ], capture_output=True, text=True, encoding='utf-8', errors='replace')
            
            # Also generate documents using Python for additional formats
            python_success = self._generate_python_documents()
            
            # Combine results
            if result.returncode == 0 or python_success:
                combined_stdout = result.stdout if result.stdout else ""
                if python_success:
                    combined_stdout += "\n✅ Additional Python-generated documents created successfully!"
                    combined_stdout += f"\nOutput directory: {self.output_dir}"
                
                return type('Result', (), {
                    'returncode': 0,
                    'stdout': combined_stdout,
                    'stderr': result.stderr if result.stderr else ""
                })()
            else:
                return result
            
        except FileNotFoundError:
            # PowerShell not found, fallback to Python-only generation
            print("PowerShell not found, falling back to Python generation...")
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
                    'stderr': 'Document generation failed: PowerShell not available and Python generation failed'
                })()
        
        except Exception as e:
            # Fallback to Python-only generation
            print(f"PowerShell script failed, falling back to Python generation: {e}")
            if self._generate_python_documents():
                return type('Result', (), {
                    'returncode': 0,
                    'stdout': f"✅ Documents generated successfully using Python fallback!\nOutput directory: {self.output_dir}",
                    'stderr': f'PowerShell failed: {str(e)}'
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
                try:
                    os.remove(script_path)
                except:
                    pass  # Ignore cleanup errors