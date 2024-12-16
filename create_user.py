from app import create_app, db
from models.user import User
from werkzeug.security import generate_password_hash

def create_user(username, email, password):
    """Creates a new user and stores it in the database."""
    app = create_app()
    with app.app_context():
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        print(f"User {username} created successfully.")

if __name__ == "__main__":
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    create_user(username, email, password)
