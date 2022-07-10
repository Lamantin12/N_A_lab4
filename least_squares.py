from numpy import sqrt, ndarray, zeros
from numpy.linalg import solve
##############################################################################################################################################
class least_squares:
    def __init__(self) -> None:
        self.coeficients: ndarray = None
        self.power: int = None

    def fit(self,x_array: ndarray,f_array: ndarray, power: int) -> None:
        self.power = power
        s = zeros((2 * self.power, 1))
        b_ = zeros((self.power, 1))
        for i in range(2 * self.power):
            s[i] = (x_array**i).sum()
            
        for i in range(self.power):
            b_[i] = (f_array * x_array**i).sum()
            
        A = zeros((self.power, self.power))
        for i in range(self.power):
            for j in range(self.power):
                A[i,j] = s[j+i]
                
        self.coeficients = solve(A,b_)

    def solve(self, x_array: ndarray) -> ndarray:
        res = 0
        for i in range(self.power):
            res = res + x_array**i * self.coeficients[i]
        return res

##############################################################################################################################################

def count_mse(polynom: ndarray, actual: ndarray) -> float:
    return sqrt(((polynom - actual)**2).sum() / (len(actual) + 1))