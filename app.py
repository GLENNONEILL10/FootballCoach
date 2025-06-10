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

def dribbles_success_rate_calc(dribbles_att,dribbles_comp):

    dribbles_success_rate = (dribbles_comp / dribbles_att ) * 100

    dribbles_success_rate = "{:.2f}".format(dribbles_success_rate)

    return dribbles_success_rate

def key_passes_percentage(key_p,passes_att):

    key_passes_per = (key_p / passes_att) * 100

    key_passes_per = "{:.2f}".format(key_passes_per)

    return key_passes_per

def touches_in_opp_box_per_90_calc(touches_in_box,minutes):

    touches_in_opp_box_per_90 = (touches_in_box / minutes) * 90

    touches_in_opp_box_per_90 = "{:.2f}".format(touches_in_opp_box_per_90)

    return touches_in_opp_box_per_90

def offsides_per_90_calc(offs,minute):

    offsides_per_90 = (offs / minute) * 90

    offsides_per_90 = "{:.2f}".format(offsides_per_90)

    return offsides_per_90

def fouls_drawn_per_90_calc(fouls_d,minute):

    fouls_drawn_per_90 = (fouls_d / minute) * 90

    fouls_drawn_per_90 =  "{:.2f}".format(fouls_drawn_per_90)

    return fouls_drawn_per_90

def crossing_accuracy_calc(crosses_att,crosses_comp):

    crossing_accuracy = (crosses_comp / crosses_att) * 100

    crossing_accuracy = "{:.2f}".format(crossing_accuracy)

    return crossing_accuracy


def tackling_accuracy_calc(tackles_att,tackles_comp):

    tackling_accuracy = (tackles_comp / tackles_att ) * 100

    tackling_accuracy = "{:.2f}".format(tackling_accuracy)

    return tackling_accuracy

def interception_rate_calc(intercept,minute):

    interception_rate = (intercept / minute) * 90

    interception_rate = "{:.2f}".format(interception_rate)

    return interception_rate
    

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


def generate_function_feedback():

    postion_based_feedback = []

    

