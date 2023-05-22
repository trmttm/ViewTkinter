import os_identifier

LEFT_CLICK = 1
RIGHT_CLICK = 2
MIDDLE_CLICK = 3
if not os_identifier.is_mac:
    RIGHT_CLICK = 3
    MIDDLE_CLICK = 2
