from flask import Flask, make_response, jsonify
from bd_professores import Professores

app = Flask(__name__)
    
    
@app.route('/professores', methods=['GET'])
def get_professores():
    return make_response(
        jsonify (
            Professores
        )
    )


app.run()

