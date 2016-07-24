from src.lib.loggingmixin import LoggingMixin
from src.lib.createmodel import CreateModel
# from optparse import OptionParser

# parser = OptionParser()
# parser.add_option("-n", "--project-name", dest="projectname", help="Name of The projects")
# parser.add_option("-q", "--quiet",action="store_false", dest="verbose", default=True,
#                   help="don't print status messages to stdout")
#
# (options, args) = parser.parse_args()

projects_name = "sample-projects"



filename = CreateModel()
Debug_message = "Created Model {}".format(filename)
debug = LoggingMixin(Debug_message ,projects_name).addlog
