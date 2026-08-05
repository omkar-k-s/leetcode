def merge(intervals):

    intervals.sort()

    result = [intervals[0]]

    for current in intervals[1:]:

        last = result[-1]

        if current[0] <= last[1]:

            last[1] = max(last[1], current[1])

        else:

            result.append(current)

    return result


intervals = [[1,3],[2,6],[8,10],[15,18]]

print(merge(intervals))