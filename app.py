from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import json
import os

app = Flask(__name__)

DATA_FILE = 'data.json'

# Load tasks from JSON
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

# Save tasks to JSON
def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

tasks = load_tasks()
edit_index = None  # Global flag to keep track of which task is being edited

@app.route('/')
def index():
    global edit_index
    return render_template('index.html', tasks=tasks, edit_index=edit_index)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    deadline = request.form['deadline']
    priority = request.form['priority']
    tasks.append({
        'task': task,
        'deadline': deadline,
        'priority': priority,
        'done': False
    })
    save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/complete/<int:index>')
def complete(index):
    if 0 <= index < len(tasks):
        tasks[index]['done'] = not tasks[index]['done']  # Toggle done status
        save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    global edit_index
    if request.method == 'POST':
        # Update the task
        tasks[index]['task'] = request.form['task']
        tasks[index]['deadline'] = request.form['deadline']
        tasks[index]['priority'] = request.form['priority']
        save_tasks(tasks)
        edit_index = None
        return redirect(url_for('index'))

    # Set the edit index to show form in HTML
    edit_index = index
    return redirect(url_for('index'))

@app.route('/cancel')
def cancel():
    global edit_index
    edit_index = None
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)




# from flask import Flask, render_template, request, redirect, url_for
# from datetime import datetime
# import json
# import os

# app = Flask(__name__)

# DATA_FILE = 'data.json'

# # Load tasks from JSON
# def load_tasks():
#     if os.path.exists(DATA_FILE):
#         with open(DATA_FILE, 'r') as f:
#             return json.load(f)
#     return []

# # Save tasks to JSON
# def save_tasks(tasks):
#     with open(DATA_FILE, 'w') as f:
#         json.dump(tasks, f, indent=4)

# tasks = load_tasks()

# @app.route('/')
# def index():
#     return render_template('index.html', tasks=tasks)

# @app.route('/add', methods=['POST'])
# def add():
#     task = request.form['task']
#     deadline = request.form['deadline']
#     priority = request.form['priority']
#     tasks.append({
#         'task': task,
#         'deadline': deadline,
#         'priority': priority,
#         'done': False
#     })
#     save_tasks(tasks)
#     return redirect(url_for('index'))

# @app.route('/complete/<int:index>')
# def complete(index):
#     if 0 <= index < len(tasks):
#         tasks[index]['done'] = True
#         save_tasks(tasks)
#     return redirect(url_for('index'))

# @app.route('/delete/<int:index>')
# def delete(index):
#     if 0 <= index < len(tasks):
#         tasks.pop(index)
#         save_tasks(tasks)
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template, request, redirect, url_for
# from datetime import datetime

# app = Flask(__name__)

# tasks = []

# @app.route('/')
# def index():
#     return render_template('index.html', tasks=tasks)

# @app.route('/add', methods=['POST'])
# def add():
#     task = request.form['task']
#     deadline = request.form['deadline']
#     priority = request.form['priority']
#     tasks.append({
#         'task': task,
#         'deadline': deadline,
#         'priority': priority,
#         'done': False
#     })
#     return redirect(url_for('index'))

# @app.route('/complete/<int:index>')
# def complete(index):
#     tasks[index]['done'] = True
#     return redirect(url_for('index'))

# @app.route('/delete/<int:index>')
# def delete(index):
#     tasks.pop(index)
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)
