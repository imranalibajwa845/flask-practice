from app import ma
from marshmallow import fields, validates, ValidationError

class ProductSchema(ma.Schema):
    id = fields.String(dump_only=True)
    name = fields.String(required=True)
    price = fields.Float(required=True)
    quantity = fields.Integer(required=True)
    created_at = fields.DateTime(dump_only=True)

    @validates("price")
    def validate_price(self, value):
        if value <= 0:
            raise ValidationError("Price must be greater than zero.")

    @validates("quantity")
    def validate_quantity(self, value):
        if value < 0:
            raise ValidationError("Quantity cannot be negative.")

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
