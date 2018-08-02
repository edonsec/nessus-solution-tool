from api import Api
from entry import Entry

class IssueApi(Api):
    def __init__(self):
        super(IssueApi, self).__init__()

    def get_issue(self, term):
        results = self.search(term)
        correct_entry = [x for x in results['props']['pageProps']['plugins'] if x['_source']['script_name'].lower() == term.lower()]

        if len(correct_entry) == 0:
            return Entry(issue=term)

        return Entry(nessus_id=correct_entry[0]['_id'], issue=term, description=correct_entry[0]['_source']['description'], solution=correct_entry[0]['_source']['solution'])
