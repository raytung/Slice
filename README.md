Bulk Buy
=====================


Getting Started:

    cd Slice
    pip install -r requirements.txt
    python manage.py runserver

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

This step loads my pre-defined data for deal_category from
deal/fixture/deal_category.yaml    
*Note*: If it throws a `no module name yaml` error,  

    sudo pip install yaml    

or If you're on OSX Mavericks

    sudo pip install pyyaml    



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
