from application import db, login_manager
from flask_login import UserMixin

#-----------------user-login-manager-----------------------------

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

#-------------------user modeling table----------------------------------

class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        user_name = db.Column(db.String(30), unique=True)
        email = db.Column(db.String(150), nullable=False, unique=True)
        prizes = db.relationship('Prizes', backref='author', lazy=True)

        def __repr__(self):
              return ''.join([
                        'User ID: ', str(self.id), '\r\n',
                        'User_name:', str(self.user_name), '\r\n',
                        'Email: ', self.email, '\r\n',
                        'Prizes ', self.prizes, ' ', self.prizes])
#--------------------prizes table-------------------------------------------
class Prizes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user_id"), nullable=false)
    pound_prize = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return ''.join([
                    'User_id:' , self.user_id, '\r\n',
                    'Pound_prize:' , self.pound_prize,
        ])

#-------------------could add another table for cards-- moscow ---------------
'''class Cards(db.Model):
    id = db.Column(db.Integer, primary_keys=True)
    card_name = db.Column(db.String(25), nullable=False, unique=True)
    card_worth = db.Column(db.String, nullable=False)

    def __repr__(self):
        return ''.join([
                'Card_name:' , self.card_name, '\r\n',
                'Card_worth:' , self.card_worth,
        ])
'''
