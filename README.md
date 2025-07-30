# FootballCoach

A Flask-based web application that allows football (soccer) players to input match performance statistics by position (Striker, Winger, Midfielder, Defender, Goalkeeper) and receive detailed feedback based on calculated metrics. Users can optionally create an account to save and revisit their performance history.

Features

Position-Specific Input Forms: Dynamic forms tailored to each on-field position.

Real-Time Feedback: Calculate key performance statistics (e.g., passing accuracy, shot conversion, save percentage) and generate actionable feedback messages.

User Authentication: Register and log in to save performance entries.

Performance History: Authenticated users can view past entries by position, with combined average statistics and aggregated feedback.

Responsive Design: Clean and modern UI with CSS, supporting desktop and mobile devices.

Technologies

Backend: Python, Flask, Flask-Login, Flask-SQLAlchemy

Database: SQLite (via SQLAlchemy ORM)

Frontend: HTML5, CSS3, Jinja2 templates

Security: Password hashing with Werkzeug

Usage

Home Page: Choose your playing position and enter match stats.

Results Page: View calculated metrics and personalized feedback.

Register/Login: Save your performance entries by creating an account.

History: After logging in, navigate to the History page to review past performances and combined averages.

Future Improvements

Deploy to Heroku or AWS with Docker and CI/CD.

Add unit and integration tests with pytest and Flask testing tools.

Enhance frontend with React or Vue for dynamic updates.

Implement data visualizations (charts for trends over time).
