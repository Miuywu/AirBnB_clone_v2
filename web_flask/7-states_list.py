#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """Display list of states"""
    state_list = storage.all(State).values()
    return render_template('7-states_list.html', states=state_list)


@app.teardown_appcontext
def session_off(self):
    """Shuts down app"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
