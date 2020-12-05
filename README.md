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
 For Linux:  
 ```export FLASK_APP=run.py```  
 ```export FLASK_CONFIG=*config*```
 
  Replace the \*config* with one of the values: *development*,
 *production*, *testing*
 