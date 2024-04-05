from flask import Flask, send_from_directory
from flask_cors import CORS
import os
import os.path

app = Flask(__name__)
CORS(app)

def root_dir(): 
    return os.path.abspath(os.path.dirname(__file__))

@app.route("/<path:model>/<path:filename>")
def launch_server(model, filename):
    try:
        src = os.path.join(root_dir(), 'models', model, 'Build')
        print(f'16: src >>>\n{src}')
        return send_from_directory(src, filename)
    except Exception as exc:
        return str(exc)

if __name__ == "__main__":
    app.run(debug=True)