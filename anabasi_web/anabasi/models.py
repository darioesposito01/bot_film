from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from anabasi import db, login_manager
from flask_login import UserMixin
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
      id = db.Column(db.Integer, primary_key = True)
      created_at = db.Column(db.DateTime, default=datetime.now)
      name = db.Column(db.String(100), unique=True, nullable= False)
      username = db.Column(db.String(50), unique=True, nullable=False)
      password = db.Column(db.String(250), nullable=False)
      anabasi_vendite = db.Column(db.Boolean, default=False, nullable=False)
      anabasi_finanaza = db.Column(db.Boolean, default=False, nullable = False)
      anabasi_co_an = db.Column(db.Boolean, default=False, nullable=False)
      anabasi_produco = db.Column(db.Boolean, default=False, nullable=False)
      anabasi_logistica = db.Column(db.Boolean, default=False, nullable=False)
      anabasi_crisi = db.Column(db.Boolean, default=False, nullable=False)
      link_workset = db.Column(db.String(250), nullable = True)
      link_anabasi_vend = db.Column(db.String(250), nullable=True)
      link_anabasi_fina = db.Column(db.String(250), nullable=True)
      link_anabasi_co_an = db.Column(db.String(250), nullable=True)
      link_anabasi_produco = db.Column(db.String(250), nullable=True)
      link_anabasi_logistica = db.Column(db.String(250), nullable=True)
      link_anabasi_crisi = db.Column(db.String(250), nullable=True)
      def set_password_hash(self, password):
          self.password = generate_password_hash(password)


      def check_password(self, password):
          return check_password_hash(self.password, password)
