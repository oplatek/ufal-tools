from flask import Flask, url_for, render_template
import os


class DevelopmentProxyFix:
    """Source https://stackoverflow.com/a/63429418/2171485"""
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        environ["SCRIPT_NAME"] = os.environ.get("SCRIPT_NAME")
        print(environ["SCRIPT_NAME"], flush=True)
        # environ["wsgi.url_scheme"] = "https"
        return self.app(environ, start_response)

def create_app():
    app = Flask(__name__)
    if app.config.get("ENV") == "development":
        print(app.config["ENV"])
        app.wsgi_app = DevelopmentProxyFix(app.wsgi_app)
    return app


app = create_app()

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", message="Hello from INDEX flask view")


@app.route("/second")
def second():
    return render_template("index.html", message="Hello from  SECOND flask view")
