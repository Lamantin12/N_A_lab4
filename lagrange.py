from numpy import ndarray
##############################################################################################################################################
def lagrange(x_range: ndarray, x_poly: ndarray, y_poly: ndarray) -> float:
    res = 0
    for i in range(len(y_poly)): # i проходит по точкам
        temp = 1
        for j in range(len(y_poly)): # j проходит для произведения
            if i!=j:
                temp *=  (x_range - x_poly[j]) / (x_poly[i] - x_poly[j])
        res += y_poly[i] * temp        
    return res
##############################################################################################################################################