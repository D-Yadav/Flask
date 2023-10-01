from flask import Flask
app=Flask(__name__) ###WSGI application

@app.route('/') ## Decorator (route home webpage '/' --> url in string fmt)
def welcome():
    return 'Welcome to the Flask, "HARDIK SUSWAGATAM" - Buddy'

@app.route('/members')
def GoodBye():
    return 'GoodBye sweetheart, See ya soon.'

@app.route('/andromeda')
def amazon():
    return'Anacondas are the largest reptilian in Earth, what about Mars?'

if __name__=='__main__':
    app.run(debug=True)