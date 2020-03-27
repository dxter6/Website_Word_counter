### This is a python3 , Flask , Sqlalchemy , redis , rq  Based application


##### Introduction To [Website_Word_counter..!](https://github.com/shinu007/Website_Word_counter)


## Linux  Needed Packages
```bash
 # apt-package manager
 $ sudo apt-get insall redis sqlite  
```
## To Setup and Run
```bash
    ./setup.sh
    ./start.sh
```
## Points to  Note
```bash 
    0. Start the Redis server and rq 
    1. Run setup.sh before Starting the application
    2. Sign-up before Sign-in
    3. Login before you add the tasks
    
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
