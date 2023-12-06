import flask
import threading
from flask import make_response

from driver import HibotDriver
import yixinbei
from action import HandAction

app = flask.Flask(__name__)

hibot: HibotDriver = None

api_mutex = threading.Lock()


@app.route("/api/v1/")
def test():
    return flask.render_template("test.html")


@app.route("/api/v1/action", methods=["get"])
def action():
    if not flask.request.args:
        flask.abort(400)
    if api_mutex.locked():
        response = flask.jsonify({"error": "busy"})
        response.status_code = 400
        flask.abort(response)
    api_mutex.acquire()
    try:
        action = flask.request.args["action"]
        print(action)
        if action not in dir(HandAction):
            response = flask.jsonify({"error": f"action {action} not found"})
            response.status_code = 400
            flask.abort(response)

        a = getattr(HandAction, action)
        if not callable(a):
            response = flask.jsonify({"error": f"action {action} not callable"})
            response.status_code = 400
            flask.abort(response)

        hibot.do_action(a)
    finally:
        api_mutex.release()
    return flask.jsonify({"action": action})


@app.route("/api/v1/yixinbei", methods=["get"])
def look():
    if not flask.request.args:
        flask.abort(400)
    if api_mutex.locked():
        response = flask.jsonify({"error": "busy"})
        response.status_code = 400
        flask.abort(response)
    api_mutex.acquire()
    try:
        func = flask.request.args["func"]
        print(func)
        func_map = {
            "look_random_start": yixinbei.look_random_start,
            "look_random_stop": yixinbei.look_random_stop,
            "action1": yixinbei.action1,
            "dance_start": yixinbei.dance_start,
            "dance_stop": yixinbei.dance_stop,
            "wave_start": yixinbei.wave_start,
            "wave_stop": yixinbei.wave_stop,
        }
        if func not in func_map:
            response = flask.jsonify({"error": f"func {func} not found"})
            response.status_code = 400
            flask.abort(response)

        func_map[func](hibot)
    finally:
        api_mutex.release()

    return flask.jsonify({"yixinbei": func})


def init(hibot_driver: HibotDriver):
    global hibot
    hibot = hibot_driver
    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)
