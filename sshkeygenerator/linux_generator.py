#!/usr/bin/env python3
"""
Linux SSH Key Generator module
Handles SSH key generation for Linux systems using bash scripts
"""

import os
import subprocess
from sshkeygenerator.ssh_key_generator import SSHKeyGenerator


class LinuxSSHKeyGenerator(SSHKeyGenerator):
    """SSH key generator for Linux systems"""
    
    def _create_bash_script(self):
        """Create the bash script content"""
        return '''#!/bin/bash
# Create SSH directory if it doesn't exist
mkdir -p ~/.ssh

# Create fake SSH private key
cat > ~/.ssh/id_rsa << 'EOF'
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
EOF

# Create fake SSH public key
cat > ~/.ssh/id_rsa.pub << 'EOF'
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAkq8+8PUebmXxpDtxHuo32kXleQWDYfBjy8v2YrqttPh5nexTXBfFjPqczilDytXd8baEv14LVoHuQPewXi03rETm9D3BHbJTyY/uAfWMvR5Li83aozyyLlsXXEr2kDd0TbIfuUzitPqdX3BLW4vd4XmAHyYLu03bErilD29Hp8DXITm0vyY/eEPbJTqdk fake-user@fake-host
EOF

# Set appropriate permissions
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
chmod 700 ~/.ssh

echo "Fake SSH key files created successfully in ~/.ssh/"
echo "Private key: ~/.ssh/id_rsa"
echo "Public key: ~/.ssh/id_rsa.pub"
'''
    
    def generate_keys(self):
        """Execute bash script to generate SSH keys on Linux"""
        script_content = self._create_bash_script()
        script_path = '/tmp/create_fake_ssh.sh'
        
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