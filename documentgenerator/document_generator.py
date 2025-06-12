#!/usr/bin/env python3
"""
Base Document Generator module
Contains the abstract base class for document generation
"""

from pathlib import Path
from datetime import datetime
import json
import random


class DocumentData:
    """Class to manage fake document data"""
    
    @staticmethod
    def get_fake_documents():
        """Generate fake document data"""
        return {
            'text_documents': [
                {
                    'name': 'Meeting_Notes_2024.txt',
                    'content': '''Meeting Notes - Project Alpha
Date: December 15, 2024
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
'''
                },
                {
                    'name': 'Project_Requirements.txt',
                    'content': '''Project Requirements Document
Version: 1.2
Last Updated: December 10, 2024

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
'''
                },
                {
                    'name': 'Personal_Journal.txt',
                    'content': '''Personal Journal Entry
Date: December 12, 2024

Today was quite productive. Finished the quarterly review and started planning for next year's goals. The weather was perfect for a morning walk, which helped clear my mind for the day ahead.

Key accomplishments:
- Completed the client presentation
- Reviewed team performance metrics
- Planned vacation schedule for Q1 2025

Tomorrow's priorities:
- Team meeting at 10 AM
- Code review session
- Update project documentation

Reflection:
This quarter has been challenging but rewarding. Looking forward to the holiday break and spending time with family.
'''
                }
            ],
            'word_documents': [
                {
                    'name': 'Business_Proposal.docx',
                    'content': '''BUSINESS PROPOSAL

Company: Tech Solutions Inc.
Date: December 2024
Prepared by: Business Development Team

EXECUTIVE SUMMARY

We propose to develop a comprehensive digital transformation solution for your organization. Our approach combines cutting-edge technology with industry best practices to deliver measurable results.

SCOPE OF WORK

Phase 1: Assessment and Planning (4 weeks)
- Current system analysis
- Requirements gathering
- Solution architecture design
- Project timeline development

Phase 2: Implementation (12 weeks)
- System development
- Integration testing
- User training
- Deployment

Phase 3: Support and Maintenance (Ongoing)
- 24/7 technical support
- Regular system updates
- Performance monitoring
- User support

INVESTMENT

Phase 1: $50,000
Phase 2: $200,000
Phase 3: $5,000/month

BENEFITS

- Increased efficiency by 40%
- Cost reduction of 25%
- Improved customer satisfaction
- Enhanced data security
- Scalable architecture

TIMELINE

Project Duration: 16 weeks
Go-live Date: April 2025

NEXT STEPS

1. Proposal review and approval
2. Contract execution
3. Project kickoff meeting
4. Phase 1 initiation

We look forward to partnering with you on this exciting project.
'''
                }
            ],
            'pdf_documents': [
                {
                    'name': 'Financial_Report_Q4.pdf',
                    'content': '''QUARTERLY FINANCIAL REPORT
Q4 2024

EXECUTIVE SUMMARY
This report presents the financial performance for Q4 2024, highlighting key metrics and trends.

REVENUE ANALYSIS
Total Revenue: $2,450,000
Growth Rate: 18% YoY
Key Drivers:
- Product sales: $1,800,000
- Service revenue: $650,000

EXPENSE BREAKDOWN
Operating Expenses: $1,650,000
- Personnel: $950,000
- Technology: $300,000
- Marketing: $200,000
- General & Admin: $200,000

NET INCOME
Gross Profit: $800,000
Net Income: $650,000
Profit Margin: 26.5%

CASH FLOW
Operating Cash Flow: $750,000
Free Cash Flow: $550,000
Cash on Hand: $1,200,000

KEY PERFORMANCE INDICATORS
- Customer Acquisition Cost: $150
- Customer Lifetime Value: $2,500
- Monthly Recurring Revenue: $185,000
- Churn Rate: 3.2%

OUTLOOK
We expect continued growth in Q1 2025 with projected revenue of $2,800,000.

RECOMMENDATIONS
1. Increase marketing spend by 15%
2. Expand technical team
3. Optimize operational processes
4. Explore new market opportunities
'''
                }
            ],
            'spreadsheet_documents': [
                {
                    'name': 'Budget_Analysis_2024.xlsx',
                    'content': '''BUDGET ANALYSIS 2024

DEPARTMENT BUDGETS
Department,Allocated,Spent,Remaining,Percentage
Engineering,500000,485000,15000,97%
Marketing,300000,275000,25000,92%
Sales,400000,390000,10000,98%
Operations,250000,235000,15000,94%
HR,150000,145000,5000,97%

QUARTERLY BREAKDOWN
Quarter,Revenue,Expenses,Profit,Margin
Q1,1800000,1350000,450000,25%
Q2,2100000,1575000,525000,25%
Q3,2250000,1688000,562000,25%
Q4,2450000,1650000,800000,33%

PROJECT COSTS
Project,Budget,Actual,Variance,Status
Alpha,100000,95000,5000,Complete
Beta,150000,145000,5000,Complete
Gamma,200000,185000,15000,Complete
Delta,250000,240000,10000,In Progress

EMPLOYEE COSTS
Position,Salary,Benefits,Total,Count
Senior Engineer,120000,30000,150000,8
Junior Engineer,80000,20000,100000,12
Manager,100000,25000,125000,5
Administrator,60000,15000,75000,3
'''
                }
            ]
        }
    
    @staticmethod
    def get_document_templates():
        """Get document templates for different types"""
        return {
            'meeting_notes': '''Meeting Notes - {title}
Date: {date}
Attendees: {attendees}

Key Points:
{key_points}

Action Items:
{action_items}

Next Meeting: {next_meeting}
''',
            'project_plan': '''Project Plan - {title}
Version: {version}
Last Updated: {date}

Project Overview:
{overview}

Requirements:
{requirements}

Timeline:
{timeline}

Resources:
{resources}
''',
            'financial_report': '''Financial Report - {period}
Generated: {date}

Revenue Analysis:
{revenue_data}

Expense Breakdown:
{expense_data}

Key Metrics:
{metrics}

Recommendations:
{recommendations}
'''
        }


class DocumentGenerator:
    """Base class for document generation"""
    
    def __init__(self):
        self.document_data = DocumentData.get_fake_documents()
        self.templates = DocumentData.get_document_templates()
        self.output_dir = self._get_documents_directory()
    
    def _get_documents_directory(self):
        """Get the default documents directory path for the current OS"""
        home = Path.home()
        # Try common document directories
        possible_dirs = [
            home / 'Documents',
            home / 'My Documents',
            home / 'Desktop'
        ]
        
        for dir_path in possible_dirs:
            if dir_path.exists():
                return dir_path / 'Generated_Documents'
        
        # Fallback to home directory
        return home / 'Generated_Documents'
    
    def _create_output_directory(self):
        """Create the output directory if it doesn't exist"""
        try:
            self.output_dir.mkdir(parents=True, exist_ok=True)
            return True
        except Exception as e:
            print(f"Error creating output directory: {e}")
            return False
    
    def _generate_filename(self, base_name, extension):
        """Generate a unique filename with timestamp"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{base_name}_{timestamp}{extension}"
    
    def generate_documents(self):
        """Abstract method to be implemented by subclasses"""
        raise NotImplementedError("Subclasses must implement generate_documents method")
    
    def get_supported_formats(self):
        """Get list of supported document formats"""
        return ['txt', 'docx', 'pdf', 'xlsx', 'csv', 'json']