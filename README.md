Bulk Buy
=====================


Getting Started:

    cd bulkbuy
    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py runserver

Setup database:    
1 - Install this backend binding
[postgresql_psycopg2](http://initd.org/psycopg/)    
2 - go to terminal/command line   
  
    psql -d template1

3 - type in    

    CREATE DATABASE bulkbuy;    
    CREATE USER bulkbuy_admin WITH PASSWORD 'elec3609';    
    GRANT ALL PRIVILEGES ON DATABASE bulkbuy TO bulkbuy_admin;    
    \q    

4 - go to bulkbuy/ directory    

    python manage.py syncdb    

5 - when it asks to create superuser, just type no    


File Locations
===============
**Note: All directories are under Slice/**

#####Index page.    
The body of the index is located in 
/Slice/templates/homepage.html
