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
    
@app.route('/temp', methods=['GET','POST'])
def updateIdTemperatures():
    update_info = request.get_json()
    for i in temperatures:
        if(i['temp_id'] == update_info['updated_id']):
            i['temp_id']= update_info['temp_id']
            i['date'] = update_info['date']
            i['temperature']= update_info['temperature']
            return {'id': len(temperatures)}, 200
    return 'UPDATE FAILED'
    
    
if __name__ == '__main__':
    app.run()
