#!/usr/bin/python3
"""
    Initializing app.py api
"""

from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Closes the storage"""
    storage.close()

@app.errorhandler(404)
def handle_404_error(error):
    """Handles 404 errors and returns a JSON response"""
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    import os

    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
