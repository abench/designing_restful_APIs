from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Puppy

database = 'sqlite:///puppies.db'

def db_init(path='sqlite:///puppies.db'):
    engine = create_engine(path)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session

app = Flask(__name__)


# Create the appropriate app.route functions,
# test and see if they work


# Make an app.route() decorator here
@app.route("/")
@app.route("/puppies/", methods=['GET', 'POST'])
def puppiesFunction():
    if request.method == 'GET':
        # Call the method to Get all of the puppies
        return getAllPuppies()
    elif request.method == 'POST':
        # Call the method to make a new puppy
        print("Making a New puppy")

        name = request.args.get('name', '')
        description = request.args.get('description', '')
        print(name)
        print(description)
        return makeANewPuppy(name, description)


# Make another app.route() decorator here that takes in an integer id in the URI
@app.route("/puppies/<int:id>/", methods=['GET', 'PUT', 'DELETE'])
# Call the method to view a specific puppy
def puppiesFunctionId(id):
    if request.method == 'GET':
        return getPuppy(id)

    # Call the method to edit a specific puppy
    elif request.method == 'PUT':
        name = request.args.get('name', '')
        description = request.args.get('description', '')
        return updatePuppy(id, name, description)

    # Call the method to remove a puppy
    elif request.method == 'DELETE':
        return deletePuppy(id)


def getAllPuppies():
    puppies = db.query(Puppy).all()
    return jsonify(Puppies=[i.serialize for i in puppies])


def getPuppy(id):
    puppy = db.query(Puppy).filter_by(id=id).one()
    return jsonify(puppy=puppy.serialize)


def makeANewPuppy(name, description):
    puppy = Puppy(name=name, description=description)
    db.add(puppy)
    db.commit()
    return jsonify(Puppy=puppy.serialize)


def updatePuppy(id, name, description):
    puppy = db.query(Puppy).filter_by(id=id).one()
    if not name:
        puppy.name = name
    if not description:
        puppy.description = description
    db.add(puppy)
    db.commit()
    return "Updated a Puppy with id %s" % id


def deletePuppy(id):
    puppy = db.query(Puppy).filter_by(id=id).one()
    db.delete(puppy)
    db.commit()
    return "Removed Puppy with id %s" % id


if __name__ == '__main__':
    db = db_init(database)
    app.debug = False
    app.run(host='0.0.0.0', port=5000)