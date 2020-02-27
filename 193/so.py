import requests
from bs4 import BeautifulSoup

cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    toplist = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for summary in soup.find_all(class_="question-summary"):
        question = summary.find_next(class_="question-hyperlink").text.strip()
        vote = summary.find_next(class_="vote-count-post").text.strip()
        views = summary.find_next(class_="views").text.strip()
        toplist.append( (question, vote, views) )
    toplist_filtered = [ (q[0],int(q[1])) for q in toplist if 'm' in q[2] ]
    return sorted(toplist_filtered, key=lambda x: x[1], reverse=True)

