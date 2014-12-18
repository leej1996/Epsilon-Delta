class Linear:

    def __init__(self, limit, equation):
        """(int, str) -> Linear

        >>> l = Linear(4, '2*x')
        >>> l.limit
        4
        >>> l.fx
        '2*x'
        >>> l.answer
        8
        """
        self.limit = limit
        self.fx = equation

        answer = ''
        for ch in self.fx:
            if ch == 'x':
                answer += str(self.limit)
            else:
                answer += ch
        x = eval(answer)

        self.answer = x

        self.make_factor()
        self.factor()
        if self.factored[0].isdigit():
            self.delta = 'e/{0}'.format(self.factored[0])
        else:
            self.delta = 'e'

        #self.delta = 'e/{0}'.format(self.factored[0])



    def __str__(self):
        return 'For all e > 0, there exists d > 0 : 0 < |x - {0}| < d -> |{1} - {2}| < e'.format(self.limit, self.fx, self.answer)

    def make_factor(self):
        w = '{0} - {1}'.format(self.fx, self.answer)
        if '-' in self.fx:
            x = w.split('-')
        elif '+' in self.fx:
            x = w.split('+')
            x[1] = eval(x[1])
        else:
            x = w
        to_factor = ''
        for s in x:
            to_factor += str(s)
        self.to_factor = to_factor

    def factor(self):
        factored = ''
        divide_by = self.to_factor[0]
        factored += divide_by + '('
        for n in self.to_factor:
            if n.isdigit():
                x = str((int(n)/int(divide_by)))

                if x == '1':
                    factored += ''
                else:
                    factored += x
            else:
                factored += n
        q = factored + ')'
        self.factored = q.replace('*', '')


class Quadratic:
    def __init__(self, limit, equation):
        """Precondition: equation is a str in form n ** x,
         where x is a variable and n is an int"""
        self.limit = limit
        self.fx = equation
        #to find exponent
        #do I even need this?
        self.exponent = int(self.fx.split('**')[1][0])

        #finding answer by replacing x w/ limit then evaluating.
        no_x_equation = ''
        for x in self.fx:
            if x == 'x':
                no_x_equation += str(self.limit)
            else:
                no_x_equation += x
        self.answer = eval(no_x_equation)
        self.factor()

    def __str__(self):
        return 'For all e > 0, there exists d > 0 : 0 < |x - {0}| < d -> |{1} - {2}| < e'.format(self.limit, self.fx, self.answer)

    def factor(self):
        if '-' in self.fx:
            no_minus = self.fx.split('-')
            print(no_minus)
            subtract = '0-{0}-{1}'.format(no_minus[-1], self.answer)
            x_minus = eval(subtract)
        else:
            no_plus = self.fx.split('+')
            print(no_plus)
            subtract = '{0}-{1}'.format(no_plus[-1], self.answer)
            x_minus = eval(subtract)
        self.to_factor = x_minus
        self.factored = '|x + {0}| * |x - {0}|'.format(self.limit)
        self.xbound = 1 + int(self.limit)
        self.bound = 2*int(self.limit) + 1
        self.delta = 'e/{0}'.format(self.bound)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
