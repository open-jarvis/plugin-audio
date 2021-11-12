"""
Copyright (c) 2021 Philipp Scheer
"""


import os
import json

from jarvis_sdk import PluginServer
from jarvis_sdk import Logger


# define your API endpoints in the endpoints folder
import endpoints


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
CURRENT_WORKING_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
FILE_BASE_NAME = os.path.basename(__file__).split('.')[0]
CONFIG = json.load(f"{CURRENT_WORKING_DIRECTORY}/plugin.json")
PORT = CONFIG.get("port", 6001)

logger = Logger(f"{CURRENT_WORKING_DIRECTORY}/{FILE_BASE_NAME}.log")
server = PluginServer(PORT, logger.info)

logger.info(f"Started {FILE_BASE_NAME} plugin on port {PORT}")
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Perform any actions before script start here
# server.handle_requests() is blocking and will run until the parent kills us

try: server.handle_requests()
except KeyboardInterrupt: pass

# Place actions you want to perform before exit here

logger.info("Stopping plugin")
