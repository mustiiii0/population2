# Placeholder for activity_log.py
from datetime import datetime
from . import db

class ActivityLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    action = db.Column(db.String(50), nullable=False)  # LOGIN, LOGOUT, CREATE, UPDATE, DELETE
    description = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    ip_address = db.Column(db.String(50))

    user = db.relationship('User', backref='activities')

    @staticmethod
    def log_activity(user_id, action, description, ip_address=None):
        log = ActivityLog(
            user_id=user_id,
            action=action,
            description=description,
            ip_address=ip_address
        )
        db.session.add(log)
        db.session.commit()