#!/usr/bin/env python3
"""
Windows SSH Key Generator module
Handles SSH key generation for Windows systems using PowerShell scripts
"""

import subprocess
from sshkeygenerator.ssh_key_generator import SSHKeyGenerator


class WindowsSSHKeyGenerator(SSHKeyGenerator):
    """SSH key generator for Windows systems"""
    
    def _create_powershell_script(self):
        """Create the PowerShell script content"""
        return '''# Create SSH directory if it doesn't exist
$sshDir = Join-Path $env:USERPROFILE ".ssh"
if (-not (Test-Path $sshDir)) {
    New-Item -ItemType Directory -Path $sshDir -Force | Out-Null
}

# Create fake SSH private key
$privateKey = @"
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAFwAAAAdzc2gtcn
NhAAAAAwEAAQAAAQEAwJKvPvD1Hm5l8aQ7cR7qN9pF5XkFg2HwY8vL9mK6rT4eZ3sU1w
XxYz6nM4pQ8rV3fG2hL9eC1aB7kD3sF4tN6xE5vQ9wR2yU8mP7gH1jL0eS4vN2qM8t
C5bF1xK9pA3dE2yH7lM4rT6nV9wS1uL3eF5gB8mC7tN2xK4pQ9vR6fA1yE5tL8mP3h
D2yU6nV9wS1uL3eF5gB8mC7tN2xK4pQ9vR6fA1yE5tL8mP3hD2yU6nV9wS1uL3eF5g
B8mC7tN2xK4pQ9vR6fA1yE5tL8mP3hD2yU6nV9wS1uL3eF5gB8mC7tN2xK4pQ9vR6f
A1yE5tL8mP3hD2yU6nV9wS1uL3eF5gB8mC7tN2xK4pQ9vR6fA1yE5tL8mP3hD2yU6n
V9wS1uL3eF5gB8mC7tN2x
-----END OPENSSH PRIVATE KEY-----
"@

# Create fake SSH public key
$publicKey = @"
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAkq8+8PUebmXxpDtxHuo32kXleQWDYfBjy8v2YrqtPh5nexTXBfFjPqczilDytXd8baEv14LVoHuQPewXi03rETm9D3BHbJTyY/uAfWMvR5Li83aozyyLlsXXEr2kDd0TbIfuUzitPqdX3BLW4vd4XmAHyYLu03bErilD29Hp8DXITm0vyY/eEPbJTqdk fake-user@fake-host
"@

# Write the keys to files
$privateKeyPath = Join-Path $sshDir "id_rsa"
$publicKeyPath = Join-Path $sshDir "id_rsa.pub"

$privateKey | Out-File -FilePath $privateKeyPath -Encoding ASCII -NoNewline
$publicKey | Out-File -FilePath $publicKeyPath -Encoding ASCII -NoNewline

# Set file permissions (equivalent to chmod 600 for private key)
$acl = Get-Acl $privateKeyPath
$acl.SetAccessRuleProtection($true, $false)
$accessRule = New-Object System.Security.AccessControl.FileSystemAccessRule($env:USERNAME, "FullControl", "Allow")
$acl.RemoveAccessRuleAll($acl.Access)
$acl.SetAccessRule($accessRule)
Set-Acl -Path $privateKeyPath -AclObject $acl

Write-Host "Fake SSH key files created successfully in $sshDir"
Write-Host "Private key: $privateKeyPath"
Write-Host "Public key: $publicKeyPath"
'''
    
    def generate_keys(self):
        """Execute PowerShell script to generate SSH keys on Windows"""
        script_content = self._create_powershell_script()
        
        # Execute PowerShell script directly
        result = subprocess.run(
            ['powershell', '-ExecutionPolicy', 'Bypass', '-Command', script_content],
            capture_output=True,
            text=True
        )
        
        return result