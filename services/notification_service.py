from flask_mail import Mail, Message
from threading import Thread
from flask import current_app

class NotificationService:
    def __init__(self, app):
        self.mail = Mail(app)
    
    def send_async_email(self, app, msg):
        with app.app_context():
            self.mail.send(msg)
    
    def send_email(self, subject, recipients, body):
        """Send email notification"""
        msg = Message(
            subject,
            sender=current_app.config['MAIL_DEFAULT_SENDER'],
            recipients=recipients
        )
        msg.body = body
        
        Thread(
            target=self.send_async_email,
            args=(current_app._get_current_object(), msg)
        ).start()
    
    def notify_admin_large_update(self, count):
        """Notify admins about large data updates"""
        subject = f"تنبيه: تحديث بيانات كبير ({count} سجل)"
        body = f"""
        تم تحديث عدد كبير من السجلات ({count}).
        يرجى مراجعة سجل النشاطات للتفاصيل.
        """
        admin_emails = self._get_admin_emails()
        self.send_email(subject, admin_emails, body)
    
    def _get_admin_emails(self):
        """Get list of admin email addresses"""
        from models import User
        admins = User.query.filter_by(role='admin').all()
        return [admin.email for admin in admins]