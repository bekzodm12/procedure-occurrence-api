from flask import Flask, jsonify
from procedure import procedure_count_rows, procedure_count_persons_for_n_last_date


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return """
    <p>Welcome to the Procedure Occurrence API!</p>

    <p>The following endpoints are available:</p>

    <p>/countrows</p>
    <p>/countpersons/{n}</p>
    """

@app.route('/countrows', methods=['GET'])
def procedure_query_count_rows():
    return procedure_count_rows()

@app.route('/countpersons/<int:n>', methods=['GET'])
def procedure_query_count_persons(n):
    return procedure_count_persons_for_n_last_date(n)



# Error handler for 404 ("Not found")
@app.errorhandler(404)
def not_found(error):
    return jsonify({
    'success': False,
    'error': 404,
    'message': 'Page Not found'
    }), 404

# Error handler for 500 ("Internal server error")
@app.errorhandler(500)
def server_error(error):
    return jsonify({
        'success': False,
        'error': 500,
        'message': 'Internal server error'
    }), 500

if __name__ == '__main__':
    app.run(debug=True)