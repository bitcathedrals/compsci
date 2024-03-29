class Entry:
    def __init__(self, digit):
        self.digit = digit
        self.count = 1

    def inc(self):
        self.count += 1
    
    def __lt__(self, b):
        return self.count < b.count
        
class Solution:
    def find_small_values_set(self, ordered, target_value, larger_index):
        sum = ordered[larger_index].count
        
        count = 1
        smaller_index = 0
        
        while sum < target_value and smaller_index < larger_index:
            smaller_value = ordered[smaller_index].count
                
            sum += smaller_value
            count += 1
            smaller_index += 1
        
        if sum >= target_value:
            return count
        
        return 0
    
    def find_larger_values_set
    
    def minimum_to_remove_half(self, ordered, target):
        if len(ordered) == 1:
            return 1
        
        target = target // 2
        
        largest_index = len(ordered) - 1
        
        result = 0
        
        while largest_index > 0:
            set_size = self.find_small_values_set(ordered, target, largest_index)
            
            print("set size is: " + str(set_size))
            
            if set_size > 0:
                if result > 0:
                    result = min(result, set_size)
                else:
                    result = set_size
                    
            largest_index -= 1
        
        return result
    
    def minSetSize(self, arr: List[int]) -> int:
        # initialize result to zero
        result = 0
        
        # corner case: no input, return immediately
        if not arr:
            return result
        
        table = dict()
        
        # build a structure that is the digit value plus the count
        # of elements.
        for digit in arr:
            if digit in table:
                table[digit].inc()
            else:
                table[digit] = Entry(digit)
        
        
        ordered = sorted(table.values())
            
        result = self.minimum_to_remove_half(ordered, len(arr))
        
        return result
