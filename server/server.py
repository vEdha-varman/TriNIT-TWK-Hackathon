from flask import Flask, request
import requests
import pandas as pd

# create the Flask app
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/query-example')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')
    print(request.args)

    return f"<h1>The language value is: {language}</h1>"

# allow both GET and POST requests


@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '''
                  <h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Language: <input type="text" name="language"></label></div>
               <div><label>Framework: <input type="text" name="framework"></label></div>
               <input type="submit" value="Submit">
           </form>'''

# GET requests will be blocked


@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()

    language = None
    framework = None
    python_version = None
    example = None
    boolean_test = None

    if request_data:
        if 'language' in request_data:
            language = request_data['language']

        if 'framework' in request_data:
            framework = request_data['framework']

        if 'version_info' in request_data:
            if 'python' in request_data['version_info']:
                python_version = request_data['version_info']['python']

        if 'examples' in request_data:
            if (type(request_data['examples']) == list) and (len(request_data['examples']) > 0):
                example = request_data['examples'][0]

        if 'boolean_test' in request_data:
            boolean_test = request_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)


# GET requests will be blocked
@app.route('/json', methods=['POST'])
def json():
    request_data = request.get_json()
    if request_data == None:
        # print("req::",request_data)
        return "Hello World, TriNIT Hackathon'23"
    avg_v_effective = None
    avg_eff_acc = None
    avg_pwr_rtio = None

    if request_data:
        if 'avg_v_effective' in request_data:
            avg_v_effective = float(request_data['avg_v_effective'])

        if 'avg_eff_acc' in request_data:
            avg_eff_acc = float(request_data['avg_eff_acc'])

        if 'avg_pwr_rtio' in request_data:
            avg_pwr_rtio = float(request_data['avg_pwr_rtio'])

    lights = [0, 0, 0]
    # condns
    if avg_v_effective > 25:
        lights[0] = 1
    if avg_eff_acc > 1.4705:
        lights[1] = 1
    if avg_pwr_rtio > 30:
        lights[2] = 1

    # resp = '''
    #        The acc value is: {}
    #        The framework value is: {}'''.format(acc, brake)
    resp = {"l1":lights[0],"l2":lights[1],"l3":lights[2]}
    # resp.to_
    # print(resp)

    return resp


@app.route('/<name>')
def my_view_func(name):
    return name


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
