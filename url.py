## Building url dynamically
## Variable Rules and URL Building

from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/')
def Welcome():
    return'Hey Welcome to the Goa'

@app.route('/vegetables')
def Veggies():
    return 'I like to eat Vegetables raw and fresh. It is good for health'

@app.route('/success/<int:score>')
def success(score):
    #return "The Person has passed and the score is "+ str(score) # concatenating with string func
    return "<html><body><h1>The result is Passed</h1></body></html>"

@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the score is "+ str(score) # concatenating with string func

# Result Checker
@app.route('/results/<int:marks>')
def results(marks):
    results=""
    if marks<50:
        results='fail'
    else:
        results = 'success'
    #return results
    return redirect(url_for(results,score=marks))

if __name__=='__main__':
    app.run(debug=True)