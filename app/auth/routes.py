from flask import Blueprint
from .views import register

auth_bp = Blueprint("auth", __name__)

# Register the class-based view
auth_bp.add_url_rule("/register", view_func=register, methods=["GET", "POST"])
