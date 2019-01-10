#!/usr/bin/env python3

# polynomial object

class Poly(object):
    '''creating a polynomial object'''

    def __doc__():
        return '''This Polynomial class provides a way to represnt polynomils in single variable'''
    
    def __init__(self, elems : dict, name : str = 'x', description : str = 'a polynomial object'):
        '''elems is a dictionary of exponents as keys and coefficients as values
        another assumption is that the exponents values are non-repeating'''
        self.elems = elems
        self.name = name
        self.__dict__['description'] = description
    
    def __str__(self):
        elems = self.elems
        exponents = sorted(elems.keys(), reverse = True)
        #coefficeints = [elems[exp] for exp in exponents]
        
        out = ''
        for exp in exponents:
            sign = ''
            if elems[exp] >= 0:
                sign = '+ '
            out = out + sign + str(elems[exp]) + self.name +'^' + str(exp) + ' '
        return out
    
    def __repr__(self):

        def sign(val):
            if val < 0:
                return '-'
            return '+'
        
        elems = self.elems
        exponents = sorted(elems.keys(), reverse = True)
        var = self.name
        return 'Polynomial: ' + " ".join([sign(self.elems[exp]) + str(abs(self.elems[exp])) + var + '^' + str(exp) for exp in exponents])
    
    def valueAt(self, x):
        result = 0
        for exp in self.elems.keys():
            result += self.elems[exp] * (x  ** exp)
        return result
    
    def addTerm(self, exp, coeff):
        '''term is a tuple with the first element as exponents and the second as the coefficient'''
        if exp in self.elems.keys():
            self.elems[exp] += coeff
        else:
            self.elems[exp] = coeff

    def getDegree(self):
        return max(self.elems.keys())

    def addPoly(self, other):
        '''assuming other be another polynomial object'''
        for exp in self.elems.keys():
            other.addTerm(exp, self.elems[exp])
        return other

    def derivative(self, at = None):
        new_elems = {}
        for exp in self.elems.keys():
            if exp != 0:
                new_elems[exp-1] = exp * self.elems[exp]
        
        if at is None:
            return Poly(new_elems, self.name, self.description)
        else:
            return Poly(new_elems, self.name, self.description).valueAt(at)

    def integral(self, at_0 = None, at_1 = None):
        new_elems = {}
        for exp in self.elems.keys():
            if exp != -1:
                new_elems[exp+1] = self.elems[exp] / (exp + 1)
            else:
                raise ValueError("Can not handle non-polynomial forms!")
        
        if at_0 is None and at_1 is None:
            return Poly(new_elems, self.name, self.description)
        elif (at_1 is not None) and (at_1 is not None):
            integral_at_0 = Poly(new_elems, self.name, self.description).valueAt(at_0)
            integral_at_1 = Poly(new_elems, self.name, self.description).vp1alueAt(at_1)
            return integral_at_1 - integral_at_0
        else:
            raise ValueError("Error: invalid ")
