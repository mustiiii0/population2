from flask import Flask
from extensions import db, jwt
from flask_migrate import Migrate
from api.routes import register_blueprints
import os

# Factory function
def create_app(config_class="config.Config"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    Migrate(app, db)

    # Register blueprints
    register_blueprints(app)

    @app.errorhandler(404)
    def not_found_error(error):
        return {"error": "Resource not found"}, 404

    @app.errorhandler(500)
    def internal_error(error):
        return {"error": "Internal server error"}, 500

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
