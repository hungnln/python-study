
from app import *
from utils.api import *
from config.firebase_config import *

if __name__ == "__main__":
    app.run(host=app.config['FLASK_RUN_HOST'])