from flask import Blueprint
from flask import render_template


tasks_print = Blueprint('tasks', __name__, url_prefix='/tasks')


@tasks_print.route('/')
def index():
    return render_template('/home/dashboard.html')

@tasks_print.route('/add')
def add_task():
    return '404'