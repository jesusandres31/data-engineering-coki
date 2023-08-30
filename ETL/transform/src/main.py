# Import transformation modules
from utils.denormalize_um import denormalize_um
from utils.inconsistency_fix import inconsistency_fix
from utils.transform_cod import transform_cod

# Execute transformations
inconsistency_fix()
denormalize_um()
transform_cod()
