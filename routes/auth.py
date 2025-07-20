
from flask import Blueprint,render_template,request,redirect,url_for,session,flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import User,db

auth = Blueprint('auth',__name__)


@auth.route('/login',methods=['GET','POST'])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password,password):

            flash("Invalid username or password","error")

            return redirect(url_for("auth.login"))
        
        session["user_id"] = user.user_id
        session["username"] = user.username

        flash("Logged In Successfully","success")

        return redirect(url_for("app.index"))
    
    return render_template("login.html")


@auth.route('/register',methods=['GET','POST'])
def register():

    if request.method == "POST":

        first_name = request.form["firstName"]
        surname = request.form["surname"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:

            flash("The passwords you entered dont match","error")

            return redirect(url_for('auth.register'))

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:

            flash("Already Registered","error")

            return redirect(url_for('auth.register'))
        
        hashed_password = generate_password_hash(password)

        new_user = User(

            first_name = first_name,
            surname = surname,
            email = email,
            username = username,
            password = hashed_password,

        )

        db.session.add(new_user)
        db.session.commit()

        flash("Account Created. Please Log In Now","info")
        
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth.route("/logout")
def logout():

    session.clear()

    flash("Logged Out Successfully","info")

    return redirect(url_for("auth.login"))