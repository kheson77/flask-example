from flask import Flask, make_response, render_template
from .models import Product, db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    
    app.config.update(
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{app.instance_path}/product.db",
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        # http://
    )
    
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)
    
    # p1 = Product(name = "cake")
    # p2 = Product(name = 'pen')
    
    
    @app.route("/")
    def index():
        # p1 = Product(name = "cake")
        # p2 = Product(name = 'pen')
        # db.session.add(p1)
        # db.session.add(p2)
        
        # db.session.commit()
        user = {
            "name": "Son Khe"
        }
        return render_template("index.html", user = user)
    
    @app.route("/about-me")
    def about_me():
        return {
            "name":"Son", 
            "age": 10
        }

    @app.route("/favorite-food")
    def favorite_food():
        return make_response("<h1>My favorite food is beef</h1>")
    
    # @app.route("/products/<id>") # products/1
    # @app.route("/products/<id>/hi") # products/1
    # def get_product(id):
    #     return render_template("products/product-detail.html")
    
    @app.route("/products")
    def get_all_products():
        # products = [
        #     {
        #         "id": 1,
        #         "name": "cake",
        #         "description": "wonderful",
        #         "price": 100,
        #         "color": "red"
        #     },
        #     {
        #         "id": 2,
        #         "name": "pen",
        #         "description": "wonderful",
        #         "price": 6,
        #         "color": "blue"
        #     },
        #     {
        #         "id": 3,
        #         "name": "rice",
        #         "description": "wonderful",
        #         "price": 10,
        #         "color": "white"
        #     }
        # ]
        
        products = Product.query.all()
        # for product in products:
        return render_template("products/products.html", products = products)
    
    
    @app.route("/products/<int:id>") # products/1
    def get_product_by_id(id): # get_product_by_id
        products = [
            {
                "id": 1,
                "name": "cake",
                "description": "wonderful",
                "price": 100,
                "color": "red"
            },
            {
                "id": 2,
                "name": "pen",
                "description": "wonderful",
                "price": 6,
                "color": "blue"
            },
            {
                "id": 3,
                "name": "rice",
                "description": "wonderful",
                "price": 10,
                "color": "white"
            }
        ]
        
        product = None
        for item in products:
            if item['id'] == id:
                product = item
        return render_template("products/product-detail.html", product = product)
    
    # url_for
    
    return app