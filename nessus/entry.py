class Entry(object):
    nessus_id = None
    issue = None
    description = None
    solution = None
    url = None

    def __init__(self, nessus_id, issue, description, solution):
        self.nessus_id = nessus_id
        self.issue = issue
        self.description = description
        self.solution = solution
        self.url = "https://www.tenable.com/plugins/nessus/{}".format(nessus_id)

