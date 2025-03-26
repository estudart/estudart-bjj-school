from flask import Flask
from flasgger import Swagger
from flask_cors import CORS

from services.api.routes import bp_student
from utils.extensions import db

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

    db.init_app(app)

    swagger_config = {
        "headers": [
        ],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": f"/index.html/",
        "title": "BJJ School API",
    }

    # Initialize Swagger
    swagger = Swagger(app, config=swagger_config)

    @app.route("/healthcheck", methods=["GET"])
    def health_check():
        """
        Healthcheck endpoint
        ---
        tags:
            - Healthcheck
        responses:
            200:
                desecription: Status OK
        """
        return {"message": "Status OK"}, 200
    
    with app.app_context():
        db.create_all()

    app.register_blueprint(bp_student, url_prefix="/api/v1")

    return app

