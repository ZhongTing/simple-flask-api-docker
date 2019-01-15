import os

from flask import Flask


def get_path(path):
    abs_path = os.path.join(os.path.dirname(__file__), path)
    return abs_path


def create_app():
    _app = Flask(__name__)
    from my_app.api.endpoint import hello
    _app.register_blueprint(hello.bp)
    _app.config['JSON_AS_ASCII'] = False
    return _app


app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", debug=True, port=port, threaded=True)