@app.route('/',methods =['GET','POST'])
def index():

    error = None
 
    if request.method == "POST":

        try:

            form_type = request.form.get("formType") 

            if not form_type:

                return "Missing formType", 400

            session["position"] = form_type
        
            if form_type == "striker":

                time_played = request.form["timePlayed"]
                distance_ran = request.form["distanceRan"]
                unit = request.form["unit"]
                passes_complete = request.form["passesComplete"]
                passes_attempted = request.form["passesAttempted"]
                shots_attempted = request.form["shotsAttempted"]
                shots_on_target = request.form["shotsOnTarget"]
                player_goals = request.form["goals"]
                player_assists = request.form["assists"]
                key_passes = request.form["keyPasses"]
                dribbles_attempted = request.form["dribblesAttempted"]
                dribbles_completed = request.form["dribblesCompleted"]
                touches_in_opp_box = request.form["touchesInOppBox"]
                offsides = request.form["offsides"]
                fouls_drawn = request.form["foulsDrawn"]

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
                
                if not key_passes or not key_passes.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                key_p = int(key_passes)

                if key_p < 0:

                    error="Key passes cant be less than 0"
                    raise ValueError(error)
                
                if not dribbles_attempted or not dribbles_attempted.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                dribbles_att = int(dribbles_attempted)

                if dribbles_att < 0:

                    error = "Dribbles Attempted cant be less than 0"
                    raise ValueError(error)
                
                if not dribbles_completed or not dribbles_completed.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                dribbles_comp = int(dribbles_completed)

                if dribbles_comp < 0 :

                    error="Dribbles Completed cant be less than 0"
                    raise ValueError(error)
                
                if not touches_in_opp_box or not touches_in_opp_box.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                touches_in_box = int(touches_in_opp_box)

                if touches_in_box < 0:

                    error = "Touches in opponent box cant be less than 0"
                    raise ValueError(error)
                
                if not offsides or not offsides.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                

                offs = int(offsides)

                if offs < 0:

                    error = "Offsides cant be less than 0"
                    raise ValueError(error)
                
                if not fouls_drawn or not fouls_drawn.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                fouls_d = int(fouls_drawn)

                if fouls_d < 0:

                    error = "Fouls drawn cant be less than 0"
                    raise ValueError(error)

                session["striker_data"] = {

                "time_played":minutes,
                "distance_ran":distance,
                "unit":unit,
                "passes_attempted":passes_att,
                "passes_complete":passes_comp,
                "shots_attempted":shots_att,
                "shots_on_target":shots_on,
                "player_goals":goals,
                "player_assists":assist,
                "key_passes":key_p,
                "dribbles_attempted":dribbles_att,
                "dribbles_completed":dribbles_comp,
                "touches_in_opp_box":touches_in_box,
                "offsides":offs,
                "fouls_drawn":fouls_d
                }

                passing_accuracy = passing_calculation(passes_att,passes_comp)
                shooting_accuracy,shot_conversion_rate = shots_calculation(shots_att,shots_on,goals)
                goal_rate_calc = goal_rate(goals,minutes)
                assist_rate_calc = assist_rate(assist,minutes)
                goal_contributions_calc = goal_contributions(goals,assist,minutes)
                dribbles_success_rate = dribbles_success_rate_calc(dribbles_att,dribbles_comp)
                key_passes_per = key_passes_percentage(key_p,passes_att)
                touches_in_opp_box_per_90 = touches_in_opp_box_per_90_calc(touches_in_box,minutes)
                offsides_per_90 = offsides_per_90_calc(offs,minutes)
                fouls_drawn_per_90 = fouls_drawn_per_90_calc(fouls_d,minutes)

                session["striker_calculated_stats"] ={

                    "passing_accuracy":float(passing_accuracy),
                    "shot_accuracy":float(shooting_accuracy),
                    "shot_conversion":float(shot_conversion_rate),
                    "goal_rate":float(goal_rate_calc),
                    "assist_rate":float(assist_rate_calc),
                    "goal_contributions":float(goal_contributions_calc),
                    "dribbles_success_rate":float(dribbles_success_rate),
                    "key_passes_rate":float(key_passes_per),
                    "touches_in_box_rate":float(touches_in_opp_box_per_90),
                    "offsides_rate":float(offsides_per_90),
                    "fouls_drawn_rate":float(fouls_drawn_per_90)

                }

            

            elif form_type == "winger":
                print("DEBUG FORM DATA:", request.form)

                 
                time_played = request.form["timePlayed"]
                distance_ran = request.form["distanceRan"]
                unit = request.form["unit"]
                passes_complete = request.form["passesComplete"]
                passes_attempted = request.form["passesAttempted"]
                shots_attempted = request.form["shotsAttempted"]
                shots_on_target = request.form["shotsOnTarget"]
                player_goals = request.form["goals"]
                player_assists = request.form["assists"]
                key_passes = request.form["keyPasses"]
                dribbles_attempted = request.form["dribblesAttempted"]
                dribbles_completed = request.form["dribblesCompleted"]
                crosses_attempted = request.form["crossesAttempted"]
                crosses_completed = request.form["crossesCompleted"]

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
                
                if not key_passes or not key_passes.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                key_p = int(key_passes)

                if key_p < 0:

                    error="Key passes cant be less than 0"
                    raise ValueError(error)
                
                if not dribbles_attempted or not dribbles_attempted.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                dribbles_att = int(dribbles_attempted)

                if dribbles_att < 0:

                    error = "Dribbles Attempted cant be less than 0"
                    raise ValueError(error)
                
                if not dribbles_completed or not dribbles_completed.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                dribbles_comp = int(dribbles_completed)

                if dribbles_comp < 0 :

                    error="Dribbles Completed cant be less than 0"
                    raise ValueError(error)
                
                if not crosses_attempted or not crosses_attempted.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
            
                crosses_att = int(crosses_attempted)

                if crosses_att < 0 :

                    error = "Crosses Attempted cant be less than 0"
                    raise ValueError(error)
                

                if not crosses_completed or not crosses_completed.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                crosses_comp = int(crosses_completed)

                if crosses_comp < 0:

                    error = "Crosses Completed cant be less than 0"
                    raise ValueError(error)
                
                session["winger_data"]={

                    "time_played":minutes,
                    "distance_ran":distance,
                    "unit":unit,
                    "passes_attempted":passes_att,
                    "passes_complete":passes_comp,
                    "shots_attempted":shots_att,
                    "shots_on_target":shots_on,
                    "player_goals":goals,
                    "player_assists":assist,
                    "key_passes":key_p,
                    "dribbles_attempted":dribbles_att,
                    "dribbles_completed":dribbles_comp,
                    "crosses_attempted":crosses_att,
                    "crosses_completed":crosses_comp

            	 }

                passing_accuracy = passing_calculation(passes_att,passes_comp)
                shooting_accuracy,shot_conversion_rate = shots_calculation(shots_att,shots_on,goals)
                goal_rate_calc = goal_rate(goals,minutes)
                assist_rate_calc = assist_rate(assist,minutes)
                goal_contributions_calc = goal_contributions(goals,assist,minutes)
                dribbles_success_rate = dribbles_success_rate_calc(dribbles_att,dribbles_comp)
                key_passes_per = key_passes_percentage(key_p,passes_att)
                crossing_accuracy = crossing_accuracy_calc(crosses_att,crosses_comp)
               
                
                session["winger_calculated_stats"]={

                    "passing_accuracy":float(passing_accuracy),
                    "shot_accuracy":float(shooting_accuracy),
                    "shot_conversion":float(shot_conversion_rate),
                    "goal_rate":float(goal_rate_calc),
                    "assist_rate":float(assist_rate_calc),
                    "goal_contributions":float(goal_contributions_calc),
                    "dribbles_success_rate":float(dribbles_success_rate),
                    "key_passes_rate":float(key_passes_per),
                    "crossing_accuracy":float(crossing_accuracy)

                }
                
            elif form_type == "midfielder":

                time_played = request.form["timePlayed"]
                distance_ran = request.form["distanceRan"]
                unit = request.form["unit"]
                passes_complete = request.form["passesComplete"]
                passes_attempted = request.form["passesAttempted"]
                player_goals = request.form["goals"]
                player_assists = request.form["assists"]
                key_passes = request.form["keyPasses"]
                dribbles_attempted = request.form["dribblesAttempted"]
                dribbles_completed = request.form["dribblesCompleted"]
                tackles_attempted = request.form["tacklesAttempted"]
                tackles_completed = request.form["tacklesCompleted"]
                interceptions = request.form["interceptions"]


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
                

                if not key_passes or not key_passes.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                key_p = int(key_passes)

                if key_p < 0:

                    error="Key passes cant be less than 0"
                    raise ValueError(error)
                
                if not dribbles_attempted or not dribbles_attempted.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                dribbles_att = int(dribbles_attempted)

                if dribbles_att < 0:

                    error = "Dribbles Attempted cant be less than 0"
                    raise ValueError(error)
                
                if not dribbles_completed or not dribbles_completed.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                dribbles_comp = int(dribbles_completed)

                if dribbles_comp < 0 :

                    error="Dribbles Completed cant be less than 0"
                    raise ValueError(error)
                
                if not tackles_attempted or not tackles_attempted.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                tackles_att = int(tackles_attempted)

                if tackles_att < 0 :

                    error = "Tackles attempted cant be less than 0"
                    raise ValueError(error)
                
                if not tackles_completed or not tackles_completed.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                tackles_comp = int(tackles_completed)


                if tackles_comp < 0:

                    error = "Tackles Completed cant be less than 0"
                    raise ValueError(error)
                
                if not interceptions or not interceptions.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                intercept = int(interceptions)

                if intercept < 0:

                    error = "Interceptions cant be less than 0"
                    raise ValueError(error)
                


                session["midfielder_data"]={
                    
                    "time_played":minutes,
                    "distance_ran":distance,
                    "unit":unit,
                    "passes_attempted":passes_att,
                    "passes_complete":passes_comp,
                    "player_goals":goals,
                    "player_assists":assist,
                    "key_passes":key_p,
                    "dribbles_attempted":dribbles_att,
                    "dribbles_completed":dribbles_comp,
                    "tackles_attempted":tackles_att,
                    "tackles_completed":tackles_comp,
                    "interceptions":intercept

                }

                passing_accuracy = passing_calculation(passes_att,passes_comp)
                goal_rate_calc = goal_rate(goals,minutes)
                assist_rate_calc = assist_rate(assist,minutes)
                goal_contributions_calc = goal_contributions(goals,assist,minutes)
                dribbles_success_rate = dribbles_success_rate_calc(dribbles_att,dribbles_comp)
                key_passes_per = key_passes_percentage(key_p,passes_att)
                tackling_accuracy_rate = tackling_accuracy_calc(tackles_att,tackles_comp)
                interception_rate = interception_rate_calc(intercept,minutes)


                session["midfielder_calculated_stats"]={

                    "passing_accuracy":float(passing_accuracy),
                    "goal_rate":float(goal_rate_calc),
                    "assist_rate":float(assist_rate_calc),
                    "goal_contributions":float(goal_contributions_calc),
                    "dribbles_success_rate":float(dribbles_success_rate),
                    "key_passes_rate":float(key_passes_per),
                    "tackling_accuracy_rate":float(tackling_accuracy_rate),
                    "interception_rate":float(interception_rate)

                }

            elif form_type == "defender":

                time_played = request.form["timePlayed"]
                distance_ran = request.form["distanceRan"]
                unit = request.form["unit"]
                passes_complete = request.form["passesComplete"]
                passes_attempted = request.form["passesAttempted"]
                player_goals = request.form["goals"]
                tackles_attempted = request.form["tacklesAttempted"]
                tackles_completed = request.form["tacklesCompleted"]
                interceptions = request.form["interceptions"]
                clearance = request.form["clearance"]
                blocks = request.form["blocks"]
                aerial_duels_attempted = request.form["aerialDuelsAttempted"]
                aerial_duels_completed = request.form["aerialDuelsCompleted"]
                fouls_committed = request.form["foulsCommitted"]
                


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
                
                if not player_goals or not player_goals.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)

                goals = int(player_goals)

                if goals < 0 :

                    error = "Goals cant be less than 0"
                    raise ValueError(error)

                if not tackles_attempted or not tackles_attempted.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                tackles_att = int(tackles_attempted)

                if tackles_att < 0 :

                    error = "Tackles attempted cant be less than 0"
                    raise ValueError(error)
                
                if not tackles_completed or not tackles_completed.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                tackles_comp = int(tackles_completed)


                if tackles_comp < 0:

                    error = "Tackles Completed cant be less than 0"
                    raise ValueError(error)
                
                if not interceptions or not interceptions.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                intercept = int(interceptions)

                if intercept < 0:

                    error = "Interceptions cant be less than 0"
                    raise ValueError(error)
                
                if not clearance or not clearance.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                clear = int(clearance)

                if clear < 0:

                    error = "Clearances cant be less than 0"
                    raise ValueError(error)
                
                if not blocks or not blocks.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                bloc = int(blocks)

                if bloc < 0:

                    error = "Blocks cant be less than 0"
                    raise ValueError(error)
                
                if not aerial_duels_attempted or not aerial_duels_attempted.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                aerial_duels_att = int(aerial_duels_attempted)

                if aerial_duels_att < 0:

                    error = "Aerial Duels cant be less than 0"
                    raise ValueError(error)
                
                if not aerial_duels_completed or not aerial_duels_completed.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                aerial_duels_comp = int(aerial_duels_completed)

                if aerial_duels_comp < 0:

                    error = "Aerials Duels Completed cant be less than 0"
                    raise ValueError(error)
                
                if not fouls_committed or not fouls_committed.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                fouls_c = int(fouls_committed)

                if fouls_c < 0:

                    error = "Fouls Committed cant be less than 0"
                    raise ValueError(error)
                
                session["defender_data"]={
                    
                    "time_played":minutes,
                    "distance_ran":distance,
                    "unit":unit,
                    "passes_attempted":passes_att,
                    "passes_complete":passes_comp,
                    "player_goals":goals,
                    "tackles_attempted":tackles_att,
                    "tackles_completed":tackles_comp,
                    "interceptions":intercept,
                    "clearance":clear,
                    "blocks":bloc,
                    "aerial_duels_attempted":aerial_duels_att,
                    "aerial_duels_completed":aerial_duels_comp,
                    "fouls_committed":fouls_c

                }
            
            elif form_type == "goalkeeper":

                time_played = request.form["timePlayed"]
                shots_faced = request.form["shotsFaced"]
                saves_made = request.form["savesMade"]
                goals_conceded = request.form["goalsConceded"]
                error_leading_to_shot = request.form["errorLeadingToShot"]
                error_leading_to_goal = request.form["errorLeadingToGoal"]
                passes_attempted = request.form["passesAttempted"]
                passes_complete = request.form["passesComplete"]
                

                if not time_played or not time_played.isdigit():

                    error= "Please enter only Numeric Value"
                    raise ValueError(error)
            
                minutes = int(time_played)

                if minutes < 0:

                    error= "Cant be less than 0 Minutes"
                    raise ValueError(error)
                
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
                
                if not shots_faced or not shots_faced.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                shots_f = int(shots_faced)

                if shots_f < 0:

                    error = "Shots faced cant be less than 0"
                    raise ValueError(error)
                
                if not saves_made or not saves_made.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                saves_m = int(saves_made)

                if saves_m < 0:

                    error = "Saves made cant be less than 0"
                    raise ValueError(error)
                
                if not goals_conceded or not goals_conceded.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                goals_c = int(goals_conceded)

                if goals_c < 0:

                    error = "Goals Conceded cant be less than 0"
                    raise ValueError(error)
                
                if not error_leading_to_shot or not error_leading_to_shot.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                error_leading_shot = int(error_leading_to_shot)

                if error_leading_shot < 0:

                    error = "Errors leading to shots cant be less than 0"
                    raise ValueError(error)
                
                if not error_leading_to_goal or not error_leading_to_goal.isdigit():

                    error = "Please enter only numeric value"
                    raise ValueError(error)
                
                error_leading_goal = int(error_leading_to_goal)

                if error_leading_goal < 0:

                    error = "Error leading to goal cant be less than 0"
                    raise ValueError(error)
                
                session["goalkeeper_data"]={

                    "time_played":minutes,
                    "passes_attempted":passes_att,
                    "passes_complete":passes_comp,
                    "shots_faced":shots_f,
                    "saves_made":saves_m,
                    "goals_conceded":goals_c,
                    "error_leading_to_shot":error_leading_shot,
                    "error_leading_to_goal":error_leading_goal

                }
                
            else:

                error = "Error"

                raise ValueError(error)

        
            return redirect('/result')

        except ValueError as ve:
            error = str(ve)
        except Exception as e:
            error = "An unexpected error occurred: " + str(e)

            

    return render_template('index.html', error=error)

