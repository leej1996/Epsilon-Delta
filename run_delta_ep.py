import delta_ep

def main():
    print('Multiplication symbol must be expressed with a *, ** for powers')
    print('Quadratics must be written in from c*x**2 +/- n, where c,n are integers')
    print('Linear equations must be written in form n*x + c, where n,c is an integer')
    print('=================================================================')
    print('Type no to exit.')
    question = input("Do you want to generate an epsilon delta proof?: ")
    while question != '' and question.lower() != 'no':
        limit = str(input('What does x go to?: '))
        equation  = input('What is the equation?: ')
        if limit.lower() == 'no' or equation.lower() == 'no':
            break
        print('=================================================================')
        if '**' in equation:
            b = delta_ep.Quadratic(limit, equation)
            print ('Specific Definition:')
            print (str(b))
            print('=================================================================')
            print ('Scratch:')
            if b.fx[0].isdigit():
                print('\tTo set a bound on x, notice that |{0} - {1}| = |{2}*x**{3} {4}| = |{2}*(x**{3} - {5})| '.format(b.fx, str(b.answer), b.multiplier, b.exponent, b.to_factor, str(abs(int(b.to_factor)/int(b.multiplier)))))
                print('\t\t\t\t\t\t\t = |{0}*({1})'.format(b.multiplier, b.factored))
            else:
                print('\tTo set a bound on x, notice that |{0} - {1}| = |x**{2} {3}|={4}'.format(b.fx,str(b.answer), str(b.exponent), str(b.to_factor), b.factored))
            print ('\tAssume 𝛿 = 1')
            print ('\tThen |x - {0}| < 𝛿 = 1'.format(b.limit))
            print ('\tThen |x - {0}| < 1'.format(b.limit))
            print ('\tThen -1 + {0} < x < 1 + {0}'.format(b.limit))
            print ('\tThen x < {0}'.format(b.xbound))
            print ('\tThen {0} < |{1} + {2}|*|x - {2}| < {3}|x - {2}|'.format(b.factored, b.xbound, b.limit, b.bound))
            print ('\tThen we can choose 𝛿 = ε/{0}'.format(b.bound))
            print('=================================================================')
            print ('Proof:')
            print ('Choose 𝛿 = min(1, ε/{0})'.format(b.bound))
            print ('\t|{0} - {1}| = |x**{2} {3}|={4}'.format(b.fx,str(b.answer), str(b.exponent), str(b.to_factor), b.factored))
            print ('\t           <= {0} * |x - {1}| <= {0}(ε/{0}) = ε'.format(b.bound, b.limit))
            print ('QED')
        else:
            a = delta_ep.Linear(limit, equation)
            print ('Specific Definition:')
            print (str(a))
            print('=================================================================')
            print ('Proof:')
            print ('choose 𝛿 = {0}'.format(a.delta))
            print ('\t 0 < |x - {0}| < d'.format(a.limit))
            print ('\t 0 < |x - {0}| < {1}'.format(a.limit, a.delta))
            print ('\t 0 < |{0}| < ε'.format(a.factored))
            print ('\t 0 < |{0}| < ε'.format(a.to_factor))
            print ('\t |({0}) - {1}| < ε'.format(a.fx, a.answer))
            print ('QED')

if __name__ == '__main__':
    main()
