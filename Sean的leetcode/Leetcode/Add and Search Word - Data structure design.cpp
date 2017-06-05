class WordDictionary {
public:
    struct TrieNode
    {
        unordered_map<char, TrieNode*>dict;
        int end;
        TrieNode(): end(0) {}
    };

    TrieNode *root = new TrieNode();

    // Adds a word into the data structure.
    void addWord(string word) {
        TrieNode *curr = root;
        for (auto c : word)
        {
            if (!curr->dict.count(c))
                curr->dict[c] = new TrieNode();
            curr = curr->dict[c];
        }
        curr->end = 1;
    }

    bool find(string s, int start_index, TrieNode *root)
    {
        if (s.size() == start_index && root->end)
            return true;

        if (root->dict.count(s[start_index]))
            return find(s, start_index+1, root->dict[s[start_index]]);

        if (s[start_index] == '.')
        {
            for (auto m : root->dict)
                if (find(s, start_index+1, m.second))
                    return true;
        }
        return false;
    }

    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    bool search(string word) {
        return find(word, 0, root);
    }
};

// Your WordDictionary object will be instantiated and called as such:
// WordDictionary wordDictionary;
// wordDictionary.addWord("word");
// wordDictionary.search("pattern");