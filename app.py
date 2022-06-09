

from flask import Flask, render_template, request
import pickle

model=pickle.load(open('random_forest_regression.pkl','rb'))


app=Flask(__name__)
@app.route('/')
def welocme():
    return render_template('index.html')

@app.route('/form.html')
def form():
    return render_template('form.html')

@app.route('/submit',methods=["POST"])
def submit():
    year=float(request.form['year'])
    price=float(request.form['price'])
    no_of_kms=float(request.form['no_of_kms'])
    no_of_owners=float(request.form['no_of_owners'])
    fuel=request.form['fuel']
    D_I=request.form['D_I']
    transmission_type=request.form['transmission_type']


    
    Present_Price=price/100000
    Kms_Driven=no_of_kms
    Owner=no_of_owners
    no_of_years=2022-year

    if fuel=="cng":
        Fuel_Type_Diesel=0
        Fuel_Type_Petrol=0
    elif fuel=="diesel":
        Fuel_Type_Diesel=1
        Fuel_Type_Petrol=0
    elif fuel=="petrol":
        Fuel_Type_Diesel=0
        Fuel_Type_Petrol=1
    
    if D_I=="dealer":
        Seller_Type_Individual=0
    else:
        Seller_Type_Individual=1
    
    if transmission_type=="manual":
        Transmission_Manual=1
    else:
        Transmission_Manual=0
    
    prediction=model.predict([[Present_Price, Kms_Driven, Owner, no_of_years,
       Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual,
       Transmission_Manual]])
    output=round(prediction[0],2)
    return render_template('prediction.html',price=output)

    







if __name__=="__main__":
    app.run(debug=True)