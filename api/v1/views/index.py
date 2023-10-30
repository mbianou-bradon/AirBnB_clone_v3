#!/usr/bin/python3
""" First apu route and response statust"""

from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'])
def get_stats():
    stats = {}
    classes = ['Amenity', 'City', 'Place', 'Review', 'State', 'User']

    for cls in classes:
        count = storage.count(cls)
        stats[cls] = count

    return jsonify(stats)

