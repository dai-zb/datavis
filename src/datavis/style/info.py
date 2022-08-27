class Info:
    def __init__(self, name, **kwargs):
        self.name = name
        self.kwargs = kwargs

    def __contains__(self, item):
        return item in self.kwargs

    def __getitem__(self, item):
        return self.kwargs[item]
