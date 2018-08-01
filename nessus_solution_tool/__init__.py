import sys
import argparse
from nessus.issue_api import IssueApi
from presenter.plain_text_presenter import PlainTextPresenter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--issue", help="Issue to lookup")
    parser.add_argument("-f", "--file", help="Input file containing issues to lookup")

    args = parser.parse_args()
    presenter = PlainTextPresenter(IssueApi())
    issue_api = IssueApi()

    if not args.issue and not args.file:
        parser.print_help()
        sys.exit(0)

    if args.file:
        with open(args.file) as f:
            for entry in f:
                presenter.display(issue_api.get_issue(entry.strip()))

    if args.issue:
        presenter.display(issue_api.get_issue(args.issue))
