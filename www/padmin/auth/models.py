from padmin.extensions import db

class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                onupdate=db.func.current_timestamp())
    

class Users(Base):
    __tablename__ = 'auth_user'

    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.SmallInteger, nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)

    def __init__(self, username, email, password, role=1, ):
        self.username = username
        self.email = email
        self.password = password
    
    def __repr__(self):
        return '<User %r>' % (self.username)
    
    #flask-login
    def get_id(self):
        return self.id

    def is_authenticated(self):
        if self.role == 1:
            return True
        else:
            return False
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False