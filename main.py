class calculator:
    """ Simple calculator """

    def add (self, a, b):
        return a + b
    
if __name__ == "__main__":

    calc = calculator()
    print("Addition: ", calc.add(5,9))