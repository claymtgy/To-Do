from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Database configuration
# Replace the placeholders with your MySQL connection details
app.config['MYSQL_HOST'] = 'your_mysql_host'
app.config['MYSQL_USER'] = 'your_mysql_user'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'your_mysql_database'

# Define routes
@app.route('/', methods=['GET'])
def index():
    # Get current user from session or None if not logged in
    current_user = Flask.session.get('username')
    
    if current_user:
        # Fetch user's tasks from the database
        tasks = fetch_user_tasks(current_user)
        return render_template('index.html', current_user=current_user, tasks=tasks)
    else:
        return render_template('index.html', current_user=None)

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the form
    username = request.form['username']
    password = request.form['password']
    
    # Validate the username and password
    if validate_user(username, password):
        # Store the username in the session
        Flask.session['username'] = username
        return Flask.redirect(Flask.url_for('index'))
    else:
        return "Invalid username or password"

@app.route('/logout', methods=['GET'])
def logout():
    # Clear the username from the session
    Flask.session.pop('username', None)
    return Flask.redirect(Flask.url_for('index'))

@app.route('/other_user_tasks', methods=['GET'])
def get_other_user_tasks():
    # Fetch other user's tasks from the database
    other_user_tasks = fetch_user_tasks('other_user')
    
    # Return the tasks as JSON response
    return jsonify({'tasks': other_user_tasks})

# Helper functions for database operations
def fetch_user_tasks(username):
    # Perform a database query to retrieve the tasks for the specified username
    # Replace the placeholders with your own code to fetch tasks from MySQL
    
    # Example query:
    # SELECT task FROM tasks WHERE username = '<username>'
    tasks = ["test"]
    # Return the list of tasks
    return tasks

def validate_user(username, password):
    # Perform a database query to validate the username and password
    # Replace the placeholders with your own code to validate the user from MySQL
    
    # Example query:
    # SELECT COUNT(*) FROM users WHERE username = '<username>' AND password = '<password>'
    is_valid_user = True
    # Return True if the user is valid, False otherwise
    return is_valid_user

if __name__ == '__main__':
    app.secret_key = 'your_secret_key'
    app.run()
