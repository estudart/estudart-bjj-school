import logging

from services.api import create_app

logging.basicConfig(level="INFO")

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)