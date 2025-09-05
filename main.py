from flask import Flask , jsonify
from flask_cors import CORS , cross_origin
from flask import request
from newDir.m3N import main

app = Flask(__name__)
CORS(app)

def convertto2DArray(data):
    data = data.strip()
    data = data.replace(" ", ",")
    print(data)
    return data

def getDataReady(data):
    '''if str(data) == "None":
        res = "0"
        return res'''
    res = str(main(data))
    #res = convertto2DArray(data)
    #print(res)
    print(data)
    return res

@app.route("/gettext" , methods=["POST"])
@cross_origin()
def getText():
    data = request.json["text"]
    print("json data : " , data)
    res = getDataReady(data)
    dicti = {
        "probability" : res
    }
    dicti = jsonify(dicti)
    return dicti #, 200, {"Access-Control-Allow-Origin": "*"}




if __name__ == "__main__":
    app.run(port=8000 , debug=True)