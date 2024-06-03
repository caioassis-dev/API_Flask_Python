from flask import Flask, make_response, jsonify, request 
from bd_professores import Professores

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
    
@app.route('/professores', methods=['GET'])
def get_professores():
    return make_response(
        jsonify(
            Professores
            )
        )

@app.route('/professores', methods=['POST'])
def create_professor():
    professor = request.json
    Professores.append(professor)
    return Professores
    
app.run()

