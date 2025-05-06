from Hajime import * 
from scripts.python.counter import * 

app = Hajime()
@app.route("/")
def home(environ):
    return "<h1>Hello!</h1>"

port_1,port_2 = 6000, 6001
app.launch(
    port_1,
    port_2
)