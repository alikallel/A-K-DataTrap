# A-K DataTrap

A-K DataTrap is an advanced deception framework that populates systems with realistic but fake data to create convincing decoy environments. It is designed for security testing, digital forensics, red teaming, and education purposes.

---

## Features

- **SSH Key Generation**  
  Generate SSH keys in OS-appropriate formats.

- **Web History Injection**  
  Inject realistic browsing history into Chrome, Chromium, Brave, Edge, and Firefox using dynamic, schema-aware techniques.

- **Document Generation**  
  Create documents in multiple formats: TXT, CSV, JSON, HTML, and more.

- **API Key Generation**  
  Generate fake API keys and credentials for AWS, GCP, Azure, OpenAI, GitHub, Docker, Stripe, Slack, and databases.

- **Source Code Generation**  
  Produce source code files in various programming languages.

- **Log Generation**  
  Simulate system and application logs in OS-specific formats.

---

## Supported Platforms

- **Linux**
- **Windows**

---

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-org/ak-datatrap.git
   cd ak-datatrap
   ```

2. **Run the main application:**
   ```bash
   python main.py
   ```

3. **Follow the prompts:**
   - The application will auto-detect your OS.
   - Choose which operations to perform (or run all).
   - Artifacts are generated in user-appropriate directories.

---

##  Project Structure
````
├── main.py                  # Main application entry point
├── os_detector.py           # OS detection utilities
├── README.md                # This file
│
├── apikeygenerator/         # API key generation components
│   ├── api_factory.py
│   ├── api_key_generator.py
│   ├── linux_generator.py
│   └── windows_generator.py
│
├── documentgenerator/       # Document generation components
│   ├── document_factory.py
│   ├── document_generator.py
│   ├── linux_generator.py
│   └── windows_generator.py
│
├── loggenerator/            # Log generation components
│   ├── log_factory.py
│   ├── log_generator.py
│   ├── linux_generator.py
│   └── windows_generator.py
│
├── sourcecodegenerator/     # Source code generation components
│   ├── source_code_factory.py
│   ├── source_code_generator.py
│   ├── linux_generator.py
│   └── windows_generator.py
│
├── sshkeygenerator/         # SSH key generation components
│   ├── factory.py
│   ├── ssh_key_generator.py
│   ├── linux_generator.py
│   └── windows_generator.py
│
└── webhistory/              # Web history injection components
    ├── history_factory.py
    ├── web_history_injector.py
    ├── linux_history_injector.py
    └── windows_history_injector.py
````
---

## Cleaning Up
To remove generated artifacts, you can run the cleanup script:

```bash
# Interactive mode (default)
python clean_generated_artifacts.py

# Preview what would be deleted
python clean_generated_artifacts.py --preview

# Force cleanup without prompts
python clean_generated_artifacts.py --force

# Show help
python clean_generated_artifacts.py --help
```

---


## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer
This tool is intended for legitimate security testing and educational purposes only. Use responsibly and only on systems you have permission to access.