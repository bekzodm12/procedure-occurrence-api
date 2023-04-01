from flask import Flask
from procedure import procedure_count_rows, procedure_count_persons_for_n_last_date


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return """
    <p>Welcome to the Procedure Occurrence API!</p>

    <p>The following endpoints are available:</p>

    <p>/countrows</p>
    <p>/countpersons/n <i>(here n is an integer)</i></p>
    """

@app.route('/countrows')
def procedure_query_count_rows():
    return procedure_count_rows()

@app.route('/countpersons/<int:n>')
def procedure_query_count_persons(n):
    return procedure_count_persons_for_n_last_date(n)


# Error handler for 404 ("Not found")
@app.errorhandler(404)
def not_found(error):
    return 'Please check your endpoind and try again', 404

if __name__ == '__main__':
    app.run()