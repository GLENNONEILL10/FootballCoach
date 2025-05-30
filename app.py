from flask import Flask,render_template,request,session,redirect

app = Flask(__name__)
app.secret_key = 'your-secret-key' 

def passing_calculation(passes_att,passes_comp):
    
    passing = (passes_comp/passes_att) * 100

    passing_accuracy = "{:.2f}".format(passing) 

    return passing_accuracy


def shots_calculation(shots_att,shots_on,goals):

    shot1 = (shots_on / shots_att) * 100

    shot2 = (goals / shots_att) * 100

    shot_accurracy = "{:.2f}".format(shot1)

    shot_conversion = "{:.2f}".format(shot2)

    return shot_accurracy,shot_conversion

def goal_rate(goals,minutes):

    goals_scored = (goals/minutes) * minutes

    goals_scored_rate = "{:.2f}".format(goals_scored)

    return goals_scored_rate

def assist_rate(assist,minutes):

    assists1 = (assist/minutes) * minutes

    assists_rate = "{:.2f}".format(assists1)
    
    return assists_rate

def goal_contributions(goals,assists,minutes):

    goal_con = (goals + assists)

    goal_contribution_rate = "{:.2f}".format(goal_con)

    return goal_contribution_rate


def generate_passing_feedback(passing_accuracy):

    if passing_accuracy:
        
        if passing_accuracy > 85:

            feedback = "Your passing is terrific , Keep it up"

            return feedback
        
        elif passing_accuracy >=60 and passing_accuracy < 85:

            feedback = "Your passing is decent but you need to improve"

            return feedback
        
        else:

            feedback = "Your passing isnt good you should take some time to improve passing accuracy and timing"

            return feedback
        
def generate_shooting_feedback(shot_accuracy,shot_conversion,shots_att):

    feedback = []

    if shot_accuracy and shot_conversion:

        if shot_accuracy > 85:

            feedback.append("Your shooting on target well, you will score many goals")
    
        elif shot_accuracy >= 60 and shot_accuracy < 85:

            feedback.append("You shooting is decent, continue woring on it and you will improve")

        else:

            feedback.append("You shooting isnt good, you will need to work on this if you want to convert into goals")

    
        if shot_conversion > 40 and shots_att >= 4:

            feedback.append("You didnt do this, this is far above what even messi gets this")

        
        elif shot_conversion > 25 and shot_conversion < 40 :

            feedback.append("This is pro standard keep it up")
        
        elif shot_conversion > 10 and shot_conversion < 25:

            feedback.append("This is good shooting, keep improving and you will score many goals")
    
        else:

            feedback.append("You werent clinicle enough in this match, yo need to work on your shot conversion")

        return feedback
        

def generate_goal_contribution_feedback(goal_rate,assist_rate,goal_contributions):

    feedback = []

    if goal_rate and assist_rate and goal_contributions:

        if goal_rate >= 2:

            feedback.append("You scored very well today")

        elif goal_rate == 1:

            feedback.append("Nice you scored well done")

        else:

            feedback.append("Unlucky you didnt score this time")

        if assist_rate >=2:

            feedback.append("Well done your provided your teamates with lots of goals")

        elif assist_rate == 1:

            feedback.append("Nice Assist today")

        else:

            feedback.append("Unlucky you didnt provide assist")

        if goal_contributions > 6:

            feedback.append("Terrific performance today you were the best player on the pitch")
        
        elif goal_contributions < 6 and goal_contributions >= 3:

            feedback.append("Very good performance keep it up")

        elif goal_contributions < 3 and goal_contributions > 1:

            feedback.append("Nice performance keep working to ensure its consistant")

        else:

            feedback.append("Unlucky you didnt contribute to any goals")        
    else:

        return "Error you didnt fill out the form properly"

    return feedback

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

    feedback_list = []

    passing_feedback = generate_passing_feedback(player_calculated_data["passing_accuracy"])

    shooting_feedback = generate_shooting_feedback(

        player_calculated_data["shot_accuracy"],
        player_calculated_data["shot_conversion"],
        player_inputted_data["shots_attempted"]

    )
    goal_contribution_feedback = generate_goal_contribution_feedback(
        
        player_calculated_data["goal_rate"],
        player_calculated_data["assist_rate"],
        player_calculated_data["goal_contributions"]
    )

    for feedback in [passing_feedback, shooting_feedback, goal_contribution_feedback]:
        
        if isinstance(feedback, list):

            feedback_list.extend(feedback)

        elif feedback:
            feedback_list.append(feedback)
     

    if not player_inputted_data or not player_calculated_data:

        return redirect('/')

    return render_template('result.html',player_inputted_data=player_inputted_data,player_calculated_data=player_calculated_data
                                        ,feedback_list=feedback_list)


if __name__ == "__main__":
    app.run(debug=True)