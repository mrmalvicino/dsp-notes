import numpy as np
import sys
import os

base_path = os.path.abspath(os.path.join(os.getcwd(), "../../dsp-package"))
sys.path.append(base_path)

from dsp.signal import Signal
from dsp.grapher import Grapher
from dsp.archive import Archive

grapher = Grapher()
archive = Archive()
archive.output_path = "../src/images"