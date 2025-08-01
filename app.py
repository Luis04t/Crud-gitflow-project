# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
task_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    global task_id_counter
    description = request.form.get('description')
    if description:
        tasks.append({'id': task_id_counter, 'description': description, 'done': False})
        task_id_counter += 1
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
