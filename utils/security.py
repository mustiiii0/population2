# Placeholder for security.py
from functools import wraps
from flask import abort
from flask_login import current_user
import jwt
from datetime import datetime, timedelta
from config import Config

def require_auth(roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(401)
            if current_user.role not in roles:
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def generate_national_id(birth_date):
    """Generate national ID based on birth date and sequence"""
    date_str = birth_date.strftime('%Y%m%d')
    from models import Person
    # Get count of people born on same date
    count = Person.query.filter(
        Person.birth_date == birth_date
    ).count()
    sequence = format(count + 1, '04d')
    return f"{date_str}-{sequence}"

def generate_token(user_id):
    """Generate JWT token for API authentication"""
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=1)
    }
    return jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')

def verify_token(token):
    """Verify JWT token"""
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    