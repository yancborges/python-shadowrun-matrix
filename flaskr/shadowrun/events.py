from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db


sr_events = Blueprint('events', __name__, url_prefix='/shadowrun/events')


@sr_events.route('/trending')
def trending():

    db = get_db()
    events = list(db.events.find({}))

    return render_template('shadowrun/trending.html', events=events)
