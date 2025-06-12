#!/usr/bin/env python3
"""
Windows API Key Generator module
Handles API key generation for Windows systems using PowerShell scripts
"""

import subprocess
from apikeygenerator.api_key_generator import APIKeyGenerator


class WindowsAPIKeyGenerator(APIKeyGenerator):
    """API key generator for Windows systems"""
    
    def _create_powershell_script(self):
        """Create the PowerShell script content"""
        return '''# Create API keys directory if it doesn't exist
$apiDir = Join-Path $env:USERPROFILE ".api_keys"
if (-not (Test-Path $apiDir)) {
    New-Item -ItemType Directory -Path $apiDir -Force | Out-Null
}

Write-Host "Creating fake API keys for various services..."

# AWS Credentials
$awsCredentials = @"
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
"@

# Google Cloud Service Account
$gcpServiceAccount = @"
{
  "type": "service_account",
  "project_id": "master-project-12345",
  "private_key_id": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC7VJTUt9Us8cKB\nwjlCYvXIFklyQY5uAdAzz06vdkUyU77uL2jSHVSuqAthUvoXdlrU4Y+v6uIgNmz7\n2sp4Mp0w7HM4j6tkEOtWGqjO5r2qmgbV9C6J6sF8CZVgY+9e5pZMJq2w7uV+2mGg\n...(truncated for brevity)\n-----END PRIVATE KEY-----\n",
  "client_email": "master-service@master-project-12345.iam.gserviceaccount.com",
  "client_id": "123456789012345678901",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/master-service%40master-project-12345.iam.gserviceaccount.com"
}
"@

# OpenAI API Key
$openaiEnv = @"
OPENAI_API_KEY=sk-master1234567890abcdefghijklmnopqrstuvwxyz123456789012345
OPENAI_ORG_ID=org-master0123456789abcdefghijklmn
"@

# GitHub Personal Access Token
$githubEnv = @"
GITHUB_TOKEN=ghp_master1234567890abcdefghijklmnopqrstuvwxyz123
GITHUB_USERNAME=master-developer
"@

# Docker Hub Credentials
$dockerEnv = @"
DOCKER_USERNAME=master-dockeruser
DOCKER_PASSWORD=master-docker-password-123
DOCKER_EMAIL=master-user@example.com
"@

# Azure Credentials
$azureEnv = @"
AZURE_CLIENT_ID=12345678-1234-1234-1234-123456789012
AZURE_CLIENT_SECRET=master-azure-secret-key-12345
AZURE_TENANT_ID=87654321-4321-4321-4321-210987654321
AZURE_SUBSCRIPTION_ID=abcdefab-1234-5678-9012-abcdefabcdef
"@

# Stripe API Keys
$stripeEnv = @"
STRIPE_PUBLISHABLE_KEY=pk_test_master1234567890abcdefghijklmnopqrstuvwxyz
STRIPE_SECRET_KEY=sk_test_master0987654321zyxwvutsrqponmlkjihgfedcba
STRIPE_WEBHOOK_SECRET=whsec_master1234567890abcdefghijklmnopqr
"@

# Slack Bot Token
$slackEnv = @"
SLACK_BOT_TOKEN=xoxb-master-1234567890-1234567890123-master-slacktokenhere123
SLACK_APP_TOKEN=xapp-master-1234567890-1234567890123-master-slackapptoken
SLACK_SIGNING_SECRET=master1234567890abcdefghijklmnopqrstuvwx
"@

# Database Credentials
$databaseEnv = @"
DB_HOST=master-db-host.example.com
DB_PORT=5432
DB_NAME=master_production_db
DB_USER=master_db_user
DB_PASSWORD=master-super-secure-password-123
REDIS_URL=redis://master-redis-host:6379/0
MONGODB_URI=mongodb://master-mongo-user:master-mongo-pass@master-mongo-host:27017/master-db
"@

# Write all the credential files
$files = @{
    "aws_credentials" = $awsCredentials
    "gcp_service_account.json" = $gcpServiceAccount
    "openai.env" = $openaiEnv
    "github.env" = $githubEnv
    "docker.env" = $dockerEnv
    "azure.env" = $azureEnv
    "stripe.env" = $stripeEnv
    "slack.env" = $slackEnv
    "database.env" = $databaseEnv
}

foreach ($fileName in $files.Keys) {
    $filePath = Join-Path $apiDir $fileName
    $files[$fileName] | Out-File -FilePath $filePath -Encoding UTF8 -NoNewline
    
    # Set file permissions (equivalent to chmod 600)
    $acl = Get-Acl $filePath
    $acl.SetAccessRuleProtection($true, $false)
    $accessRule = New-Object System.Security.AccessControl.FileSystemAccessRule($env:USERNAME, "FullControl", "Allow")
    $acl.RemoveAccessRuleAll($acl.Access)
    $acl.SetAccessRule($accessRule)
    Set-Acl -Path $filePath -AclObject $acl
}

Write-Host "Fake API key files created successfully in $apiDir"
Write-Host "Generated credentials for:"
Write-Host "  - AWS (aws_credentials)"
Write-Host "  - Google Cloud Platform (gcp_service_account.json)"
Write-Host "  - OpenAI (openai.env)"
Write-Host "  - GitHub (github.env)"
Write-Host "  - Docker Hub (docker.env)"
Write-Host "  - Azure (azure.env)"
Write-Host "  - Stripe (stripe.env)"
Write-Host "  - Slack (slack.env)"
Write-Host "  - Database connections (database.env)"
Write-Host ""
Write-Host "WARNING: These are FAKE credentials for demonstration purposes only!" -ForegroundColor Red
'''
    
    def generate_keys(self):
        """Execute PowerShell script to generate API keys on Windows"""
        script_content = self._create_powershell_script()
        
        # Execute PowerShell script directly
        result = subprocess.run(
            ['powershell', '-ExecutionPolicy', 'Bypass', '-Command', script_content],
            capture_output=True,
            text=True
        )
        
        return result