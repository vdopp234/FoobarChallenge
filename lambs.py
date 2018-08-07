def answer(total_lambs):
    min = getMinimum(total_lambs)
    max = getMaximum(total_lambs)
    return min - max

def can_add(ranks, addLamb):
    high1 = ranks[len(ranks) - 1]
    high2 = 0
    try:
        high2 = ranks[len(ranks) - 2]
    except Exception as e:
        return addLamb < 2*high1
    if addLamb > 2*high1:
        return False
    if addLamb < high1 + high2:
        return False
    return True

def can_add_lambs(ranks, totLambs):
    start = ranks[len(ranks) - 1] + ranks[len(ranks) - 2]
    return start <= totLambs

def getMinimum(total_lambs):
    ranks = []
    ranks.append(1)
    currLambs = total_lambs - 1
    while can_add_lambs(ranks, currLambs):
        if len(ranks) > 1:
            add_num = ranks[len(ranks) - 1] + ranks[len(ranks) - 2]
            ranks.append(add_num)
            currLambs -= add_num
        else:
            ranks.append(1)
            currLambs -= 1
    return len(ranks)

def getMaximum(total_lambs):
     ranks = []
     ranks.append(1)
     currLambs = total_lambs - 1
     while can_add_lambs(ranks, currLambs):
         start = ranks[len(ranks) - 1] * 2
         end = ranks[len(ranks) - 1] + ranks[len(ranks) - 2]
         while start >= end:
             if can_add(ranks, start):
                 ranks.append(start)
                 currLambs -= (start)
                 break
             else:
                start -= 1
     return len(ranks)
