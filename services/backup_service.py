# Placeholder for backup_service.py
import os
import json
import shutil
from datetime import datetime
from models import Person, db

class BackupService:
    def __init__(self, backup_dir):
        self.backup_dir = backup_dir
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
    
    def create_backup(self):
        """Create a full database backup"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = os.path.join(self.backup_dir, f'backup_{timestamp}')
        
        try:
            # Create backup directory
            os.makedirs(backup_path)
            
            # Backup person data
            persons = Person.query.all()
            person_data = [person.to_dict() for person in persons]
            
            with open(os.path.join(backup_path, 'persons.json'), 'w') as f:
                json.dump(person_data, f, ensure_ascii=False, indent=2)
            
            # Backup database file
            db_path = db.engine.url.database
            if db_path:
                shutil.copy2(db_path, backup_path)
            
            return True, f"Backup created successfully at {backup_path}"
        except Exception as e:
            return False, str(e)
    
    def restore_backup(self, backup_path):
        """Restore from backup"""
        try:
            # Restore person data
            with open(os.path.join(backup_path, 'persons.json'), 'r') as f:
                person_data = json.load(f)
            
            # Clear existing data
            Person.query.delete()
            
            # Insert backup data
            for data in person_data:
                person = Person(**data)
                db.session.add(person)
            
            db.session.commit()
            
            return True, "Backup restored successfully"
        except Exception as e:
            db.session.rollback()
            return False, str(e)