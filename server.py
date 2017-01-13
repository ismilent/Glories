#!/usr/bin/env python
#-*- coding: utf-8 -*-


from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request

import celery
from tasks import nmap_dispath
from tasks import celery_app


flask_app = Flask(__name__)


@flask_app.route('/api/v1.0/task/info/<string:task_id>', methods=['GET'])
def get_portmap_tasks(task_id):

    rs = celery_app.AsyncResult(task_id)
    task = {
        'task_id': task_id,
        'status': rs.status
    }
    return jsonify({'tasks': task})

@flask_app.route('/api/v1.0/task/portmap', methods=['POST'])
def create_portmap_tasks():
    if not request.json or not 'target' in request.json:
        abort(400)
    ip = request.json.get('target')
    task_id = celery.uuid()
    celery_task = nmap_dispath.apply_async((ip,), task_id=task_id)
    task = {
        'task_id': celery_task.task_id,
        'target': ip,
        'status': celery_task.status
    }

    return jsonify({'task': task})

@flask_app.route('/api/v1.0/stop/portmap/<string:task_id>', methods=['GET'])
def exit_portmap(task_id):
    pass

@flask_app.errorhandler(400)
def handler_400(error):
    return make_response(jsonify({'error': 'Code 400'}))

@flask_app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}))

if __name__ == '__main__':
    flask_app.run(debug=True)