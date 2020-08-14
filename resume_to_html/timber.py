import datetime
import os
import errno


def banner(message):
    padding = 3
    border = "#" * (len(message) + padding * 2)
    spacing = " " * padding
    log("\n\n" + border + "\n" + spacing + message.upper() + "\n" + border + "\n")


def log(message):
    out = writeout(message)
    # try:
    #     with open(logfile, "w") as f:
    #         # f.write(out)
    #         f.close()
    # except IOError as e:
    #     writeout("File does not exist! %s" % e)


def writeout(message):
    out = ("%s:\t%s" % (datetime.datetime.now(), message))
    print out
    return out


def get_timestamp():
    dt = datetime.datetime.now()
    return int((dt - datetime.datetime(1970, 1, 1)).total_seconds())


logfile = "logs/log_%d.log" % get_timestamp()
if not os.path.exists(os.path.dirname(logfile)):
    try:
        os.makedirs(os.path.dirname(logfile))
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
