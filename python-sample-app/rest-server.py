from flask import Flask
from flask import jsonify

app = Flask(__name__)
@app.route('/api', methods=['GET', 'POST'])
def welcome():
    mock_response = {
        "source": "from mock rest API, served very private through AWS VPC Endpoint Service :P"
    }
    return jsonify(mock_response)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)