from dotenv import load_dotenv
from app import create_app, db
from flask_migrate import Migrate

app = create_app()
load_dotenv()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
