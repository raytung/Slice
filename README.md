Slice of Pie - A Bulkbuy Website designed for students
=====================
Slice of Pie is a group buy website that aims to provide cheap deals for and by students. 



### Setup

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
