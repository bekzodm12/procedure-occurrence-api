from flask import Flask, jsonify
from procedure import procedure_count_rows, procedure_count_persons_for_n_last_date


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """
    Index endpoint which is called upon lauch of development server
    """
    return """
    <p>Welcome to the Procedure Occurrence API!</p>

    <p>Endpoints despcription is available <a href="https://app.swaggerhub.com/apis/MAKHMUDOVB/ProcedureOccurrenceAPI/1.0.0" target="_blank">here</a>.</p>
    """

@app.route('/countrows', methods=['GET'])
def procedure_query_count_rows():
    """
    This endpoint returns the total count of rows in table procedure_occurrence
    """
    return procedure_count_rows()

@app.route('/countpersons/<int:n>', methods=['GET'])
def procedure_query_count_persons(n):
    """
    This endpoint returns the total count of distinct persons in the last N procedure_date from procedure_occurrence table
    """
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