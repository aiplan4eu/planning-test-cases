
class TestCaseProblem(object):
    def __init__(self, expected_version):
        if expected_version != self.version():
            raise ValueError("Wrong version")
        pass

    def get_problem(self):
        raise NotImplementedError

    def get_description(self):
        raise NotImplementedError

    def version(self):
        raise NotImplementedError