# import necessary modules for sending emails (e.g., smtplib, email.message)

def send_confirmation_email(user_email, confirmation_link):
    # Create the email message
    subject = 'Confirm Your Email'
    body = f'Click the following link to confirm your email: {confirmation_link}'
    # Set up the email message headers, sender, recipient, etc.

    # Use smtplib to send the email
    # Make sure to set up your email server configuration properly

def send_password_reset_email(user_email, reset_link):
    # Create the email message
    subject = 'Password Reset'
    body = f'Click the following link to reset your password: {reset_link}'
    # Set up the email message headers, sender, recipient, etc.

    # Use smtplib to send the email
    # Make sure to set up your email server configuration properly

# Add other email utility functions as needed
