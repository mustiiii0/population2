from app import create_app, db
from models import *

def create_all_tables():
    """Creates all tables defined in the models."""
    app = create_app()
    with app.app_context():
        db.create_all()
        print("All tables created successfully.")

if __name__ == "__main__":
    create_all_tables()
