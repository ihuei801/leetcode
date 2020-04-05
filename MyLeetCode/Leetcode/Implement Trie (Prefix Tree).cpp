class TrieNode {
public:
    // Initialize your data structure here.
    TrieNode() : isWord(false) {
        child = vector<TrieNode*>(26);
        
    }
    bool isWord;
    vector<TrieNode*> child;
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    void insert(string word) {
        TrieNode* curr = root;
        for (auto c : word) {
            if (!curr->child[c - 'a']) {
                curr->child[c - 'a'] = new TrieNode();
            }
            curr = curr->child[c - 'a'];
        }
        curr->isWord = true;
    }

    // Returns if the word is in the trie.
    bool search(string word) {
        return find(word, true);
        
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    bool startsWith(string prefix) {
        return find(prefix, false);
    }

private:
    TrieNode* root;
    bool find(string word, bool end) {
        TrieNode* curr = root;
        for (auto c : word) {
            if (!curr->child[c-'a']) {
                return false;
            }
            curr = curr->child[c - 'a'];
        }
        return end? curr->isWord : true;
    }
};

// Your Trie object will be instantiated and called as such:
// Trie trie;
// trie.insert("somestring");
// trie.search("key");
//Sean's solution
class TrieNode {
public:
    unordered_map<char, TrieNode*>dict;
    int end;

    // Initialize your data structure here.
    TrieNode() {
        end = 0;
    }
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    void insert(string word) {
        TrieNode *curr = root;
        for (int i = 0; i < word.size(); i++)
        {
            if (!curr->dict.count(word[i]))
                curr->dict[word[i]] = new TrieNode();
            curr = curr->dict[word[i]];
        }
        curr->end = 1;
    }

    // Returns if the word is in the trie.
    bool search(string word) {
        return find(word, 1);
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    bool startsWith(string prefix) {
        return find(prefix, 0);
    }

private:
    TrieNode* root;
    bool find(string s, int is_end)
    {
        TrieNode *curr = root;
        for (int i = 0; i < s.size(); i++)
        {
            if (!curr->dict.count(s[i]))
                return false;
            curr = curr->dict[s[i]];
        }
        return is_end ? curr->end == 1 : true;
    }
};

// Your Trie object will be instantiated and called as such:
// Trie trie;
// trie.insert("somestring");
// trie.search("key");