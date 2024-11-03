
# Log Analysis Project
This project aims to stretch the SQL database skills. Practicing interacting with a live database both from the command line and from code.

## Table of Content
The following files can be found in the project.

* README.md
* log_analysis.py
* output.txt

## Description
* log_analysis.py contains 
* output.txt 

## Requirements
 - Python 2 or 3
 Python can be downloaded from [here](https://www.python.org/downloads/)
 
 - Vagrant
    Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from [vagrantup.com](https://www.vagrantup.com/downloads.html). Install the version for your operating system.
    
 - VirtualBox
    VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org, [here](https://www.virtualbox.org/wiki/Downloads). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

- Download the VM configuration
    There are a couple of different ways you can download the VM configuration.You can download and unzip this file: FSND-Virtual-Machine.zip This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.
    
    Alternately, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.
    
    Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory

-   From your terminal, inside the vagrant subdirectory, run the command
    vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.
    
-   When vagrant up is finished running, you will get your shell prompt back.
    At this point, you can run vagrant ssh to log in to your newly installed Linux VM!
    
## Download the data
-   Next, download the data here. You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

    To load the data, use the command psql -d news -f newsdata.sql. Here's what this command does:

    psql — the PostgreSQL command line program
    -d news — connect to the database named news which has been set up for you
    -f newsdata.sql — run the SQL statements in the file newsdata.sql
    Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.
    
## Running the project
* Run the command python log_analysis.py from command line like this.
vagrant@vagrant:/vagrant/log$ python log_analysis.py;

## Views created
* view regarding question 1
    - create view popular_articles as select regexp_replace(path, '.+[/\\]', '','g') as 
    new_path, count(*) as views from log where path != '/' group by path order by views         desc;
* View regarding question 2
    -   create view popular_authors as select author, title, views as total_views from     
    articles inner join popular_articles on articles.slug = popular_articles.new_path;
* View regarding Question 3
    - create view numerator as select time::date as time , count(*) from log group by     
        time::date;
    - create view denominator as select time::date as time , count(*) from log where status         like '4%' group by time::date order by time;
    -   create view errors as select time, error_percentages from (select numerator.time,           ((cast(numerator.nume as float) / denominator.deno )* 100) as error_percentages from         numerator inner join denominator on numerator.time = denominator.time) as foo;


## Lincense
MIT License

Copyright (c)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
