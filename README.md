Bulk Buy
=====================

Note: If you have django-user-account and pinax-theme-bootstrap, remove them using   

    sudo pip uninstall django-user-account && sudo pip uninstall pinax-theme-bootstrap
    
I have added them directly into our app for easier customization

Getting Started:

    cd Slice
    sudo pip install -r requirements.txt

Setup database:    
1 - Install this backend binding
[postgresql_psycopg2](http://initd.org/psycopg/)    
2 - go to terminal/command line   
  
    psql -d template1

3 - type in    

    CREATE DATABASE bulkbuy;    
    CREATE USER bulkbuy WITH PASSWORD 'elec3609';    
    GRANT ALL PRIVILEGES ON DATABASE bulkbuy TO bulkbuy;    
    \q    

4 - go to Slice/ directory    

    python manage.py syncdb    

5 - when it asks to create superuser, just type create one    

6 - go to Slice/ directory    

    python manage.py loaddata deal_category  
    python manage.py loaddata initial_data
 

This step loads my pre-defined data for deal_category from
deal/fixture/deal_category.yaml    
*Note*: If it throws a `no module name yaml` error,  

    sudo pip install yaml    

or If you're on OSX Mavericks

    sudo pip install pyyaml    


#Others
1 - If you see this screen, it would be because of the database configuration for Heroku.
![Screen Shot 2014-11-01 at 1.29.03 pm.png](https://bitbucket.org/repo/XGAX6y/images/2892636378-Screen%20Shot%202014-11-01%20at%201.29.03%20pm.png)

Please go to `Slice/settings.py` and remove the following 2 lines.
![Screen Shot 2014-11-01 at 1.30.23 pm.png](https://bitbucket.org/repo/XGAX6y/images/3852973062-Screen%20Shot%202014-11-01%20at%201.30.23%20pm.png)

2 - Make sure you have **Postgres** running on port 5432

3 - Because we don't have an e-mail server, once you signed up, go to the Terminal,  copy and paste the confirmation link to your browser
![Screen Shot 2014-11-01 at 1.32.49 pm.png](https://bitbucket.org/repo/XGAX6y/images/3609837378-Screen%20Shot%202014-11-01%20at%201.32.49%20pm.png)


HTML Locations
===============
**Note: All directories are under Slice/**

#####Index page.    
The body of the index is located in 
/Slice/templates/homepage.html

#####Footer
/Slice/templates/_footer.html

#####Navgivation bar
This part is specifically for the RIGHT side of the Bootstrap navbar    
/Slice/templates/_account_bar.html


Quick Django 101
===============
####Basic Terms
- A Project = Our website
- App = a specific function of the website that can be re-used.
  - e.g Account (provided by pinax)
  - Deals    

####Quick rundown   
- Our project name is called `Slice`   
- Inside our project, there's a dir called `Slice`   
  - Everything inside this inner *Slice* directory manages everything. 
  - Think of it as the "core" of our website
  - Glues everything (templates, apps) together    
  - The only part of the website that should not be re-usable   
  - Has `settings.py`, `urls.py`, templates/, static/

urls.py
=======
- Takes the input URL and map it to a view (html file)  
- Maps url using regex.  

templates/    
==========
- Where we put all our HTML files. 

####Basic Commands    
New project:   `django-admin startproject <project name>`    
New app:    `dango-admin startapp <app name>`    
Run the server:   `python manage.py runserver`    
Database synchronization:     `python manage.py syncdb`     

#Git Basic    
=======
####Branches     
To create a new branch     

      git checkout -b <new-branch-name>   

To switch to another branch    

      git checkout <branch-name>    

To push to your branch     

     git push origin <branch-name>    

To update your branch to align with master    

    git pull origin master