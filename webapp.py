from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/response")
def render_response():
    length = Float(request.args['length'])
    reply = "your new length is" + length + "."
    return render_template('response.html', response = reply)
@app.route("/metersToMiles")
def render_page1():
    length = Float(request.args['length']* .00062137)
    reply = "your new length is" + length + "."
    return render_template('metersToMiles.html', response = reply)

@app.route("/milesToKilos")
def render_page2():
    length = Float(request.args['length']* 1.60934)
    reply = "your new length is" + length + "."
    return render_template('milesToKilos.html', response = reply)
@app.route("/kilosToMiles")
def render_page3():
    length = Float(request.args['length']*  0.621371)
    reply = "your new length is" + length + "."
    return render_template('kilosToMiles.html', response = reply)
if __name__=="__main__":
    app.run(debug=False, port=54321)
