from drawdiamond import draw_diamond


def test_diamond():
    assert draw_diamond("C") ==  """
    
    
    
   A  
 B   B 
C     C
 B   B 
   A  
"""