from flask import Flask, render_template, session, request
import random

app = Flask(__name__)
app.secret_key = "something very random and secure obviously"

data = {
    "materials": [
        "School-issued laptop and charger", 
        "Pencil",
        "Binder with lined paper OR spiral notebook and pocket folder"
    ],
    "avail": [
        "Period 2A",
        "Period 4",
        "Period 8",
        "Period 9"
    ],
    "units": {
        "Unit 1": {
            "title": "Building Blocks of Code",
            "topics": [
                "Using VS Code and Python",
                "Variables",
                "Data Types"
            ],
        },
        "Unit 2": {
            "title": "Conditionals",
            "topics": [
                "Boolean Expressions",
                "Boolean Operators",
                "If/Elif/Else",
                "Nested and Compound Conditionals"
            ]
        },
        "Unit 3": {
            "title": "Creating Functions",
            "topics": [
                "User-Defined Functions",
                "Functions with Parameters",
                "Function Documentation",
                "Functions with Optional Parameters"
            ]
        },
        "Unit 4": {
            "title": "Loops",
            "topics": [
                "'While' Loops",
                "'For' Loops",
                "Applications of Loops",
                "Input Validation and Error Handling",
                "Writing Code for Future Use"
            ]
        },
        "Unit 5": {
            "title": "Data Structures",
            "topics": [
                "Lists",
                "Tuples and Multiple Assignment",
                "Searching",
                "Sorting",
                "2D Lists",
                "Dictionaries"
            ]
        },
    },
    "roster": [("Sawyer", "Tom"), ("Finn", "Huckleberry")],
}


@app.route('/')
def index():
    return render_template("courseoutline.html", data = data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/signatures', methods = ['GET', 'POST'])
def signatures():
    session.setdefault('signed', False)
    
    if request.method == "POST":
        first, last = request.form['first name'], request.form['last name']
        student = (last, first)
        if student not in data['roster']:
            data['roster'].append(student)
        session['signed'] = True
    return render_template("signatures.html", signed = session['signed'])
        

@app.route('/roster', methods = ['GET', 'POST'])
def roster():
    session.setdefault('authorized', False)
    if request.method == 'POST':
        if request.form["username"] == "herrkm" and request.form["password"] == "SecretPassword":
            session["authorized"] = True
    return render_template("roster.html", names = data["roster"], authorized = session["authorized"])


# keep this at the end!
app.run(host = '0.0.0.0', port = 8080, debug = True)