@app.route('/result')
def result():

    form_type = session.get("position")

    if form_type == "striker":

        player_inputted_data = session.get("striker_data")
        striker_calculated_data = session.get("striker_calculated_stats")

        session["player_calculated_data"] = striker_calculated_data
        player_calculated_data = session.get("player_calculated_data")

        session["player_position"] = "striker"
        position = session.get("player_position")


        
    elif form_type == "winger":

        player_inputted_data = session.get("winger_data")
        winger_calculated_data = session.get("winger_calculated_stats")

        session["player_calculated_data"] = winger_calculated_data
        player_calculated_data = session.get("player_calculated_data")

        session["player_position"] = "winger"
        position = session.get("player_position")

    elif form_type == "midfielder":

        player_inputted_data = session.get("midfielder_data")
        midfielder_calculated_data = session.get("midfielder_calculated_stats")

        session["player_calculated_data"] = midfielder_calculated_data
        player_calculated_data = session.get("player_calculated_data")

        session["player_position"] = "midfielder"
        position = session.get("player_position")

    elif form_type == "defender":

        player_inputted_data = session.get("defender_data")

    elif form_type == "goalkeeper":

        player_inputted_data = session.get("goalkeeper_data")

    else:
        return redirect("/")

    feedback_list = []

    '''
    for feedback in [passing_feedback, shooting_feedback, goal_contribution_feedback]:

        if isinstance(feedback, list):

            feedback_list.extend(feedback)

        elif feedback:
            feedback_list.append(feedback)

    '''
     

    if not player_inputted_data or not player_calculated_data :

        return redirect('/')

    return render_template('result.html',player_inputted_data=player_inputted_data,player_calculated_data=player_calculated_data,position=position
                                        ,feedback_list=feedback_list)


if __name__ == "__main__":
    app.run(debug=True)