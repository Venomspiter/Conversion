from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/response")
def render_response():
    length = float(request.args['length','apage'])
   if apage == "milesToKilos"{
       reply = "your new length is" + length * 1.60934 + "."
   }
   if apage == "kilosToMiles"{
       reply = "your new length is" + length * 0.621371 + "."
   }
    if apage == "metersToMiles"{
       reply = "your new length is" + length * .0006213709999975145 + "."
   }
    return render_template('templates/response.html', response = reply)
if __name__=="__main__":
    app.run(debug=False, port=54321)
@app.route("/metersToMiles")
def render_page1():
    return render_template('metersToMiles.html')

@app.route("/milesToKilos")
def render_page2():
    return render_template('milesToKilos.html')
@app.route("/kilosToMiles")
def render_page3():
    return render_template('kilosToMiles.html')
