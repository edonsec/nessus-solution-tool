class PlainTextPresenter(object):
    def __init__(self):
        pass

    def display(self, issue):
        print "\033[1m{title}\033[0m\n".format(title=issue.issue)
        print "{solution}\n\n".format(solution=issue.solution)
        print "{url}\n".format(url=issue.url)
    
