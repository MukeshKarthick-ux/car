"""
Script to create a sample company policies PDF for testing the RAG application
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from datetime import datetime

# Create PDF
pdf_path = "policies.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter,
                        rightMargin=0.75*inch, leftMargin=0.75*inch,
                        topMargin=0.75*inch, bottomMargin=0.75*inch)

# Container for PDF elements
elements = []

# Define styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#1f1f1f'),
    spaceAfter=30,
    alignment=1
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=14,
    textColor=colors.HexColor('#333333'),
    spaceAfter=12,
    spaceBefore=12
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['BodyText'],
    fontSize=11,
    alignment=4,
    spaceAfter=10
)

# Title
elements.append(Paragraph("COMPANY POLICY MANUAL", title_style))
elements.append(Paragraph(f"Effective Date: {datetime.now().strftime('%B %d, %Y')}", styles['Normal']))
elements.append(Spacer(1, 0.3*inch))

# Policy 1: Work Hours
elements.append(Paragraph("1. WORK HOURS AND ATTENDANCE POLICY", heading_style))
elements.append(Paragraph(
    "1.1 Standard Work Hours: All employees are expected to work 40 hours per week, "
    "Monday through Friday, from 9:00 AM to 5:00 PM with one hour for lunch. Work-from-home "
    "arrangements must be approved by the employee's direct manager and department head.",
    body_style
))
elements.append(Paragraph(
    "1.2 Attendance: Employees must notify their manager at least 30 minutes before their "
    "scheduled start time if they will be absent or late. Excessive absences may result in "
    "disciplinary action up to and including termination.",
    body_style
))
elements.append(Paragraph(
    "1.3 Tardiness: Arriving more than 15 minutes late without prior approval is considered "
    "late. Three late arrivals in a month will result in a written warning. Chronic tardiness "
    "may lead to suspension or termination.",
    body_style
))

# Policy 2: Code of Conduct
elements.append(Paragraph("2. CODE OF CONDUCT AND PROFESSIONALISM", heading_style))
elements.append(Paragraph(
    "2.1 Professional Behavior: All employees must maintain professional conduct at all times. "
    "This includes appropriate language, respectful treatment of colleagues, clients, and business partners. "
    "Harassment, discrimination, or hostile behavior towards others is strictly prohibited.",
    body_style
))
elements.append(Paragraph(
    "2.2 Dress Code: Business casual attire is required. This means dress pants or skirts with "
    "collared shirts or blouses. Jeans, t-shirts with logos, and flip-flops are not permitted. "
    "Exceptions may be made for specific departments with manager approval.",
    body_style
))
elements.append(Paragraph(
    "2.3 Social Media: Employees must not post confidential company information on personal social media accounts. "
    "Negative comments about the company or its clients on social media may result in disciplinary action.",
    body_style
))

# Policy 3: Confidentiality
elements.append(Paragraph("3. CONFIDENTIALITY AND DATA PROTECTION", heading_style))
elements.append(Paragraph(
    "3.1 Confidential Information: All proprietary information, trade secrets, client lists, and "
    "financial data are considered confidential. Employees must not disclose this information to "
    "unauthorized parties during or after employment.",
    body_style
))
elements.append(Paragraph(
    "3.2 Data Security: Passwords must be at least 12 characters long and changed every 90 days. "
    "Employees must lock their computers when stepping away from their desks. Sharing passwords is strictly prohibited.",
    body_style
))
elements.append(Paragraph(
    "3.3 Document Handling: All confidential documents must be stored securely and destroyed properly. "
    "Removing company documents from the office without authorization is prohibited.",
    body_style
))

# Policy 4: Safety
elements.append(Paragraph("4. WORKPLACE SAFETY AND SECURITY", heading_style))
elements.append(Paragraph(
    "4.1 Safety Compliance: All employees must comply with OSHA regulations and company safety procedures. "
    "Hazardous materials must be handled according to safety data sheets. Safety equipment must be worn as required.",
    body_style
))
elements.append(Paragraph(
    "4.2 Emergency Procedures: Employees must familiarize themselves with emergency evacuation routes and procedures. "
    "Fire drills will be conducted quarterly. All employees must participate.",
    body_style
))
elements.append(Paragraph(
    "4.3 Incident Reporting: All workplace injuries, near-misses, or safety concerns must be reported immediately "
    "to the manager and HR department. Failure to report incidents may result in disciplinary action.",
    body_style
))

# Policy 5: Use of Company Property
elements.append(Paragraph("5. USE OF COMPANY PROPERTY AND EQUIPMENT", heading_style))
elements.append(Paragraph(
    "5.1 Equipment: Company-provided equipment including computers, phones, and vehicles are for business use only. "
    "Personal use must be minimal and approved by management. Equipment must be maintained in good condition.",
    body_style
))
elements.append(Paragraph(
    "5.2 Software: Installing unauthorized software on company computers is prohibited. All software must be "
    "properly licensed. Illegal downloads or software piracy will result in immediate termination.",
    body_style
))
elements.append(Paragraph(
    "5.3 Internet Usage: Company internet is for business purposes. Accessing inappropriate websites, downloading "
    "large files, or streaming video is prohibited. Internet usage may be monitored.",
    body_style
))

# Policy 6: Leave and Time Off
elements.append(Paragraph("6. LEAVE AND TIME OFF POLICY", heading_style))
elements.append(Paragraph(
    "6.1 Vacation: Full-time employees receive 15 days of paid vacation per year. Part-time employees receive "
    "7.5 days. Vacation requests must be submitted 30 days in advance and approved by the manager.",
    body_style
))
elements.append(Paragraph(
    "6.2 Sick Leave: Employees receive 10 days of paid sick leave per year. A doctor's note is required for "
    "absences exceeding three consecutive days.",
    body_style
))
elements.append(Paragraph(
    "6.3 Holidays: The company observes 10 federal holidays plus 2 additional days to be determined by management. "
    "Employees required to work on holidays will receive holiday pay plus regular wages.",
    body_style
))

# Policy 7: Discipline and Termination
elements.append(Paragraph("7. DISCIPLINARY ACTION AND TERMINATION", heading_style))
elements.append(Paragraph(
    "7.1 Discipline: The company follows a progressive discipline policy: verbal warning, written warning, "
    "suspension, and termination. However, severe misconduct may result in immediate termination.",
    body_style
))
elements.append(Paragraph(
    "7.2 Grounds for Immediate Termination: Theft, violence, being under the influence of drugs or alcohol, "
    "gross misconduct, or violation of confidentiality agreements.",
    body_style
))
elements.append(Paragraph(
    "7.3 Final Paycheck: Employees will receive their final paycheck within 5 business days of termination, "
    "including payment for accrued but unused vacation days.",
    body_style
))

# Policy 8: Travel and Expenses
elements.append(Paragraph("8. BUSINESS TRAVEL AND EXPENSE REIMBURSEMENT", heading_style))
elements.append(Paragraph(
    "8.1 Approval: All business travel must be approved in advance by the manager. Employees must use company "
    "approved travel vendors when possible to get discounted rates.",
    body_style
))
elements.append(Paragraph(
    "8.2 Expenses: Reasonable business expenses will be reimbursed within 30 days of submitting receipts. "
    "Alcohol and entertainment expenses require manager approval. Personal expenses will not be reimbursed.",
    body_style
))
elements.append(Paragraph(
    "8.3 Ground Transportation: Employees should use public transportation or company cars when available. "
    "Mileage reimbursement is $0.67 per mile for personal vehicle use on approved business travel.",
    body_style
))

# Build PDF
doc.build(elements)
print(f"✓ Sample policies PDF created successfully: {pdf_path}")
