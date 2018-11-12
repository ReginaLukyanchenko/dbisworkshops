from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello from Flask<h1>'


teacher_dictionary = {
    "id_code": "3595602420",
    "degree": "ассистент"
}

check_in_dictionary = {
    "student_card": "кв10742572",
    "lesson_id": "45",
    "check_in_date": "22.10.2018"
}

available_dictionary = dict.fromkeys(['teacher', 'check_in'], "dict_name")


@app.route('/api/<action>', methods=['GET'])
def apiGet(action):
    if action == "teacher":
        return render_template("teacher.html", teacher=teacher_dictionary)
    elif action == "check_in":
        return render_template("check_in.html", check_in=check_in_dictionary)
    elif action == "all":
        return render_template("all.html", check_in=check_in_dictionary, teacher=teacher_dictionary)
    else:
        return render_template("404.html", action_value=action, available=available_dictionary)


@app.route('/api', methods=['POST'])
def apiPost():
    if request.form["action"] == "teacher_update":
        teacher_dictionary["id_code"] = request.form["id_code"]
        teacher_dictionary["degree"] = request.form["degree"]

        return redirect(url_for('apiGet', action="all"))

    elif request.form["action"] == "check_in_update":
        check_in_dictionary["student_card"] = request.form["student_card"]
        check_in_dictionary["lesson_id"] = request.form["lesson_id"]
        check_in_dictionary["check_in_date"] = request.form["check_in_date"]

        return redirect(url_for('apiGet', action="all"))


if __name__ == '__main__':
    app.run(debug=True, port=8085)
