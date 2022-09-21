def maxFrequency(self, A, k):
        i = 0
        A.sort()
        for j in xrange(len(A)):
            k += A[j]
            if k < A[j] * (j - i + 1):
                k -= A[i]
                i += 1
        return j - i + 1
