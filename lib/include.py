# -*- coding: utf-8 -*-
import os
import sys
p_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lib_dir = os.path.dirname(os.path.abspath(__file__))
conf_dir = p_dir + os.path.sep + "conf" + os.path.sep + "scan_ini.ini"

sys.path.append(p_dir)
sys.path.append(lib_dir)
