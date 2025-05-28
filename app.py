from flask import Flask,render_template,request,session,redirect

app = Flask(__name__)
app.secret_key = 'your-secret-key' 

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
                "shots_on_target":shots_on,
                "player_goals":goals,
                "player_assists":assist
            }

            
            return redirect('/result')

        except:

            pass

    return render_template('index.html', error=error)

@app.route('/result')
def result():

    data = session.get("player_entered_data")

    print("Session data:", data)

    if not data:

        return redirect('/')

    return render_template('result.html',data=data)





if __name__ == "__main__":
    app.run(debug=True)