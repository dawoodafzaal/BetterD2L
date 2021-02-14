from flask import jsonify
from flask_cors import CORS, cross_origin
from flask import Flask, g, request
import sqlite3
import requests
import json
import collections
import random

app = Flask(__name__)

STUDENT_ID = 195
DATABASE = 'checklist.db'

headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjYzYzc5ZjIzLWZiMTAtNGI4YS1hMjdlLWI4YTc4NGJmNWI5MCJ9.eyJpc3MiOiJodHRwczovL2FwaS5icmlnaHRzcGFjZS5jb20vYXV0aCIsImF1ZCI6Imh0dHBzOi8vYXBpLmJyaWdodHNwYWNlLmNvbS9hdXRoL3Rva2VuIiwiZXhwIjoxNjEzMjU0MjM1LCJuYmYiOjE2MTMyNTA2MzUsInN1YiI6IjEyNTUiLCJ0ZW5hbnRpZCI6IjUyNzMxMzE3LTM3MmEtNGRiNC1iNDlkLTQ5NTAyY2U0M2YyYiIsImF6cCI6IjVkMjc0NTBmLTJjZTktNGRjZS05NTcwLTBiMjM0NTgwZGZkZCIsInNjb3BlIjoiY29udGVudDoqOiogY29yZToqOiogZGF0YWh1YjoqOiogZGlzY3Vzc2lvbnM6KjoqIGVucm9sbG1lbnQ6KjoqIGdyYWRlczoqOiogcXVpenppbmc6KjoqIHJlcG9ydGluZzoqOiogcm9sZToqOiogdXNlcnM6KjoqIiwianRpIjoiNGUyOTdkYTEtZDg4Ni00ODI3LTgyN2ItZmE4OGM0MWM5ZjExIn0.k4ndXz5MuMjwu20AXhb6kpOwfVy-iClslOsm7XglIrzO1TKBy1key-iO0MDOhNrAC5A4CpZyWUk3VtOLL8DAM-RGRSXYxEBXpJ8Hnbb2kgUVtBU9ZB7kagfulIRihH5lgEIX08smsokviWowZVT2pUNWxBFpIoJjCdIoXTJ5NAis0pVTPa0EzjELnNFuSuGk91X8Jpv5Gh7sFzDerm9rgjHCzi6it3hW--7Mxh4Rpge8dbEinbC3ugbj4YeCorkScTH65prXGyzbovX1cuNAqTyst0sRxNC7PG0F__d-OW7Q--SYckrYSdMkkg8Q19g2UpQI9pbzk23tGifeFGlHlQ',
  'Cookie': 'ADRUM=s=1613250634620&r=https%3A%2F%2Fdevcop.brightspace.com%2Fd2l%2FsystemCheck%2Fwidget%3F0; d2lSessionVal=TKH40vprvvlOxHs5ZGSliFnXb; d2lSecureSessionVal=Y2iwueXFvbe2Ygxmc183PA5zw'
}


cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/checklist', methods=['GET', 'POST', 'PATCH', 'DELETE'])
@cross_origin()
def checklist():
    conn = get_db()
    cur = conn.cursor()
    if request.method == 'POST':
        payload = request.get_json(force=True)
        try:
            title = payload['title']
            print(title)
            if 'duedate' in payload:
                duedate = payload['duedate']
            else:
                duedate = 'None'
            if 'link' in payload:
                link = payload['link']
            else:
                link = 'None'
            checkedat = 'None'
            cur.execute("SELECT COUNT(*) FROM checklist")
            is_empty = cur.fetchone()
            print(is_empty)
            if is_empty[0] == 0:
                sql_string = "INSERT INTO checklist VALUES (1, '%s', '%s', '%s', '%s')" % (title, link, checkedat, duedate)
                print(sql_string)
                cur.execute(sql_string)
            else:
                sql_string = "INSERT INTO checklist VALUES ((SELECT MAX(id) + 1 FROM checklist), '%s', '%s', '%s', '%s')" % (title, link, checkedat, duedate)
                cur.execute(sql_string)
            
            conn.commit()

            cur.execute("SELECT MAX(id) FROM checklist")
            item_id = cur.fetchone()
            return str(item_id)
        except:
            return '500'
    elif request.method == 'PATCH':
        payload = request.get_json(force=True)
        try:
            item_id = payload['id']
            checkedat = payload['checkedat']
            sql_string = "UPDATE checklist SET checkedat = '%s' WHERE id = %d", (checkedat, item_id)
            cur.execute(sql_string)

            conn.commit()

            return '204'
        except:
            return '500'
    elif request.method == 'DELETE':
        payload = request.get_json(force=True)
        try:
            item_id = (payload['id'],)
            cur.execute("DELETE FROM checklist WHERE id = ?", item_id)

            conn.commit()

            return '202'
        except:
            return '500'
    else:
        cur.execute("SELECT * FROM checklist")
        rows = cur.fetchall()
        
        # Convert query to objects of key-value pairs
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d["id"] = row[0]
            d["title"] = row[1]
            d["link"] = row[2]
            d["checkedat"] = row[3]
            d["duedate"] = row[4]
            objects_list.append(d)
        
        return jsonify(objects_list)

