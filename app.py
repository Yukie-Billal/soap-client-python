from flask import Flask, render_template, request
from zeep import Client

client = Client('http://localhost/soap-web-service/calculator.wsdl')
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('calculator.html')
    
    par = request.values

    try:
        if not par.get('num1') or not par.get('num2') or not par.get('operator'):
            raise Exception("Required input")
        
        operator = par['operator']
        if operator == "add":
            result = client.service.add(par['num1'], par['num2'])
            return render_template('calculator.html', result=f"Result: {str(result)}")
        elif operator == "subtract":
            result = client.service.subtract(par['num1'], par['num2'])
            return render_template('calculator.html', result=f"Result: {str(result)}")
        else: raise Exception("Invalid operator")

    except Exception as e:
        print(e)
        return render_template('calculator.html', error=f"500: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)