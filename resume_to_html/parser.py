import htmlstructure
import timber
from bs4 import BeautifulSoup


class ResumeParser:
    soup = None
    header = None
    skip = False
    resume = {}
    data = []

    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')

    def parse(self):
        a = self.soup.findAll("a", href=True)[0]
        a["href"] = htmlstructure.website_link
        a["class"] = htmlstructure.website_cls
        spans = self.soup.findAll("span")

        for span in spans:
            indent = '--- '
            text = span.get_text()
            timber.log(span)
            if self.skip or len(text) == 0 or not span.has_attr("class"):
                self.skip = False
                continue
            cls = span["class"][0]
            if cls == "c1" or "c13" in span["class"]:
                self.header = span
                if cls == "c1":
                    span["class"] = htmlstructure.heading_cls
                else:
                    span["class"] = htmlstructure.section_cls
                self.resume[self.header] = []
                self.data = self.resume[self.header]
            elif cls == "c2":
                span["class"] = htmlstructure.item_cls
                self.data.append(span)
                indent += "--- --- "
            elif cls == "c7":
                date_range = span.next_sibling.get_text()
                job = text + date_range
                span.string = job
                self.data.append(span)
                self.skip = True
                span["class"] = htmlstructure.job_cls
                indent += "--- "
            elif cls == "c12":
                if len(text) < 5:
                    continue
                self.data.append(span)
                span["class"] = htmlstructure.personal_info_cls
                indent += "--- "
            elif cls == "c6":
                span["class"] = htmlstructure.subsection_cls
                if "Languages" not in text and "Miscellaneous" not in text:
                    self.skip = True
                    span.string = span.string + span.next_sibling.string
                    text = text + span.next_sibling.get_text()
                    span["class"] = [htmlstructure.subsection_cls, htmlstructure.location_cls]
                self.data.append(span)
                indent += "--- "
            else:
                indent = "Unknown element found"
            cls = span["class"]
            timber.log(("%s%s\t{CLASS=\"%s\"}" % (indent, text, cls)).encode('utf-8'))

        return self.resume

    def prettify(self):
        timber.log(self.soup.prettify())
