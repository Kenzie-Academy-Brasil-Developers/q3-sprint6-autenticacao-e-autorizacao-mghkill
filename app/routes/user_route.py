from flask import Blueprint
from app.controllers import user_controller

bp_user = Blueprint("api", __name__, url_prefix="/api")


bp_user.post("signup")(user_controller.create_user)
bp_user.post("signin")(user_controller.login_user)
bp_user.get("")(user_controller.read_user)
bp_user.put("")(user_controller.update_user)
bp_user.delete("")(user_controller.delete_user)