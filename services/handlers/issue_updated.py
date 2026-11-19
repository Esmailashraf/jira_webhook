import logging
def handle_issue_updated(data):
    issue=data.get('issue',{})
    issue_key=issue.get('key')
    change_log=data.get('changelog',{})
    items=change_log.get('items',[])
    if not items:
        logging.info(f"Issue updated: {issue_key} - No changes detected")
        return
    for item in items:
        field=item.get('field')
        old_value=item.get('fromString')
        new_value=item.get('toString')
        logging.info(f"Issue updated: {issue_key} - Field '{field}' changed from '{old_value}' to'{new_value}'")
