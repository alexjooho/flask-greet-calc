from flask import Flask, request

app = Flask(__name__)

#/welcome returns "welcome"
# /welcome/home returns "welcome home"
# /welcome/back returns "welcome back"


@app.get('/welcome')
def say_welcome():
    """ Return "welcome" """

    html = "<html><body><h1>welcome</h1></body></html>"
    return html

@app.get('/welcome/home')
def say_welcome_home():
    """ Return welcome home """

    html = "<html><body><h1>welcome home</h1></body></html>"
    return html

@app.get('/welcome/back')
def say_welcome_back():
    """ Return welcome back """

    html = "<html><body><h1>welcome back</h1></body></html>"
    return html