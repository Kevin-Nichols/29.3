"""Flask app for Cupcakes""" 
from flask import Flask, render_template, request, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'hushhush'

connect_db(app)

@app.route('/')
def homepage():
    """Renders homepage"""
    return render_template('index.html')

@app.route('/api/cupcakes')
def list_cupcakes():
    """List all cupcakes in database."""
    all_cupcakes =[cupcake.serialize() for cupcake in Cupcake.query.all()]
    
    return jsonify(cupcakes=all_cupcakes)


@app.route('/api/cupcake/<int:id>')
def get_cupcake(id):
    """List info on given cupcake id."""
    cupcake = Cupcake.query.get_or_404(id)
    
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    """Create and add cupcake to database."""
    new_cupcake = Cupcake(flavor=request.json['flavor'],
                        size=request.json['size'],
                        rating=request.json['rating'],
                        image=request.json['image'])
                        
    db.session.add(new_cupcake)
    db.session.commit()
    res_json = jsonify(cupcake=new_cupcake.serialize())
    return (res_json, 201)


@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    """Updates info about a given cupcake id."""
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    """Removes a given cupcake id from the database."""
    cupcake = Cupcake.query.get_or_404(id)
    
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message='Deleted')