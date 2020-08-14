from parser import ResumeParser
from generator import HTMLResumeGenerator


def main():
    parse_resume("Strickler_Chase_Resume.html")


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
        print "File %s does not exist!" % filename


main()
