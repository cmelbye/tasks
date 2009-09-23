from google.appengine.ext import db

class Task(db.Model):
	body = db.StringProperty(required=True)
	description = db.StringProperty(multiline=True)
	owner = db.UserProperty(auto_current_user_add=True)
	created = db.DateProperty(auto_now_add=True)
	modified = db.DateProperty(auto_now=True)
