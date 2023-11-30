import flask

from driver import HibotDriver
import yixinbei
from action import HandAction

app = flask.Flask(__name__)

hibot: HibotDriver = None


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/api/v1/action", methods=["get"])
def action():
    if not flask.request.args:
        flask.abort(400)
    action = flask.request.args["action"]
    print(action)
    if action not in dir(HandAction):
        flask.abort(400, f"action {action} not found")

    a = getattr(HandAction, action)
    if not callable(a):
        print(type(a))
        flask.abort(400, f"action {action} not callable")

    hibot.do_action(a)
    return flask.jsonify({"action": action})


@app.route("/api/v1/yixinbei", methods=["get"])
def look():
    if not flask.request.args:
        flask.abort(400)
    func = flask.request.args["func"]
    print(func)
    func_map = {
        "look_random_start": yixinbei.look_random_start,
        "look_random_stop": yixinbei.look_random_stop,
        "action1": yixinbei.action1,

        "dance_start": yixinbei.dance_start,
        "dance_stop": yixinbei.dance_stop,
    }
    if func not in func_map:
        flask.abort(400)

    func_map[func](hibot)

    return flask.jsonify({"yixinbei": func})


def init(hibot_driver: HibotDriver):
    global hibot
    hibot = hibot_driver
    app.run(host="0.0.0.0", port=5000, debug=True)
