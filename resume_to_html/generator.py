import timber

class HTMLResumeGenerator:
    original = None
    generated = None

    def __init__(self, resume):
        self.original = resume

    def generate(self):
        assert isinstance(self.original, dict)
        timber.banner("beginning generation")
        for item in self.original:
            timber.log(item)
            if type(self.original.get(item)) is list:
                for elm in self.original.get(item):
                    tabs = "\t"
                    if elm["class"] == "item":
                        tabs += tabs
                    timber.log("%s%s" % (tabs, elm))
            else:
                print (self.original.get(item))
        timber.banner("finished generation")
