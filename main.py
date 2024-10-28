from flask import Flask
from config import Config
from models import db
from auth import auth_bp
from tasks import tasks_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(tasks_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
