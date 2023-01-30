class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def deepFirstSearch(i, cur, total):
            if total == target:
                result.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            deepFirstSearch(i, cur, total + candidates[i])
            cur.pop()
            deepFirstSearch(i+1, cur, total)


        deepFirstSearch(0, [], 0)
        return result

            
