from sys import argv
from glob import glob
import os
import shutil

def process_files(folder):
    flask_file = ''
    flask_file += generate_head()
    if not os.path.exists("templates"):
        os.mkdir("templates")
    files = glob(folder+"/*.html")
    for File in files:
        new_file = File.replace(folder,"").replace("/","")
        shutil.copy2(File,"templates/"+new_file)
        route = "a_"+remove_special(new_file.split(".")[0])
        flask_file += generate_decorator("/"+route)
        flask_file += generate_body(route)
        flask_file += generate_html_response(new_file)
    
    flask_file += generate_run()
    with open("routes.py","w") as f:
        f.write(flask_file)

def remove_special(file_path):
    return file_path.replace("/","").replace("[","").replace("]","").replace("&","").replace("%","").replace("@","").replace("$","").replace("=","").replace("+","")

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
    return "\treturn render_template('"+html_page+"')\n"

def generate_head():
    return """from flask import Flask, render_template
app = Flask(__name__)
    
""".replace("\t","")

def generate_run():
    return """
if __name__ == '__main__':
    app.run(debug=True)
    """
    
if __name__ == '__main__':
    folder = argv[1]
    process_files(folder)
