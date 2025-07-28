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


def clearances_rate_calc(clear,minutes):

    clearances_rate = (clear / minutes) * 90

    clearances_rate = "{:.2f}".format(clearances_rate)

    return clearances_rate


def block_rate_calc(bloc,minutes):

    block_rate = (bloc / minutes) * 90

    block_rate = "{:.2f}".format(block_rate)

    return block_rate

def aerial_duel_success_rate_calc(aerial_duels_att,aerial_duels_comp):

    aerial_duel_success_rate = (aerial_duels_comp / aerial_duels_att) * 100

    aerial_duel_success_rate = "{:.2f}".format(aerial_duel_success_rate)

    return aerial_duel_success_rate

def fouls_committed_rate_calc(fouls_c,minutes):

    fouls_committed_rate = (fouls_c / minutes) * 90

    fouls_committed_rate = "{:.2f}".format(fouls_committed_rate)

    return fouls_committed_rate

def save_percentage_calc(saves_m,shots_f):

    save_percentage = (saves_m / shots_f) * 100

    save_percentage = "{:.2f}".format(save_percentage)

    return save_percentage

def goals_conceded_rate(goals_c , minutes):

    if goals_c == 0:

    
        return 0

    else:

        goals_conceded = (goals_c / minutes) * 90

        goals_conceded = "{:.2f}".format(goals_conceded)

        return goals_conceded


def save_to_goal_ratio_calc(saves_m,goals_c):

    if goals_c == 0:

        return 0

    else:
        save_to_goal_ratio = (saves_m / goals_c)

        save_to_goal_ratio = "{:.2f}".format(save_to_goal_ratio)

        return save_to_goal_ratio

def errors_per_90_calc(error_leading_to_shot,error_leading_to_goal,minutes):

    errors_per_90 = ((error_leading_to_shot + error_leading_to_goal) / minutes) * 100

    errors_per_90 = "{:.2f}".format(errors_per_90)

    return errors_per_90

def clean_sheets_rate(goals_c):

    if goals_c == 0:

        return "Yes"
    
    elif goals_c > 0:

        return "No"

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

    
        if shot_conversion >= 40 and shots_att > 4:

            feedback.append("You didnt do this, this is far above what even messi gets this")

        
        elif shot_conversion > 40 :

            feedback.append("This is pro standard keep it up")
        
        elif shot_conversion > 25:

            feedback.append("This is good shooting, keep improving and you will score many goals")
    
        else:

            feedback.append("You werent clinicle enough in this match, yo need to work on your shot conversion")

        return feedback
        

def generate_goal_contribution_feedback(goal_rate,assist_rate,goal_contributions):

    feedback = []

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

    elif goal_contributions >= 1:

        feedback.append("Nice performance you contributed to your teams goals, keep working to ensure its consistant")

    else:

        feedback.append("Unlucky you didnt contribute to any goals")        
  

    return feedback


def generate_key_passes_feedback(key_passes_per):

    feedback = []

    if key_passes_per :

        if key_passes_per >= 10:

            feedback.append("Well Done You were very creative with today, with many of your passes being key")

        elif key_passes_per > 5:

            feedback.append("Decent creative performance today, you should try and convert some of your passive passes to forward key passes")

        else:

            feedback.append("Not good enough with your forward creative passes, you need to work on creating more chances to improve your teams "
                            "chance of scoring")
            
        return feedback
    

def generate_dribbling_feedback(dribbles_success_rate):

    feedback = []

    if dribbles_success_rate:

        if dribbles_success_rate >=70:

            feedback.append("Brilliant Dribbling today you beat your man well and made it a nightmare for him, keep it up")

        elif dribbles_success_rate >=50:

            feedback.append("Good Dribbling today, keep trying and you will improve, you will cause danger")

        else:

            feedback.append("You Should release the ball more and choose your dribbles better")

        return feedback
    
def generate_touches_in_opp_box_feedback(touches_in_opp_box_per_90):

    feedback = []

    if touches_in_opp_box_per_90:

        if touches_in_opp_box_per_90 >= 8:

            feedback.append("Very Strong Attacking Presence today, you will find many opportunities to score")

        elif touches_in_opp_box_per_90 >= 4:

            feedback.append("You should stay more forward to take and recieve scoring opportunities")

        else:

            feedback.append("You lacked forward penetration, you are playing too deep, you will need to improve this to score more"
                            " and become a better striker")
            
        return feedback
            
def generate_offside_feedback(offsides_per_90):

    feedback = []

    if offsides_per_90:

        if offsides_per_90 >= 4:

            feedback.append("You were offside too often today, you need to do better and watch your runs")

        elif offsides_per_90 >= 1:

            feedback.append("You were offside more times than you should be, its nothing to be worried about you just need to"
                            " improve your timing when making runs")
            
        else:

            feedback.append("You had no offsides today, well done you timed your runs very well")

        return feedback

