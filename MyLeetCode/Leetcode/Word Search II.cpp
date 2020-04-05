//https://leetcode.com/discuss/36660/my-ac-solution-using-trie
//1. construct all words into a trie.
//2. use the trie to compare all possible words in DFS.
class Solution {
public:
    struct TrieNode{
        bool isWord;
        vector<TrieNode*> next;
        TrieNode():isWord(false), next(26){}
    };
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        TrieNode* root = buildTree(words);
        vector<string> re;
        int rows = board.size();
        int cols = rows? board[0].size() : 0;
        if (!rows || !cols) return re;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                string path;
                dfs(board, i, j, root, path, re);
            }
        }
        return re;
    }
    void dfs(vector<vector<char>>& board, int r, int c, TrieNode* root, string& path, vector<string>& re) {
        TrieNode* curr = root->next[board[r][c] - 'a'];
        if (!curr) return;
        int rows = board.size();
        int cols = board[0].size();
        char tmp = board[r][c];
        path += tmp;
        board[r][c] = NULL;
        if (curr->isWord) {
            re.push_back(path);
            curr->isWord = false;
        }
        vector<pair<int, int>> dir = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        for (auto d : dir) {
            int nb_r = r + d.first;
            int nb_c = c + d.second;
            if (nb_r >= 0 && nb_r < rows && nb_c >=0 && nb_c < cols && board[nb_r][nb_c]) {
                dfs(board, nb_r, nb_c, curr, path, re);
            }
        }
        path.pop_back();
        board[r][c] = tmp;
        
    }
    TrieNode* buildTree(vector<string>& words) {
        TrieNode* root = new TrieNode();
        TrieNode* curr;
        for (auto s : words) {
            curr = root;
            int l = s.size();
            for (int i = 0; i < l; i++) {
                if(!curr->next[s[i] - 'a']) {
                    curr->next[s[i] - 'a'] = new TrieNode();
                }
                curr = curr->next[s[i] - 'a'];
            }
            curr->isWord = true;
        }
        return root;
    }
};


class Solution {
public:
    struct TrieNode{
        vector<TrieNode*> table;
        bool is_word;
        TrieNode(): is_word(false), table(26) {}
    };
    void insert(TrieNode* root, string& word) {
        int size = word.size();
        TrieNode* curr = root;
        for (int i = 0; i < size; i++) {
            if (!curr->table[word[i] - 'a']) {
                curr->table[word[i] - 'a'] = new TrieNode();
            }
            curr = curr->table[word[i] - 'a'];
        }
        curr->is_word = true;
    }
    void dfs(TrieNode* root, vector<vector<char>>& board, int r, int c, string& one_sol, vector<string>& res) {
        int rows = board.size();
        int cols = rows? board[0].size() : 0;
        if (!root || r < 0 || c < 0 || r >= rows || c >= cols) return;
        if (!board[r][c] || !root->table[board[r][c] - 'a']) return;
        char ch = board[r][c];
        TrieNode* next = root->table[ch - 'a'];
        one_sol.push_back(ch);
        if (next->is_word) {
            res.push_back(one_sol);
            next->is_word = false;
        }
        board[r][c] = NULL;
        dfs(next, board, r-1, c, one_sol, res);
        dfs(next, board, r+1, c, one_sol, res);
        dfs(next, board, r, c-1, one_sol, res);
        dfs(next, board, r, c+1, one_sol, res);
        one_sol.pop_back();
        board[r][c] = ch;
        
    }
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        vector<string> res;
        int rows = board.size();
        int cols = rows? board[0].size() : 0;
        TrieNode* root = new TrieNode();
        int word_cnt = words.size();
        string one_sol;
        for (int i = 0; i < word_cnt; i++) {
            insert(root, words[i]);
        }
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols && res.size() < word_cnt; j++) {
                dfs(root, board, i, j, one_sol, res);
            }
        }
        return res;
    }
};
//Sean's solution
class Solution {
    struct TrieNode {
        map<char, TrieNode*>table;
        int is_word;
        TrieNode(): is_word(0) {}
    };

    void insert(TrieNode *root, string word)
    {
        TrieNode *curr = root;
        int size = word.size();
        for (int i = 0; i < size; i++)
        {
            if (curr->table.count(word[i]) == 0)
                curr->table[word[i]] = new TrieNode();

            curr = curr->table[word[i]];
        }
        curr->is_word = 1;
    }

    void dfs(TrieNode *root, vector<vector<char>>& board, int row, int col, string &one_sol, vector<string> &res)
    {
        if (!root
            || row < 0
            || col < 0
            || row > board.size()-1
            || col > board[0].size()-1)
            return;

        if (board[row][col] == NULL || !root->table.count(board[row][col]))
            return;

        char t = board[row][col];
        TrieNode *next = root->table[t];

        one_sol.push_back(t);
        if (next->is_word)
        {
            res.push_back(one_sol);
            //set to 0 to prevent duplicate one_sol.
            next->is_word = 0;
        }

        board[row][col] = NULL;

        dfs(next, board, row+1, col, one_sol, res);
        dfs(next, board, row, col+1, one_sol, res);
        dfs(next, board, row-1, col, one_sol, res);
        dfs(next, board, row, col-1, one_sol, res);

        one_sol.pop_back();
        board[row][col] = t;
    }

public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        TrieNode *root = new TrieNode();
        int rows = board.size();
        int cols = board[0].size();
        vector<string>res;
        string one_sol;
        int word_count = words.size();

        //build trie tree
        for (int i = 0; i < word_count; i++)
            insert(root, words[i]);

        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols && res.size() < word_count; j++)
            {
                dfs(root, board, i, j, one_sol, res);
            }
        return res;
    }
};