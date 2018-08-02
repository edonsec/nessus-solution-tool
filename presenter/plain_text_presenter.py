class PlainTextPresenter(object):
    def __init__(self):
        pass

    def display(self, issue):
        print "\033[1m{title}\033[0m\n".format(title=issue.issue)

        if not issue.solution:
            print "Unable to find details."
        else:
            print "{solution}\n".format(solution=issue.solution)
            print "{url}\n".format(url=issue.url)
