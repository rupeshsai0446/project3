#!/usr/bin/env python3

import psycopg2
import time

task_1 = 'What are the most popular three articles of all time?'
command_1 = """select title, count(*) as i
            from articles, log
            where log.status='200 OK'
            and articles.slug = substr(log.path, 10)
            group by title
            order by i desc
            limit 3;
            """

task_2 = 'Who are the most popular article authors of all time?'
command_2 = """
select authors.name, count(*) as views from articles inner join
authors on articles.author = authors.id inner join
log on concat('/article/', articles.slug) = log.path where
log.status like '%200%' group by authors.name order by views desc
"""

task_3 = 'On which days did more than 1% of requests lead to errors?'
command_3 = """
select * from (
    select a.day,
    round(cast((100*b.hits) as numeric) / cast(a.hits as numeric), 2)
    as errp from
        (select date(time) as day, count(*) as hits from log group by day) as a
        inner join
        (select date(time) as day, count(*) as hits from log where status
        like '%404%' group by day) as b
    on a.day = b.day)
as t where errp > 1.0;
"""


class Project:
    def __init__(self):
        try:
            self.database = psycopg2.connect('dbname=news')
            self.cursor = self.database.cursor()
        except Exception as e:
            print e

    def execute_command(self, command):
        self.cursor.execute(command)
        return self.cursor.fetchall()

    def solve(self, task, command, x='views'):
        command = command.replace('\n', ' ')
        data = self.execute_command(command)
        print task
        for a in range(len(data)):
            print'(', a + 1, ')', data[a][0], ':', data[a][1], x
        # blank line
        print ''

    def exit(self):
        self.database.close()


def required_data(psql_query):
    ''' Database is accessed and required data from database is returned'''
    conn = psycopg2.connect(dbname="news")
    cursor = conn.cursor()
    cursor.execute(psql_query)
    data = cursor.fetchall()
    conn.close()
    return data


def day_more_errors():
    day_more_errors = required_data(command_3)
    print("On which days did more than 1% of requests lead to errors?")
    for name, num in day_more_errors:
        print("""{0:%B %d,%Y} ->{1:.2f} errors""".format(name, num))

if __name__ == '__main__':
    rupesh = Project()
    rupesh.solve(task_1, command_1)
    rupesh.solve(task_2, command_2)
    day_more_errors()
    rupesh.exit()
