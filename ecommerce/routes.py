import os
from flask import current_app as app
from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename
from . import db
from .db_models import Orders, User, Cart, Product, Shipping, Payment, Purchase_history, OrderedProduct
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


# creating a blueprint for routes.py
routes = Blueprint('routes', __name__)


# File integrity checker 
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# index.html 
@routes.route('/')
def index():

    return render_template('index.html', user=current_user)

# products.html
@routes.route('/products', methods=['GET', 'POST'])
def products():
    products = Product.query.all()
    #print(products)
    return render_template('products.html', user=current_user, products=products)

@routes.route('/products/<string:category>', methods=['GET', 'POST'])
def products_by_category(category):
    curr_category = category
    products = Product.query.all()
    prod_by_category = Product.query.filter_by(category=curr_category)
    return render_template('products.html', user=current_user, curr_category=curr_category, prod_by_category=prod_by_category, products=products)
#{{ url_for('routes.products', user=current_user, category=curr_category) }}

@routes.route('/productDisplay/<int:product_id>', methods=['GET', 'POST'])
def productDisplay(product_id):

    product = Product.query.get_or_404(product_id)
    product_owner = User.query.get_or_404(product.user_id)
    location = product_owner.user_address
    if location:
        splitlocation = location.split(',')
        located = splitlocation[3] + ',' + splitlocation[5]
        print(located)
    
    id = current_user.get_id()
    prod_display_user = id
    if request.method == 'POST':

        new_cart = Cart(user_id=id, product_id=product_id, quantity=1)
        db.session.add(new_cart)
        db.session.commit()
        flash("Added to cart!", category="success")
        return redirect(url_for('routes.products'))
#       return render_template('productDisplay.html', user=current_user, product=product, owner=product_owner, location=located)
    if location:
        return render_template('productDisplay.html', user=current_user, product=product, owner=product_owner, location=located)
    else:
        return render_template('productDisplay.html', user=current_user, product=product, owner=product_owner)
    
@routes.route('/addProduct', methods=['GET', 'POST'])
@login_required
def addProduct():
    id = current_user.get_id()
    add_prod_user = User.query.get(id) # assign id to user_to_update

    p_name = request.form.get("p_name")
    p_price = request.form.get("p_price")
    p_desc = request.form.get("p_desc")
    category = request.form.get("category")

    #print(file.filedata)
    if request.method == 'POST':

        file = request.files['uploadedFile']
        print(file.filename)
        print(file)
        print(file.read())

        if len(p_name) < 4:
            flash("Invalid product name", category="error")
        elif p_price.isdigit() == False:
            flash("Invalid price!", category="error")
        elif len(p_desc) < 5:
            flash("Invalid description!", category="error")
        elif len(category) < 3:
            flash("Invalid category", category="error")
        else:
            # check if the post request has the file part
            if 'uploadedFile' not in request.files:
                flash('No file part', category="error")
                return redirect(url_for('routes.addProduct'))
            file = request.files["uploadedFile"]
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(url_for('routes.addProduct'))
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.seek(0)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                new_product = Product(user_id=id, product_name=p_name, prod_price=p_price, prod_desc=p_desc, category=category, prod_owner=id, filename=filename)
                db.session.add(new_product)
                db.session.commit()
                #return redirect(url_for('uploaded_file', filename=filename))
            
        flash("Product was added!", category="success")
        return render_template('addProduct.html', user=current_user)
    
    return render_template('addProduct.html', user= current_user )
 
