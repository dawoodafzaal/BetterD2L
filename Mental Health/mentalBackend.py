from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
import random

app = Flask(__name__)
STUDENT_ID = 195
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjYzYzc5ZjIzLWZiMTAtNGI4YS1hMjdlLWI4YTc4NGJmNWI5MCJ9.eyJpc3MiOiJodHRwczovL2FwaS5icmlnaHRzcGFjZS5jb20vYXV0aCIsImF1ZCI6Imh0dHBzOi8vYXBpLmJyaWdodHNwYWNlLmNvbS9hdXRoL3Rva2VuIiwiZXhwIjoxNjEzMjU0MjM1LCJuYmYiOjE2MTMyNTA2MzUsInN1YiI6IjEyNTUiLCJ0ZW5hbnRpZCI6IjUyNzMxMzE3LTM3MmEtNGRiNC1iNDlkLTQ5NTAyY2U0M2YyYiIsImF6cCI6IjVkMjc0NTBmLTJjZTktNGRjZS05NTcwLTBiMjM0NTgwZGZkZCIsInNjb3BlIjoiY29udGVudDoqOiogY29yZToqOiogZGF0YWh1YjoqOiogZGlzY3Vzc2lvbnM6KjoqIGVucm9sbG1lbnQ6KjoqIGdyYWRlczoqOiogcXVpenppbmc6KjoqIHJlcG9ydGluZzoqOiogcm9sZToqOiogdXNlcnM6KjoqIiwianRpIjoiNGUyOTdkYTEtZDg4Ni00ODI3LTgyN2ItZmE4OGM0MWM5ZjExIn0.k4ndXz5MuMjwu20AXhb6kpOwfVy-iClslOsm7XglIrzO1TKBy1key-iO0MDOhNrAC5A4CpZyWUk3VtOLL8DAM-RGRSXYxEBXpJ8Hnbb2kgUVtBU9ZB7kagfulIRihH5lgEIX08smsokviWowZVT2pUNWxBFpIoJjCdIoXTJ5NAis0pVTPa0EzjELnNFuSuGk91X8Jpv5Gh7sFzDerm9rgjHCzi6it3hW--7Mxh4Rpge8dbEinbC3ugbj4YeCorkScTH65prXGyzbovX1cuNAqTyst0sRxNC7PG0F__d-OW7Q--SYckrYSdMkkg8Q19g2UpQI9pbzk23tGifeFGlHlQ',
  'Cookie': 'ADRUM=s=1613250634620&r=https%3A%2F%2Fdevcop.brightspace.com%2Fd2l%2FsystemCheck%2Fwidget%3F0; d2lSessionVal=TKH40vprvvlOxHs5ZGSliFnXb; d2lSecureSessionVal=Y2iwueXFvbe2Ygxmc183PA5zw'
}

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

questions = ["How are you doing?", "How much time have you spent today exercising?", "When was the last time you drank water?", "Am I tired?"]

@app.route('/mentalHealth')
@cross_origin()
def mentalHealth():
  randomnum = random.randint(0,4)
  question = questions[randomnum]

  return jsonify({"question": question})




if __name__ == '__main__':
    app.run()
        

    


