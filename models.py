"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG = 'https://tinyurl.com/demo-cupcake'

def connect_db(app):
    """For connection to database."""
    db.app = app
    db.init_app(app)
    app.app_context().push()
    
class Cupcake(db.Model):
    """Cupcake Model"""
    __tablename__ = 'cupcakes'
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMG)
    
    def serialize(self):
        """Serialize cupcake to a dictionary of info about the cupcake."""
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }