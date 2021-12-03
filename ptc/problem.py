
class TestCaseProblem(object):
    def __init__(self, version):
        if version != self._version():
            raise ValueError("Wrong version")
        pass

    def get_problem(self):
        raise NotImplementedError

    def get_description(self):
        raise NotImplementedError

    def _version():
        raise NotImplementedError