import converters
print(converters.lbs_to_kg(160))
#or
from converters import kg_to_lbs
print(kg_to_lbs(72))


from utils import find_max
print(find_max([5, 6, 2, 1, 0]))


####### importing packages ##########

import ecommerce.shipping
ecommerce.shipping.calc_shipping()

from ecommerce.shipping import calc_shipping
calc_shipping()

from ecommerce import shipping
shipping.calc_shipping()