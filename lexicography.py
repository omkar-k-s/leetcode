class Solution(object):
    def largestPower(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)

        # Initially, all elements can be arranged freely
        groups = [nums[:]]

        power = []

        # Process bits from 14 down to 0
        for bit in range(14, -1, -1):

            prefix = 0
            split_done = False

            for i in range(len(groups)):
                group = groups[i]

                ones = []
                zeros = []

                for x in group:
                    if (x >> bit) & 1:
                        ones.append(x)
                    else:
                        zeros.append(x)

                # This entire group can come before the first zero
                if len(zeros) == 0:
                    prefix += len(group)
                    continue

                # This is the first group containing a zero
                power.append(prefix + len(ones))

                new_groups = groups[:i]

                if len(ones) > 0:
                    new_groups.append(ones)

                if len(zeros) > 0:
                    new_groups.append(zeros)

                new_groups.extend(groups[i + 1:])

                groups = new_groups
                split_done = True
                break

            # Every element has this bit set
            if not split_done:
                power.append(n)

        return power