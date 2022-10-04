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
    
if __name__ == '__main__':
    app.run()