@app.route('/dropboxes')
@cross_origin()
def dropboxes():
    # URL for dropboxes endpoint
    dropboxes_url = "https://devcop.brightspace.com/d2l/api/le/1.51/7855/dropbox/folders/"

    # Call API and serialize response into a dictionary (JSON)
    dropboxes = requests.request("GET", dropboxes_url, headers=headers, data={}).json()

    if len(dropboxes) == 0:
        return {}

    response = { 'Computer Basics': [], 'Physics': []}

    # Loop through dropboxes and construct response
    for db in dropboxes:
        db_id = db['Id']
        info = {}
        info['id'] = db_id
        info['title'] = db['Name']
        info['due_on'] = db['DueDate'][0:10]

        # Call API to get relevant submission info for our student
        submissions_url = "https://devcop.brightspace.com/d2l/api/le/1.51/7855/dropbox/folders/"+str(db_id)+"/submissions/"
        submissions = requests.request("GET", submissions_url, headers=headers, data={}).json()

        try:
            sbmsn = next(item for item in submissions if item['Entity']['EntityId'] == STUDENT_ID)
            info['num_of_submissions'] = len(sbmsn['Submissions'])
            info['latest_submission'] = sbmsn['CompletionDate'][0:10]
        except:
            info['num_of_submissions'] = 0
            info['latest_submission'] = None
        
        info['org_id'] = 7855

        response['Computer Basics'].append(info)

    # URL for dropboxes endpoint
    dropboxes_url = "https://devcop.brightspace.com/d2l/api/le/1.51/7032/dropbox/folders/"

    # Call API and serialize response into a dictionary (JSON)
    dropboxes = requests.request("GET", dropboxes_url, headers=headers, data={}).json()

    if len(dropboxes) == 0:
        return {}

    # Loop through dropboxes and construct response
    for db in dropboxes:
        db_id = db['Id']
        info = {}
        info['id'] = db_id
        info['title'] = db['Name']
        info['due_on'] = db['DueDate'][0:10]

        # Call API to get relevant submission info for our student
        submissions_url = "https://devcop.brightspace.com/d2l/api/le/1.51/7855/dropbox/folders/"+str(db_id)+"/submissions/"
        submissions = requests.request("GET", submissions_url, headers=headers, data={}).json()

        try:
            sbmsn = next(item for item in submissions if item['Entity']['EntityId'] == STUDENT_ID)
            info['num_of_submissions'] = len(sbmsn['Submissions'])
            info['latest_submission'] = sbmsn['CompletionDate'][0:10]
        except:
            info['num_of_submissions'] = 0
            info['latest_submission'] = None
        
        info['org_id'] = 7032

        response['Physics'].append(info)
    
    return jsonify(response)

@app.route('/quizzes')
def quizzes():
    # URL for quizzes endpoint
    quizzes_url = "https://devcop.brightspace.com/d2l/api/le/1.51/7855/quizzes/"

    # Call API and serialize response into a dictionary (JSON)
    quizzes = requests.request("GET", quizzes_url, headers=headers, data={}).json()
    quizlist = quizzes['Objects']
    
    if len(quizlist) == 0:
        return {}

    response = []

    # Loop through quizzes and construct response
    for quiz in quizlist:
        quiz_id = quiz['QuizId']
        info = {}
        info['id'] = quiz_id
        info['title'] = quiz['Name']
        info['start_date'] = None if quiz['StartDate'] == None else quiz['StartDate'][0:10]
        info['end_date'] = None if quiz['EndDate'] == None else quiz['EndDate'][0:10]
        info['due_date'] = None if quiz['DueDate'] == None else quiz['DueDate'][0:10]

        # Call API to get relevant attempt info for our student
        attempts_url = "https://devcop.brightspace.com/d2l/api/le/1.51/7855/quizzes/"+str(quiz_id)+"/attempts/"
        attempts_list = requests.request("GET", attempts_url, headers=headers, data={}).json()['Objects']
        user_attempts = [d for d in attempts_list if d['UserId'] == STUDENT_ID]  # filter attempts for our user

        info['num_of_attempts'] = len(user_attempts)
        grade = None
        for attempt in user_attempts:
            if grade == None:
                grade = attempt['Score']
            else:
                grade = max(grade, attempt['Score'])
        info['grade'] = grade

        response.append(info)
    
    return jsonify(response)

questions = ["How are you doing?", "How much time have you spent today exercising?", "When was the last time you drank water?", "Am I tired?"]

@app.route('/mentalHealth')
@cross_origin()
def mentalHealth():
  randomnum = random.randint(0,4)
  question = questions[randomnum]

  return jsonify({"question": question})
