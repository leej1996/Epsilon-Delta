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
                x = str(int(int(n)/int(divide_by)))

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
        self.goesto = limit
        self.answer = int(self.goesto) ** 2
        self.fx = equation
    def __str__(self):
        return 'For all e > 0, there exists d > 0 : 0 < |x - {0}| < d -> |{1} - {2}| < e'.format(self.goesto, self.fx, self.answer)
    def multiply(self):
        answer = int(self.goesto) ** 2
        self.answer = answer
        #self.coefficient = 1
    def factor(self):
        a = '{0} - {1}'.format(self.fx, str(self.answer))
        splits = a.split(' - ')
        self.factored = '|x + {0}| * |x - {0}|'.format(self.goesto)
        self.bound = 2*int(self.goesto) + 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
