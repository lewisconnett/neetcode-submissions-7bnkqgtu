class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for operation in operations:                
            
            if operation == '+':
                score1 = int(scores[-1])
                score2 = int(scores[-2])
                scores.append(score1 + score2)
            
            elif operation == 'D':
                score = int(scores[-1])
                scores.append(score * 2)

            elif operation == 'C':
                scores.pop()

            else:
                scores.append(operation)

        
        total_score = 0
        for score in scores:
            total_score += int(score)
        
        return total_score
