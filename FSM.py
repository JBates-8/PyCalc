"""
File: FSM.py
Author: Jackson Bates
Created: 6/7/2019 7:55 PM
"""

import logging

class FSM:

    def __init__(self, setup_file):
        self.logger = logging.getLogger(__name__)
        self.logger.info("Setup file passed to FSM: {}".format(setup_file))
        self.setup(setup_file)

    def setup(self, fn):
        self.logger.info("Setup called for FSM...")
        with open(fn) as f:
            lines = [l.strip() for l in f.readlines()]
            N_States = int(lines[0])
            Accept_States = [int(x) for x in lines[1].split()]
            self.generate_states(N_States,Accept_States)
            for i in range(2,len(lines)):
                cur = lines[i]
                trans,details = cur.split(":")
                s1,s2 = [int(x) for x in trans.split(">")]
                chars,action = details.split(";")
                chars = chars.split(",")
                if len(chars) == 2:
                    chars = [int(i) for i in range(int(chars[0]),int(chars[1]))]
                self.states[s1].transitions[repr(chars)] = [s2,action]

    def generate_states(self, n, acc):
        self.logger.info("Generating states and setting accept states...")
        self.states = []
        for i in range(n):
            if i in acc:
                s = State(True)
                self.logger.info("Accept state set: {}".format(s))
            else:
                s = State(False)
            self.states.append(s)
        self.logger.info("States: {}".format(self.states))

    def evaluate(self, string):
        cur = self.states[0]
        self.logger.info("Evaluating string: {}\nStart state: {}".format(string,cur))
        for i,ch in enumerate(string):
            transitions = cur.transitions
            self.logger.info("Character read: {}, transitions available: {}".format(ch, transitions))
            for lst in transitions.keys():
                if ch in list(lst):
                    cur = transitions[lst]
                    self.logger.info("Transitioned to state: {}".format(cur))
        transitions = cur.transitions
        if "$" in transitions:
            return [True, transitions["$"]]
        else:
            return [False, None]



class State:

    ID = 0

    def __init__(self, accept):
        self.ID = State.ID
        State.ID += 1
        self.isAccept = accept
        self.transitions = {}  # charset : state to go to

    def __repr__(self):
        return "S_"+str(self.ID)






def get_ints():
    return [int(x) for x in input().strip().split(" ")]


if __name__ == '__main__':
    fsm = FSM("fsm_setup.txt")
    print(fsm.states)
    for s in fsm.states:
        print(s.ID,s.isAccept,s.transitions)