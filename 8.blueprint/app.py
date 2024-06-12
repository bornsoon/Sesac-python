from flask import Flask, render_template
from admin.admin import admin_app
from product.product import product_app
from user.user import user_app

app = Flask(__name__)

app.register_blueprint(admin_app, url_prefix="/admin")
app.register_blueprint(product_app, url_prefix="/product")
app.register_blueprint(user_app, url_prefix="/user")

@app.route('/')
def home():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)