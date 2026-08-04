class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # def sorting_two_pointers():
        #     # time: nlogn
        #     # space: n
        #     people.sort()
        #     l, r = 0, len(people) - 1
        #     count = 0
        #     while l <= r:
        #         free = limit - people[r]
        #         count += 1
        #         r -= 1
        #         if l <= r and free >= people[l]:
        #             l+=1
            
        #     return count
        
        # return sorting_two_pointers()

        def counting_sort():
            m = max(people)
            n = len(people)
            count = [0] * (m+1)
            for i in range(n):
                count[people[i]] += 1
            
            idx, i = 0, 1
            while idx < n:
                while count[i] == 0:
                    i+=1
                
                people[idx] = i
                count[i]-=1
                idx+=1
            
            l, r = 0, n-1
            out = 0
            while l <= r:
                free = limit - people[r]
                r-=1
                out+=1
                if l <= r and free >= people[l]:
                    l+=1
            
            return out

        return counting_sort()

                