# accountManagement.html
@routes.route('/shipping', methods=['GET', 'POST'])
@routes.route('/accountManagement', methods=['GET', 'POST'])
@login_required
def accountManagement():
    # set the current user ID
    id = current_user.get_id()
    user_to_update = User.query.get(id) # assign id to user_to_update

    # gathering all the form data from accountManagement.html
    username = request.form.get("update_username")
    password1 = request.form.get("password1")
    password2 = request.form.get("update_password2")
    email = request.form.get("update_email")
    saddress1 = request.form.get("update_s_address1")
    saddress2 = request.form.get("update_s_address2")
    scity = request.form.get("update_s_city")
    sstate = request.form.get("update_s_state")
    szip = request.form.get("update_s_zip_code")
    scountry = request.form.get("update_s_country")
    baddress1 = request.form.get("update_b_addres1")
    baddress2 = request.form.get("update_b_address2")
    bcity = request.form.get("update_b_city")
    bstate = request.form.get("update_b_state")
    bzip = request.form.get("update_b_zip_code")
    bcountry = request.form.get("update_b_country")

    if request.method == 'POST':
        print("Triggered")
        # store the address
        saddress = ''
        baddress = ''

        if username:
            print(username)
            user_to_update.user_name = username
            db.session.commit()
            flash('Sucessfully updated your information!', category='success')
        if password1:
            print('exist')
            if check_password_hash(user_to_update.password, password1):
                print('matches')
                if len(password1) > 7:
                    print('length')
                    user_to_update.password = generate_password_hash(password2, method='pbkdf2:sha256')
                    db.session.commit()
                    flash('Sucessfully updated your information!', category='success')
                else:
                    flash('Password must be greater than 7 characters.', category='error')
            else:
                flash('Password doesn\'t match existing password!', category='error')
        if email:
            temp_email = email
            user_to_update.user_email = email
            db.session.commit()
            if temp_email != user_to_update.user_email:
                flash('Sucessfully updated your information!', category='success')

        # shipping address
        if saddress2:
            saddress = saddress + saddress2 + ', '
        if saddress1:
            saddress = saddress + saddress1 + ', '
        if scity:
            saddress = saddress + scity + ', '
        if sstate:
            saddress = saddress + sstate + ', '
        if szip:
            saddress = saddress + szip + ', ' 
        if scountry:
            saddress = saddress + scountry
        #if saddress != '':
            #flash('Sucessfully updated your information!', category='success')

        # billing address
        if baddress2:
            baddress = baddress + baddress2 + ', '
        if baddress1:
            baddress = baddress + baddress1 + ', '
        if bcity:
            saddress = baddress + bcity + ', '
        if bstate:
            saddress = baddress + bstate + ', '
        if szip:
            baddress = baddress + bzip + ', ' 
        if scountry:
            baddress = baddress + bcountry + ', '
        #if baddress != '':
            #flash('Sucessfully updated your information!', category='success')
        
        # adding the address into the database if baddress is same as shipping we take saddress information
        if len(saddress) > 1:

            # update user's normal address
            user_to_update.user_address = saddress

            # query the shipping table for the existence of user and certain address
            # to prevent from creating multiple rows with the same id and address
            existing_info_s = Shipping.query.filter_by(user_id=id, shipping_addr= saddress).first()
            # if the check for the user and address came back positive
            if existing_info_s:
                existing_info_s.shipping_addr = saddress # we leave the address the same
            else:
                new_shipping = Shipping(user_id=id, shipping_addr=saddress) # we create a new shipping id 
                db.session.add(new_shipping)

            db.session.commit()
            flash('Sucessfully updated your information!', category='success')

        if len(baddress) > 5:

            # query the Payment table for the existence of user and certain address
            # to prevent from creating multiple rows with the same id and address
            existing_info_b = Payment.query.filter_by(user_id=id, billing_addr= baddress).first()
            if existing_info_b:
                existing_info_b.billing_addr = baddress # leave everything the same
            else:
                # create a new Payment
                new_payments = Payment(user_id=id, card_num=None, card_holder_name=None, card_exp=None, card_pin=None, billing_addr=baddress)
                db.session.add(new_payments)

            db.session.commit()
            flash('Sucessfully updated your information!', category='success')
        else:

            # query the Payment table for the existence of user and certain address
            # to prevent from creating multiple rows with the same id and address
            baddress = saddress # make shipping address and billing address the same
            existing_info_b = Payment.query.filter_by(user_id=id, billing_addr= baddress).first()
            if existing_info_b:
                existing_info_b.billing_addr = baddress # leave everything the same
            else:
                # create a new payment
                new_payments = Payment(user_id=id, card_num=None, card_holder_name=None, card_exp=None, card_pin=None, billing_addr=baddress)
                db.session.add(new_payments)
            flash('Sucessfully updated your information!', category='success')
            db.session.commit()

        baddress = ''
        saddress = ''
        return render_template('accountManagement.html', user=current_user)
    
    else:
        return render_template('accountManagement.html', user=current_user)
    #return render_template('accountManagement.html', user=current_user)

