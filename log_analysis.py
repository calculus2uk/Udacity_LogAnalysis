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

    """Return All the most popular three articles of all time."""
    query = '''select title, views as total_views from
               articles inner join popular_articles on
               articles.slug = popular_articles.new_path
               limit 3;'''
    most_popular_three_articles_query = execute_function(query)
    print('\nThe most popular three articles of all time are: \n')
    for article in most_popular_three_articles_query:
        print('\t' + str(article[0]) + ' ---- ' + str(article[1]) + ' views')

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
