"""
File: FSM.py
Author: Jackson Bates
Created: 6/7/2019 7:55 PM
"""

import logging
import json


class FSM:
    def __init__(self, setup_file):
        self.logger = logging.getLogger(__name__)
        self.logger.info("Setup file passed to FSM: {}".format(setup_file))
        self.setup(setup_file)

    def setup(self, fn):
        self.logger.info("Setup called for FSM...")
        with open(fn) as f:
            lines = [l.strip() for l in f.readlines()]
            n_states = int(lines[0])
            a_states = [int(x) for x in lines[1].split()]
            self.generate_states(n_states,a_states)
            self.logger.info("Setting transitions for states")
            for i in range(2,len(lines)):
                cur = lines[i]
                trans,details = cur.split(":")
                self.logger.debug("Transitions: {}, Details: {}".format(trans, details))
                s1,s2 = [int(x) for x in trans.split(">")]
                chars,action = details.split(";")
                self.logger.debug("chars: {}, action: {}".format(chars, action))
                chars = chars.split(",")
                self.logger.debug("chars reformated: {}".format(chars))
                if len(chars) == 2:
                    chars = [str(i) for i in range(int(chars[0]),int(chars[1]))]
                self.states[s1].transitions[json.dumps(chars)] = [s2,action]


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
                json_lst = json.loads(lst)
                if ch in json_lst:
                    cur = self.states[transitions[lst][0]]
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



if __name__ == '__main__':
    fsm = FSM("fsm_setup.txt")
    print(fsm.states)
    for s in fsm.states:
        print(s.ID,s.isAccept,s.transitions)