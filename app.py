from flask import Flask,render_template,request,session,redirect

app = Flask(__name__)
app.secret_key = 'your-secret-key' 

def passing_calculation(passes_att,passes_comp):
    
    passing = (passes_comp/passes_att) * 100

    passing_accuracy = "{:.2f}".format(passing) 

    return passing_accuracy


def shots_calculation(shots_att,shots_on,goals):

    shot1 = (shots_on / shots_att) * 100

    shot2 = (goals / shot1) * 100

    shot_accurracy = "{:.2f}".format(shot1)

    shot_conversion = "{:.2f}".format(shot2)

    return shot_accurracy,shot_conversion

def goal_rate(goals,minutes):

    goals_scored = (goals/minutes) * 100

    goals_scored_rate = "{:.2f}".format(goals_scored)

    return goals_scored_rate

def assist_rate(assist,minutes):

    assists1 = (assist/minutes) * 100

    assists_rate = "{:.2f}".format(assists1)
    
    return assists_rate

def goal_contributions(goals,assists,minutes):

    goal_con = ((goals + assists) / minutes) * 100

    goal_contribution_rate = "{:.2f}".format(goal_con)

    return goal_contribution_rate


@app.route('/',methods =['GET','POST'])
def index():

    error = None
 
    if request.method == "POST":

        try:
            time_played = request.form["timePlayed"]
            distance_ran = request.form["distanceRan"]
            unit = request.form["unit"]
            passes_complete = request.form["passesComplete"]
            passes_attempted = request.form["passesAttempted"]
            shots_attempted = request.form["shotsAttempted"]
            shots_on_target = request.form["shotsOnTarget"]
            player_goals = request.form["goals"]
            player_assists = request.form["assists"]

            if not time_played or not time_played.isdigit():

                error= "Please enter only Numeric Value"
                raise ValueError(error)
            
            minutes = int(time_played)

            if minutes < 0:

                error= "Cant be less than 0 Minutes"
                raise ValueError(error)

            if not distance_ran:

                error= "Please enter only numeric value"
                raise ValueError(error)

            try:

                distance = float(distance_ran)

            except ValueError:

                error = "Please enter a valid numeric value for Distance Ran"
                raise ValueError(error)

            if not unit:

                error="Please select unit"
                raise ValueError(error)
            
            if unit == "km":

                if distance > 17:
                    error = "You didnt run more than the 17k "

                #used for later
                distance_metres = distance * 1000

            elif unit == "m":

                if distance > 17000:

                    error = "You didnt run more than the 17000m "



            if not passes_attempted or not passes_attempted.isdigit():

                error = "Please enter only numeric value"
                raise ValueError(error)

            passes_att = int(passes_attempted)

            if passes_att < 0:

                error = "Passes attempted cant be less than 0"
                raise ValueError(error)

            if not passes_complete or not passes_complete.isdigit():

                error = "Please enter only numeric value"
                raise ValueError(error)

            passes_comp = int(passes_complete)

            if passes_comp < 0:

                error = "Passes complete cant be less than 0"
                raise ValueError(error)
            
            if not shots_attempted or not shots_attempted.isdigit():

                error = "Please enter only numeric value"
                raise ValueError(error)
            
            shots_att = int(shots_attempted)

            if shots_att < 0:

                error = "Shots Attempted cant be less than 0"
                raise ValueError(error)

            if not shots_on_target or not shots_on_target.isdigit():

                error = "Please enter only numeric value"
                raise ValueError(error)

            shots_on = int(shots_on_target)

            if shots_on < 0:

                error = "Shots on target cant be less than 0"
                raise ValueError(error)

            if not player_goals or not player_goals.isdigit():

                error = "Please enter only numeric value"
                raise ValueError(error)

            goals = int(player_goals)

            if goals < 0 :

                error = "Goals cant be less than 0"
                raise ValueError(error)

            if not player_assists or not player_assists.isdigit():

                error = "Please enter only numeric value"
                raise ValueError(error)

            assist = int(player_assists)

            if assist < 0:

                error = "Assist cant be less than 0"
                raise ValueError(error)

            session["player_entered_data"] = {

                "time_played":minutes,
                "distance_ran":distance,
                "unit":unit,
                "passes_attempted":passes_att,
                "passes_complete":passes_comp,
                "shots_attempted":shots_att,
                "shots_on_target":shots_on,
                "player_goals":goals,
                "player_assists":assist
            }

            passing_accuracy_calc = passing_calculation(passes_att,passes_comp)
            shot_accuracy_calc, shot_conversion_rate = shots_calculation(shots_att,shots_on,goals)
            goal_rate_calc = goal_rate(goals,minutes)
            assist_rate_calc = assist_rate(assist,minutes)
            goal_contributions_calc = goal_contributions(goals,assist,minutes)

            session["player_calculated_stats"] = {
                
                "passing_accuracy": float(passing_accuracy_calc),
                "shot_accuracy": float(shot_accuracy_calc),
                "shot_conversion": float(shot_conversion_rate),
                "goal_rate": float(goal_rate_calc),
                "assist_rate": float(assist_rate_calc),
                "goal_contributions": float(goal_contributions_calc),
            }

            return redirect('/result')

        except ValueError as ve:
            error = str(ve)
        except Exception as e:
            error = "An unexpected error occurred: " + str(e)

            

    return render_template('index.html', error=error)

@app.route('/result')
def result():

    player_inputted_data = session.get("player_entered_data")
    player_calculated_data = session.get("player_calculated_stats")


    if not player_inputted_data or not player_calculated_data:

        return redirect('/')

    return render_template('result.html',player_inputted_data=player_inputted_data,player_calculated_data=player_calculated_data)


if __name__ == "__main__":
    app.run(debug=True)