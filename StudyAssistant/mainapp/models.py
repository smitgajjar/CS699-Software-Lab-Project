'''
The classes defined in models.py are mapped to tables in actual database. For any table that has to be created in database,
the corresponding model class needs to be defined here. The fields of the table are defined as variables inside its class along with 
its type and attributes. 

'''

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """This class maps to the authentication table in the database and is extended by admin.py.
    
    It defines the authentication information of a registered user.
    All the custom fields that are required in authentication are defined here. 
    Currently has two custom fields (is_teacher and is_student ) both of boolean type
    which defines whether the user is a student or a teacher. Apart from the custom fields
    it also has other default Django authentication fields as it inherits the AbstractUser class.
    
    """
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class UserCourses(models.Model):
    """This class maps to the UserCourses table in the database. 
    
    It defines the user to courses mapping which is one to many.
    It has two fields namely username (type: char) and course (type: char).
    username defines the user name of the currently logged in user and 
    course defines the courses which are mapped to that user.
        
    """
    username = models.CharField(User, max_length=10)
    course = models.CharField(max_length=5)

class PrivateDeadlines(models.Model):
    """This class maps to the PrivateDeadlines table in the database. 
    
    It defines the personal deadlines of a user. It has following fields,namely:
    username defines the user name of the currently logged in user.
    course defines the course for which the deadline has been added.
    Event defines the event name of the deadline.
    Start_Date defines the Starting date of the deadline.
    Start_Time defines the Starting time of the deadline.
    End_Date defines the Ending date of the deadline.
    End_Time defines the Ending time of the deadline.
        
    """
    username = models.CharField(User, max_length=10) # hello there
    course = models.CharField(max_length=5)
    Event = models.TextField()
    Start_Date = models.DateField() 
    Start_Time = models.TimeField()
    End_Date= models.DateField()
    End_Time= models.TimeField()	

class PublicDeadlines(models.Model):
    """This class maps to the PublicDeadlines table in the database. 
    
    It defines the public deadlines of a course. These deadlines will be visible to all the 
    users that have taken that course. 
    It has following fields,namely:
    username defines the user name of the currently logged in user.
    course defines the course for which the deadline has been added.
    Event defines the event name of the deadline.
    Start_Date defines the Starting date of the deadline.
    Start_Time defines the Starting time of the deadline.
    End_Date defines the Ending date of the deadline.
    End_Time defines the Ending time of the deadline.
    
    """
    username = models.CharField(User, max_length=10)
    course = models.CharField(max_length=5)
    Event = models.TextField()
    Start_Date = models.DateField() 
    Start_Time = models.TimeField()
    End_Date= models.DateField()
    End_Time= models.TimeField()


class UserNotes(models.Model):
    """This class maps to the UserNotes table in the database. 
    
    It defines personal notes of a user. It has the following fields,namely:
    username defines the user name of the currently logged in user.
    course defines the course for which the note has been added.
    Title defines the Title of the note.
    Content defines the Content of the note.
    
    """
    username = models.CharField(User, max_length=10)
    course = models.CharField(max_length=5)
    Title = models.TextField()
    Content = models.TextField()

