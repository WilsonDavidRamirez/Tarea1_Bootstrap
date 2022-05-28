from flask import Flask, render_template

app = Flask(__name__)                       

@app.route('/')
def principal():                            #Llamamiento al html
    return  render_template('home.html');

if __name__ == '__main__':                 #Ejecucion del Main
    app.run(debug=True, port=5000)