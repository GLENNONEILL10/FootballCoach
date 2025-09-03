#FootballCoach ⚽

A Flask-based web application that allows football (soccer) players to input match performance statistics by position (Striker, Winger, Midfielder, Defender, Goalkeeper) and receive detailed feedback based on calculated metrics. Users can optionally create an account to save and revisit their performance history.








✨ Features

Position-Specific Input Forms: Dynamic forms tailored to each on-field position.

Real-Time Feedback: Calculate key performance statistics (e.g., passing accuracy, shot conversion, save percentage) and generate actionable feedback.

User Authentication: Register and log in to save performance entries.

Performance History: Authenticated users can view past entries by position, with combined averages and aggregated feedback.

Responsive Design: Clean, modern UI with CSS, supporting desktop and mobile devices.

📦 Technologies

Backend: Python, Flask, Flask-Login, Flask-SQLAlchemy

Database: SQLite (via SQLAlchemy ORM)

Frontend: HTML5, CSS3, Jinja2 templates

Security: Password hashing with Werkzeug

🚀 Getting Started

Clone the repo

git clone https://github.com/GLENNONEILL10/FootballCoach.git
cd FootballCoach


Create and activate a virtual environment

python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Run the app

flask run


Visit http://127.0.0.1:5000
.

🎮 Usage

Home Page: Choose your playing position and enter match stats.

Results Page: View calculated metrics and personalized feedback.

Register/Login: Create an account to save your performance history.

History Page: Review past performances and combined averages.

📸 Screenshots

Add screenshots or GIFs of your app here (recommended: form page, results page, history page).

Example:

<img width="1883" height="904" alt="Screenshot 2025-07-30 010905" src="https://github.com/user-attachments/assets/d4fea996-a983-4198-9cb2-e657f6be97ee" />


<img width="1889" height="869" alt="Screenshot 2025-07-30 010943" src="https://github.com/user-attachments/assets/e8564e94-d874-466e-9c2c-09e934698bf1" />


<img width="1667" height="617" alt="Screenshot 2025-07-30 011016" src="https://github.com/user-attachments/assets/71d2ffda-ee27-4d1a-945a-dfe50119ab4d" />


🧾 What I Learned

Building authentication and persistence with Flask-Login and SQLAlchemy.

Designing position-specific feedback logic and metrics calculations.

Structuring a Flask app with templates, static files, and modular routes.

Improving my ability to debug and test full-stack applications.

🛣️ Future Improvements

Deploy to Heroku, Render, or AWS with Docker and CI/CD.

Add unit and integration tests with pytest and Flask testing tools.

Enhance frontend with React or Vue for dynamic updates.

Implement data visualizations (charts for trends over time).
