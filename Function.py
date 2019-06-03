import logging
import numbers

class Function():

    def __init__(self, text_repr, var, domain):
        self.text_repr = text_repr # type : str
        self.var = var             # type : chr
        self.logger = logging.getLogger(__name__)

    def __str__(self):
        return self.text_repr

    def __repr__(self):
        return self.__str__()

    def evaluate_at(self, pt):
        self.logger.debug("point evaluated at '{}'".format(pt))
        replaced = self.text_repr.replace(self.var,str(pt)).replace('^','**')
        self.logger.debug("replaced function text: '{}'".format(replaced))
        self.logger.info(eval(replaced))

