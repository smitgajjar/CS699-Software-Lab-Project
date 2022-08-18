'''
Contains view functions of the mainapp app of StudyAssistant project

Templates of the front end will be rendered after calling corresponding
view functions specified in urls.py and defined here and passing context
dictionaries along with the same.
'''
from django.shortcuts import render
from .models import (PrivateDeadlines, UserCourses,
	PublicDeadlines, UserNotes)

# Create your views here.


def get_courses_list(request):
	'''Returns list of dictionaries containing courses taken by a user specified by
	request object username

	Each Dictionary entry has column names as keys and corresponding tuples
	as values. UserCourse model has username and courses. So, the username derived
	from the request object is taken and corresponding courses from the UserCourse
	model is returned as a list of dictionaries. Note that it is a utility function
	to be called from view functions.

	Parameters
	----------
	request : HttpRequest Object

	Returns
	-------
	courses_list : list of dictionaries of courses QuerySet
	'''
	dbObj = UserCourses.objects.all()
	courses_list = []
	for row in dbObj.iterator():
		if str(row.username) == str(request.user.username):
			courses_list.append(str(row.course))
	return courses_list

def get_deadlines_list(request):
	'''Returns list of dictionaries containing deadlines of a user specified by
	request object username

	Each Dictionary entry has column names as keys and corresponding tuples
	as values. There are two types of deadlines including private as well as public
	deadlines and corresponding models in the database are PrivateDeadlines and
	PublicDeadlines. PrivateDeadlines contain the personalized deadlines of student
	user and  PublicDeadlines contain the deadlines given by the teacher of the
	courses taken by the student user. Both type of deadlines are returned as a list
	of dictionaries by this function. Note that it is a utility function to be
	called from view functions.

	Parameters
	----------
	request : HttpRequest Object

	Returns
	-------
	deadline_list : list of dictionaries of deadline QuerySet
	'''

	try:
		selected_course = request.POST['dropdown']
	except:
		selected_course = 'all'
	dbObj = PrivateDeadlines.objects.all()
	publicDbObj = PublicDeadlines.objects.all()
	deadline_list = []
	courses_list = get_courses_list(request)

	for row in publicDbObj.iterator():
		if str(row.course) in courses_list:
			if str(selected_course)=="all":
				deadline_list.append(row)
			elif str(row.course) == str(selected_course):
				deadline_list.append(row)

	for row in dbObj.iterator():
		if str(selected_course)=="all" and str(row.username) == str(request.user.username):
			deadline_list.append(row)
		if str(row.username) == str(request.user.username) and str(row.course) == str(selected_course):
			deadline_list.append(row)
	return deadline_list

def get_notes_list(request):
	'''Returns list of dictionaries containing notes of a user specified by
	request object username
	
	Each Dictionary entry has column names as keys and corresponding tuples
	as values. UserNotes model has username, course name, note title and
	note content fields. So, the username derived from the request object
	is used to determine the corresponding tuple and used to fetch the note
	title as well as note content subjectwise. Consequently, these are
	returned by this function as a list of dictionaries. It is a utility
	function to be called from view functions.

	Parameters
	----------
	request : HttpRequest Object

	Returns
	-------
	response : HttpResponse Object
	'''

	try:
		selected_course = request.POST['dropdown']
	except:
		selected_course = 'all'
	dbObj = UserNotes.objects.all()
	notes_list = []

	for row in dbObj.iterator():
		if str(selected_course)=="all" and str(row.username) == str(request.user.username):
			notes_list.append(row)
		if str(row.username) == str(request.user.username) and str(row.course) == str(selected_course):
			notes_list.append(row)
	return notes_list

def home(request):
	'''View function for the home(/) page of project

	Takes request object and calls get_courses_list() utility function
	to get the list of dictionaries containing the tuples of database
	table UserCourses and passes it as an argument to the render function
	specifying the context dictionary to be used in the corresponding
	home.html page.

	Parameters
	----------
	request : HttpRequest Object

	Returns
	-------
	response : HttpResponse Object
	'''
	courses_dict = {'courses': get_courses_list(request)}
	return render(request,'home.html', courses_dict)

