#!/usr/bin/env python3
"""
Linux Source Code Generator module
Handles source code generation for Linux systems using bash scripts
"""

import os
import subprocess
from sourcecodegenerator.source_code_generator import SourceCodeGenerator


class LinuxSourceCodeGenerator(SourceCodeGenerator):
    """Source code generator for Linux systems"""
    
    def _create_bash_script(self):
        """Create the bash script content"""
        return '''#!/bin/bash
# Create output directory if it doesn't exist
mkdir -p ~/Code_Source/{python,javascript,java,cpp,bash,c}

# Generate Python source files
cat > ~/Code_Source/python/calculator.py << 'EOF'
#!/usr/bin/env python3
"""
Simple calculator application
Demonstrates basic Python programming concepts
"""

class Calculator:
    """A simple calculator class"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Add two numbers"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract two numbers"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        """Get calculation history"""
        return self.history
    
def main():
    calc = Calculator()
    print("Simple Calculator")
    print(f"Addition: {calc.add(10, 5)}")
    print(f"Subtraction: {calc.subtract(10, 5)}")
    print(f"Multiplication: {calc.multiply(10, 5)}")
    print(f"Division: {calc.divide(10, 5)}")
    print("History:", calc.get_history())

if __name__ == "__main__":
    main()
EOF

# Generate JavaScript source file
cat > ~/Code_Source/javascript/todo_app.js << 'EOF'
/**
 * Simple Todo Application
 * Demonstrates JavaScript ES6+ features
 */

class TodoApp {
    constructor() {
        this.todos = [];
        this.nextId = 1;
    }

    addTodo(text) {
        const todo = {
            id: this.nextId++,
            text: text,
            completed: false,
            createdAt: new Date()
        };
        this.todos.push(todo);
        return todo;
    }

    removeTodo(id) {
        this.todos = this.todos.filter(todo => todo.id !== id);
    }

    toggleTodo(id) {
        const todo = this.todos.find(todo => todo.id === id);
        if (todo) {
            todo.completed = !todo.completed;
        }
    }

    getTodos(filter = 'all') {
        switch (filter) {
            case 'completed':
                return this.todos.filter(todo => todo.completed);
            case 'active':
                return this.todos.filter(todo => !todo.completed);
            default:
                return this.todos;
        }
    }

    getStats() {
        const total = this.todos.length;
        const completed = this.todos.filter(todo => todo.completed).length;
        const active = total - completed;
        return { total, completed, active };
    }
}

// Example usage
const app = new TodoApp();
app.addTodo("Learn JavaScript");
app.addTodo("Build a project");
app.addTodo("Deploy to production");

console.log("All todos:", app.getTodos());
console.log("Stats:", app.getStats());
EOF

# Generate Java source file
cat > ~/Code_Source/java/BankAccount.java << 'EOF'
/**
 * Bank Account Management System
 * Demonstrates Java OOP concepts
 */

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

class Transaction {
    private String type;
    private double amount;
    private LocalDateTime timestamp;
    
    public Transaction(String type, double amount) {
        this.type = type;
        this.amount = amount;
        this.timestamp = LocalDateTime.now();
    }
    
    // Getters
    public String getType() { return type; }
    public double getAmount() { return amount; }
    public LocalDateTime getTimestamp() { return timestamp; }
    
    @Override
    public String toString() {
        return String.format("%s: $%.2f at %s", type, amount, timestamp);
    }
}

public class BankAccount {
    private String accountNumber;
    private String owner;
    private double balance;
    private List<Transaction> transactions;
    
    public BankAccount(String accountNumber, String owner, double initialDeposit) {
        this.accountNumber = accountNumber;
        this.owner = owner;
        this.balance = initialDeposit;
        this.transactions = new ArrayList<>();
        if (initialDeposit > 0) {
            transactions.add(new Transaction("Initial Deposit", initialDeposit));
        }
    }
    
    public void deposit(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Deposit amount must be positive");
        }
        balance += amount;
        transactions.add(new Transaction("Deposit", amount));
    }
    
    public void withdraw(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdrawal amount must be positive");
        }
        if (amount > balance) {
            throw new IllegalArgumentException("Insufficient funds");
        }
        balance -= amount;
        transactions.add(new Transaction("Withdrawal", amount));
    }
    
    public double getBalance() {
        return balance;
    }
    
    public List<Transaction> getTransactionHistory() {
        return new ArrayList<>(transactions);
    }
    
    public static void main(String[] args) {
        BankAccount account = new BankAccount("123456789", "John Doe", 1000.0);
        
        account.deposit(500.0);
        account.withdraw(200.0);
        
        System.out.println("Balance: $" + account.getBalance());
        System.out.println("Transaction History:");
        for (Transaction t : account.getTransactionHistory()) {
            System.out.println(t);
        }
    }
}
EOF

# Generate C++ source file
cat > ~/Code_Source/cpp/vector_operations.cpp << 'EOF'
/**
 * Vector Operations Library
 * Demonstrates C++ STL and template usage
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <functional>

template<typename T>
class VectorOperations {
public:
    static T sum(const std::vector<T>& vec) {
        return std::accumulate(vec.begin(), vec.end(), T{});
    }
    
    static double average(const std::vector<T>& vec) {
        if (vec.empty()) return 0.0;
        return static_cast<double>(sum(vec)) / vec.size();
    }
    
    static T max_element(const std::vector<T>& vec) {
        if (vec.empty()) throw std::runtime_error("Vector is empty");
        return *std::max_element(vec.begin(), vec.end());
    }
    
    static T min_element(const std::vector<T>& vec) {
        if (vec.empty()) throw std::runtime_error("Vector is empty");
        return *std::min_element(vec.begin(), vec.end());
    }
    
    static std::vector<T> filter(const std::vector<T>& vec, std::function<bool(const T&)> predicate) {
        std::vector<T> result;
        std::copy_if(vec.begin(), vec.end(), std::back_inserter(result), predicate);
        return result;
    }
    
    static void print_vector(const std::vector<T>& vec, const std::string& name = "Vector") {
        std::cout << name << ": [";
        for (size_t i = 0; i < vec.size(); ++i) {
            std::cout << vec[i];
            if (i < vec.size() - 1) std::cout << ", ";
        }
        std::cout << "]" << std::endl;
    }
};

int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    VectorOperations<int>::print_vector(numbers, "Numbers");
    
    std::cout << "Sum: " << VectorOperations<int>::sum(numbers) << std::endl;
    std::cout << "Average: " << VectorOperations<int>::average(numbers) << std::endl;
    std::cout << "Max: " << VectorOperations<int>::max_element(numbers) << std::endl;
    std::cout << "Min: " << VectorOperations<int>::min_element(numbers) << std::endl;
    
    auto even_numbers = VectorOperations<int>::filter(numbers, [](const int& n) {
        return n % 2 == 0;
    });
    
    VectorOperations<int>::print_vector(even_numbers, "Even Numbers");
    
    return 0;
}
EOF

# Generate C source file
cat > ~/Code_Source/c/file_manager.c << 'EOF'
/**
 * Simple File Manager in C
 * Demonstrates file I/O and string manipulation
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h>

#define MAX_PATH_LENGTH 1024
#define MAX_LINE_LENGTH 256

typedef struct {
    char path[MAX_PATH_LENGTH];
    long size;
    int is_directory;
} FileInfo;

int file_exists(const char* filename) {
    struct stat buffer;
    return (stat(filename, &buffer) == 0);
}

long get_file_size(const char* filename) {
    struct stat st;
    if (stat(filename, &st) == 0) {
        return st.st_size;
    }
    return -1;
}

int create_file(const char* filename, const char* content) {
    FILE* file = fopen(filename, "w");
    if (file == NULL) {
        return 0;
    }
    
    if (content != NULL) {
        fprintf(file, "%s", content);
    }
    
    fclose(file);
    return 1;
}

int read_file(const char* filename, char* buffer, size_t buffer_size) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        return 0;
    }
    
    size_t bytes_read = fread(buffer, 1, buffer_size - 1, file);
    buffer[bytes_read] = '\\0';
    
    fclose(file);
    return 1;
}

void print_file_info(const FileInfo* info) {
    printf("Path: %s\\n", info->path);
    printf("Size: %ld bytes\\n", info->size);
    printf("Type: %s\\n", info->is_directory ? "Directory" : "File");
    printf("------------------------\\n");
}

int main() {
    const char* test_filename = "test_file.txt";
    const char* test_content = "Hello, World!\\nThis is a test file created by the C file manager.\\n";
    char buffer[1024];
    
    printf("=== Simple File Manager ===\\n");
    
    // Create a test file
    if (create_file(test_filename, test_content)) {
        printf("File '%s' created successfully.\\n", test_filename);
    } else {
        printf("Failed to create file '%s'.\\n", test_filename);
        return 1;
    }
    
    // Check if file exists
    if (file_exists(test_filename)) {
        printf("File '%s' exists.\\n", test_filename);
        
        // Get file info
        FileInfo info;
        strcpy(info.path, test_filename);
        info.size = get_file_size(test_filename);
        info.is_directory = 0;
        
        print_file_info(&info);
        
        // Read file content
        if (read_file(test_filename, buffer, sizeof(buffer))) {
            printf("File content:\\n%s\\n", buffer);
        }
    }
    
    // Clean up
    if (remove(test_filename) == 0) {
        printf("Test file cleaned up.\\n");
    }
    
    return 0;
}
EOF

# Generate Bash script
cat > ~/Code_Source/bash/system_monitor.sh << 'EOF'
#!/bin/bash
# System Monitor Script
# Demonstrates bash scripting and system commands

set -e  # Exit on any error

# Colors for output
RED='\\033[0;31m'
GREEN='\\033[0;32m'
YELLOW='\\033[1;33m'
BLUE='\\033[0;34m'
NC='\\033[0m' # No Color

# Function to print colored output
print_color() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

# Function to get system information
get_system_info() {
    print_color $BLUE "=== SYSTEM INFORMATION ==="
    echo "Hostname: $(hostname)"
    echo "OS: $(uname -s)"
    echo "Kernel: $(uname -r)"
    echo "Architecture: $(uname -m)"
    echo "Uptime: $(uptime -p 2>/dev/null || uptime)"
    echo
}

# Function to get CPU information
get_cpu_info() {
    print_color $BLUE "=== CPU INFORMATION ==="
    if [ -f /proc/cpuinfo ]; then
        echo "CPU Model: $(grep 'model name' /proc/cpuinfo | head -1 | cut -d: -f2 | xargs)"
        echo "CPU Cores: $(nproc)"
        echo "CPU Usage: $(top -bn1 | grep "Cpu(s)" | cut -d: -f2 | awk '{print $1}' | sed 's/%us,//')%"
    else
        echo "CPU information not available on this system"
    fi
    echo
}

# Function to get memory information
get_memory_info() {
    print_color $BLUE "=== MEMORY INFORMATION ==="
    if command -v free >/dev/null 2>&1; then
        free -h
    elif [ -f /proc/meminfo ]; then
        echo "Total RAM: $(grep MemTotal /proc/meminfo | awk '{print $2, $3}')"
        echo "Available RAM: $(grep MemAvailable /proc/meminfo | awk '{print $2, $3}')"
    else
        echo "Memory information not available"
    fi
    echo
}

# Function to get disk information
get_disk_info() {
    print_color $BLUE "=== DISK INFORMATION ==="
    if command -v df >/dev/null 2>&1; then
        df -h | grep -E '^/dev/'
    else
        echo "Disk information not available"
    fi
    echo
}

# Function to get network information
get_network_info() {
    print_color $BLUE "=== NETWORK INFORMATION ==="
    if command -v ip >/dev/null 2>&1; then
        echo "Network interfaces:"
        ip addr show | grep -E '^[0-9]+:' | awk '{print $2}' | tr -d ':'
    elif command -v ifconfig >/dev/null 2>&1; then
        echo "Network interfaces:"
        ifconfig | grep -E '^[a-z]' | awk '{print $1}' | tr -d ':'
    else
        echo "Network information not available"
    fi
    echo
}

# Function to get running processes
get_top_processes() {
    print_color $BLUE "=== TOP 10 CPU PROCESSES ==="
    if command -v ps >/dev/null 2>&1; then
        ps aux --sort=-%cpu | head -11
    else
        echo "Process information not available"
    fi
    echo
}

# Main function
main() {
    print_color $GREEN "Starting System Monitor..."
    echo "Generated on: $(date)"
    echo
    
    get_system_info
    get_cpu_info
    get_memory_info
    get_disk_info
    get_network_info
    get_top_processes
    
    print_color $GREEN "System monitoring complete!"
}

# Check if script is being sourced or executed
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
EOF

# Make bash script executable
chmod +x ~/Code_Source/bash/system_monitor.sh

echo "Source code files generated successfully!"
echo "Generated files:"
echo "  Python: ~/Code_Source/python/calculator.py"
echo "  JavaScript: ~/Code_Source/javascript/todo_app.js"
echo "  Java: ~/Code_Source/java/BankAccount.java"
echo "  C++: ~/Code_Source/cpp/vector_operations.cpp"
echo "  C: ~/Code_Source/c/file_manager.c"
echo "  Bash: ~/Code_Source/bash/system_monitor.sh"
'''
    
    def generate_source_code(self):
        """Execute bash script to generate source code files on Linux"""
        script_content = self._create_bash_script()
        script_path = '/tmp/create_source_code.sh'
        
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