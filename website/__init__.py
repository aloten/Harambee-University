from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
  app = Flask(__name__)
  CORS(app)
  app.config['SECRET_KEY'] = 'asd;licwe,'
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  db.init_app(app)

  from .views import views
  app.register_blueprint(views, url_prefix='/')

  # API data routes
  @app.route("/addStudent", methods=['POST'])
  def add_student():
    req = request.json
    new_student = Student(f_name=req['firstName'],l_name=req['lastName'],class_yr=req['classYear'],)
    db.session.add(new_student)
    db.session.commit()
    return {'msg':'new student added'}, 200

  @app.route("/students", methods=['GET'])
  def get_students():
    query = Student.query.all()
    students = []
    for student in query:
      students.append(student.as_dict())
    return {"students":students}

  from .models import Student
  create_database(app)

  return app

def create_database(app):
  if not path.exists('website/' + DB_NAME):
    db.create_all(app=app)
    print('Created Database!')