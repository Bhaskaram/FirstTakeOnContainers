from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


@app.route('/application')
def get_application():
    return 'Application'

@app.route('/another_value')
def get_another_value():
    return 'Another value'


if __name__ == '__main__':
    app.run(host= "0.0.0.0",port=5000, debug =True)