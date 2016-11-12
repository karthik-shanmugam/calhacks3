from imgurpython import ImgurClient

imgur_client = "0f8ebdce6b83981"
imgur_secret = "f5b5ca46e0ea44e94b5cc3f6e9ebe4dc4a8aa254"
client = ImgurClient(imgur_client, imgur_secret)
print(client.upload_from_path("karthik.png"))




from __future__ import print_function
from flask import Flask, request, send_from_directory
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    print("ayyy")
    return send_from_directory('face-demo', 'index.html')

@app.route('/<string:path>')
def static_proxy(path):
    print(path)
    return send_from_directory('face-demo', path)


if __name__ == "__main__":
    app.run(debug=True)