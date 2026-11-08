import os
import sys

# Inject local python libs and scripts path
LOCAL_LIBS = "/home/kadefue/Course_Notes/.python_libs"
if os.path.exists(LOCAL_LIBS) and LOCAL_LIBS not in sys.path:
    sys.path.insert(0, LOCAL_LIBS)

SCRIPTS_DIR = "/home/kadefue/Course_Notes/BIT 111/Scripts"
if os.path.exists(SCRIPTS_DIR) and SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

from compendium_base import *

print("Starting Topic 1 Compendium generation...")
