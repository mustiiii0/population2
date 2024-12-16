from models.person import Person
from models.death_records import DeathRecord
from app import db

def age_distribution():
    """Returns age distribution of persons."""
    persons = Person.query.all()
    current_year = db.func.extract('year', db.func.current_date())
    ages = [current_year - person.date_of_birth.year for person in persons if person.date_of_death is None]
    return {"average_age": sum(ages) / len(ages), "age_distribution": ages}

def death_causes():
    """Returns distribution of death causes."""
    records = DeathRecord.query.all()
    causes = {}
    for record in records:
        causes[record.cause_of_death] = causes.get(record.cause_of_death, 0) + 1
    return causes
