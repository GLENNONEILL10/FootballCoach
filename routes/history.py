# routes/history.py
from flask import Blueprint, render_template, session, request, redirect, url_for, flash
import json
from models import Submission, db
from utils import login_required
from stats_feedback import (
    generate_passing_feedback,
    generate_tackling_feedback,
    generate_interception_feedback,
    generate_clearance_feedback,
    generate_block_feedback,
    generate_aerial_duel_feedback,
    generate_fouls_committed_feedback,
    generate_shooting_feedback,
    generate_goal_contribution_feedback,
    generate_key_passes_feedback,
    generate_dribbling_feedback,
    generate_crossing_feedback,
    generate_touches_in_opp_box_feedback,
    generate_offside_feedback,
    generate_fouls_drawn_feedback,
    generate_save_percentage_feedback,
    generate_goals_conceded_feedback,
    generate_save_to_goal_feedback,
    generate_errors_per_90_feedback,
    generate_clean_sheet_feedback,
    shots_calculation
)

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
            sub.inputted = json.loads(sub.inputted_data)


    combined_stats = {}
    combined_feedback = []

    if submissions:
        keys = submissions[0].calculated.keys()
        for key in keys:
            # collect all values we can turn into floats
            numeric_vals = []
            for sub in submissions:
                v = sub.calculated.get(key)
                try:
                    # e.g. v could be int, float, or a numeric string
                    numeric_vals.append(float(v))
                except (TypeError, ValueError):
                    # skip booleans, strings like "Yes"/"No", etc.
                    continue

            # compute the average if we got any numbers
            if numeric_vals:
                combined_stats[key] = sum(numeric_vals) / len(numeric_vals)
            else:
                # or set to None, or pass through the first entry (e.g. clean_sheet)
                combined_stats[key] = None

    if selected == 'defender':
            
            combined_feedback.append(generate_passing_feedback(combined_stats['passing_accuracy']))

            raw = [

                generate_tackling_feedback(combined_stats['tackling_accuracy_rate']),
                generate_interception_feedback(combined_stats['interception_rate']),
                generate_clearance_feedback(combined_stats['clearance_rate']),
                generate_block_feedback(combined_stats['block_rate']),
                generate_aerial_duel_feedback(combined_stats['aerial_duel_success_rate']),
                generate_fouls_committed_feedback(combined_stats['fouls_committed_rate'])
            ]
            
            for msg in raw:
                 
                if isinstance(msg,list):
                      
                    combined_feedback.extend(msg)

                elif msg:
                     
                     combined_feedback.extend(msg)

    elif selected == "striker":
            
            sa = combined_stats["shot_accuracy"]
            sc = combined_stats["shot_conversion"]
            gr = combined_stats["goal_rate"]
            ar = combined_stats["assist_rate"]
            gc = combined_stats["goal_contributions"]

            shots_att = sum(s.inputted.get('shots_att', 0) for s in submissions)

            combined_feedback.append(generate_passing_feedback(combined_stats['passing_accuracy']))

            raw = [
                  
                generate_shooting_feedback(sa,sc,shots_att),
                generate_goal_contribution_feedback(gr,ar,gc),
                generate_key_passes_feedback(combined_stats['key_passes_rate']),
                generate_dribbling_feedback(combined_stats['dribbles_success_rate']),
                generate_touches_in_opp_box_feedback(combined_stats['touches_in_box_rate']),
                generate_offside_feedback(combined_stats['offsides_rate']),
                generate_fouls_drawn_feedback(combined_stats['fouls_drawn_rate'])
            ]

            for msg in raw:
                  
                if isinstance(msg,list):
                        
                    combined_feedback.extend(msg)

                elif msg:

                     combined_feedback.extend(msg)    
                
    
            

    elif selected == "winger":
            
            sa = combined_stats["shot_accuracy"]
            sc = combined_stats["shot_conversion"]
            gr = combined_stats["goal_rate"]
            ar = combined_stats["assist_rate"]
            gc = combined_stats["goal_contributions"]

            shots_att = sum(s.inputted.get('shots_att', 0) for s in submissions)

            combined_feedback.append(generate_passing_feedback(combined_stats['passing_accuracy']))

            raw = [
                 
                
                generate_shooting_feedback(sa,sc,shots_att),
                generate_goal_contribution_feedback(gr,ar,gc),
                generate_key_passes_feedback(combined_stats['key_passes_rate']),
                generate_dribbling_feedback(combined_stats['dribbles_success_rate']),
                generate_crossing_feedback(combined_stats['crossing_accuracy'])


            ]

            for msg in raw:
                 
                if isinstance(msg,list):
                      
                    combined_feedback.extend(msg)

                elif msg:
                     
                     combined_feedback.extend(msg)


    elif selected == "midfielder":
            
            
            gr = combined_stats["goal_rate"]
            ar = combined_stats["assist_rate"]
            gc = combined_stats["goal_contributions"]

            combined_feedback.append(generate_passing_feedback(combined_stats['passing_accuracy']))
            

            raw = [
                
                generate_goal_contribution_feedback(gr, ar, gc),
                generate_key_passes_feedback(combined_stats['key_passes_rate']),
                generate_dribbling_feedback(combined_stats['dribbles_success_rate']),
                generate_tackling_feedback(combined_stats['tackling_accuracy_rate']),
                generate_interception_feedback(combined_stats['interception_rate']),

            ]
         
            
            for msg in raw:
                 
                if isinstance(msg,list):
                      
                  combined_feedback.extend(msg)

                elif msg:
                     
                     combined_feedback.extend(msg)

    elif selected == "goalkeeper":
            
            combined_feedback.append(generate_passing_feedback(combined_stats['passing_accuracy']))
            
            raw = [
                 
                generate_save_percentage_feedback(combined_stats['save_percentage']),
                generate_goals_conceded_feedback(combined_stats['goals_conceded']),
                generate_save_to_goal_feedback(combined_stats['save_to_goal_ratio']),
                generate_errors_per_90_feedback(combined_stats['errors_per_90']),
                generate_clean_sheet_feedback(combined_stats['clean_sheet'])

            ]

            for msg in raw:
                 
                if isinstance(msg,list):
                      
                    combined_feedback.extend(msg)

                elif msg:
                     
                     combined_feedback.extend(msg)

    # 5) Always return this template (no path skips this)
    return render_template(
        'history.html',
        positions=positions,
        selected_position=selected,
        submissions=submissions,
        combined_stats=combined_stats,
        combined_feedback=combined_feedback

    )
