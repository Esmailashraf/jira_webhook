from flask import Blueprint,request,jsonify
import logging
from services.event_dispatcher import dispatch_event

logging.basicConfig(level=logging.INFO)
webhook_bp=Blueprint('webhook',__name__)

@webhook_bp.route('/webhook/jira', methods=['POST'])
def handle_jira_webhook():
    try:
        data=request.get_json(silent=True)
        if not isinstance(data,dict) or not data:
            logging.error("No JSON payload received")
            return jsonify({"error": "No JSON payload received"}), 400
        
        event=data.get('webhookEvent')
        if not event:
            logging.error("Missing 'webhookEvent' in payload")
            return jsonify({"error": "Missing 'webhookEvent' in payload"}), 400
        issue=data.get('issue',{})
        if not isinstance(issue,dict) or not issue:
            logging.error("Missing 'issue' in payload")
            return jsonify({"error": "Missing 'issue' in payload"}), 400
        issue_key=issue.get('key')
        if not issue_key:
            logging.error("Missing 'key' in 'issue'")
            return jsonify({"error": "Missing 'key' in 'issue'"}), 400
        logging.info(f"Processing webhook event: {event}, Issue Key: {issue_key}")
        dispatch_event(data)
        return jsonify({
            "status": "received",
            "event": event,
            "issue_key": issue_key
        }), 200
    except Exception:
        logging.exception("Unexpected error processing webhook")

        return jsonify({
            "error": "Internal server error"
        }), 500