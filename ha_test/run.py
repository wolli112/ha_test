#!/usr/bin/env python3

import time
import logging
import json

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# Konfigurationsdatei laden
with open('/data/options.json', 'r') as f:
    options = json.load(f)

VA1 = options.get('VA1')
VA2 = options.get('VA2')
VA3 = options.get('VA3')

while True:
    logging.info(VA1)
    logging.info(VA2)
    logging.info(VA3)
    time.sleep(60)
