import logging
def handle_issue_deleted(data):
    issue=data.get('issue',{})
    issue_key=issue.get('key')
    issue_id=issue.get('id')
    logging.info(f"Issue deleted: {issue_key} (ID: {issue_id})")
