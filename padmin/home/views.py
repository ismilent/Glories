from flask import Blueprint, url_for, render_template
from flask_login import login_required


home_print = Blueprint('home', __name__, url_prefix='/home')

@home_print.route('/')
@home_print.route('/index')
@login_required
def index():
    tasks = []
    for x in range(1,5,1):
        tasks.append({'task_id': x, 'task': 'task' + str(x), 'worker': 'sada', 'status': 'up'})
    return render_template('home/index.html', tasks=tasks)