def deadline(request):
	'''View function for the /deadline page of project

	Takes request object and calls get_courses_list() utility function
	to get the list of dictionaries containing the tuples of database
	table UserCourses, calls get_deadlines_list() utility function to
	get the list of dictionaries containing the tuples of PrivateDeadlines
	as well as PublicDeadlines tables of database and consequently, 
	passes it as an argument to the render function specifying the
	context dictionary deadline_dict to be used in the corresponding
	deadline.html page.

	Parameters
	----------
	request : HttpRequest Object

	Returns
	-------
	response : HttpResponse Object
	'''
	deadline_dict = {'deadlines': get_deadlines_list(request),
	'courses': get_courses_list(request)}
	return render(request, 'deadline.html',deadline_dict)

def notes(request):
	'''View function for the /notes page of project

	Takes request object and calls get_courses_list() utility function
	to get the list of dictionaries containing the tuples of database
	table UserCourses, calls get_notes_list() utility function to
	get the list of dictionaries containing the tuples of UserNotes
	table of database and consequently, 
	passes it as an argument to the render function specifying the
	context dictionary notes_dict to be used in the corresponding
	notes.html page.

	Parameters
	----------
	request : HttpRequest Object

	Returns
	-------
	response : HttpResponse Object
	'''
	notes_dict = {'notes': get_notes_list(request),
	'courses': get_courses_list(request)}
	return render(request, 'notes.html', notes_dict)

def add_deadline(request):
	'''View function for the /add_deadline page of project

	Takes request object and calls get_courses_list() utility function
	to get the list of dictionaries containing the tuples of database
	table UserCourses and passes it as an argument to the render function
	specifying the context dictionary to be used in the corresponding
	add_deadline.html page.

	Parameters
	----------
	request : HttpRequest Object

	Returns
	-------
	response : HttpResponse Object
	'''
	courses_dict = {'courses': get_courses_list(request)}
	return render(request, 'add_deadline.html', courses_dict)

def add_note(request):
	'''View function for the /add_note page of project

	Takes request object and calls get_courses_list() utility function
	to get the list of dictionaries containing the tuples of database
	table UserCourses and passes it as an argument to the render function
	specifying the context dictionary courses_dict to be used in the
	corresponding add_note.html page.

	Parameters
	----------
	request : HttpRequest Object

	Returns
	-------
	response : HttpResponse Object
	'''
	courses_dict = {'courses': get_courses_list(request)}
	return render(request, 'add_note.html', courses_dict)

def put_deadline(request):
	'''View function for the /put_deadline of project

	Takes request object and adds a deadline entry to the database.
	The request object user can be a teacher or a student user. If the
	request object user is a student, the PrivateDeadlines table of
	the database will get updated using this view function. Otherwise,
	i.e if it is a teacher user, PrivateDeadlines table of the database
	will get updated. Once the entry is made in the respective tables,
	request will redirect to /deadline page.

	Parameters
	----------
	request : HttpRequest Object

	Returns
	-------
	response : HttpResponse Object
	'''
	pd = None
	if request.user.is_student:
		pd = PrivateDeadlines()
	else:
		pd = PublicDeadlines()
	pd.username = request.user.username
	pd.course = request.POST['dropdown']
	pd.Event = request.POST['EventName']
	pd.Start_Date = request.POST['StartDate']
	pd.Start_Time = request.POST['StartTime']
	pd.End_Date= request.POST['EndDate']
	pd.End_Time= request.POST['EndTime']
	pd.save()
	return deadline(request)

