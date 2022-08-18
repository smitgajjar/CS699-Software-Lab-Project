from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):

    ''' Extends default authentication model of Django (UserAdmin) and adds custom fields to it which have been defined in User 
    class in Models.py. So adding or removing custom fields from authentication table can be done by defining them in User class in 
    Models.py. Two fields namely is_teacher and is_student have been definded in User class to be added to authentication 
    system in order to differentiate wether the user is a teacher or a student.  
            
    This class contains 3 tuples namely list_display , field_sets and add_fieldsets.

    list_display defines the field (both custom and default) that should be visible in admin dashboard of django. 'Email' field has
    been removed from admin view and both the custom fields (is_teacher and is_student) have been added.  

    fieldsets defines the field that would be present in the user authentication table in database. 'Email' has been removed and 
    'is_teacher' and 'is_student' have been added under Additional info key.

    add_fieldsets defines the fields that have to be filled while adding users in admin dashboard. 'Email' has been removed and both custom
    fields ('is_student' and 'is_teacher') have been added. 

    Fields in both fieldsets and add_fieldsets have been divided amonng various keys depending on type of information they provide. 
    'fields' key contains the field important for authentication (eg username and password).
    'Personal info' key contains the field having basic information about the user (eg. name and Email).
    'Permission' key contains the field which defines the level of access and persmission the user has. 
    'Important dates' key contains date related fields about the user. (eg last login and date joined).
    'Additional info' key contains the extra imformation required about the user not provided by default django authentication system. All the custom defined fields will go here.  

    '''

    list_display = (
        'username', 'first_name', 'last_name', 'is_staff',
        'is_teacher', 'is_student'
        )
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('is_student', 'is_teacher')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('is_student', 'is_teacher')
        })
    )

admin.site.register(User, CustomUserAdmin) #CustomUserAdmin model registered with Django 