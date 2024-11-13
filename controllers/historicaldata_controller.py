from flask import Blueprint, request, jsonify
from services import historicaldata_service

historicaldata_bp = Blueprint('historicaldata_bp', __name__)

@historicaldata_bp.route('/api/historicaldata', methods=['GET'])
def get_historicaldata():
    historicaldata = historicaldata_service.get_all_historicaldata()
    return jsonify(historicaldata)