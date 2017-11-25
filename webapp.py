from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/response")
def render_response():
    length = request.args['length']
    oneOf = request.args['checker']
     if oneOf == "m2k":
        newLength = float(length) * 1.60934 	
     if oneOf == "k2m":
        newLength = float(length) *  0.621371 	
     if oneOf == "m2m":
        newLength = float(length) * .00062137 
    reply = "your new length is " + newLength + "."
    return render_template('response.html', response = reply)
@app.route("/metersToMiles")
def render_page1():
    return render_template('metersToMiles.html')
@app.route("/milesToKilos")
def render_page2():
    return render_template('milesToKilos.html')
@app.route("/kilosToMiles")
def render_page3():
    return render_template('kilosToMiles.html')
if __name__=="__main__":
    app.run(debug=False, port=54321)
