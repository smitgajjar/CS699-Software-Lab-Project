# Study Assistant App
### Group Name: TSS


### Problem Statement :
- To develop a webapp to track various academic aspect for a user ( students and teachers ) like managing deadlines, making study notes and other important things in one place.

### Sell your product :
- A centralised place for managing all your deadlines and notes. 

### List of features :

- Adding Deadlines 
- Viewing Deadlines  
- Deleting Deadlines 
- Importing Deadlines by students 
- Exporting Deadlines by teachers 
- Filter Deadlines by subject 
- Sort Deadlines by any field
- Adding Notes 
- Viewing Notes 
- Editing Notes
- Deleting Notes 
- Filtering Notes by subject  
- Sorting Notes by any field

### Technology Stack :

#### Learnt in class : 
- **HTML**
- **CSS**  
- **Javascript** 
- **Bootstrap**
- **Python** 
- **Sphinx**

#### Others :
- Django
- Postgresql



### List of deliverables :
- [x] Creating an authentication system and supporting multiple users.  
- [x] Ability to add, view and delete deadlines by a user.
- [x] Ability to export deadlines.
- [x] Ability to import deadlines.
- [x] Ability to create subject wise notes for a user.

### Hardware/Software Requirements :

#### Hardware Requirements : 
- Any system that supports browsers.

#### Software requirements ; 
- Latest browser that supports HTML5.

### How to operate and run this project on your machine :
- Prerequistes:
	- Postgresql
	- Django
	- virtualenv
	- pip

#### Steps:
1. Install all the above mentioned prerequisites
2. Create a virtual environment and install python requirements from requirements.txt
3. Now, create a psql database and a root user having all privileges of the database created
4. Update the credentials in StudyAssistant/settings.py
5. Run `python manage.py makemigrations` to make migrations in the migrations directory
6. Run `python manage.py migrate` to make model migrations in the actual database
7. Now, run `python manage.py runserver` and launch localhost
8. Create some users of teacher type and students type from django admin localhost:8000/admin
9. Give some courses to each user in the UserCourses table
10. There you go! Run the server and our project is up and running in your machine.

### Primary stakeholders of the product :
- Students and Teachers 

### Team details along with the contribution :
#### Group Members:
- Tanmay Joshi (213050018) (Overview of contribution : Front end of notes module , made backend logic for add and view feature in notes. )
- Siddhant Singh (213050031) (Overview of contribution : Front end of authentication module , made backend logic for adding , viewing public deadlines and deleting notes. ) 
- Smit Gajjar (213050051) (Overview of contribution : Front end of Deadline module , made backend logic for adding , viewing private deadlines and deleting deadlines. )

- __Everybody contributed equally in every module and helped the other whenever they were stuck in their part. Also everybody made improvements in any feature wherever possible.__ 

### Path to Code Documentation (index.html) : 
- [StudyAssistant/docs/_build/html/index.html](StudyAssistant/docs/_build/html/index.html)

