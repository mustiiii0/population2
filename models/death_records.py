from app import db

class DeathRecord(db.Model):
    __tablename__ = 'death_records'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('persons.id'), nullable=False)
    cause_of_death = db.Column(db.String(200), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    person = db.relationship("Person", backref="death_record")

    def to_dict(self):
        """Returns death record data as a dictionary."""
        return {
            "id": self.id,
            "person_id": self.person_id,
            "cause_of_death": self.cause_of_death,
            "person": self.person.to_dict()
        }
