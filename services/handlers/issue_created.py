import logging
def handle_issue_created(data):
   issue=data.get('issue', {})
   issue_key=issue.get('key')
   issue_summary=issue.get('fields',{}).get('summary')
   logging.info(f"Handling issue created event for issue: {issue_key} - {issue_summary}")
   # Add your logic to process the created issue here 