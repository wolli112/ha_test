#!/usr/bin/env python3

import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# Konfigurationsdatei laden
with open('/data/options.json', 'r') as f:
    options = json.load(f)

VA1 = options.get('VA1', 'fallback1')
VA2 = options.get('VA2', 'fallback2')
VA3 = options.get('VA3', 'fallback3')

while True:
    logging.info(VA1,VA2,VA3)
    time.sleep(60)
