from __future__ import print_function

from parser import ResumeParser
from generator import HTMLResumeGenerator
import retriever


def main():
    parse_resume(retriever.get())


def parse_resume(filename):
    try:
        with open(filename, "r") as f:
            resume = f.read()
            f.close()
            parser = ResumeParser(resume)
            parsed_resume = parser.parse()
        generator = HTMLResumeGenerator(parsed_resume)
        generator.generate()
    except IOError as e:
        print("File %s does not exist!" % e.filename)
        raise e


main()
