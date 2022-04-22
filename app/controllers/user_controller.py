from http import HTTPStatus
from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
from app.models.user_model import UserModel
from app.configs.database import db
from sqlalchemy.orm.session import Session
from app.configs.auth import auth
import secrets



def create_user():

    data = request.get_json()
    try:
        data["api_key"] = secrets.token_urlsafe(64)

        user: UserModel = UserModel(**data)
        
        db.session.add(user)
        db.session.commit()

        return jsonify(user), HTTPStatus.CREATED


    except (TypeError, KeyError, NameError):
        return {"Error": "Incorrect format key"}, HTTPStatus.BAD_REQUEST
        
    except IntegrityError:
        return {"error": "User already exists"}, HTTPStatus.BAD_REQUEST



def login_user():
    data = request.get_json()

    email = data["email"]

    password = data["password"]

    session: Session = db.session

    query =  session.query(UserModel)
    
    user_by_email = query.filter(UserModel.email == email).first()   

    if not user_by_email:
        return {"Error": "User not found"}, HTTPStatus.NOT_FOUND

    allowed = user_by_email.check_password(password)

    if not allowed:
        return {"Error": "Invalid password"}, HTTPStatus.NOT_FOUND

    api_key = user_by_email.api_key

    return {"api_key": api_key}



@auth.login_required
def read_user():

    current_user = auth.current_user()

    return jsonify(current_user)



@auth.login_required
def update_user():
    data = request.get_json()

    email = data["email"]

    name = data["name"]

    last_name = data["last_name"]

    password = data["password"]

    session: Session = db.session

    
    output_user = session.query(UserModel).filter(UserModel.email == email).first()   


    if not output_user:
        return {"Error": "Email not found"}, HTTPStatus.NOT_FOUND

    output_user.name = name
    output_user.last_name = last_name
    output_user.password = password
    
    return jsonify(output_user)




@auth.login_required
def delete_user():

    current_user = auth.current_user()

    email = current_user.email

    session: Session = db.session

    output_delete_user = session.query(UserModel).filter(UserModel.email == email).first()   

    if not output_delete_user:
        return {"Error": "Email not found"}, HTTPStatus.NOT_FOUND

    output_message = {
        "message": f"User {output_delete_user.name} has been deleted."
    }

    session.delete(output_delete_user)
    session.commit()


    return jsonify(output_message)

    