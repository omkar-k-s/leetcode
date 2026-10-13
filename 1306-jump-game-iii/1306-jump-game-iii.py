class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        if start<0 or start >=len(arr) or arr[start]<0:
            return False

        if arr[start]==0:
            return True

        step=arr[start]
        arr[start]=-arr[start]

        return self.canReach(arr,start+step)or self.canReach(arr,start-step)