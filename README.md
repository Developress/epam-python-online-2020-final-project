# Department app
This is a web application for managing departments and
employees. It uses a RESTful web service to perform crud 
operations. The app allows you to:  
- display a list of departments and the average salary
calculated automatically for these departments  
- display a list of employees in the departments 
with an indication of the salary for each employee 
and a search field to search for employees born on a
 certain date or in the period between dates
 - create, update and delete the departments and the
 employees
 
 ## How to build
 #### Clone the repo  
 ```git@gitlab.com:developress/epam-python-online-2020-final-project.git```
   
 #### Install all the dependencies
 ```pip install -r requirements.txt```
 
 #### Set up the database
 MySql must be installed. Go to the mysql console,
  login as root and create a new user:  
 ```CREATE USER *user* IDENTIFIED BY *password*```  
 Create a database for the app:  
 ```CREATE DATABASE IF NOT EXISTS department_app_db```  
 Grant all the privileges on the created database to the user:  
 ```GRANT ALL PRIVILEGES ON department_app_db . * TO '*user*'@'localhost'```  
 Replace the \*user* and the \*password* with your own values
 
 #### Set the environmental variables
 For Windows:  
```set FLASK_APP=run.py```  
```set FLASK_CONFIG=*config*```   
```set SECRET_KEY=*secret_key*```  
```set DB_URL=mysql+mysqlconnector://*user*:*password*@localhost/department_app_db```  
 For Linux:  
```export FLASK_APP=run.py```  
```export FLASK_CONFIG=*config*```
```export SECRET_KEY=*secret_key*```  
```export DB_URL=mysql+mysqlconnector://*user*:*password*@localhost/department_app_db``` 
 
Replace the \*config* with one of the values: *development*,
 *production*, *testing*

Replace the \*key*, \*user* and the \*password* with your own values
 
 #### Run the migration scripts to create database schema
 Run the following commands:  
 ```flask db migrate```  
 ```flask db upgrade```
 
 If you encounter some problems, remove the migration folder
 from project root and run the following commands:  
 ```flask db init```  
 ```flask db migrate```  
 ```flask db upgrade```
 
 ### Everything is ready! Run the app
 To launch the app just run:  
 ```flask run```
 
 ## If you see this page, everything has been installed successfully 
 ![1](documentation/img/homepage.png)
 
 ## What you can do
 ### Here is the list of available addresses of web service:
 
 #### Departments api:
 - GET /api/departments - return all departments in json format
 - POST /api/departments - add a new department to the database (post request must be followed
 with json with the fields to add). Example:  
 ```json
{
"name": "HR",
"description": "Information Technologies"
}
```
- GET /api/departments/*id* - return the department with the given id 
in json format
- PUT /api/departments/*id* - updates the department with the given id
with the values, provided in json format. Example:  
 ```json
{
"name": "HR"
}
```
- DELETE /api/departments/*id* - deletes the department with the given id  
   
   #### Employees api
 - GET /api/employees - return all employees in json format
 - POST /api/employees - add a new employee to the database (post request must be followed
 with json with the fields to add). Example:  
 ```json
{
"name": "Tom",
"surname": "Black",
"salary": 500,
"date_of_birth": "03/12/1998"
}
```
Date must be in 'mm/dd/yyyy' format

- GET /api/employees/*id* - return the employee with the given id 
in json format
- PUT /api/employees/*id* - updates the employee with the given id
with the values, provided in json format. Example:  
 ```json
{
"salary": 900
}
```
- DELETE /api/employees/*id* - deletes the employee with the given id  
- GET /api/employees?date='*date*' - searches employees born on a specific date (replace the *date* with some value)
and returns them in json format
- GET /api/employees?start_date='*start_date*'&end_date='*end_date*' - 
  search employees born on a specific date range
   (replace the *start_date* and *end_date* with some value) and returns
   them in json format
   
 #### Here is the list of available addresses of web application:
 
 - /departments - display all the departments
 - /departments/add - add a new department
 - /departments/edit/*id* - edit a department with a specified id (replace the *id* with some value)
 - /departments/delete/*id* - delete a department with a specified id (replace the *id* with some value)
   
   
 - /employees - display all the employees
 - /employees/add - add a new employee
 - /employees/edit/*id* - edit an employee with a specified id (replace the *id* with some value)
 - /employees/delete/*id* - delete an employee with a specified id (replace the *id* with some value)
 - /employees?date='*date*' - search employees born on a specific date (replace the *date* with some value)
  - /employees?start_date='*start_date*'&end_date='*end_date*' - 
  search employees born on a specific date range
   (replace the *start_date* and *end_date* with some value)
   
  For more details read the [specification](documentation/SRS.md)