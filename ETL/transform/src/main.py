# Import transformation modules
from utils.denormalize_um import denormalize_um
from utils.inconsistency_fix import inconsistency_fix
from utils.transform_cod import transform_cod
from utils.remove_anomalies import remove_anomalies
from utils.denormalize_state import denormalize_state
from utils.remove_columns import remove_columns

# Execute transformations
inconsistency_fix()
denormalize_um()
transform_cod()
remove_anomalies()
denormalize_state()
remove_columns()
