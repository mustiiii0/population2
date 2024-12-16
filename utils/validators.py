# Placeholder for validators.py
import re
from datetime import datetime

def allowed_file(filename):
    """Check if file extension is allowed"""
    from app import app
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def validate_national_id(national_id):
    """Validate national ID format (YYYYMMDD-XXXX)"""
    pattern = r'^\d{8}-\d{4}$'
    if not re.match(pattern, national_id):
        return False
    
    date_str = national_id[:8]
    try:
        datetime.strptime(date_str, '%Y%m%d')
        return True
    except ValueError:
        return False

def validate_person_data(data):
    """Validate person data before saving"""
    errors = []
    
    # Required fields
    required_fields = ['first_name', 'last_name', 'mother_name', 'gender', 
                      'birth_date', 'residence', 'marital_status']
    
    for field in required_fields:
        if not data.get(field):
            errors.append(f"{field} is required")
    
    # Validate gender
    if data.get('gender') and data['gender'] not in ['male', 'female']:
        errors.append("Invalid gender value")
    
    # Validate marital_status
    valid_statuses = ['single', 'married', 'divorced', 'widowed']
    if data.get('marital_status') and data['marital_status'] not in valid_statuses:
        errors.append("Invalid marital status")
    
    # Validate birth_date
    if data.get('birth_date'):
        try:
            birth_date = datetime.strptime(data['birth_date'], '%Y-%m-%d')
            if birth_date > datetime.now():
                errors.append("Birth date cannot be in the future")
        except ValueError:
            errors.append("Invalid birth date format")
    
    return errors