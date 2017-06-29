import numpy as np
from numpy import testing as npt
import ArraySum
    
def test_ArraySumFunction():
    # testing ArraySum function
    array1 = 2*np.ones(100)
    array2 = np.ones(100)
    res = ArraySum.ArraySumFunction(array1,array2)
    npt.assert_equal(res, 3*np.ones(100))
