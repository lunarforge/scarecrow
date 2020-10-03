from scarecrow_core.network.messages import Messages
from scarecrow_core.plugin_base.base import *

from scarecrow_core.utilities.utils import get_logger
logger = get_logger()

class MotionDetectionPlugin(ImageDetectorBasePlugin):
    name = 'motion'
    mode = 'client'
    def __init__(self, configuration):
        ClientImageBasePlugin.__init__(self, configuration, self.mode)

    def run_before(self, frame):
        if frame:
            print('MotionDetectionPlugin run_before')

    def run_after(self, frame):
         if frame:
            print('MotionDetectionPlugin run_after')