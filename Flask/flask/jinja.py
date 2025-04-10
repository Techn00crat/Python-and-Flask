## Building url dynamically
## Variable rules
## Jinja 2 template engine

### Jinja 2 template engine
"""
{{  }} expression to print output in html
{%...%} for conditions and loops
{#...#} for comments
"""

from flask import Flask, render_template, request,redirect, url_for

"""
It creates an instance of the Flask class,
which will be your WSGI application.
"""

## WSGI application

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<html><H1>Welcome to the Flask App! That's a great start! Let's build something amazing together.</H1></html>"

@app.route('/index')
def index():
    return render_template('index.html', methods = ['GET'])

@app.route('/about')
def about():
    return render_template('about.html')

## Variable rule
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"

    return render_template('result.html', results=res)

@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"

    exp = {'score':score, 'result':res}

    return render_template('result1.html', results=exp)

## if condition

@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html', results=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', results=score)

# @app.route('/submit', methods=['GET','POST'])
# def submit():
#     total_score = 0
#     if request.method == 'POST':
#         science = float(request.form['science'])
#         maths = float(request.form['maths'])
#         c = float(request.form['c'])
#         data_science = float(request.form['data_science'])
#         total_score = (science + maths + c + data_science) / 4
#     else:
#         return render_template('getresult.html')

#     return redirect(url_for('successres', score = total_score))

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score))
    





if __name__ == '__main__':
    app.run(debug=True)