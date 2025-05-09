print(__name__) # This is for to get the module name or file name.
import module_sample #Importing the whole module which we want to execute in this module.
import  module_sample as ms # We can rename to smaller name. if the module name is too bigger.
from module_sample import check_neg_or_pos # Importing just an single function from the module to execute here.
from module_sample import check_neg_or_pos as check # Here we renamed function name itself.
print(module_sample.__name__) # This is also to get name of the module.

module_sample.check_neg_or_pos() # Calling that function from the whole module imported here.
ms.check_neg_or_pos() # Calling that renamed module like this way.
check_neg_or_pos() # Calling that function itself.
check() # Just call the renamed function itself.

