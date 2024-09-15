# Phishing Demonstration Project: PayPal 2015 Incident

### **Project Overview**

This project demonstrates a phishing attack by recreating a PayPal phishing scenario, similar to the infamous 2015 PayPal phishing incident. The project shows how attackers trick users into providing their credentials using a fake login page and email spoofing. For educational purposes, this demo emphasizes the importance of recognizing phishing attempts and protecting sensitive information.

### **Key Features**
- **Fake PayPal Login Page:** A login page mimicking the legitimate PayPal site to collect users' credentials.
- **Data Storage:** Collected credentials are stored in an Airtable database for review.
- **Email Bait:** A fake phishing email designed to look like a PayPal security notice, with an embedded malicious hyperlink.
- **Educational Demonstration:** The demo provides a visual and practical example of phishing and steps users can take to avoid such scams.

### **How It Works**
1. **Phishing Page Creation:**  
   A PayPal login page has been created where users can input their credentials. The page looks authentic to fool users into believing it's the official PayPal login.

2. **Airtable Integration:**  
   The credentials entered into the fake login page are stored in a table on Airtable for later analysis.

3. **Email Setup:**  
   A fake email resembling a PayPal security notice is sent to a user. The email contains a sense of urgency, instructing the user to click the hyperlink (disguised malicious URL) to resolve account issues.

4. **2015 PayPal Phishing Incident Case Study:**  
   This project highlights the techniques used in the real-world 2015 PayPal phishing attack and discusses why it was successful, impacting a large number of PayPal users.

5. **User Awareness & Prevention Tips:**  
   The demonstration concludes with key tips on identifying phishing emails, verifying URLs, and other best practices to protect against phishing attacks.

### **Project Components**

- **Fake PayPal Login Page**  
   - HTML/CSS-based page that resembles PayPal's real login interface.
   - Captures user input (email and password fields).
   - Data is sent to Airtable for storage.

- **Phishing Email**  
   - Crafted email with a PayPal-like address.
   - Contains a fake hyperlink leading to the phishing page.
   - Uses scare tactics like “Account Suspension” or “Suspicious Activity Detected” to compel action.

- **Airtable Database**  
   - Credentials entered into the fake PayPal page are stored here for demonstration purposes.
   - Shows how easy it is for attackers to collect sensitive information.

### **Setup Instructions**

1. **Create Airtable Database**
   - Go to [Airtable](https://airtable.com/) and sign up for an account.
   - Create a new base for storing the credentials, with fields like "Email" and "Password".
   - Get the Airtable API key and base ID to integrate it with the fake PayPal page.

2. **Run the Fake PayPal Login Page**
   - Clone this repository:  
     ```
     git clone https://github.com/your-username/paypal-phishing-demo.git
     ```
   - Navigate to the project directory and open `index.html` in your browser.
   - Ensure that the data entered on the login page is successfully stored in Airtable.

3. **Send the Phishing Email**
   - Create a fake PayPal email using any email service that allows spoofing.
   - In the email, add the link to the fake PayPal login page (e.g., `http://your-domain.com/fake-login-page`).
   - Send the email to the targeted recipient with a message urging them to act quickly.

4. **Analyze Data in Airtable**
   - Once users enter their credentials in the fake login page, go to your Airtable base to see the stored data.
   - This showcases how phishing attacks harvest sensitive data.

### **2015 PayPal Phishing Incident Overview**

The 2015 PayPal phishing incident is one of the most notorious phishing attacks in recent years. Attackers used email spoofing to send emails that appeared to come from PayPal's official email address. These emails contained links to fake PayPal login pages, where users were tricked into entering their credentials. The incident became widespread due to the high number of victims who fell for the attack, highlighting the need for better user awareness and security practices.

### **Phishing Prevention Tips**
- Always check the URL for SSL certificates and domain integrity (e.g., `https://www.paypal.com`).
- Look out for grammatical errors and strange sender addresses in emails.
- Avoid clicking on links in unsolicited emails—always manually enter the URL in the browser.
- Enable multi-factor authentication (MFA) on important accounts to add extra layers of security.
- Use anti-phishing browser extensions or tools to help detect malicious websites.

### **Disclaimer**

This project is intended for **educational purposes only**. The demonstration aims to raise awareness of phishing tactics and help individuals and organizations take proactive steps to prevent such attacks. Misusing this information for illegal activities is strictly prohibited.
