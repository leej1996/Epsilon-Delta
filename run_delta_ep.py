import delta_ep

def proof(limit, equation):
    print('=================================================================')
    if '**' in equation:
        b = delta_ep.Quadratic(limit, equation)
        if b.fx[0].isdigit():
            ["Specific Definition: ",
              "================================================================= ",
              "Scratch: ",
            #   "To set a bound on x, notice that |{0} - {1}| = |{2}*x**{3} {4}| = |{2}*(x**{3} - {5})| ".format(b.fx,
            #                str(b.answer), b.multiplier, b.exponent, b.to_factor,
            #                str(abs(int(b.to_factor)/int(b.multiplier))))
              "Assume 𝛿 = 1 ",
              "\tThen |x - {0}| < 𝛿 = 1 ".format(b.limit),
              "\tThen |x - {0}| < 1 ".format(b.limit),
              "\tThen -1 + {0} < x < 1 + {0} ".format(b.limit),
              "\tThen x < {0} ".format(b.xbound),
              "\tThen {0} < |{1} + {2}|*|x - {2}| < {3}|x - {2}| ".format(b.factored,
                        b.xbound, b.limit, b.bound),
              "\tThen we can choose 𝛿 = ε/{0} ".format(b.bound),
              "================================================================= ",
              "Proof: ",
              "Choose 𝛿 = min(1, ε/{0}) ".format(b.bound) ,
              "\t|{0} - {1}| = |x**{2} {3}|={4} ".format(b.fx,str(b.answer),
                        str(b.exponent), str(b.to_factor), b.factored),
              "\t    <= {0} * |x - {1}| <= {0}(ε/{0}) = ε ".format(b.bound, b.limit),
              "QED "

              ]
        else:
            w =["Specific Definition: ",
              "================================================================= ",
              "Scratch: ",
              '\tTo set a bound on x, notice that |{0} - {1}| = |x**{2} {3}|={4}'.format(b.fx,str(b.answer), str(b.exponent), str(b.to_factor), b.factored),
              "\tAssume 𝛿 = 1 ", "\tThen |x - {0}| < 𝛿 = 1 ".format(b.limit),
              "\tThen |x - {0}| < 1 ".format(b.limit),
              "\tThen -1 + {0} < x < 1 + {0} ".format(b.limit),
              "\tThen x < {0} ".format(b.xbound),
              "\tThen {0} < |{1} + {2}|*|x - {2}| < {3}|x - {2}| ".format(b.factored,
                        b.xbound, b.limit, b.bound),
              "\tThen we can choose 𝛿 = ε/{0} ".format(b.bound),
              "================================================================= ",
              "Proof: ",  "Choose 𝛿 = min(1, ε/{0}) ".format(b.bound) ,
              "\t|{0} - {1}| = |x**{2} {3}|={4} ".format(b.fx,str(b.answer),
                        str(b.exponent), str(b.to_factor), b.factored),
              "\t    <= {0} * |x - {1}| <= {0}(ε/{0}) = ε ".format(b.bound, b.limit),
              "QED "
              ]
        return w


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