def generate_fouls_drawn_feedback(fouls_drawn_per_90):

    feedback = []

    if fouls_drawn_per_90:

        if fouls_drawn_per_90 > 5:

            feedback.append("Terrific you caused the defenders so many problems today keep it up and you will win frees and penos")

        elif fouls_drawn_per_90 >= 1:

            feedback.append("Nice you drew fouls meaning you were a threat today")

        else:

            feedback.append("You didnt cause the centre backs enough problems today, doesnt mean you played bad" \
                            " but it is something to be mindful about")
            
        return feedback
    
def generate_crossing_feedback(crossing_accuracy):

    feedback = []

    if crossing_accuracy:

        if crossing_accuracy > 70:

            feedback.append("Utter Class Crossing today, keep it up")

        elif crossing_accuracy >=20:

            feedback.append("Your Crossing Was decent today, You need still need to work on it")

        else:

            feedback.append("Your Crossing was terrible today, you need to improve in this key area")

        return feedback    

def generate_tackling_feedback(tackling_accuracy):

    feedback = []

    if tackling_accuracy:

        if tackling_accuracy >= 80:

            feedback.append("Your Tackling was second to none, absolutly brilliant")

        elif tackling_accuracy >60:

            feedback.append("Your tackling was good today, but you will need to improve")

        else:

            feedback.append("Your tackling was very bad today, you need to learn to judge the tackle better")

        return feedback
    
def generate_interception_feedback(interception_rate):

    feedback = []

    if interception_rate:

        if interception_rate >= 3:

            feedback.append("You read the play unbelievably today, great preformance")

        elif interception_rate >=1:

            feedback.append("Good reading of the play today, keep it up")

        else:

            feedback.append("You should try and keep your head up and anticipate the play better")


        return feedback
    
def generate_clearance_feedback(clearance_rate):

    feedback = []

    if clearance_rate:

        if clearance_rate >= 6:

            feedback.append("Your clearances were vital for your team today, terrific keep it up")

        elif clearance_rate >=2:

            feedback.append("Well done on your clearances, you got your team out of trouble at times")

        else:

            feedback.append("Unlucky, you should try and judge the ball when its in the box to clear")

        return feedback

def generate_block_feedback(block_rate):


    feedback = []

    if block_rate:

        if block_rate >=3:

            feedback.append("Brave performance today, you put your body on the line to help your team")

        elif block_rate >=1:

            feedback.append("Good blocking today keep it up")

        else:

            feedback.append("You need to be more brave in your defending")

        return feedback
    
def generate_aerial_duel_feedback(aerial_duel_success_rate):

    feedback = []

    if aerial_duel_success_rate:

        if aerial_duel_success_rate > 60:

            feedback.append("You dominated your aerial duels today, very good performance, keep it up")

        elif aerial_duel_success_rate >=40:

            feedback.append("You done well against the striker today, but you need to improve to dominate")

        else:

            feedback.append("You were bullied by your opponent today, you need to improve in this area to become a complete defender")

        return feedback

def generate_fouls_committed_feedback(fouls_committed_rate):

    feedback = []

    if fouls_committed_rate:

        if fouls_committed_rate > 5:

            feedback.append("You need to be more deciplined in your defending to prevent conceding fouls")

        elif fouls_committed_rate >= 1:

            feedback.append("You committed too many fouls")

        else:

            feedback.append("Very deciplined in your defending today keep it up")

        return feedback
    

def generate_save_percentage_feedback(save_percentage):

    feedback = []

    if save_percentage:

        if save_percentage > 75:

            feedback.append("Great shot stopping today, well done")

        elif save_percentage >= 60:

            feedback.append("Decent performance, you still need to work on this area to get better")

        else:

            feedback.append("Terrible performance, you need to improve tremendously")

        return feedback
    
def generate_goals_conceded_feedback(goals_conceded):

    feedback = []

    if goals_conceded:

        if goals_conceded > 3:

            feedback.append("You conceded too many goals, you need to improve your goal stopping to help your team")

        elif goals_conceded >=1:

            feedback.append("Unlucky today, just keep working in training and you will prevent goals")

        else:

            feedback.append("Well Done you didnt concede any goals")

        return feedback
    

def generate_save_to_goal_feedback(save_to_goal_ratio):

    feedback = []

    if save_to_goal_ratio:

        if save_to_goal_ratio > 3.0:

            feedback.append("Well done you saved the ball more than you conceded goals")

        elif save_to_goal_ratio >=1:

            feedback.append("Decent performance you still need to work on your shot and goal stopping")

        else:

            feedback.append("You need to improve your goalkeeping if you want to stay in the team")

        return feedback
            
def generate_errors_per_90_feedback(errors_per_90):

    feedback = []

    if errors_per_90:

        if errors_per_90 >= 4:

            feedback.append("Very bad, You need to keep tuned in and improve your distribution badly")

        elif errors_per_90 >=1:

            feedback.append("You need to keep the mistakes out of your game and you will improve")

        else:

            feedback.append("Well done you were very diciplined in your performance, keep it up well done")

        return feedback
    

def generate_clean_sheet_feedback(goals_c):

    feedback = []

    if goals_c:

        if goals_c == 0:

            feedback.append("Well Done you kept a clean sheet today")

        else:

            feedback.append("Unlucky you werent able to keep a clean sheet")

        return feedback

