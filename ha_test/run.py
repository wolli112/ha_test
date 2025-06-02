#!/usr/bin/env python3

import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

while True:
    logging.info("Läuft noch")
    time.sleep(60)
