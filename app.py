from flask import Flask
from flask import render_template
from flask import request
from article import summarize_article_at_url

import json, traceback

app = Flask("News-Summarizer")

@app.route("/")
def index():
    return render_template("index.html", log="")

@app.route("/processURL/")
def test():
    try:
        url = json.loads(request.args["url"])
        return { "status": True, "result": [ summarize_article_at_url(u) for u in url ] }
    except:
        return  { "status": False, "error": traceback.format_exc() }