def put_note(request):
	'''View function for the /put_note of project

	Takes request object and adds a note entry to the database.
	The request object user can be a student user only. After this
	function is called, UserNotes table  of the database will get
	updated. Once the entry is made in the respective table,
	request will redirect to /notes page.

	Parameters
	----------
	request : HttpRequest Object

	Returns
	-------
	response : HttpResponse Object
	'''
	pd = UserNotes()
	pd.username = request.user.username
	try:
		pd.course = request.POST['dropdown']
	except:
		pd.course = request.POST['course']
	pd.Title = request.POST['Title']
	pd.Content = request.POST['Content']
	try:
		UserNotes.objects.filter(id=request.POST['id']).delete()
	except:
		pass
	pd.save()
	return notes(request)

def delete_deadline(request):
	'''View function for the /delete_deadline of project

	Takes request object and deletes a deadline entry from the database.
	The request object user can be a teacher or a student user. If the
	request object user is a student, the PrivateDeadlines table of
	the database will get updated using this view function. Otherwise,
	i.e if it is a teacher user, PrivateDeadlines table of the database
	will get updated. Once the entry is made in the respective tables,
	request will redirect to /deadline page.  The row selected by the
	checkbox in the front end is taken by the POST request to delete
	the corresponding entry.

	Parameters
	----------
	request : HttpRequest Object

	Returns
	-------
	response : HttpResponse Object
	'''
	pd = None
	if 'share_button' in request.POST:
		return share_deadline(request)
	elif request.user.is_student:
		idx_list = request.POST.getlist('selected_row')
		for idx in idx_list:
			PrivateDeadlines.objects.filter(id=idx).delete()
	else:
		idx_list = request.POST.getlist('selected_row')
		for idx in idx_list:
			PublicDeadlines.objects.filter(id=idx).delete()
	return deadline(request)

def delete_note(request):
	'''View function for the /delete_note of project

	Takes request object and deletes a note entry from the database.
	The request object user can be a student user only. After this
	function is called, UserNotes table  of the database will get
	updated. Once the entry is made in the respective table,
	request will redirect to /notes page. The row selected by the
	checkbox in the front end is taken by the POST request to delete
	the corresponding entry.

	Parameters
	----------
	request : HttpRequest Object

	Returns
	-------
	response : HttpResponse Object
	'''
	idx_list = request.POST.getlist('selected_row')
	for idx in idx_list:
		UserNotes.objects.filter(id=idx).delete()
	return notes(request)

def view_note(request):
	'''View function for the /view_note of project

	Takes request object and returns a note entry from the database
	to the html page to view the corresponding note selected by the
	frontend. The request object user can be a student user only.
	First, the button of a row in the front end is clicked to trigger
	a POST request to this view function. Now, the row which was
	selected to be viewed is returned by this function it as an
	argument to the render function specifying the context dictionary
	notes_dict to be used in the view_note.html page.

	Parameters
	----------
	request : HttpRequest Object

	Returns
	-------
	response : HttpResponse Object
	'''
	row = None
	notes_dict={}
	idx = request.POST['current_row']
	row=UserNotes.objects.filter(id=idx)
	for row1 in row:
		notes_dict={'viewed_content':row1.Content,'viewed_title':row1.Title,
		'viewed_course':row1.course, 'viewed_id': row1.id}
	return render(request, 'view_note.html',notes_dict)

def share_deadline(request):
	'''Utility function for sharing deadline

	Parameters
	----------
	request : HttpRequest Object

	Returns
	-------
	deadline_list : HttpResponse Object
	'''
	idx_list = request.POST.getlist('selected_row')
	for idx in idx_list:	
		friend_username = request.POST['friend_username']
		pd = PrivateDeadlines()
		row = next(PrivateDeadlines.objects.filter(id=idx).iterator())
		pd.username = friend_username
		pd.course = row.course
		pd.Event = row.Event
		pd.Start_Date = row.Start_Date
		pd.Start_Time = row.Start_Time
		pd.End_Date= row.End_Date
		pd.End_Time= row.End_Time

		canSave = False
		dbObj = UserCourses.objects.all()
		for r in dbObj.iterator():
			if str(r.username) == str(friend_username) and str(r.course) == str(pd.course):
				canSave = True
		if friend_username == request.user.username:
			canSave = False
		if canSave:
			pd.save()
		else:
			del pd
	return deadline(request)