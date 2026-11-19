import logging
from services.handlers.issue_created import handle_issue_created
from services.handlers.issue_updated import handle_issue_updated
from services.handlers.issue_deleted import handle_issue_deleted
def dispatch_event(data):
    event=data.get('webhookEvent')
    handlers={
        "jira:issue_created": handle_issue_created,
        "jira:issue_updated": handle_issue_updated,
        "jira:issue_deleted": handle_issue_deleted
    }
    handler=handlers.get(event)
    if handler is None:
        logging.warning(f"No handler found for event: {event}")
        return
    handler(data)
   