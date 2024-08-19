class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        def _quick_select_(nums, k):
            left, mid, right = [],[], []
            pivo = random.choice(nums)

            # Partindo os numeros com o pivo
            for num in nums:
                if int(num) > int(pivo):
                    left.append(num)
                elif int(num) < int(pivo):
                    right.append(num)
                else:
                    mid.append(num)
                    
            # Verifica a posição do k-ésimo maior número
            
            if k <= len(left):
                return _quick_select_(left, k)

            if k > len(left) + len(mid):
                return _quick_select_(right, k - len(left) - len(mid))

            return pivo
        
        return _quick_select_(nums, k)