class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for operation in operations:                
            
            if operation == '+':
                scores.append(int(scores[-1]) + int(scores[-2]))
            
            elif operation == 'D':
                scores.append(int(scores[-1]) * 2)

            elif operation == 'C':
                scores.pop()

            else:
                scores.append(operation)

        
        total_score = 0
        for score in scores:
            total_score += int(score)
        
        return total_score
