#

from mongoengine import *
  
import datetime

class Page(Document):  
    title = StringField(max_length=200, required=True)  
    date_modified = DateTimeField(default=datetime.datetime.now())

class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)
    
    
    
    
