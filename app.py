from flask import  Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///recetario.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Ingrediente (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    cantidad = db.Column(db.Float)
    unidad = db.Column(db.String)
    receta = db.relationship('Receta', secondary='receta_ingrediente')
    def __repr__(self):
        return f"{self.nombre}"
    
class Categoria(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String)
    receta = db.relationship("Receta",backref="categoria")
    def __repr__(self):
        return f"{self.nombre}"
    
class Receta(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nombre = db.Column(db.String)
    id_categoria= db.Column(db.Integer, db.ForeignKey('Categoria.id'))
    ingrediente = db.relationship('Ingrediente', secondary='receta_ingrediente')
    def __repr__(self):
        return f"{self.nombre}"

receta_ingrediente = db.Table('receta_ingrediente',
                               db.Column('receta_id', db.Integer, db.ForeignKey('receta.id')),
                               db.Column('ingrediente_id', db.Integer, db.ForeignKey('ingrediente.id'))
                               )


