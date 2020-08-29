import createTT
import json
from flask import Flask,jsonify,request

app=Flask("__name__")
app.config["DEBUG"]=True

@app.route('/',methods=['GET'])
def home():
    return(jsonify("HELLO!! Welcome to the homepage!"))

@app.route('/api',methods=['GET'])
def api():
    TT=dict()
    Errors=dict()
    if not 'stream' in request.args:
        return(jsonify("This is the API page --- Pass values with the stream, year and sem params. "))
    else:
        try:
            stream=request.args['stream']
            year=int(request.args['year'])
            sem=int(request.args['sem'])
        except:
            Errors["Error"]="Please enter all keys"

    if 'Error' in Errors:
        return(jsonify(Errors))
    else:
        TT=createTT.returnData(stream,year,sem)
        return(jsonify(TT))
    #TT=createTT.returnData(stream,year,sem)
if __name__=='__main__':
    class component:
        pass
    app.run()
