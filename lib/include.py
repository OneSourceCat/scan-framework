#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: anchen
# @Date:   2015-04-11 10:44:36
# @Last Modified by:   anchen
# @Last Modified time: 2015-04-11 13:15:32
import os,sys
p_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lib_dir = os.path.dirname(os.path.abspath(__file__))
conf_dir = p_dir + os.path.sep + "conf" + os.path.sep + "scan_ini.ini"

sys.path.append(p_dir)
sys.path.append(lib_dir)
