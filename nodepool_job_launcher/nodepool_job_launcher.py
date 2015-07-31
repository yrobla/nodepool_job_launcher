#!/usr/bin/env python

import logging
import yaml

class Launcher():
    log = logging.getLogger("nodepool_job_launcher.Launcher")

    def __init__(self, configfile, job):
        self.configfile = configfile
        self.job = job
        self.loadConfig()

    def loadConfig(self):
        config = yaml.load(open(self.configfile))
        print config
