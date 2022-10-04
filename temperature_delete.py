from flask import Flask, jsonify, request


app = Flask(__name__)

temperatures = [{
"temp_id" : 1,
"date" : "October 3, 2022",
"temperature" : "48 Degree Celcius"
},
{
"temp_id" : 2,
"date" : "October 4, 2022",
"temperature" : "47 Degree Celcius"
}
]

@app.route('/temp', methods=['GET'])
def displayTemperatures():
    return jsonify(temperatures)
    
@app.route('/temp', methods=['DELETE','POST'])
def deleteIdTemperatures():
    delete_info = request.get_json()
    index = 0
    for i in temperatures:
        if(i['temp_id'] == delete_info['id_to_delete']):
            temperatures.pop(index)
            return 'Temperature was successfully deleted', 200
        index += 1
    return 'NON EXISTING ID, DELETE FAILED'
    
    
if __name__ == '__main__':
    app.run()
