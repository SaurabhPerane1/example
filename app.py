from flask import Flask, render_template

app = Flask(__name__)  #create instance with argument which return name if we are at python script or return name of that script


@app.route('/')   # / represents current base directory
def front():
    return render_template('index.html')

@app.route('/home')   # / represents current base directory
def home():
    import python_flask


if __name__ == "__main__":   #return main if we are at current python script
    app.run(debug=True)
