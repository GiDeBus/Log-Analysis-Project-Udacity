#Udacity - News Log Analysis Project

###Project Overview
You have been asked to build an internal reporting tool that will communicate with a local database and assist answering queries otherwise would have taken longer to perform.

####Installation Requirements
 * [Python 2](https://www.python.org/downloads/release/python-2715/)
    - psycopg2 library from within Python
 * [Vagrant](https://www.vagrantup.com/)
 * [VirtualBox](https://www.virtualbox.org/)
 * ['News' Database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

1. Once all software have been installed, launch your favorite terminal (for Windows you might need to download [gitbash](https://git-scm.com/downloads) for Mac you can use your terminal)

2. With your terminal open 'cd' to the folder where the News Database is located. Once there run the command 'vagrant up' to initialize the virtual machine.

3. Log into your virtual machine with 'vagrant ssh' after the initialization is complete.

4. Once inside the virtual machine move to the shared directory between your virtual machine and your local PC with the command 'cd /vagrant'. Note that without the backlash the terminal might not recognize it, and give an error. You should know you are in the right folder if you run 'ls' and you are able to see the News Database File.

5. Run the commands 'psql -d news -f newsdata.sql'. From here on, you can only use the command 'psql -d news' to reconnect to the News Database File if you ever close the connection.

#####Views Required For This Project

Once in the `news` database and within your virtual machine, ensure to create the following views to obtain the right information required to answer each query for this project:

**View For Top Three Articles**

`CREATE VIEW article_popularity AS SELECT title, author, count(*) AS times_accessed FROM articles, log WHERE log.path LIKE concat('%', articles.slug) GROUP BY articles.title, articles.author ORDER BY times_accessed DESC;`

**Column** | **Type**
--- | ---
title | text
author | text
times_accessed | integer

**View For Most Popular Authors**

`CREATE VIEW authors_popularity AS SELECT authors.name, authors.id, sum(article_popularity.times_accessed) AS total_author_popularity FROM authors, article_popularity WHERE authors.id = article_popularity.author GROUP BY authors.id ORDER BY total_author_popularity DESC;`

**Column** | **Type**
--- | ---
name | text
author ID | text
total_author_popularity | integer

**View For Days Where Request Errors Were Higher Than 1%**

`CREATE VIEW errors_view AS SELECT date(time),round(100.0*sum(CASE log.status WHEN '404 NOT FOUND' THEN 1 ELSE 0 END)/count(log.status),1) AS "percent_error" FROM log GROUP BY date(time) ORDER BY "percent_error" DESC;`

**Column** | **Type**
--- | ---
date | date
percent_error | integer

######How to Run the Code?

Once you are logged into vagrant, and you are located inside the virtual machine shared directory run the following code:
(_hint: if you run the command 'ls' on your terminal you should see a file named 'log_analysis_project_code.py', if so, you are in the right directory.

`python log_analysis_project_code.py`
