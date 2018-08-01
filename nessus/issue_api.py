from api import Api
from entry import Entry

class IssueApi(Api):
    def __init__(self):
        super(IssueApi, self).__init__()

    def get_issue(self, term):
        results = self.search(term)
        correct_entry = [x for x in results['props']['pageProps']['plugins'] if x['_source']['script_name'] == term][0]

        return Entry(nessus_id=correct_entry['_id'], issue=term, description=description['_source']['description'], solution=correct_entry['_source']['solution']  
