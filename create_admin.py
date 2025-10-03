from app import db, User
from werkzeug.security import generate_password_hash

def create_admin():
    username = "DevTole"
    password = "DevTole"
    role = "admin"
    if User.query.filter_by(username=username).first():
        print("Admin user already exists.")
        return
    admin = User(
        username=username,
        password_hash=generate_password_hash(password),
        role=role
    )
    db.session.add(admin)
    db.session.commit()
    print("Admin user created successfully.")

if __name__ == "__main__":
    from app import app
    with app.app_context():
        create_admin()
