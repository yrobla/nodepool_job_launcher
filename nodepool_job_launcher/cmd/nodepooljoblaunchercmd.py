# -*- coding: utf-8 -*-
#!/usr/bin/env python
__author__ = 'Yolanda Robla'
__email__ = 'yolanda.robla-mota@hp.com'
__version__ = '0.1.0'

import argparse
import logging.config
import sys

from nodepool_job_launcher import nodepool_job_launcher

class NodepoolJobLauncherCmd(object):
    def __init__(self):
        self.args = None

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description='Nodepool Job launcher.')
        parser.add_argument('-c', dest='config',
                            default='/etc/nodepool_job_launcher/config.yaml',
                            help='path to config file')
        parser.add_argument('-j', dest='job',
                            default='Job to be executed')

        self.args = parser.parse_args()

    def main(self):
        self.nodepool_job_launcher = nodepool_job_launcher.Launcher(self.args.config, self.args.job)

def main():
    cmd = NodepoolJobLauncherCmd()
    cmd.parse_arguments()
    return cmd.main()

if __name__ == "__main__":
    sys.exit(main())

