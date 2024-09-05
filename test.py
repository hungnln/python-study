from flask_sqlalchemy import SQLAlchemy

from services.flask_service import app

if __name__ == "__main__":
    print(app.config)
    db = SQLAlchemy(app)

