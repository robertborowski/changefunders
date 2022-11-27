# ------------------------ imports start ------------------------
from email.policy import default
from website import db
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from website import secret_key_ref
# ------------------------ imports end ------------------------


# ------------------------ models start ------------------------
# ------------------------ individual model start ------------------------
# class CandidatesCapacityOptionsObj(db.Model):
#   id = db.Column(db.String(150), primary_key=True)
#   created_timestamp = db.Column(db.DateTime(timezone=True))
#   candence = db.Column(db.String(10))
#   price = db.Column(db.Float)
#   fk_stripe_price_id = db.Column(db.String(150))
# ------------------------ individual model end ------------------------
# ------------------------ models end ------------------------