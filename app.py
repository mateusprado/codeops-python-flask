from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
   app_name = "mkt-place-api"
   app.logger.debug("estou em modo debu")

   return render_template("hello.html", app_name=app_name)

@app.route("/users", methods=['GET','POST'])
def users():
  if request.method == "POST":
    return "creating users"
  else:
    return "listing users"

@app.route("/orders")
def orders():
  return "blah"

@app.route("/orders/<int:order_id>")
def show_order(order_id):
  return 'listing order id %d' % order_id

@app.route("/customers", methods=['GET','PUT'])
def customers():
  if request.method == "PUT":
    return "updating customer"
  else:
    return "listing customers"

@app.route("/packages", methods=['GET','DELETE'])
def packages():
  if request.method == "DELETE":
    return "removing package"
  else:
    return "listing packages"
 
if __name__ == "__main__":
  app.run()


