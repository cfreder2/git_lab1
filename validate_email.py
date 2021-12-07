import pandas as pd

def validate_email(email):
    """ Ensure that emails are valid
    
    Arguments:
    email - A pandas series of emails

    Return:
    A boolean pandas series.  True means valid.  False means invalid.
    """

    bool_email = email.str.contains(r"[A-z0-9]+@[A-z0-9.]+.com")
    return bool_email

emails = pd.Series(['cfreder2@nd.com','happyday@gmail.com', '1123 main street'])
print(validate_email(emails))