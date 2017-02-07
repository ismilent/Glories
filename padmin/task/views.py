import re
from flask import Blueprint
from flask_login import login_required
from flask import render_template, request, jsonify, abort
from celery import uuid
from tasks import nmap_dispath

task_print = Blueprint('task', __name__, url_prefix='/task')

@login_required
@task_print.route('/add', methods=['POST'])
def add_task():
    if not request.json or not 'target' in request.json:
        abort(400)
    if not re.match(r'', request.json.get('target')):
        abort(400)
    ip = request.json.get('target')
    task_id = uuid()
    celery_task = nmap_dispath.apply_async((ip,), task_id=task_id)
    task = {
        'task_id': celery_task.task_id,
        'target': ip,
        'status': celery_task.status
    }

    return jsonify({'task': task})

@task_print.route('/task-add.html')
def test():
    return render_template('/task/task-add.html')