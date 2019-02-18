from modules import day_errors, top_authors, top_three_articles

def main():
    # exc 1
    print "What are the most popular three articles of all time?:"
    for result in top_three_articles.get_top_three_articles():
        print "\"{0}\" - {1} views".format(result[0], result[1])

    print "\n"

    # exc 2
    print "Who are the most popular article authors of all time? "
    for result in top_authors.get_top_authors():
        print "{0} - {1} views".format(result[0], result[1])

    print "\n"

    # exc 3
    print "On which days did more than 1% of requests lead to errors?"
    for result in day_errors.get_day_errors():
        print "{0} - {1}%".format(result[0].date(), result[1])


if __name__ == '__main__':
    main()
