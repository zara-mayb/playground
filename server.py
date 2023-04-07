from flask import Flask , render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("index.html",rep = 3, change = "aqua")

@app.route('/play/<int:num>')
def repeat(num):
    rep = int(num)
    return render_template("index.html", rep = rep)

@app.route('/play/<int:num>/<string:color>')
def change_color(num, color):
    rep = int(num)
    change = color
    return render_template("index.html", rep = rep, change = change)

if __name__=="__main__": 
    app.run(debug=True)