# Search feature
@routes.route('/search')
def search():
    query = request.args.get('q', '')
    results = Product.query.filter(Product.product_name.ilike(f"%{query}%")).all()
    return render_template(
        'products.html',
        user=current_user,
        products=results,
        query=query,
        curr_category=None,
        prod_by_category=None
    )

#shoppingCart.html
#@routes.route("/payment", methods=['GET', 'POST'])
@routes.route('/shoppingCart', methods=['GET', 'POST'])
def shoppingCart():

     # set the current user ID
    id = current_user.get_id()
    cart_customer = User.query.get(id) # assign id to user_to_update
    cart = Cart.query.filter_by(user_id=id).all()
    #p_id = Product.query.all()
    print('here')
    

    ## DONT FORGET TO ADD CURRENT PRODUCTS IN CART 
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    card_num = request.form.get("card__num")
    name_on_card = request.form.get("name__on__card")
    card_exp = request.form.get("card__exp")
    card_pin = request.form.get("card__sec__pin")
    saddress1 = request.form.get("update_s_address1")
    saddress2 = request.form.get("update_s_address2")
    scity = request.form.get("update_s_city")
    sstate = request.form.get("update_s_state")
    szip = request.form.get("update_s_zip_code")
    scountry = request.form.get("update_s_country")
    baddress1 = request.form.get("update_b_addres1")
    baddress2 = request.form.get("update_b_address2")
    bcity = request.form.get("update_b_city")
    bstate = request.form.get("update_b_state")
    bzip = request.form.get("update_b_zip_code")
    bcountry = request.form.get("update_b_country")

    if request.method == 'POST':
        print("Triggered")
        saddress = ''
        baddress = ''

        if len(fname) < 2:
            flash("Please enter a valid first name.", category="error")
        elif len(lname) < 2: 
            flash("Please enter a valid last name.", category="error")
        elif len(email) < 5: 
            flash("Please enter a valid email.", category="error")
        elif len(card_num) != 16:
            flash("Please enter a valid 16 digit card number.", category="error")
        elif len(name_on_card) < 4:
            flash("Please entere a valid name on card.", category="error")
        elif len(card_exp) > 5:
            flash("Please enter a valid card expiriation date.", category="error")
        #elif "/" not in card_exp:
        #    flash("Forgot / in card expiration date.", category="error")
        elif len(card_pin) > 4:
            flash("Incorrect card security pin.", category="error")
        else:  

            # shipping address
            if saddress2:
                saddress = saddress + saddress2 + ', '
            if saddress1:
                saddress = saddress + saddress1 + ', '
            if scity:
                saddress = saddress + scity + ', '
            if sstate:
                saddress = saddress + sstate + ', '
            if szip:
                saddress = saddress + szip + ', ' 
            if scountry:
                saddress = saddress + scountry
            #if saddress != '':
                #flash('Sucessfully updated your information!', category='success')

            # billing address
            if baddress2:
                baddress = baddress + baddress2 + ', '
            if baddress1:
                baddress = baddress + baddress1 + ', '
            if bcity:
                saddress = baddress + bcity + ', '
            if bstate:
                saddress = baddress + bstate + ', '
            if szip:
                baddress = baddress + bzip + ', ' 
            if scountry:
                baddress = baddress + bcountry + ', '
            #if baddress != '':
                #flash('Sucessfully updated your information!', category='success')
        
                
            if len(saddress) > 5:

                # update user's normal address
                cart_customer.user_address = saddress
                print("Here")
                # query the shipping table for the existence of user and certain address
                # to prevent from creating multiple rows with the same id and address
                existing_info_s = Shipping.query.filter_by(user_id=id, shipping_addr= saddress).first()
                # if the check for the user and address came back positive
                if existing_info_s:
                    existing_info_s.shipping_addr = saddress # we leave the address the same
                else:
                    new_shipping = Shipping(user_id=id, shipping_addr=saddress) # we create a new shipping id 
                    db.session.add(new_shipping)

                db.session.commit()
            else:
                existing_info_s = Shipping.query.filter_by(user_id=id).first()
                saddress = existing_info_s.shipping_addr



            if len(baddress) > 5:

                # if they enter a new billing address we update the existing billing address
                existing_payment = Payment.query.filter_by(user_id=id, card_num=card_num).first()
                # we check for a payment method containing this billing address and update it there
                if existing_payment:
                    print("exist")
                    existing_payment.card_num = card_num
                    existing_payment.card_holder_name = name_on_card
                    existing_payment.card_exp = card_exp
                    existing_payment.card_pin = card_pin
                    existing_payment.billing_addr = baddress
                    db.session.commit()
                # otherwise we create a new payment setup with the new billing address
                else:
                    new_payments = Payment(user_id=id, card_num=card_num, card_holder_name=name_on_card, card_exp=card_exp, card_pin=card_pin, billing_addr=baddress)
                    db.session.add(new_payments)
                    db.session.commit()

                # query the Payment table for the existence of user and certain address
                # to prevent from creating multiple rows with the same id and address
                existing_info_b = Payment.query.filter_by(user_id=id, billing_addr= baddress).first()
                if existing_info_b:
                    existing_info_b.billing_addr = baddress # leave everything the same
                else:
                    # create a new Payment
                    print("Shot")
                    new_payments = Payment(user_id=id, card_num=None, card_holder_name=None, card_exp=None, card_pin=None, billing_addr=baddress)
                    db.session.add(new_payments)

                db.session.commit()
                flash('Sucessfully updated your information!', category='success')
            else:

                existing_payment = Payment.query.filter_by(user_id=id, card_num=card_num).first()
                # if the user already has an existing payment setup fill in only this
                # informaton
                if existing_payment:
                    print("exist")
                    existing_payment.card_num = card_num
                    existing_payment.card_holder_name = name_on_card
                    existing_payment.card_exp = card_exp
                    existing_payment.card_pin = card_pin
                    existing_payment.billing_addr = saddress
                    db.session.commit()
                # otherwise we create a whole new payment method for the user 
                else:
                    new_payments = Payment(user_id=id, card_num=card_num, card_holder_name=name_on_card, card_exp=card_exp, card_pin=card_pin, billing_addr=baddress)
                    db.session.add(new_payments)
                    db.session.commit()

                # query the Payment table for the existence of user and certain address
                # to prevent from creating multiple rows with the same id and address
                baddress = saddress # make shipping address and billing address the same
                existing_info_b = Payment.query.filter_by(user_id=id, billing_addr= baddress).first()
                if existing_info_b:
                    existing_info_b.billing_addr = baddress # leave everything the same
                else:
                    print("dead")
                    # create a new payment
                    new_payments = Payment(user_id=id, card_num=None, card_holder_name=None, card_exp=None, card_pin=None, billing_addr=baddress)
                    db.session.add(new_payments)
                flash('Sucessfully updated your information!', category='success')
                db.session.commit()

            # looking for existing payment id to add to the order
            payment_info = Payment.query.filter_by(user_id=id, card_num=card_num).first()
            paymentID = payment_info.payment_id # retrieving user's payment id

            # creating a new order
            new_order = Orders(fname=fname, lname=lname, user_email=email, user_id=id, payment_id=paymentID, shipping_addr=saddress, billing_addr=baddress)
            db.session.add(new_order)
            db.session.commit()

            # adding products to a one to many relationship with orders to keep track of items purchased.
            for items in cart_customer.cart:
                new_ordered_product = OrderedProduct(order_id=new_order.order_id, product_id=items.product_id, quantity=items.quantity)
                db.session.add(new_ordered_product)
                db.session.commit()

            cust_cart = Cart.query.filter_by(user_id=id).all()
            # removing existing cart for user
            for row in cust_cart:
                db.session.delete(row)
                db.session.commit()


            baddress = ''
            saddress = ''
            flash("Order completed!", category="success")

        return render_template('shoppingCart.html', user=current_user, cart=cart)
    return render_template('shoppingCart.html', user=current_user, cart=cart)


