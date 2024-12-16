from flask import jsonify, Blueprint
from utils.statistics import age_distribution, death_causes

statistics_api = Blueprint('statistics_api', __name__)

@statistics_api.route('/statistics/age', methods=['GET'])
def get_age_distribution():
    """API endpoint for age distribution."""
    data = age_distribution()
    return jsonify(data)

@statistics_api.route('/statistics/deaths', methods=['GET'])
def get_death_causes():
    """API endpoint for death causes."""
    data = death_causes()
    return jsonify(data)
