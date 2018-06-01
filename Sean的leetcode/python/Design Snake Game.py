###
# Design: HashSet + deque
# Time Complexity: O(1)
# Space Complexity: O(n)
###
class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.snake = collections.deque([(0, 0)])
        self.s = set([(0, 0)])
        self.width = width
        self.height = height
        self.food = food
        self.idx = 0

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        head_r, head_c = self.snake[0]
        tail = self.snake.pop()
        self.s.remove(tail)
        
        if direction == 'U':
            head_r -= 1
        elif direction == 'D':
            head_r += 1
        elif direction == 'L':
            head_c -= 1
        else:
            head_c += 1
        if head_r < 0 or head_r >= self.height or head_c < 0 or head_c >= self.width or (head_r, head_c) in self.s:
            return -1
        
        self.snake.appendleft((head_r, head_c))
        self.s.add((head_r, head_c))
        
        if self.idx < len(self.food) and [head_r, head_c] == self.food[self.idx]:
            self.snake.append(tail)
            self.s.add(tail)
            self.idx += 1
        return len(self.snake) - 1
        
        

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
                                        
                            
                    