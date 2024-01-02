def boolchk(a):
    if type(a) == bool:
        return True
    return False

def land(p0, p1):
    if boolchk(p0) and boolchk(p1):
        return (p0 and p1)
    return Exception("Unexpected Input!")
def lnot(p0):
    if boolchk(p0):
        return not p0
    return Exception("Unexpected Input!")
