from Hajime import *

app = Hajime()
@app.route("/")
def home(environ):
  return "<h1>Hello</h1>"

app.launch(
  8800,
  8801
)
