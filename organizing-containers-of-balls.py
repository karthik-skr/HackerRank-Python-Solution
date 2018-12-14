
def organizingContainers(container):
    isPosible = True
    boxTotals = {}
    ballsTotals = {}
    for i1,v1 in enumerate(container):
        boxTotals[i1] = sum(v1)
        for i2,v2 in enumerate(v1):
            ballsTotals[i2] = ballsTotals.get(i2,0)+v2
    isPosible = (sorted(boxTotals.values()) == sorted(ballsTotals.values()))
    return "Possible" if isPosible == True else "Impossible";

if __name__ == '__main__':
    result = organizingContainers([[997612619, 934920795, 998879231, 999926463],
[960369681, 997828120, 999792735, 979622676],
[999013654, 998634077, 997988323, 958769423],
[997409523, 999301350, 940952923, 993020546]])
    print("result",result)

      
