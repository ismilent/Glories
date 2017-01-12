from padmin.extensions import db
from padmin.extensions import bcrypt

class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                onupdate=db.func.current_timestamp())
    

class User(Base):
    __tablename__ = 'user'

    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.SmallInteger, nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)

    def __init__(self, username, email, password, role=2, status=0):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.role = role
        self.status = status
    
    def __repr__(self):
        return '<User %r>' % (self.username)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    #flask-login
    def get_id(self):
        return self.id

    def is_authenticated(self):
        return False
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False