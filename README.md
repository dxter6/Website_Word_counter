### This is a python3 , Flask , Sqlalchemy , redis , rq  Based application


##### Introduction To [Website_Word_counter..!](https://github.com/shinu007/Website_Word_counter)


## Before stating the application install the requirements.txt

```pip3
    pip3 install  -r requirements.txt
```
## Linux  Needed Packages
```bash
 # apt-package manager
 $ sudo apt-get insall redis sqlite  
```
## To create database go to /Main 
```python3
    $python3
    >> from Main import db
    >> db.create_all()
```
## Points to  Note
```bash
    0.Change the Directory for the sqlite 
    1. Create Database before running the application
    2. Sign-up before Sign-in
    3. To Run the application Goto /Main/ and Run Main.py
    4. Login before you add the tasks
    5. Start the Redis server  and rq worker before adding the tasks
``` 
## To Start Web_application
```bash
    #Open in Seperate tabs
    user@user:~/Main$ redis-server 
    user@user:~/Main$ rq worker
    user@user:~/Main$ python3 Main.py 
```
## File Structure
![FileStructure](/images/Tree.png) <!--.element height="50%" width="50%"-->

## Index
![FileStructure](/images/index.png)

## Sign-up
![FileStructure](/images/sign-up.png)

## Login
![FileStructure](/images/login.png)

## Add Task
![FileStructure](/images/add-task.png)

## Dashboard
![FileStructure](/images/dashboard.png)

## Redis server
![FileStructure](/images/Redis-server.png)

## RQ worker

![FileStructure](/images/rq-worker.png)
