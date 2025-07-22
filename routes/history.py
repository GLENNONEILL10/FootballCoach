# routes/history.py
from flask import Blueprint, render_template, session, request, redirect, url_for, flash
import json
from models import Submission, db
from utils import login_required

history = Blueprint('history', __name__)

@history.route("/history")
@login_required
def view_history():
    # 1) Ensure we have a user
    user_id = session.get('user_id')
    if not user_id:
        # Should be caught by @login_required, but double‑safe:
        flash("Please log in to view history", "warning")
        return redirect(url_for('auth.login'))

    # 2) Find all distinct positions this user has submitted
    rows = (
        db.session
          .query(Submission.position)
          .filter_by(user_id=user_id)
          .distinct()
          .all()
    )
    positions = [r[0] for r in rows]  # e.g. ['defender','goalkeeper']

    # 3) Pick which position we’re showing
    selected = request.args.get('position')
    if not selected and positions:
        selected = positions[0]

    # 4) Load submissions for that position
    submissions = []
    if selected:
        submissions = (
            Submission.query
                      .filter_by(user_id=user_id, position=selected)
                      .order_by(Submission.timeStamp.desc())   # ← desc(), not dec()
                      .all()
        )
        # Deserialize for the template
        for sub in submissions:
            sub.calculated = json.loads(sub.calculated_data)

    # 5) Always return this template (no path skips this)
    return render_template(
        'history.html',
        positions=positions,
        selected_position=selected,
        submissions=submissions
    )
