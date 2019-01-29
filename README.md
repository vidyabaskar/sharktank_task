# Shark Tank

## Tools needed
  - phpmyadmin
  - PyCharm / VSCode / Linux Terminal(atleast)
  
## Installation Details
  
  - Open up mysql server in phpmyadmin and create a new database name "sharktank" or run the following query.
 ```
  CREATE DATABASE sharktank
  ```
  - Import the .sql file from the repo into the database.
  - Open up Python IDE and create a new virtualenvironment.
  - After activating the virtualenv for the project, run the following commands in the terminal.
  ```
  pip3 install Flask
  pip3 install flask-mysql
  pip3 install -U flask-cors
  ```
  - Run the code using `python3 app.py` 
##### Search Engine will be deployed in the localhost.
