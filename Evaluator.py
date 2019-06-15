"""
File: Evaluator.py
Author: Jackson Bates
Created: 5/15/2019 11:26 PM 
"""

import logging
import re

from parsing.Function import Function
from Lagrange import Lagrange
import numbers



class Evaluator:

    def __init__(self, parent_console):
        self.logger = logging.getLogger(__name__)
        self.logger.info("Evaluator initialized...")
        self.regexs = {}
        self.variables = {}
        self.running_extern = False
        self.parent = parent_console
        with open("valid_cmds",'r') as f:
            lines = f.readlines()
            size = len(lines)
            for i in range(0,size,2):
                reg = lines[i].strip()
                fun = lines[i+1].strip()
                self.regexs[re.compile(reg)] = fun
        self.logger.info("RE list created for evaluator: {}".format(self.regexs))

    def evaluate(self,cmd):
        for r in self.regexs.keys():
            logging.debug(r)
            m = re.match(r,cmd)
            if(m):
                logging.debug("Match found: {}".format(m))
                logging.debug("CALLING self.{}".format(self.regexs.get(r)))
                self.cmd = cmd
                eval("self.{}".format(self.regexs.get(r)))
                return
        self.logger.info("INVALID COMMAND: '{}'".format(cmd))

    def count_cmds(self):
        self.logger.info("commands count: {}".format(self.parent.cmds_proc))

    def quit(self):
        if self.running_extern:
            self.stop_run = True
            self.running_extern = False
            self.logger.debug("quit called while running a file")
        else:
            exit()

    def show_vars(self):
        self.logger.debug("vars called")
        self.logger.info(self.variables)

    def assign(self):
        self.logger.debug("assign called")
        name, val = [x.strip() for x in self.cmd[4:].split(" = ")]
        self.variables[name] = int(val)
        self.logger.info("set variable '{}' to {}".format(name,val))

    def run(self, test = False):
        self.stop_run = False
        if test:
            self.file_to_run = "test.txt"
        else:
            self.file_to_run = self.cmd[4:].strip()
        self.running_extern = True
        self.logger.debug("run called on file: {}".format(self.file_to_run))
        with open(self.file_to_run,'r') as f:
            for line in f.readlines():
                if not self.stop_run:
                    self.evaluate(line)

    def define_func(self):
        split = self.cmd.split("=")
        [name,str_rep] = split[0][4:].strip(),split[1].strip()
        self.logger.debug("attempting to define function '{}'".format(str_rep))
        chars_present = set([c for c in str_rep if c.isalpha()])
        self.logger.debug("char set for function: {}".format(chars_present))
        if len(chars_present) is 1:
            fun = Function(str_rep,list(chars_present)[0], numbers.Real)
            self.variables[name] =  fun
        else:
            logging.info("USER ERROR: function string must be of only one variable")

    def evaluate_at(self):
        func_to_eval = self.cmd[0]
        value = int(self.cmd[self.cmd.find("(")+1:self.cmd.find(")")])
        if func_to_eval in self.variables:
            self.logger.info("".format(self.variables[func_to_eval].evaluate_at(value)))
        self.logger.info(str())

    def lagrange(self):
        self.logger.info("lagrange called...")
        cmd = self.cmd.strip().split()
        self.logger.info("cmd: {}".format(cmd))
        l_name = cmd[1].strip()[0]

        data = cmd[2].split("],[")
        data[0] = data[0][1:]
        data[1] = data[1][:-1]
        data[0] = [int(x) for x in data[0].split(",")]
        data[1] = [int(x) for x in data[1].split(",")]
        self.logger.debug(data)
        lag = Lagrange(data[0],data[1],l_name)
        self.variables[l_name] = lag





