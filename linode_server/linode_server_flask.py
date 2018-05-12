# coding: utf-8
"""
python version: 3.6.5(using python3 to avoid encoding problmes)

an simple http server based on SimpleHTTPServer(the file display system)
using WSGIServer in gevent to enable unblocking download
"""
import os
import urllib
import cgi
from flask import Flask, g, send_from_directory
from flask import render_template
from gevent.wsgi import WSGIServer


app = Flask(__name__, template_folder='.')
work_path = input("please enter the absolute path you want the http server works: ")
os.chdir(work_path)
BASE_DIR = os.getcwd()
secret_key = os.getenv("_SECRET_KEY")
app.config.update(DEBUG=True, SECRET_KEY=secret_key)


@app.before_request
def set_g():
    """
    g.path is to store relative location under BASE_DIR
    """
    g.path = ""


@app.route('/')
@app.route("/<path:path>/")  # <path:params> this would take care of '/' in path
def file_list(path=None):
    if not path:
        path = ""
    full_path = os.path.join(BASE_DIR, path)
    g.path = os.path.join(g.path, path)
    if not os.path.isdir(full_path):
        download_path = os.path.split(full_path)
        return send_from_directory(download_path[0], download_path[1], as_attachment=True)
    dir_info = get_directory(full_path)
    return render_template("file.html", file_names=dir_info[0], error=dir_info[1])


def get_directory(full_path):
    try:
        _file_list = os.listdir(full_path)
    except os.error:
        return (None, "Permission 123")
    if not _file_list:
        return (("", ""), "No file here")
    _file_list.sort(key=lambda file: file.lower())
    file_list = []
    for name in _file_list:
        display = name + '/' if os.path.isdir(os.path.join(g.path, name)) else name
        file_list.append((urllib.parse.quote(name), cgi.escape(display)))
    return (file_list, None)


if __name__ == '__main__':
    server = WSGIServer(('', 9999), app)
    server.serve_forever()
