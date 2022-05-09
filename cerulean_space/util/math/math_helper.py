class MathHelper:
    @staticmethod
    def max(a, b):
        if a > b: return a
        return b

    @staticmethod
    def min(a, b):
        if a < b: return a
        return b

    @staticmethod
    def cutoff(a, threshold, cut_to_val):
        if a < threshold:
            return cut_to_val
        return a

    @staticmethod
    def abs(v):
        if v < 0:
            return -v
        return v
