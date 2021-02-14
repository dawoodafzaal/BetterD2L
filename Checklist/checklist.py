from flask import Flask
from flask_restful import Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///checkListdb.db'

db = SQLAlchemy(app)

class CheckList(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(500))
    link = db.Column(db.String(1000))
    checkedat = db.Column(db.DateTime)
    duedate = db.Column(db.DateTime)

check_put_args = reqparse.RequestParser()
check_put_args.add_argument("title", type=str, required=true)
check_put_args.add_argument("link", type=str, required=false)
check_put_args.add_argument("checkedat", type=datetime, required=false)
check_put_args.add_argument("duedate", type=datetime, required=false)

check_update_args = reqparse.RequestParser()
check_update_args.add_argument("title", type=str)
check_update_args.add_argument("link", type=str)
check_update_args.add_argument("checkedat", type=datetime)
check_update_args.add_argument("duedate", type=datetime)

resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'link': fields.String,
    'checkedat': fields.DateTime,
    'duedate': fields.DateTime
}

class Checks(Resource):
    @marshal_with(resource_fields)
    def get(self,entry_id):
        result = CheckList.query.get(id = entry_id)
        return result
    
    @marshal_with(resource_fields)
    def put(self, entry_id):
        args = check_put_args.parse_args()
        result = CheckList.query.filter_by(id=entry_id).first()
        check = CheckList(id=entry_id, title=args['title'], link=args['link'], checkedat=args['checkedat'], duedate=args['duedate'])
        db.session.add(check)
        db.session.commit()
        return check, 201

    @marshal_with(resource_fields)
    def patch(self, entry_id):
        args = check_update_args.parse_args()
        result = CheckList.query.filter_by(id=entry_id).first()
        if args['title']:
            result.title = args['title']
        if args['checkedat']:
            result.checkedat = args['checkedat']
        if args['duedate']:
            result.duedate = args['duedate']

        db.session.commit()
        return result

    @marshal_with(resource_fields)
    def delete(self, entry_id):
        CheckList.query.filter_by(id=entry_id).delete()
        db.session.commit()
        return '', 204

if __name__ == "__main__":
    app.run(debug=True)

# def addToList():
#     listItem = input("Add something to the checklist: ")
#     if listItem == "":
#         return
#     else:
#         checkList.append(listItem)

# def removeFromList():
#     removeItem = input("Remove something from the checklist by number: ")
#     if removeItem == "":
#         return
#     else:
#         if len(checkList) < int(removeItem):
#             print("Can't remove an item that doesn't exist!")
#             return
#         del checkList[int(removeItem)-1]

# def displayList(counter):
#     if len(checkList) == 0:
#         print("List is empty!")

#     for item in checkList:
#         counter += 1
#         print("#", counter," ", item)

# def main():
#     counter = 0
#     while 1:
#         menu = input("1 to add, 2 to remove, 3 to view, 4 to quit: ")
#         if menu == "1":
#             addToList()
#             displayList(counter)
#         elif menu == "2":
#             removeFromList()
#             displayList(counter)
#         elif menu == "3":
#             displayList(counter)
#         else:
#             break

# main()

