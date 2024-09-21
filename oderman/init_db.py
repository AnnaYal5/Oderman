from app1 import db, app

def init_db():
    with app.app_context():
        try:
            db.create_all()
            print("Database initialized!")
        except Exception as e:
            print(f"Error occurred: {e}")

if __name__ == "__main__":
    init_db()