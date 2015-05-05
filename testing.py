import os
from glob import glob
import shutil
def generate_decorator(route,methods=['GET','POST']):
    if "GET" in methods and "POST" in methods:
        router = "@app.route("+"'"+route+"',methods=['GET','POST'])"
    elif "GET" in methods:
        router = "@app.route("+"'"+route+"',methods=['GET'])"
    elif "POST" in methods:
        router = "@app.route("+"'"+route+"',methods=['GET'])"
    return router+"\n"

def generate_body(route):
    func_def = "def "+route+"():"
    return func_def+"\n"

def generate_html_response(html_page):
    return "\treturn render_template('"+html_page+"')"

def generate_head():
    return """from flask import Flask, render_template
app = Flask(__name__)
    
""".replace("\t","")

def generate_run():
    return """
if __name__ == '__main__':
    app.run(debug=True)
    """

def replicate_files():
    pass

if __name__ == '__main__':
    
    flask_file = ''
    if not os.path.exists("templates"):
        os.mkdir("templates")
    files = glob("*.html")
    for File in files:
        shutil.copyfile(File,"templates/"+File)
    flask_file += generate_head()
    flask_file += generate_decorator("/index")
    flask_file += generate_body("index")
    flask_file += generate_html_response("index.html")
    flask_file += generate_run()
    with open("routes.py","w") as f:
        f.write(flask_file)
