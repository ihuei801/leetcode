class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string res;
        for (auto s : strs)
            res += to_string(s.size())+"#"+s;
        return res;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> res;
        int pos = 0;
        while (pos < s.size()) {
            int end = s.find_first_of('#', pos);
            int len = stoi(s.substr(pos, end - pos));
            res.push_back(s.substr(end + 1, len));
            pos = end + 1 + len;
        }
        return res;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));