import pytest
from my_module import divide  

def test_divide():
    assert divide(10, 2) == 5  
    assert divide(9, 3) == 3 
    assert divide(5, 2) == 2.5 

   
    with pytest.raises(ValueError, match="Cannot divide by zero"):  
        divide(5, 0)
