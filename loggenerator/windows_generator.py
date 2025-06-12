#!/usr/bin/env python3
"""
Windows Log Generator module
Handles log file generation for Windows systems using PowerShell scripts
"""

import subprocess
from loggenerator.log_generator import LogGenerator


class WindowsLogGenerator(LogGenerator):
    """Log generator for Windows systems"""
    
    def _create_powershell_script(self):
        """Create the PowerShell script content for Windows log generation"""
        return '''# Create logs directory if it doesn't exist
$logsDir = Join-Path $env:USERPROFILE "Generated_Logs"
if (-not (Test-Path $logsDir)) {
    New-Item -ItemType Directory -Path $logsDir -Force | Out-Null
}

# Get current date and time
$currentDate = Get-Date -Format "MM/dd/yyyy HH:mm:ss"
$currentISODate = Get-Date -Format "yyyy-MM-ddTHH:mm:ss.fffZ"
$computerName = $env:COMPUTERNAME
$userName = $env:USERNAME

# Create IIS access log
$iisLog = @"
#Software: Microsoft Internet Information Services 10.0
#Version: 1.0
#Date: 2025-06-12 10:15:23
#Fields: date time s-sitename s-computername s-ip cs-method cs-uri-stem cs-uri-query s-port cs-username c-ip cs-version cs(User-Agent) cs(Cookie) cs(Referer) cs-host sc-status sc-substatus sc-win32-status sc-bytes cs-bytes time-taken
2025-06-12 10:15:23 W3SVC1 $computerName 192.168.1.10 GET /default.htm - 80 - 192.168.1.100 HTTP/1.1 Mozilla/5.0+(Windows+NT+10.0;+Win64;+x64)+AppleWebKit/537.36 - - example.com 200 0 0 2043 354 125
2025-06-12 10:15:45 W3SVC1 $computerName 192.168.1.10 GET /api/users - 80 - 192.168.1.101 HTTP/1.1 Mozilla/5.0+(Windows+NT+10.0;+Win64;+x64)+AppleWebKit/537.36 - http://example.com/ example.com 200 0 0 1532 412 89
2025-06-12 10:16:12 W3SVC1 $computerName 192.168.1.10 POST /login - 80 $userName 192.168.1.102 HTTP/1.1 Mozilla/5.0+(Windows+NT+10.0;+Win64;+x64)+AppleWebKit/537.36 - http://example.com/login example.com 200 0 0 643 287 234
2025-06-12 10:16:34 W3SVC1 $computerName 192.168.1.10 GET /dashboard - 80 $userName 192.168.1.102 HTTP/1.1 Mozilla/5.0+(Windows+NT+10.0;+Win64;+x64)+AppleWebKit/537.36 - http://example.com/ example.com 200 0 0 4521 398 156
2025-06-12 10:17:01 W3SVC1 $computerName 192.168.1.10 GET /api/data - 80 - 192.168.1.103 HTTP/1.1 curl/7.68.0 - - example.com 404 0 2 234 123 12
"@

# Create Windows Event Log style entries
$eventLog = @"
$currentDate Information Application 1000 N/A $computerName Application started successfully. Process ID: 1234
$currentDate Warning Application 1001 N/A $computerName High memory usage detected: 85% of available memory in use
$currentDate Information Security 4624 N/A $computerName An account was successfully logged on. Subject: Security ID: S-1-5-21-123456789-987654321-111111111-1001, Account Name: $userName, Account Domain: $computerName
$currentDate Information System 7036 Service Control Manager $computerName The Windows Update service entered the running state.
$currentDate Error Application 1002 N/A $computerName Failed to connect to external service: Connection timeout after 30 seconds
$currentDate Information Application 1003 N/A $computerName Database connection established successfully to server: localhost:1433
$currentDate Warning System 1530 User Profile Service $computerName Windows detected your registry file is still in use by other applications or services. The file will be unloaded now.
$currentDate Information Security 4634 N/A $computerName An account was logged off. Subject: Security ID: S-1-5-21-123456789-987654321-111111111-1001, Account Name: $userName
"@

# Create PowerShell execution log
$powershellLog = @"
$currentISODate [INFO] PowerShell execution started by user: $userName
$currentISODate [DEBUG] Module 'ActiveDirectory' loaded successfully
$currentISODate [INFO] Executing command: Get-ADUser -Filter *
$currentISODate [WARN] Command execution took longer than expected: 15.3 seconds
$currentISODate [INFO] Returned 245 user objects
$currentISODate [DEBUG] Memory usage: 156.7 MB
$currentISODate [INFO] Script execution completed successfully
$currentISODate [ERROR] Access denied when attempting to read C:\Windows\System32\config\SAM
"@

# Create SQL Server log
$sqlServerLog = @"
$currentDate spid52      Server      Microsoft SQL Server 2019 (RTM-CU19) (KB5023049) - 15.0.4312.2 (X64) 
$currentDate spid52      Server      Authentication mode is MIXED.
$currentDate spid52      Server      Logging SQL Server messages in file 'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\Log\ERRORLOG'.
$currentDate spid7s      Server      Recovery is complete. This is an informational message only. No user action is required.
$currentDate spid53      Login       Login succeeded for user '$userName'. Connection made using Windows authentication.
$currentDate spid53      Database    Setting database option SINGLE_USER to OFF for database [TestDB].
$currentDate spid54      Backup      Database backed up. Database: TestDB, creation date(time): 2025/06/01(10:15:23), pages dumped: 145, first LSN: 37:456:1, last LSN: 37:458:1
$currentDate spid55      Error       Login failed for user 'guest'. Reason: The account is disabled.
"@

# Create application-specific log
$appLog = @"
$currentISODate [INFO] CustomerService - Processing customer order #12345
$currentISODate [DEBUG] CustomerService - Validating customer ID: CUST001
$currentISODate [INFO] InventoryService - Checking product availability for SKU: PROD789
$currentISODate [WARN] InventoryService - Low stock warning: Only 5 units remaining for PROD789
$currentISODate [INFO] PaymentService - Processing payment of $149.99 via credit card
$currentISODate [INFO] PaymentService - Payment authorized successfully - Transaction ID: TXN987654321
$currentISODate [INFO] OrderService - Order #12345 completed successfully
$currentISODate [ERROR] NotificationService - Failed to send order confirmation email: SMTP server unreachable
$currentISODate [INFO] NotificationService - Retrying email notification (attempt 2/3)
$currentISODate [INFO] NotificationService - Email notification sent successfully
"@

# Create system performance log
$perfLog = @"
$currentDate,CPU Usage (%),Memory Usage (MB),Disk Usage (%),Network In (KB/s),Network Out (KB/s)
$currentDate,15.3,2048,67.2,125.4,89.7
$currentDate,23.7,2156,67.3,156.8,102.3
$currentDate,18.9,2089,67.4,98.2,76.5
$currentDate,31.2,2234,67.5,234.6,145.2
$currentDate,28.5,2198,67.6,198.3,123.8
$currentDate,22.1,2167,67.7,167.9,95.4
"@

# Write all log files
$iisLog | Out-File -FilePath (Join-Path $logsDir "iis_access.log") -Encoding UTF8
$eventLog | Out-File -FilePath (Join-Path $logsDir "windows_events.log") -Encoding UTF8
$powershellLog | Out-File -FilePath (Join-Path $logsDir "powershell_execution.log") -Encoding UTF8
$sqlServerLog | Out-File -FilePath (Join-Path $logsDir "sqlserver_error.log") -Encoding UTF8
$appLog | Out-File -FilePath (Join-Path $logsDir "application.log") -Encoding UTF8
$perfLog | Out-File -FilePath (Join-Path $logsDir "performance.csv") -Encoding UTF8

Write-Host "Log files generated successfully in $logsDir"
Write-Host "Generated files:"
Write-Host "- IIS access log: $logsDir\iis_access.log"
Write-Host "- Windows events: $logsDir\windows_events.log"
Write-Host "- PowerShell log: $logsDir\powershell_execution.log"
Write-Host "- SQL Server log: $logsDir\sqlserver_error.log"
Write-Host "- Application log: $logsDir\application.log"
Write-Host "- Performance CSV: $logsDir\performance.csv"
'''
    
    def generate_logs(self):
        """Execute PowerShell script to generate log files on Windows"""
        script_content = self._create_powershell_script()
        
        # Execute PowerShell script directly
        result = subprocess.run(
            ['powershell', '-ExecutionPolicy', 'Bypass', '-Command', script_content],
            capture_output=True,
            text=True
        )
        
        return result