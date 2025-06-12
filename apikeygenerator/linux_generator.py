#!/usr/bin/env python3
"""
Linux API Key Generator module
Handles API key generation for Linux systems using bash scripts
"""

import os
import subprocess
from apikeygenerator.api_key_generator import APIKeyGenerator


class LinuxAPIKeyGenerator(APIKeyGenerator):
    """API key generator for Linux systems"""
    
    def _create_bash_script(self):
        """Create the bash script content"""
        return '''#!/bin/bash
# Create API keys directory if it doesn't exist
mkdir -p ~/.api_keys

# Generate fake API keys for various services
echo "Creating fake API keys for various services..."

# AWS Credentials
cat > ~/.api_keys/aws_credentials << 'EOF'
[default]
aws_access_key_id = AKIA2E4JF7GH8K9L1M2N
aws_secret_access_key = wJalS9dF8g7H6j5K4l3M2n1B0q9W8e7R6t5Y4u3I2o1P
region = us-east-1
output = json

[production]
aws_access_key_id = AKIA9Z8Y7X6W5V4U3T2S
aws_secret_access_key = xKalT0eG9h8I7k6L5m4N3o2C1r0X9f8S7u6Z5v4J3i2H
region = us-west-2
output = json
EOF

# Google Cloud Service Account
cat > ~/.api_keys/gcp_service_account.json << 'EOF'
{
  "type": "service_account",
  "project_id": "master-project-12345",
  "private_key_id": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0",
  "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC7VJTUt9Us8cKB\\nwjlCYvXIFklyQY5uAdAzz06vdkUyU77uL2jSHVSuqAthUvoXdlrU4Y+v6uIgNmz7\\n2sp4Mp0w7HM4j6tkEOtWGqjO5r2qmgbV9C6J6sF8CZVgY+9e5pZMJq2w7uV+2mGg\\n...(truncated for brevity)\\n-----END PRIVATE KEY-----\\n",
  "client_email": "master-service@master-project-12345.iam.gserviceaccount.com",
  "client_id": "123456789012345678901",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/master-service%40master-project-12345.iam.gserviceaccount.com"
}
EOF

# OpenAI API Key
cat > ~/.api_keys/openai.env << 'EOF'
OPENAI_API_KEY=sk-master1234567890abcdefghijklmnopqrstuvwxyz123456789012345
OPENAI_ORG_ID=org-master0123456789abcdefghijklmn
EOF

# GitHub Personal Access Token
cat > ~/.api_keys/github.env << 'EOF'
GITHUB_TOKEN=ghp_master1234567890abcdefghijklmnopqrstuvwxyz123
GITHUB_USERNAME=master-developer
EOF

# Docker Hub Credentials
cat > ~/.api_keys/docker.env << 'EOF'
DOCKER_USERNAME=master-dockeruser
DOCKER_PASSWORD=master-docker-password-123
DOCKER_EMAIL=master-user@example.com
EOF

# Azure Credentials
cat > ~/.api_keys/azure.env << 'EOF'
AZURE_CLIENT_ID=12345678-1234-1234-1234-123456789012
AZURE_CLIENT_SECRET=master-azure-secret-key-12345
AZURE_TENANT_ID=87654321-4321-4321-4321-210987654321
AZURE_SUBSCRIPTION_ID=abcdefab-1234-5678-9012-abcdefabcdef
EOF

# Stripe API Keys
cat > ~/.api_keys/stripe.env << 'EOF'
STRIPE_PUBLISHABLE_KEY=pk_test_master1234567890abcdefghijklmnopqrstuvwxyz
STRIPE_SECRET_KEY=sk_test_master0987654321zyxwvutsrqponmlkjihgfedcba
STRIPE_WEBHOOK_SECRET=whsec_master1234567890abcdefghijklmnopqr
EOF

# Slack Bot Token
cat > ~/.api_keys/slack.env << 'EOF'
SLACK_BOT_TOKEN=xoxb-master-1234567890-1234567890123-master-slacktokenhere123
SLACK_APP_TOKEN=xapp-master-1234567890-1234567890123-master-slackapptoken
SLACK_SIGNING_SECRET=master1234567890abcdefghijklmnopqrstuvwx
EOF

# Database Credentials
cat > ~/.api_keys/database.env << 'EOF'
DB_HOST=master-db-host.example.com
DB_PORT=5432
DB_NAME=master_production_db
DB_USER=master_db_user
DB_PASSWORD=master-super-secure-password-123
REDIS_URL=redis://master-redis-host:6379/0
MONGODB_URI=mongodb://master-mongo-user:master-mongo-pass@master-mongo-host:27017/master-db
EOF

# Set appropriate permissions
chmod 600 ~/.api_keys/*
chmod 700 ~/.api_keys

echo "Fake API key files created successfully in ~/.api_keys/"
echo "Generated credentials for:"
echo "  - AWS (aws_credentials)"
echo "  - Google Cloud Platform (gcp_service_account.json)"
echo "  - OpenAI (openai.env)"
echo "  - GitHub (github.env)"
echo "  - Docker Hub (docker.env)"
echo "  - Azure (azure.env)"
echo "  - Stripe (stripe.env)"
echo "  - Slack (slack.env)"
echo "  - Database connections (database.env)"
echo ""
echo "WARNING: These are FAKE credentials for demonstration purposes only!"
'''
    
    def generate_keys(self):
        """Execute bash script to generate API keys on Linux"""
        script_content = self._create_bash_script()
        script_path = '/tmp/create_master_api_keys.sh'

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