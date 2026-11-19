from flask import Flask  
from routes.health import health_bp
from routes.webhook import webhook_bp               
app = Flask(__name__)

app.register_blueprint(health_bp)
app.register_blueprint(webhook_bp)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)