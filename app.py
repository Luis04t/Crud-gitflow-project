# app.py qa
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulación de base de datos
tasks = []
task_id_counter = 1

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
