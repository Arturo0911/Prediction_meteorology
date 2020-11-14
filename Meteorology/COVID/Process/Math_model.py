

class Math_model:

    def __init__(self, b0, b1, x, y):

        # where the x and y are the mean of columns x y 
        
        self.Beta_zero = b0
        self.Beta_one = b1
        self.Y = y
        self.X = x

    def math_model_(self):

        # In the math model Y= β0 + β1X   
        # To right predictions
        
        return "Predict model: "+self.Y+" = "+self.Beta_zero + " + "+" ("+self.Beta_one+"."+self.X+")"

        

    