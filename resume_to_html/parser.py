from bs4 import BeautifulSoup


class Souper:
    soup = None
    header = None
    skip = False
    resume = {}
    data = []

    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')

    def parse(self):
        spans = self.soup.findAll("span")
        for span in spans:
            text = span.get_text()
            if self.skip or len(text) == 0:
                self.skip = False
                continue
            if span.has_attr("class") and span["class"][0] == "c1" or "c13" in span["class"]:
                print("hd  --- --- %s" % text)
                self.header = span
                self.resume[self.header] = self.data
                self.data = []
            elif span.has_attr("class") and span["class"][0] == "c2":
                self.data.append(span)
                print("c2  --- --- --- %s" % text)
            elif span.has_attr("class") and span["class"][0] == "c7":
                date_range = span.next_sibling.get_text()
                job = text + date_range
                self.data.append(span)
                self.data.append(span.next_sibling)
                self.skip = True
                print("c7  --- --- --- %s" % job)
            elif span.has_attr("class") and span["class"][0] == "c12":
                if len(text) < 5:
                    continue
                self.data.append(span)
                print("c12 --- --- --- %s" % text)

            elif span.has_attr("class") and span["class"][0] == "c6":
                """Extra, probably location or for technical subsections"""
                self.data.append(span)
                if "languages" or "miscellaneous" not in text:
                    self.skip = True
                    self.data.append(span.next_sibling)
                    text = text + span.next_sibling.get_text()
                print("c6  --- --- --- %s " % text)
            else:
                print("Unknown element found! %s" % text)
                print("############### Class: %s" % span["class"])

    def print_html(self):
        print(self.soup.prettify())

    def prettify(self):
        print(self.soup.prettify())


def main(filename):
    with open(filename, "r") as f:
        resume = f.read()
        souper = Souper(resume)
        souper.parse()
        f.close()


main("Strickler_Chase_Resume.html")
