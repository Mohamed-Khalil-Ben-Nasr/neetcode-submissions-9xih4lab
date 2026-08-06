class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            # collision only happens if stack[-1] is moving right and the new asteroid is moving left
            if (stack and stack[-1] > 0 and asteroid< 0):
                if abs(asteroid) == stack[-1]:
                    stack.pop()
                    continue
                elif abs(asteroid) > stack[-1]:
                    while stack and stack[-1] > 0 and abs(asteroid) >   stack[-1]:
                        stack.pop()
                    if stack and abs(asteroid) < stack[-1]:
                        continue
                    elif stack and abs(asteroid) == stack[-1]:
                        stack.pop()
                    else:
                        stack.append(asteroid)
            else:
                stack.append(asteroid)
        return stack