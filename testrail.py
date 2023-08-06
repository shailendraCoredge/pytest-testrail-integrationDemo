from api_client import APIClient
from consts import (
    USER,
    PWD,
    URL,
    PROJECT_ID)


class TestRailAgent():
    def __init__(self):
        self.client = APIClient(URL)
        self.client.user = USER
        self.client.password = PWD

    def get_case(self, tid):
        """ get test case by id
        """
        return self.client.send_get('get_case/%d' % int(tid))

    def get_run(self, rid):
        """ get a test run by its id
        """
        return self.client.send_get('get_run/%d' % int(rid))

    def add_run(self, name, description='', milestone=None, assignedTo=None,
                include_all=False, case_ids=None):
        """ add test run based on parameters
            milestone: int
            assignedTo: int
            case_ids: list
        """
        if not case_ids:
            case_ids = []

        data = {
            'name': name,
            'description': description,
            'milestone_id': milestone,
            'assignedto_id': assignedTo,
            'include_all': include_all,
            'case_ids': case_ids
        }
        return self.client.send_post('add_run/%d' % PROJECT_ID, data)

    def get_tests(self, rid):
        """ get tests in a test run
        """
        return self.client.send_get('get_tests/%d' % int(rid))

    def get_case_types(self):
        """ get available case type mapping
        """
        return self.client.send_get('get_case_types')

    def get_cases_by_type(self, test_type):
        """ get all cases for a certain type
        """
        assert test_type in CASE_TYPE_TO_ID
        return self.client.send_get('get_cases/%d&type_id=%d' %
                                    (PROJECT_ID, CASE_TYPE_TO_ID[test_type]))

    def add_results(self, rid, results):
        return self.client.send_post('add_results/%d' % rid, results)

if __name__ == '__main__':
    """ test TestRailAgent
    """
    agent = TestRailAgent()






