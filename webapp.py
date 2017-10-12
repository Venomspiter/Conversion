from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/response")
def render_response():
    length = request.args['length']
    #the request object stores data about the request sent to the server
    # args is a MultiDict (like a dictionary, but can store multiple values for the same key)
    # the information in args is visible in the url for the page  being requested (i.e. ... /response?color=blue)
    return render_template('response.html', response = reply)
if __name__=="__main__":
    app.run(debug=False, port=54321)
@app.route("/me2mi")
def render_page1():
    return render_template('meterToMiles.html')

@app.route("/mi2k")
def render_page2():
    return render_template('mileToKilos.html')
@app.route("/k2mi")
def render_page3():
    return render_template('kilosToMiles.html')
