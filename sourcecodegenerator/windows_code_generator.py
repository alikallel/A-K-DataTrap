#!/usr/bin/env python3
"""
Windows Source Code Generator module
Handles source code generation for Windows systems using PowerShell scripts
"""

import subprocess
from sourcecodegenerator.source_code_generator import SourceCodeGenerator


class WindowsSourceCodeGenerator(SourceCodeGenerator):
    """Source code generator for Windows systems"""
    
    def _create_powershell_script(self):
        """Create the PowerShell script content"""
        return '''# Create output directories
$baseDir = Join-Path $env:USERPROFILE "Code_Source"
$dirs = @("python", "javascript", "java", "cpp", "powershell", "csharp")

foreach ($dir in $dirs) {
    $fullPath = Join-Path $baseDir $dir
    if (-not (Test-Path $fullPath)) {
        New-Item -ItemType Directory -Path $fullPath -Force | Out-Null
    }
}

# Generate Python source file
$pythonCode = @"
#!/usr/bin/env python3
\"\"\"
Simple calculator application
Demonstrates basic Python programming concepts
\"\"\"

class Calculator:
    \"\"\"A simple calculator class\"\"\"
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        \"\"\"Add two numbers\"\"\"
        result = a + b
        self.history.append(f`"{a} + {b} = {result}`")
        return result
    
    def subtract(self, a, b):
        \"\"\"Subtract two numbers\"\"\"
        result = a - b
        self.history.append(f`"{a} - {b} = {result}`")
        return result
    
    def multiply(self, a, b):
        \"\"\"Multiply two numbers\"\"\"
        result = a * b
        self.history.append(f`"{a} * {b} = {result}`")
        return result
    
    def divide(self, a, b):
        \"\"\"Divide two numbers\"\"\"
        if b == 0:
            raise ValueError(`"Cannot divide by zero`")
        result = a / b
        self.history.append(f`"{a} / {b} = {result}`")
        return result
    
    def get_history(self):
        \"\"\"Get calculation history\"\"\"
        return self.history
    
def main():
    calc = Calculator()
    print(`"Simple Calculator`")
    print(f`"Addition: {calc.add(10, 5)}`")
    print(f`"Subtraction: {calc.subtract(10, 5)}`")
    print(f`"Multiplication: {calc.multiply(10, 5)}`")
    print(f`"Division: {calc.divide(10, 5)}`")
    print(`"History:`", calc.get_history())

if __name__ == `"__main__`":
    main()
"@

# Generate JavaScript source file
$jsCode = @"
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
app.addTodo(`"Learn JavaScript`");
app.addTodo(`"Build a project`");
app.addTodo(`"Deploy to production`");

console.log(`"All todos:`", app.getTodos());
console.log(`"Stats:`", app.getStats());
"@

# Generate C# source file
$csharpCode = @"
/**
 * Employee Management System
 * Demonstrates C# OOP concepts and LINQ
 */

using System;
using System.Collections.Generic;
using System.Linq;

namespace EmployeeManagement
{
    public class Employee
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Department { get; set; }
        public decimal Salary { get; set; }
        public DateTime HireDate { get; set; }

        public Employee(int id, string name, string department, decimal salary)
        {
            Id = id;
            Name = name;
            Department = department;
            Salary = salary;
            HireDate = DateTime.Now;
        }

        public override string ToString()
        {
            return `$`"{Name} (ID: {Id}) - {Department} - `$`${Salary:N2}`";
        }
    }

    public class EmployeeManager
    {
        private List<Employee> employees;
        private int nextId;

        public EmployeeManager()
        {
            employees = new List<Employee>();
            nextId = 1;
        }

        public void AddEmployee(string name, string department, decimal salary)
        {
            var employee = new Employee(nextId++, name, department, salary);
            employees.Add(employee);
        }

        public void RemoveEmployee(int id)
        {
            employees.RemoveAll(e => e.Id == id);
        }

        public Employee GetEmployee(int id)
        {
            return employees.FirstOrDefault(e => e.Id == id);
        }

        public List<Employee> GetEmployeesByDepartment(string department)
        {
            return employees.Where(e => e.Department.Equals(department, StringComparison.OrdinalIgnoreCase)).ToList();
        }

        public decimal GetAverageSalary()
        {
            return employees.Any() ? employees.Average(e => e.Salary) : 0;
        }

        public void DisplayAllEmployees()
        {
            Console.WriteLine(`"=== All Employees ===`");
            foreach (var employee in employees.OrderBy(e => e.Name))
            {
                Console.WriteLine(employee);
            }
        }

        public void DisplayStatistics()
        {
            Console.WriteLine(`"=== Statistics ===`");
            Console.WriteLine(`$`"Total Employees: {employees.Count}`");
            Console.WriteLine(`$`"Average Salary: `$`${GetAverageSalary():N2}`");
            
            var departmentGroups = employees.GroupBy(e => e.Department);
            Console.WriteLine(`"Employees by Department:`");
            foreach (var group in departmentGroups)
            {
                Console.WriteLine(`$`"  {group.Key}: {group.Count()}`");
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var manager = new EmployeeManager();
            
            // Add sample employees
            manager.AddEmployee(`"John Doe`", `"Engineering`", 75000);
            manager.AddEmployee(`"Jane Smith`", `"Marketing`", 65000);
            manager.AddEmployee(`"Bob Johnson`", `"Engineering`", 80000);
            manager.AddEmployee(`"Alice Brown`", `"HR`", 60000);
            manager.AddEmployee(`"Charlie Wilson`", `"Marketing`", 70000);

            manager.DisplayAllEmployees();
            Console.WriteLine();
            manager.DisplayStatistics();

            Console.WriteLine(`"\\nPress any key to exit...`");
            Console.ReadKey();
        }
    }
}
"@

# Generate C++ source file
$cppCode = @"
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
        if (vec.empty()) throw std::runtime_error(`"Vector is empty`");
        return *std::max_element(vec.begin(), vec.end());
    }
    
    static T min_element(const std::vector<T>& vec) {
        if (vec.empty()) throw std::runtime_error(`"Vector is empty`");
        return *std::min_element(vec.begin(), vec.end());
    }
    
    static std::vector<T> filter(const std::vector<T>& vec, std::function<bool(const T&)> predicate) {
        std::vector<T> result;
        std::copy_if(vec.begin(), vec.end(), std::back_inserter(result), predicate);
        return result;
    }
    
    static void print_vector(const std::vector<T>& vec, const std::string& name = `"Vector`") {
        std::cout << name << `": [`";
        for (size_t i = 0; i < vec.size(); ++i) {
            std::cout << vec[i];
            if (i < vec.size() - 1) std::cout << `", `";
        }
        std::cout << `"]`" << std::endl;
    }
};

int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    VectorOperations<int>::print_vector(numbers, `"Numbers`");
    
    std::cout << `"Sum: `" << VectorOperations<int>::sum(numbers) << std::endl;
    std::cout << `"Average: `" << VectorOperations<int>::average(numbers) << std::endl;
    std::cout << `"Max: `" << VectorOperations<int>::max_element(numbers) << std::endl;
    std::cout << `"Min: `" << VectorOperations<int>::min_element(numbers) << std::endl;
    
    auto even_numbers = VectorOperations<int>::filter(numbers, [](const int& n) {
        return n % 2 == 0;
    });
    
    VectorOperations<int>::print_vector(even_numbers, `"Even Numbers`");
    
    return 0;
}
"@

# Generate Java source file
$javaCode = @"
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
        return String.format(`"%s: `$`$.2f at %s`", type, amount, timestamp);
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
            transactions.add(new Transaction(`"Initial Deposit`", initialDeposit));
        }
    }
    
    public void deposit(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException(`"Deposit amount must be positive`");
        }
        balance += amount;
        transactions.add(new Transaction(`"Deposit`", amount));
    }
    
    public void withdraw(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException(`"Withdrawal amount must be positive`");
        }
        if (amount > balance) {
            throw new IllegalArgumentException(`"Insufficient funds`");
        }
        balance -= amount;
        transactions.add(new Transaction(`"Withdrawal`", amount));
    }
    
    public double getBalance() {
        return balance;
    }
    
    public List<Transaction> getTransactionHistory() {
        return new ArrayList<>(transactions);
    }
    
    public static void main(String[] args) {
        BankAccount account = new BankAccount(`"123456789`", `"John Doe`", 1000.0);
        
        account.deposit(500.0);
        account.withdraw(200.0);
        
        System.out.println(`"Balance: `$`" + account.getBalance());
        System.out.println(`"Transaction History:`");
        for (Transaction t : account.getTransactionHistory()) {
            System.out.println(t);
        }
    }
}
"@

# Generate PowerShell script
$powershellCode = @"
# System Information Collector
# Demonstrates PowerShell scripting capabilities

param(
    [switch]`$Detailed,
    [string]`$OutputFile = `"`"
)

function Write-ColorOutput {
    param(
        [string]`$Message,
        [string]`$Color = `"White`"
    )
    Write-Host `$Message -ForegroundColor `$Color
}

function Get-SystemInfo {
    Write-ColorOutput `"=== SYSTEM INFORMATION ===`" -Color `"Cyan`"
    
    `$computerInfo = Get-ComputerInfo -Property @(
        'WindowsProductName',
        'WindowsVersion',
        'TotalPhysicalMemory',
        'CsProcessors'
    )
    
    Write-Host `"OS: `$(`$computerInfo.WindowsProductName)`"
    Write-Host `"Version: `$(`$computerInfo.WindowsVersion)`"
    Write-Host `"Computer Name: `$(`$env:COMPUTERNAME)`"
    Write-Host `"User: `$(`$env:USERNAME)`"
    Write-Host `"Total RAM: `$([math]::Round(`$computerInfo.TotalPhysicalMemory / 1GB, 2)) GB`"
    Write-Host `"`"
}

function Get-DiskInfo {
    Write-ColorOutput `"=== DISK INFORMATION ===`" -Color `"Cyan`"
    
    Get-WmiObject -Class Win32_LogicalDisk | Where-Object { `$_.DriveType -eq 3 } | ForEach-Object {
        `$totalSize = [math]::Round(`$_.Size / 1GB, 2)
        `$freeSpace = [math]::Round(`$_.FreeSpace / 1GB, 2)
        `$usedSpace = `$totalSize - `$freeSpace
        `$percentFree = [math]::Round((`$freeSpace / `$totalSize) * 100, 1)
        
        Write-Host `"Drive `$(`$_.DeviceID)`"
        Write-Host `"  Total: `$totalSize GB`"
        Write-Host `"  Used: `$usedSpace GB`"
        Write-Host `"  Free: `$freeSpace GB (`$percentFree%)`"
        Write-Host `"`"
    }
}

function Get-ProcessInfo {
    Write-ColorOutput `"=== TOP 10 PROCESSES BY CPU ===`" -Color `"Cyan`"
    
    Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 | 
    Format-Table Name, CPU, WorkingSet, Id -AutoSize
}

function Get-ServiceInfo {
    Write-ColorOutput `"=== WINDOWS SERVICES STATUS ===`" -Color `"Cyan`"
    
    `$runningServices = Get-Service | Where-Object { `$_.Status -eq `"Running`" } | Measure-Object
    `$stoppedServices = Get-Service | Where-Object { `$_.Status -eq `"Stopped`" } | Measure-Object
    
    Write-Host `"Running Services: `$(`$runningServices.Count)`"
    Write-Host `"Stopped Services: `$(`$stoppedServices.Count)`"
    
    if (`$Detailed) {
        Write-Host `"`nTop 10 Running Services:`"
        Get-Service | Where-Object { `$_.Status -eq `"Running`" } | Select-Object -First 10 | 
        Format-Table Name, Status, StartType -AutoSize
    }
    Write-Host `"`"
}

function Get-NetworkInfo {
    Write-ColorOutput `"=== NETWORK INFORMATION ===`" -Color `"Cyan`"
    
    Get-NetAdapter | Where-Object { `$_.Status -eq `"Up`" } | ForEach-Object {
        Write-Host `"Interface: `$(`$_.Name)`"
        Write-Host `"  Status: `$(`$_.Status)`"
        Write-Host `"  Speed: `$(`$_.LinkSpeed)`"
        Write-Host `"`"
    }
}

function Main {
    `$startTime = Get-Date
    
    Write-ColorOutput `"PowerShell System Information Collector`" -Color `"Green`"
    Write-ColorOutput `"Generated on: `$(Get-Date)`" -Color `"Yellow`"
    Write-Host `"`"
    
    Get-SystemInfo
    Get-DiskInfo
    Get-ProcessInfo
    Get-ServiceInfo
    Get-NetworkInfo
    
    `$endTime = Get-Date
    `$duration = `$endTime - `$startTime
    
    Write-ColorOutput `"Collection completed in `$(`$duration.TotalSeconds) seconds`" -Color `"Green`"
    
    if (`$OutputFile) {
        Write-Host `"Results saved to: `$OutputFile`"
    }
}

# Execute main function
Main
"@

# Write all files
$pythonPath = Join-Path $baseDir "python\calculator.py"
$jsPath = Join-Path $baseDir "javascript\todo_app.js"
$csharpPath = Join-Path $baseDir "csharp\EmployeeManager.cs"
$cppPath = Join-Path $baseDir "cpp\vector_operations.cpp"
$javaPath = Join-Path $baseDir "java\BankAccount.java"
$powershellPath = Join-Path $baseDir "powershell\system_info.ps1"

$pythonCode | Out-File -FilePath $pythonPath -Encoding UTF8
$jsCode | Out-File -FilePath $jsPath -Encoding UTF8
$csharpCode | Out-File -FilePath $csharpPath -Encoding UTF8
$cppCode | Out-File -FilePath $cppPath -Encoding UTF8
$javaCode | Out-File -FilePath $javaPath -Encoding UTF8
$powershellCode | Out-File -FilePath $powershellPath -Encoding UTF8

Write-Host "Source code files generated successfully!" -ForegroundColor Green
Write-Host "Generated files:" -ForegroundColor Cyan
Write-Host "  Python: $pythonPath" -ForegroundColor White
Write-Host "  JavaScript: $jsPath" -ForegroundColor White
Write-Host "  C#: $csharpPath" -ForegroundColor White
Write-Host "  C++: $cppPath" -ForegroundColor White
Write-Host "  Java: $javaPath" -ForegroundColor White
Write-Host "  PowerShell: $powershellPath" -ForegroundColor White
'''
    
    def generate_source_code(self):
        """Execute PowerShell script to generate source code files on Windows"""
        script_content = self._create_powershell_script()
        
        # Execute PowerShell script directly
        result = subprocess.run(
            ['powershell', '-ExecutionPolicy', 'Bypass', '-Command', script_content],
            capture_output=True,
            text=True
        )
        
        return result