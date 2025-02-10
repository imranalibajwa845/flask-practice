from flask import Blueprint, request, jsonify
from app import db
from app.models import Product
from app.schemas import product_schema, products_schema

api_bp = Blueprint("api", __name__)

# ✅ CREATE a new product
@api_bp.route("/products", methods=["POST"])
def create_product():
    try:
        data = product_schema.load(request.json)
        new_product = Product(**data)
        db.session.add(new_product)
        db.session.commit()
        return product_schema.jsonify(new_product), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ✅ READ all products
@api_bp.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return products_schema.jsonify(products), 200

# ✅ READ single product
@api_bp.route("/products/<string:id>", methods=["GET"])
def get_product(id):
    product = Product.query.get_or_404(id)
    return product_schema.jsonify(product), 200

# ✅ UPDATE product
@api_bp.route("/products/<string:id>", methods=["PUT"])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.json
    if "name" in data:
        product.name = data["name"]
    if "price" in data:
        product.price = data["price"]
    if "quantity" in data:
        product.quantity = data["quantity"]

    db.session.commit()
    return product_schema.jsonify(product), 200

# ✅ DELETE product
@api_bp.route("/products/<string:id>", methods=["DELETE"])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"}), 204
