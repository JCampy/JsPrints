from ecommerce import create_FlaskApp

app = create_FlaskApp()

if __name__ == '__main__':
    #with app.app_context():
    #    db.create_all()
    #app.run(host='0.0.0.0', port= 8000, debug=True)
    app.run(debug=True)