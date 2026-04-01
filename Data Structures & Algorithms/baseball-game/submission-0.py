class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = ['+', 'D', 'C']
        scores = []

        for operation in operations:
            if operation not in ops:
                scores.append(operation)
            
            if operation == '+':
                score1 = int(scores[-1])
                score2 = int(scores[-2])
                scores.append(score1 + score2)

            
            if operation == 'D':
                score = int(scores[-1])
                scores.append(score * 2)

            
            if operation == 'C':
                scores.pop()

        
        total_score = 0
        for score in scores:
            total_score += int(score)
        
        return total_score
