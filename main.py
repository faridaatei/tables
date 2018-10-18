from flask import (Flask, render_template, request, make_response)
import json

app = Flask('app')

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/addition',methods=['POST'])
def add():
  data=dict(request.form.items())
  
  val1=int(data.get('val1', 0))
  val2=int(data.get('val2', 0))
  total= val1 +  val2
  context = {'total':total,'val1':val1,'val2':val2}
  response = make_response(render_template("add.html",**context))
  response.set_cookie('add_app',json.dumps(context))
  return  response

@app.route('/edit')
def edit():
    data = request.cookies.get('add_app')
    context = json.loads(data)
    response = make_response(render_template("edit.html",**context))
    return response


if __name__== '__main__':
  app.run(host='0.0.0.0',port = 8080) 
