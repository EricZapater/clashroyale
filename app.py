from flask import Flask
from controllers.historicaldata_controller import historicaldata_bp

app = Flask(__name__)

app.register_blueprint(historicaldata_bp)

if __name__ == '__main__':
    app.run(debug=True)