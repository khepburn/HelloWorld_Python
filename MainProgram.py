#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      asmazo
#
# Created:     24/10/2016
# Copyright:   (c) asmazo 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def DimeLaFechaHora():
    import time
    return ("la fecha de hoy es " + time.strftime("%c"))

print("Hello Wold)
print("Ciao world" + ", " + str(DimeLaFechaHora()));
