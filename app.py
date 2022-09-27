from flask import Flask,render_template,request
import pandas as pd
import read
app = Flask(__name__ )

@app.route('/')

def customer():
   data=read.model1
   return render_template('create.html',data=data)
@app.route('/success',methods = ['POST', 'GET'])

def print_data():

   if request.method == 'POST':
      df=read.model1
      print(df)
      result = request.form
      df1=pd.DataFrame(result,index=[0])
      df=df.append(df1)
      print(df)
      df.to_csv("Sravani.csv")
      df.to_dict()
      return render_template("result.html",result = df)

if __name__ == '__main__':
   app.run(debug = True)
