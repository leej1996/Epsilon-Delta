class Proof:

    def __init__(self, limit, equation):
        """Precondition: equation is a str in form n * x,
         where x is a variable and n is an int"""
        self.goesto = limit
        self.fx = equation

    def __str__(self):
        return 'For all e > 0, there exists d > 0 : 0 < |x - {0}| < d -> |{1} - {2}| < e'.format(self.goesto, self.fx, self.answer)

    def plug_in(self):

        no_x = ''
        for ch in self.fx:
            if ch.isalpha():
                no_x += str(self.goesto)
            else:
                no_x += ch
        self.no_x = no_x

    def multiply(self):
        l = self.no_x.split('*')
        answer = int(l[0]) * int(l[1])
        self.answer = answer
        self.coefficient = l[0]

    def factor(self):
        a = '{0} - {1}'.format(self.fx, str(self.answer))
        splits = a.split(' - ')
        split_x = splits[0].split('*')
        x = split_x[1]
        c = int(splits[1]) / int(self.coefficient)
        self.factored = '{0} * ({1} - {2})'.format(self.coefficient, x, str(int(c)))


if __name__ == '__main__':
    limit = str(input('What does x go to?: '))
    equation  = input('What is the equation?: ')
    a = Proof(limit, equation)
    a.plug_in()
    a.multiply()
    a.factor()
    print (str(a))
    print ('choose d = e/{0}'.format(a.coefficient))
    print ('Proof:')
    print ('\t 0 < |x - {0}| < d'.format(a.goesto))
    print ('\t 0 < |x - {0}| < e/{1}'.format(a.goesto, a.coefficient))
    print ('\t |{0} - {1}| < e'.format(a.fx, a.answer))
