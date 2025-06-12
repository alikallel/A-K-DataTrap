#!/usr/bin/env python3
"""
Linux Log Generator module
Handles log file generation for Linux systems using bash scripts
"""

import os
import subprocess
from loggenerator.log_generator import LogGenerator


class LinuxLogGenerator(LogGenerator):
    """Log generator for Linux systems"""
    
    def _create_bash_script(self):
        """Create the bash script content for Linux log generation"""
        return '''#!/bin/bash
# Create logs directory if it doesn't exist
mkdir -p ~/Generated_Logs

# Get current date and time
CURRENT_DATE=$(date '+%b %d %H:%M:%S')
CURRENT_YEAR=$(date '+%Y')
HOSTNAME=$(hostname)
USERNAME=$(whoami)

# Create Apache access log
cat > ~/Generated_Logs/apache_access.log << 'EOF'
192.168.1.15 - - [12/Jun/2025:10:15:23 +0000] "GET /index.html HTTP/1.1" 200 2326 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
192.168.1.23 - - [12/Jun/2025:10:15:45 +0000] "GET /api/users HTTP/1.1" 200 1843 "http://example.com/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0"
10.0.0.45 - - [12/Jun/2025:10:16:12 +0000] "POST /login HTTP/1.1" 200 543 "http://example.com/login" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
192.168.1.67 - - [12/Jun/2025:10:16:34 +0000] "GET /dashboard HTTP/1.1" 200 4521 "http://example.com/" "Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0"
10.0.0.12 - - [12/Jun/2025:10:17:01 +0000] "GET /api/data HTTP/1.1" 404 234 "-" "curl/7.68.0"
192.168.1.89 - - [12/Jun/2025:10:17:23 +0000] "GET /static/style.css HTTP/1.1" 200 1245 "http://example.com/dashboard" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
EOF

# Create syslog entries
cat > ~/Generated_Logs/syslog << EOF
$CURRENT_DATE $HOSTNAME systemd[1]: Starting Network Manager...
$CURRENT_DATE $HOSTNAME NetworkManager[1234]: <info>  [1718192523.4567] device (eth0): carrier is ON
$CURRENT_DATE $HOSTNAME kernel: [12345.678901] usb 1-1: new high-speed USB device number 2 using xhci_hcd
$CURRENT_DATE $HOSTNAME systemd[1]: Started Network Manager.
$CURRENT_DATE $HOSTNAME sshd[5678]: Accepted publickey for $USERNAME from 192.168.1.100 port 54321 ssh2: RSA SHA256:abc123def456
$CURRENT_DATE $HOSTNAME sudo: $USERNAME : TTY=pts/0 ; PWD=/home/$USERNAME ; USER=root ; COMMAND=/bin/systemctl status nginx
$CURRENT_DATE $HOSTNAME systemd[1]: nginx.service: Succeeded.
$CURRENT_DATE $HOSTNAME cron[9876]: (root) CMD (test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily ))
EOF

# Create auth log
cat > ~/Generated_Logs/auth.log << EOF
$CURRENT_DATE $HOSTNAME sshd[1234]: Accepted publickey for $USERNAME from 192.168.1.100 port 54321 ssh2: RSA SHA256:abc123def456
$CURRENT_DATE $HOSTNAME sudo: $USERNAME : TTY=pts/0 ; PWD=/home/$USERNAME ; USER=root ; COMMAND=/bin/cat /var/log/syslog
$CURRENT_DATE $HOSTNAME sudo: pam_unix(sudo:session): session opened for user root by $USERNAME(uid=1000)
$CURRENT_DATE $HOSTNAME sudo: pam_unix(sudo:session): session closed for user root
$CURRENT_DATE $HOSTNAME systemd-logind[987]: New session 3 of user $USERNAME.
$CURRENT_DATE $HOSTNAME systemd-logind[987]: Session 3 logged out. Waiting for processes to exit.
EOF

# Create nginx error log
cat > ~/Generated_Logs/nginx_error.log << 'EOF'
2025/06/12 10:15:23 [error] 1234#1234: *1 open() "/var/www/html/favicon.ico" failed (2: No such file or directory), client: 192.168.1.15, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "example.com", referrer: "http://example.com/"
2025/06/12 10:16:45 [warn] 1234#1234: *2 upstream server temporarily disabled while reading response header from upstream, client: 192.168.1.23, server: localhost, request: "GET /api/slow HTTP/1.1", upstream: "http://127.0.0.1:8080/api/slow", host: "example.com"
2025/06/12 10:17:12 [notice] 1234#1234: signal process started
EOF

# Create application log
cat > ~/Generated_Logs/application.log << 'EOF'
2025-06-12T10:15:23.456Z [INFO] Application started successfully
2025-06-12T10:15:24.123Z [DEBUG] Database connection established to localhost:5432
2025-06-12T10:15:25.789Z [INFO] User authentication service initialized
2025-06-12T10:16:01.234Z [WARN] High memory usage detected: 85%
2025-06-12T10:16:45.567Z [INFO] Processing batch job: data_export_20250612
2025-06-12T10:17:12.890Z [ERROR] Failed to connect to external API: timeout after 30s
2025-06-12T10:17:30.123Z [INFO] Retrying external API connection (attempt 2/3)
2025-06-12T10:17:45.456Z [INFO] External API connection restored
EOF

# Create kernel log
cat > ~/Generated_Logs/kernel.log << EOF
$CURRENT_DATE $HOSTNAME kernel: [    0.000000] Linux version 5.15.0-72-generic (buildd@ubuntu) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.1)) #79-Ubuntu SMP Wed Apr 19 08:22:18 UTC 2023
$CURRENT_DATE $HOSTNAME kernel: [    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-5.15.0-72-generic root=UUID=abc123-def4-5678-90ab-cdef12345678 ro quiet splash
$CURRENT_DATE $HOSTNAME kernel: [12345.678901] usb 1-1: new high-speed USB device number 2 using xhci_hcd
$CURRENT_DATE $HOSTNAME kernel: [12346.789012] usb 1-1: New USB device found, idVendor=0781, idProduct=5567, bcdDevice= 1.00
$CURRENT_DATE $HOSTNAME kernel: [12347.890123] usb 1-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
EOF

# Set appropriate permissions
find ~/Generated_Logs -type f -exec chmod 644 {} \;
chmod 755 ~/Generated_Logs

echo "Log files generated successfully in ~/Generated_Logs/"
echo "Generated files:"
echo "- Apache access log: ~/Generated_Logs/apache_access.log"
echo "- System log: ~/Generated_Logs/syslog"
echo "- Authentication log: ~/Generated_Logs/auth.log"
echo "- Nginx error log: ~/Generated_Logs/nginx_error.log"
echo "- Application log: ~/Generated_Logs/application.log"
echo "- Kernel log: ~/Generated_Logs/kernel.log"
'''
    
    def generate_logs(self):
        """Execute bash script to generate log files on Linux"""
        script_content = self._create_bash_script()
        script_path = '/tmp/create_logs.sh'
        
        try:
            # Write script to file
            with open(script_path, 'w') as f:
                f.write(script_content)
            
            # Make script executable
            os.chmod(script_path, 0o755)
            
            # Execute script
            result = subprocess.run(['bash', script_path], capture_output=True, text=True)
            
            return result
            
        finally:
            # Clean up script file if it exists
            if os.path.exists(script_path):
                os.remove(script_path)