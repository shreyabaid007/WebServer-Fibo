from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route ('/', methods = ['GET'])
def index():

    #fibo_series contains a list of fibonacci series
    fibo_series = [ 0, 1 ]

    #input from console
    fibo_number = input ( "Enter a number: " )

    # creating a fibonacci series in a list upto entered fibo_number
    for i in range ( 2, int ( fibo_number ) ):
        fibo_series.append(fibo_series[i - 1] + fibo_series[i - 2])

    #converting to JSON
    json_string = json.dumps(fibo_series)

    print(fibo_series)

    #renders index.html and returns fibo_series list to html
    return render_template('index.html', temp = fibo_series)


if __name__ == '__main__':
    app.run(
        debug = True,
        host = ('0.0.0.0'),
        port = 80
    )