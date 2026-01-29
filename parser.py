import re
# Company name list
Company_list=[
    "Google","Microsoft","Apple","Amazon","Bounteous","Deloitte","IBM","Meta"
]
# Extract Company Name
def get_company_name(from_email):
    try:
        domain = from_email.split('@')[-1]
        company=domain.split('.')[0]
        return company.capitalize()
    except:
        return "Unknown"
# Extract Status of Application
def detect_status(text):
    if re.search(r"interview|schedule|shortlisted", text, re.I):
        return "Interview"
    elif re.search(r"offer|congratulations|selected", text, re.I):
        return "Offer"
    elif re.search(r"unfortunately|regret|not selected|rejected", text, re.I):
        return "Rejected"
    else:
        return "Applied"
# Extract Role
def extract_role(text):
    role_patterns = [
        r"for ([A-Za-z &\-]+?) role",
        r"position of ([A-Za-z &\-]+)",
        r"application for ([A-Za-z &\-]+)",
        r"role: ([A-Za-z &\-]+)",
    ]

    for pattern in role_patterns:
        match = re.search(pattern, text, re.I)
        if match:
            return match.group(1).strip()

    return "Unknown"
# Comapny from Text
def extract_company_from_text(text):
    for comp in Company_list:
        if comp.lower() in text.lower():
            return comp
    return "Unknown"
# Main Extract Function
def extract_details(subject,body,from_email):
    text= subject+" "+body
    company=get_company_name(from_email)
    if company.lower() in ["gmail", "yahoo", "outlook", "noreply"]:
        company = extract_company_from_text(text)
    role=extract_role(text)
    status=detect_status(text)
    return company, role, status