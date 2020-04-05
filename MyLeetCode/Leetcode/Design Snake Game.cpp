//set: every position of the snake
//deque: position of the snake
class SnakeGame {
public:
    /** Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0]. */
    int w;
    int h;
    int pos;
    vector<pair<int, int>> food;
    set<pair<int, int>> hist;
    list<pair<int, int>> snake;
    SnakeGame(int width, int height, vector<pair<int, int>> food) : w(width), h(height), pos(0) {
        this->food = food;
        hist.insert(make_pair(0, 0));
        snake.push_back(make_pair(0,0));
    }
    
    /** Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body. */
    int move(string direction) {
        int h_row = snake.front().first;
        int h_col = snake.front().second;
        pair<int, int> tail = snake.back();
        snake.pop_back();
        hist.erase(tail);
        if (direction == "U") {
            h_row--;
        }
        else if (direction == "D") {
            h_row++;
        }
        else if (direction == "L") {
            h_col--;
        }
        else {
            h_col++;
        }
        
        if (h_row < 0 || h_col < 0 || h_row >= h || h_col >= w || hist.count(make_pair(h_row, h_col))) {
            return -1;
        }
        snake.push_front(make_pair(h_row, h_col));
        hist.insert(make_pair(h_row, h_col));
        if (pos >= food.size()) {
            return snake.size() - 1;
        }
        
        if (h_row == food[pos].first && h_col == food[pos].second) {
            pos++;
            snake.push_back(tail);
            hist.insert(tail);
        }
        return snake.size() - 1;
    }
};

/**
 * Your SnakeGame object will be instantiated and called as such:
 * SnakeGame obj = new SnakeGame(width, height, food);
 * int param_1 = obj.move(direction);
 */