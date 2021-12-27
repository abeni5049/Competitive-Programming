def countingValleys(steps, path):
    count = seaLevel = 0
    for step in path:
        if step == "D":
            seaLevel -= 1
        elif step == "U":
            seaLevel += 1
        if step == "U" and seaLevel == 0:
            count += 1
    return count