#!/usr/bin/env python

import psycopg2


def run_query(query):

    conn = psycopg2.connect(database="news")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()conn.close()
return result


def print_query(question, results, suffix):
    nquery = 1
    print '\n' + '\n' + question + '\n'
    for result in results:
        print str(nquery) + '\t' + str(result[0]) \
            + ' -> ' + str(result[1]) + suffix
        nquery = nquery+1


query1 = "select title,times_accessed from article_popularity limit 3"
query2 = "select authors_popularity.name,
total_author_popularity from authors_popularity"
query3 = "select * from errors_view where percent_error > 1"


query_result1 = run_query(query1)
query_result2 = run_query(query2)
query_result3 = run_query(query3)

print_query(
    'Which articles have been accessed the most?', query_result1, ' views')
print_query(
    'Which are the most popular authors of all time?', query_result2, ' views')
print_query(
    'On which days did more than 1% of requests lead to errors?',
    query_result3, '%')
