"""
File: Console.py
Author: Jackson Bates
Created: 5/15/2019 12:43 AM 
"""
import logging
from Evaluator import Evaluator
from parsing import FSM

class Console():

    def __init__(self, prompt = ">>"):
        self.logger = logging.getLogger(__name__)
        self.evaluator = Evaluator(self)
        self.symb = prompt
        self.cmds_proc = 0
        self.cur_cmd = None
        self.fsm = FSM("fsm_setup.txt")
        self.logger.info("Console initialized... prompt set to '{}'".format(self.symb))

    def prompt(self):
        self.cur_cmd = input(self.symb).strip()

    def process(self):
        self.cur_cmd = self.cur_cmd.strip()
        result = self.fsm.evaluate(self.cur_cmd)
        self.logger.info(result)
        self.cmds_proc += 1
        self.logger.debug("input: {}".format(self.cur_cmd))

    def run(self):
        while(True):
            self.prompt()
            self.process()

    def test_run(self):
        self.evaluator.run(test=True)
