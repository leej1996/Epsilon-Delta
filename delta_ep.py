#file that defines different types of functions
class Linear:
	#class for linear functions
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
		#set the limit to the value defined by the constructor
        self.limit = limit
		#set the fx (f(x)), to the given equation from the constructor
        self.fx = equation

		#set answer to a null string
        answer = ''
		#for loop to go through whole equation
        for ch in self.fx:
            if ch == 'x':
				#add the limit as a string
                answer += str(self.limit)
            else:
				#add the limit as an int
                answer += ch
        x = eval(answer)

        self.answer = x
		
		#call the make_factor function
        self.make_factor()
		self.delta = 'ε/{0}'.format(self.factored[0])
        else:
            self.delta = 'ε'

        #self.delta = 'e/{0}'.format(self.factored[0])


	#method for when the print function is called on the object
    def __str__(self):
        return ' ∀ ε > 0,  ∃ 𝛿 > 0 : 0 < |x - {0}| < 𝛿 -> |{1} - {2}| < ε'.format(self.limit, self.fx, self.answer)
	
	#method to 
    def make_factor(self):
		#format w as the function - the answer
        w = '{0} - {1}'.format(self.fx, self.answer)
		#if theres a minus in the function, split the function at the minus sign
        if '-' in self.fx:
            x = w.split('-')
		#if theres a plus in the function, split the function at the plus sign
        elif '+' in self.fx:
            x = w.split('+')
            x[1] = eval(x[1])
        else:
		#default where the function is left as is
            x = w
		#create the to_factor variable, and puts the function casted into a string into to_factor using a for loop
        to_factor = ''
        for s in x:
            to_factor += str(s)
        self.to_factor = to_factor
	
	#method to factor function
    def factor(self):
        factored = ''
		#assign divide_by to the first digit of to_factor 
        divide_by = self.to_factor[0]
		#factored is the output, and starts 
        factored += divide_by + '('
		#iterate through each part of function
        for n in self.to_factor:
		#if it is a digit, divide the digit by divide_by
            if n.isdigit():
                x = str((int(n)/int(divide_by)))
				#if this quotient is 1, then add nothing to factored
                if x == '1':
                    factored += ''
				#otherwise add x
                else:
                    factored += x
			#if n is not a digit, just add it to factored
            else:
                factored += n
		#add the closing bracket to factored
        q = factored + ')'
		#get rid of all multiplication signs
        self.factored = q.replace('*', '')


#class for quadratic equations
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

	#method for printing the object
    def __str__(self):
        return ' ∀ ε > 0,  ∃ 𝛿 > 0 : 0 < |x - {0}| < 𝛿 -> |{1} - {2}| < e'.format(self.limit, self.fx, self.answer)

	#method for factoring object
    def factor(self):
        if '-' in self.fx:
			#split on the minus signs
            self.no_plus_minus = self.fx.split('-')
			#check if first digit of fx is numeric
            if self.fx[0].isnumeric():
				#turn string into integer
                self.multiplier = int(self.fx[0])
			#subtract is in form 0-last element of no_plus_minus - answer
            subtract = '0-{0}-{1}'.format(self.no_plus_minus[-1], self.answer)
			#evaluate the subtract function
            x_minus = εval(subtract)
		#if there is a plus
        elif '+' in self.fx:
			#split on plus signs
            self.plus_minus= self.fx.split('+')
			#check if first digit is a number
            if self.fx[0].isnumeric():
				#turn it into an int
                self.multiplier = int(self.fx[0])
			#subtract is in form last element of no_plus_minus - answer
            subtract = '{0}-{1}'.format(self.plus_minus[-1], self.answer)
			#evaluate the subtract function
            x_minus = eval(subtract)
        else:
			#check if first digit is numeric
            if self.fx[0].isnumeric():
				#turn string into integer
                self.multiplier = int(self.fx[0])
			#flip the sign by multipling by negative 1
            x_minus = -1 * self.answer
		#set to factor to x_minus
        self.to_factor = x_minus
		#format factored as |x + limit| * |x - limit|
        self.factored = '|x + {0}| * |x - {0}|'.format(self.limit)
		#set xbound as 1 plus the limit
        self.xbound = 1 + int(self.limit)
		#set bound as 2*limit plus 1
        self.bound = 2*int(self.limit) + 1
		#format delta as e/bound
        self.delta = 'e/{0}'.format(self.bound)

#if running the main file, will import doctest
if __name__ == '__main__':
    import doctest
    doctest.testmod()
