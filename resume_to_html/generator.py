import htmlstructure
from bs4 import BeautifulSoup


class HTMLResumeGenerator:
    original = None
    generated = None

    def __init__(self, resume):
        self.original = resume

    def generate(self):
        assert isinstance(self.original, dict)
        for item in self.original:
            print(item)
            if type(self.original.get(item)) is list:
                for elm in self.original.get(item):
                    tabs = "\t"
                    if elm["class"] == "item":
                        tabs += tabs
                    print (tabs + str(elm))
            else:
                print (self.original.get(item))
