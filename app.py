from flask import Flask
from api.routes import api_bp
from config import Config
from services.task_queue import init_task_queue

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register blueprints
    app.register_blueprint(api_bp)

    # Initialize task queue within app context
    with app.app_context():
        init_task_queue(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='192.168.29.96', port=8080, debug=True)