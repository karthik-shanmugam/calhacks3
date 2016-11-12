from flask import Flask, request, send_from_directory
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    print "ayyy"
    return send_from_directory('face-demo', 'index.html')

@app.route('/<string:path>')
def static_proxy(path):
    print path
    return send_from_directory('face-demo', path)


if __name__ == "__main__":
    app.run(debug=True)