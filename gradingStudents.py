def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] < 38:
            continue
        else:
            nextMultiple = grades[i]
            if grades[i] % 5 == 0:
                continue
            elif grades[i] % 5 == 1:
                nextMultiple += 4
            elif grades[i] % 5 == 2:
                nextMultiple += 3
            elif grades[i] % 5 == 3:
                nextMultiple += 2
            elif grades[i] % 5 == 4:
                nextMultiple += 1
                
            if nextMultiple - grades[i] < 3:
                grades[i] = nextMultiple
    return grades