from . import db

class Student(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  f_name = db.Column(db.String(40), nullable=False)
  l_name = db.Column(db.String(40), nullable=False)
  class_yr = db.Column(db.Integer, nullable=False)
  def __repr__(self) -> str:
      return f"<id={self.id}, f_name={self.f_name}>"
  def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
  # classes = db.relationship('Course')

# class Professor(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   f_name = db.Column(db.String(40))
#   l_name = db.Column(db.String(40))
#   dep_id = db.Column(db.String(4), db.ForeignKey('department.id'))

# class Course(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   name = db.Column(db.String(100), unique=True)
#   prof_id = db.Column(db.String(4), db.ForeignKey('professor.id'))
#   dep_id = db.Column(db.String(4), db.ForeignKey('department.id'))

# class Department(db.Model):
#   id = db.Column(db.String(4), primary_key=True)
#   name = db.Column(db.String(40))
#   chair = db.Column(db.String(40), db.ForeignKey('professor.id'))
