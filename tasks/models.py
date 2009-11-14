from google.appengine.ext import db

class Task(db.Model):
	body = db.StringProperty(required=True)
	description = db.StringProperty(multiline=True)
	owner = db.UserProperty(auto_current_user_add=True)
	created = db.DateProperty(auto_now_add=True)
	modified = db.DateProperty(auto_now=True)

class Account(db.Model):
	user = db.UserProperty(auto_current_user_add=True, required=True)
	email = db.EmailProperty(required=True) # key == <email>
	twitter_username = db.StringProperty()
	
	# Updated by middleware.AddUserToRequestMiddleware
	current_user_account = None
	
	@classmethod
	def get_account_for_user(cls, user):
		email = user.email()
		assert email
		key = '<%s>' % email
		
		# Usually the account already exists
		account = cls.get_by_key_name(key)
		if account is not None:
			return account
		
		# Doesn't exist, create it
		return cls.get_or_insert(key, user=user, email=email)
