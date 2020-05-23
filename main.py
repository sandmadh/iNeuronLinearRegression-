
# importing the necessary dependencies


from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle


app = Flask(__name__) # initializing a flask app


@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            crim    = float(request.form['CRIM'])
            print(crim)
            zn      = float(request.form['ZN'])
            print(zn)
            indus   = float(request.form['INDUS'])
            print(indus)
            chas    = float(request.form['CHAS'])
            print(chas)
            nox     = float(request.form['NOX'])
            print(nox)
            rm      = float(request.form['RM'])
            print(rm)
            age     = float(request.form['AGE'])
            print(age)
            dis     = float(request.form['DIS'])
            print(dis)
            rad     = float(request.form['RAD'])
            print(rad)
            tax     = float(request.form['TAX'])
            print(tax)
            ptratio = float(request.form['PTRATIO'])
            print(ptratio)
            bb      = float(request.form['BB'])
            print(bb)
            lstat   = float(request.form['LSTAT'])
            print(lstat)

            print("read all input features")

            filename1 = 'LinearRegression.pkl'
            loaded_model1 = pickle.load(open(filename1, 'rb')) # loading the model file from the storage
            print("loaded model 1")
            filename2 = 'StandardScalar.pkl'
            loaded_model2 = pickle.load(open(filename2, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            print("have loaded both models)")
            prediction=loaded_model1.predict(loaded_model2.transform([[crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,bb,lstat]]))


            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html',prediction=prediction[0])
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.config["TEMPLATES_AUTO_RELOAD"] = True
    #app.run(host='127.0.0.1', port=8002, debug=True)
	app.run(debug=True) # running the app