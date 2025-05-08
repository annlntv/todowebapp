from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

tasks = ['Купить фрукты', 'Запрограммировать сайт', 'Поработать']

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    new_task = request.form.get('newTask')
    if new_task:
        tasks.append(new_task)
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete_tasks():
    index = request.form.get('taskCheckbox', type=int)
    if 1 <= index <= len(tasks):
        del tasks[index - 1]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)