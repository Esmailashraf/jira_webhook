from flask import Blueprint
health_bp=Blueprint('health',__name__)

@health_bp.route('/health', methods=['GET'])
def get_health():
    return {
  "status": "UP",
  "application": "Jira Webhook"
},200

