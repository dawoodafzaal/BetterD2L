from flask import Flask, redirect, url_for, render_template, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)   #this file
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class StudentModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(500))
    link = db.Column(db.String(1000))
    due = db.Column(db.DateTime, deafault = datetime.now)
    checkedat = db.Column(db.DateTime)


video_put_args = reqparse.RequestParser()

db.create_all()

class Hello(Resource):
    def get(self, stdid):
        result = StudentModel.query.get(id = stdid)
        return result
    
    def put(self,stdid):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        item = StudentModel(id=stdid, title=args['title'], link=args['link'], due=args['due'], checkedat=args['checkedat'])
		db.session.add(item)
		db.session.commit()
		return item, 201

    def delete(self, stdid):
		del items[stdid]
		return '', 204

if __name__ == "__main__":
    app.run(debug=True)
