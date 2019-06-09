"""
File: FSM.py
Author: Jackson Bates
Created: 6/7/2019 7:55 PM
"""

import logging

class FSM:

    def __init__(self, setup_file):
        logging.info("Setup file passed to FSM: {}".format(setup_file))
        self.setup(setup_file)


    def setup(self, fn):
        logging.info("Setup called for FSM...")
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
                self.states[s1].transitions[chars] = [s2,action]

    def generate_states(self, n, acc):
        logging.info("Generating states and setting accept states...")
        self.states = []
        for i in range(n):
            if i in acc:
                s = State(True)
                logging.info("Accept state set: {}".format(s))
            else:
                s = State(False)
            self.states.append(s)




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