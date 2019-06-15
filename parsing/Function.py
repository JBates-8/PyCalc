import logging
import numbers

class Function:
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



class Variable:
    def __init__(self, ch, in_coef = 1):
        if type(ch) is str:
            if ch.isalpha() and len(ch) is 1:
                self.name = ch
            else:
                raise ValueError(repr(ch))
        else:
            raise ValueError(ch)
        self.coef = in_coef

    def __add__(self, other):
        assert type(other) is Variable, "Class not of type variable {}".format(repr(other))
        assert other.name == self.name, "Cannot add different variables together into one"
        return Variable(self.name, in_coef=self.coef+other.coef)

    def __sub__(self, other):
        assert type(other) is Variable, "Class not of type variable {}".format(repr(other))
        assert other.name == self.name, "Cannot subtract different variables together into one"
        return Variable(self.name, in_coef=self.coef - other.coef)

    def __mul__(self, other):
        assert type(other) is Variable, "Class not of type variable {}".format(repr(other))
        assert other.name == self.name, "Cannot multiply different variables together into one"
        return Variable(self.name, in_coef=self.coef + other.coef)

    def __str__(self):
        if self.coef is 1:
            return self.name
        else:
            return "{}{}".format(self.coef,self.name)

class Raised:

    def __init__(self, var, power):
        assert type(var) is Variable
        assert type(power) is int and power > 1
        self.var = var
        self.pow = power



    def __str__(self):
        return "{}^{}".format(self.var, self.pow)



















class Polynomial(Function):
    def __init__(self, text_repr, var):
        super().__init__(text_repr, var, numbers.Real)


if __name__ == '__main__':
    x = Variable('x')
    x1 = Variable('x',5)
    print(x,x1,x+x1)

