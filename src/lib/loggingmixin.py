import logging, os

BASE_DIR = os.path.dirname(os.path.realpath(__file__)).split('src')[0]

class LoggingMixin():
    """
    Provides full logging of requests and responses
    """
    def __init__(self, message, project_name):

        self.message = message
        self.goggingfile_location = BASE_DIR + "logs/" + project_name + ".log"
        self.logger = logging.getLogger('django-helper')
        self.logger.setLevel(logging.DEBUG)
        self.django_helper = logging.FileHandler(self.goggingfile_location)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.django_helper.setFormatter(self.formatter)
        self.logger.addHandler(self.django_helper)

    @property
    def addlog(self):
        self.logger = logging.getLogger('django-helper')

        try:
            self.logger.debug(self.message)
        except:
            self.logger.debug(self.message)

        return True
