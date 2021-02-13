import requests
import d2lvalence.auth as d2lauth

app_creds = { 'app_id': '5d27450f-2ce9-4dce-9570-0b234580dfdd', 'app_key': 'p5UuMuS4RkftzYQf_caM0EZF3n8hH6OO3zYZxY35XXU' }

ac = d2lauth.fashion_app_context(app_id=app_creds['app_id'], app_key=app_creds['app_key'])

auth_url = ac.create_url_for_authentication('devcop.brightspace.com', 'http://localhost:3001')

print(auth_url)

redirect_url = 'https://localhost:3001/d2loauth2/fakeendpoint'

uc = ac.create_user_context(result_uri=redirect_url, host='devcop.brightspace.com', encrypt_requests=True)

route = '/d2l/api/versions/'

url = uc.create_authenticated_url(route)

r = requests.get(url)

print(r.text)