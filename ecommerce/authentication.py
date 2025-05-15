from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .db_models import Payment, Purchase_history, User
from flask_login import login_user, login_required, logout_user, current_user

authentication = Blueprint('authentication', __name__)

# route for login.html with post and get methods for database
@authentication.route('/login', methods=['GET', 'POST'])
def login():
    # checking for a post method to retrieve the data 
    if request.method == 'POST':

        # storing data retrieved from login.html
        username = request.form.get('username__or__email')
        email = request.form.get('username__or__email')
        password = request.form.get('login__password')

        # c - check
        #
        # checking for correct email or username
        cusername = User.query.filter_by(user_name=username).first()
        cemail = User.query.filter_by(user_email=email).first()
        
        # checking first for existing email or username
        # then checking for correct password
        if cusername:
            if check_password_hash(cusername.password, password):
                flash('Logged in successfully!', category='success')
                login_user(cusername, remember=True) # keep track of which user logged in
                return redirect(url_for('routes.index'))
            else:
                flash('Incorrect password!! Try again!', category='error')
        elif cemail:
            if check_password_hash(cemail.password, password):
                flash('Logged in successfully!', category='success')
                login_user(cemail, remember=True) # keep track of which user logged in
                return redirect(url_for('routes.index'))
            else:
                flash('Incorrect password!! Try again!', category='error')
        else:
            flash('Username\\Email does not exist! Try again!', category='error')
    # display login.html
    return render_template('login.html', user=current_user)


#@authentication.route('/shipping', methods=['GET', 'POST'])
#@authentication.route('/purchase_history', methods=['GET', 'POST'])
#@authentication.route('/payment', methods=['GET', 'POST'])

# route for signup.html with post and get methods for database
@authentication.route('/signup', methods=['GET', 'POST'])
def signup():
    # checking for a post method to retrieve the data 
    if request.method == 'POST':

        # storing the data into variables
        fname = request.form.get('signUpFirstName')
        lname = request.form.get('signUpLastName')
        username = request.form.get('signUpUsername')
        email = request.form.get('signUpEmail')
        phonenum = request.form.get('signUpPhoneNum')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # c - check 
        # checking for existing username or email
        cuser = User.query.filter_by(user_name=username).first()
        cemail = User.query.filter_by(user_email=email).first()


        # checking for certain requirements to take the data retrieved and 
        # transfer it into the database
        #
        # flash method displays error or success message in browser
        if cuser:
                flash('The username you entered already exist. Try again!', category='error')
        elif cemail:
            flash('The email you entered already exist. Try again!', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error') 
        elif len(username) < 2:
            flash('Username must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('Passwords must match.', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters.', category='error')
        else:

            # phone number is optional so we are checking for that
            if phonenum:
                if len(phonenum) < 7 or '-' not in phonenum:
                    flash('Phone number must be atleast 7 digits and include \'-\'.', category='error')
                else:
                    # create new user object for database table
                    new_user = User(user_name=username, user_email=email, user_fname=fname, user_lname=lname, user_phone_num=phonenum, password=generate_password_hash(password1, method='pbkdf2:sha256'))
                    #new_payment = Payment(card_num=None, card_holder_name=None, card_exp=None, card_pin=None, billing_addr=None)
                    #new_purchase_his = Purchase_history(product_id=None, quanity=None, purchase_price=None, transaction_cost=None)
                    #new_shipping =
                    db.session.add(new_user) # add user object into database session
                    db.session.commit() # commit to the database
                    flash('Account created!', category='success')
                    return redirect(url_for('routes.index'))
            else:
                # create new user object for database table
                new_user = User(user_name=username, user_email=email, user_fname=fname, user_lname=lname, user_phone_num=None, password=generate_password_hash(password1, method='pbkdf2:sha256'))
                db.session.add(new_user) # add user object into database session
                db.session.commit() # commit to the database
                flash('Account created!', category='success')
                return redirect(url_for('authentication.login'))
            
    # display signup.html 
    return render_template('signup.html', user=current_user)

# route to log a user out
@authentication.route('/logout')
@login_required # must be logged in to see (See base.html)
def logout():
    logout_user() # logs user out
    return redirect(url_for('authentication.login')) # redirect back to login page