import delta_ep

#main function
def proof(limit, equation):
    e2 = ''
    #iterate through whole equation
    for i in range(len(equation) - 1):
	#if there is an exponent, add to e2 **
        if equation[i] == '^':
            e2 += '**'
	#if there is a number and the next symbol is multiplication symbol, add to e2 the number and then the * symbol
        elif equation[i].isdigit() and equation[i+1] == 'x':
            e2 += '{0}*'.format(equation[i])
        else:
	#else just add to e2 the number
            e2 += equation[i]
    #add the last part of the equation to e2
    e2 += equation[-1]

    #if there is an exponent in the equation
    if '^' in equation or '**' in equation:
	#find the delta epsilon of e2 (use quadratic as its a quadratic function)
        b = delta_ep.Quadratic(limit, e2)
	#display the proof if the first digit of the function is a digit
        if b.fx[0].isdigit():
            w = ["Specific Definition: ",
              " ∀ ε > 0,  ∃ 𝛿 > 0 : 0 < |x - {0}| < 𝛿 -> |{1} - {2}| < ε".format(b.limit, b.fx, b.answer),
              "================================================================= ",
              "Scratch: ",
              '\tTo set a bound on x, notice that |{0} - {1}| = |{2}*x**{3} {4}| = |{2}*(x**{3} - {5})| '.format(b.fx, str(b.answer), b.multiplier, b.exponent, b.to_factor, str(abs(int(b.to_factor)/int(b.multiplier)))),
              '\t\t\t\t\t\t\t = |{0}*({1})|'.format(b.multiplier, b.factored),
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
              " ∀ ε > 0,  ∃ 𝛿 > 0 : 0 < |x - {0}| < 𝛿 -> |{1} - {2}| < ε".format(b.limit, b.fx, b.answer),
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
	#find the delta epsilon of e2 (use linear as its a linear equation)
        a = delta_ep.Linear(limit, e2)
        w = ['Specific Definition:',
            ' ∀ ε > 0,  ∃ 𝛿 > 0 : 0 < |x - {0}| < 𝛿 -> |{1} - {2}| < ε'.format(a.limit, a.fx, a.answer),
            '=================================================================',
            'Proof:',
            'choose 𝛿 = {0}'.format(a.delta),
            '\t 0 < |x - {0}| < d'.format(a.limit),
            '\t 0 < |x - {0}| < {1}'.format(a.limit, a.delta),
            '\t 0 < |{0}| < ε'.format(a.factored),
            '\t 0 < |{0}| < ε'.format(a.to_factor),
            '\t |({0}) - {1}| < ε'.format(a.fx, a.answer),
            'QED'
            ]
        return w
