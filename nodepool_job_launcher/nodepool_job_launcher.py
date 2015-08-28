#!/usr/bin/env python

import gear
import jenkins
import json
import sys
import time
import yaml

from uuid import uuid4

class Launcher():
    def __init__(self, configfile, job):
        self.configfile = configfile
        self.job = job
        self.jobs = {}
        self.gearman = None
        self.jenkins = None

        self.loadConfig()
        self.connectGearman()
        self.connectJenkins()
        self.launchJob()

    # start the connection with gearman server
    def connectGearman(self):
        self.gearman = gear.Client()
        try:
            self.gearman.addServer(self.gearman_server, self.gearman_port)
            self.gearman.waitForServer()
        except:
            print "Error connecting to gearman server"
            sys.exit(1)

    # start the connection with jenkins server
    def connectJenkins(self):
        self.jenkins = jenkins.Jenkins(self.jenkins_config['url'], self.jenkins_config['user'],
                                       self.jenkins_config['apikey'])

    # convert the yaml in a dictionary
    def parse_job_list(self, jobs):
        for job in jobs:
            if 'node-type' in job and 'name' in job:
                self.jobs[job['name']] = job['node-type']

    # load configuration details
    def loadConfig(self):
        try:
            config = yaml.load(open(self.configfile))
        except Exception:
            error_message = "Error: cannot find configuration file %s" % self.configfile
            print error_message
            sys.exit(1)

        self.gearman_server = config.get('gearman-server', '127.0.0.1')
        self.gearman_port = config.get('gearman-port', 4730)

        self.jenkins_config = config.get('jenkins', {})
        if not set(('url', 'user', 'apikey')).issubset(self.jenkins_config):
            print "Jenkins configuration is not properly set"
            sys.exit(1)

        jobs = config.get('jobs', {})
        self.parse_job_list(jobs)

    def launchJob(self):
        # check if job name in list
        if not self.job in self.jobs:
            error_message = "Error: cannot find job %s" % self.job
            print error_message
            sys.exit(1)

        # send demand to nodepool
        gearman_job = gear.Job("build:%s:%s" % (self.job, self.jobs[self.job]),
                               json.dumps({"OFFLINE_NODE_WHEN_COMPLETE": True}), str(uuid4().hex))
        self.gearman.submitJob(gearman_job)

        # sleep for a bit, to let gearman operate
        time.sleep(1)

        # send job to jenkins
        self.jenkins.build_job(self.job)
