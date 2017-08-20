# Python --version 3.5.2
import psycopg2
DBNAME = "news"


def execute_function(query):

    """" Connects to database and execute query"""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        results = c.fetchall()
        db.close()
        return results
    except:
        print("Database connection failed. Please try again!!!")

# Question 1:


def most_popular_three_articles():

    """Return All the most popular article authors of all time."""
    query = '''select title, views as total_views from
               articles inner join popular_articles on
               articles.slug = popular_articles.new_path
               limit 3;'''
    most_popular_three_articles_query = execute_function(query)
    print('\nThe most popular three articles of all time are: \n')
    for article in most_popular_three_articles_query:
        print('\t' + str(article[0]) + ' ---- ' + str(article[1]) + ' views')

# Question 2:


def most_popular_article_authors():

    """Return All the most popular three articles of all time."""
    query = '''select name, sum(total_views) from authors inner join popular_authors on authors.id = popular_authors.author group by authors.id'''
    most_popular_article_authors_query = execute_function(query)
    print('\nThe most popular article authors of all time: \n')
    for article in most_popular_article_authors_query:
        print('\t' + str(article[0]) + ' ---- ' + str(article[1]) + ' views')

# Question 3:


def percentage_error_requests():

    """Return All the days that more than 1% of requests lead to errors."""
    query = '''select to_char(time, 'dd Month YYYY') as date, round(cast(error_percentages as numeric), 2) from (select * from errors where error_percentages = (select max(error_percentages) from errors)) as foo;'''
    percentage_error_requests_query = execute_function(query)
    print('\nDay(s) on which more than 1% of requests lead to errors: \n')
    for article in percentage_error_requests_query:
        print('\t' + str(article[0]) + ' ---- ' + str(article[1]) + ' % errors')

def print_seperator():

    """Prints an equal to sign as a seperator. For easy to ready the output"""
    print('\n' + "=" * 80 + '\n')

if __name__ == '__main__':
    """Executes all the code found here"""
    print_seperator()
    most_popular_three_articles()
    print_seperator()
    most_popular_article_authors()
    print_seperator()
    percentage_error_requests()
    print_seperator()
