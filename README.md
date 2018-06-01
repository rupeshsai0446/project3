# Project-3
Building an informative summary from logs by using psql database queries. We can interact with given database file using both python3 and terminal window.
## Technologies used:
1. PostgreSQL
2. Python DB-API
3. Linux-based virtual machine (VM) Vagrant

## Project Requirements:
Reporting tool should answer the following questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## System setup and how to view this project
This project makes use of  Linux-based virtual machine (VM) configuration which includes all of the necessary software to run the application.
1. Download [Vagrant](https://www.vagrantup.com/) and install.
2. Download [Virtual Box](https://www.virtualbox.org/) and install. 
3. Clone this repository to a directory of your choice.
4. Download the **newsdata.sql** which is downloaded in the form of zip files and extract them to your **vagrant** directory and **newsdata.py** files from the respository and move them to your **vagrant** directory within your VM.

#### Run these commands from the terminal in the folder where your vagrant is installed in: 
1. ```vagrant up``` to start up the VM.
2. ```vagrant ssh``` to log into the VM.
3. ```cd /vagrant``` to change to your vagrant directory.
4. ```psql -d news -f newsdata.sql``` to load the data and create the tables.
5. ```python3 newsdata.py``` to run the reporting tool.

