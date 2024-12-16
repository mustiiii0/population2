from app import db

class Person(db.Model):
    __tablename__ = 'persons'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    date_of_death = db.Column(db.Date, nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        """Returns person data as a dictionary."""
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": str(self.date_of_birth),
            "date_of_death": str(self.date_of_death) if self.date_of_death else None,
        }
