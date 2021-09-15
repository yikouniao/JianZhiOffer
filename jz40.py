# https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        topk = k
        if k == 0 or n == 0:
            return []

        i = n // 2
        while i > 0:
            self.adjust(arr, n, i)
            i -= 1

        while k > 0:
            self.swap(arr, 1, n)
            n -= 1
            self.adjust(arr, n, 1)
            k -= 1

        return arr[-topk:]

    def adjust(self, arr, length, i):
        if 2 * i > length or i <= 0 or length <= 0:
            return
        elif 2 * i + 1 > length or arr[2 * i - 1] < arr[2 * i]:
            if arr[2 * i - 1] < arr[i - 1]:
                self.swap(arr, i, 2 * i)
                self.adjust(arr, length, i * 2)
        elif arr[2 * i] < arr[i - 1]:
            self.swap(arr, i, 2 * i + 1)
            self.adjust(arr, length, 2 * i + 1)
        return

    def swap(self, arr, i, j):
        t = arr[i - 1]
        arr[i - 1] = arr[j - 1]
        arr[j - 1] = t
