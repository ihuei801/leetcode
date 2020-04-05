class LRUCache{
public:
    LRUCache(int capacity): size(capacity) {
    }
    
    int get(int key) {
        if (table.count(key) == 0) return -1;
        Node* nd = table[key];
        LRUlist.erase(nd->it);
        nd->it = LRUlist.insert(LRUlist.begin(), key);
        return nd->val;
    }
    
    void set(int key, int value) {
        Node* nd;
        if (table.count(key)) {
            nd = table[key];
            nd->val = value;
            LRUlist.erase(nd->it);
            nd->it = LRUlist.insert(LRUlist.begin(), key);
        }
        else {
            if (size == table.size()) {
                int rmkey = LRUlist.back();
                LRUlist.pop_back();
                table.erase(rmkey);
            }
            nd = new Node(value);
            nd->it = LRUlist.insert(LRUlist.begin(), key);
            table[key] = nd;
        }
    }
    struct Node{
        int val;
        list<int>::iterator it;
        Node(int v): val(v){}
    };
    int size;
    unordered_map<int, Node*> table;
    list<int> LRUlist;
};
//Sean's solution
class LRUCache{
public:
    struct Node
    {
        int value;
        list<int>::iterator it;
        Node(int x): value(x) {}
    };

    LRUCache(int capacity) {
        max_size = capacity;
    }

    int get(int key) {
        if (!value_map.count(key))
            return -1;
        else
        {
            Node *n = value_map[key];
            node_list.erase(n->it);
            n->it = node_list.insert(node_list.begin(), key);
            return n->value;
        }
    }

    void set(int key, int value) {
        Node *n;
        if (value_map.count(key))
        {
            n = value_map[key];
            node_list.erase(n->it);
        }
        else
        {
            if (node_list.size() == max_size)
            {
                int k = node_list.back();
                n = value_map[k];
                node_list.erase(n->it);
                value_map.erase(k);
            }
            n = new Node(value);
        }
        n->value = value;
        n->it = node_list.insert(node_list.begin(), key);
        value_map[key] = n;
    }

//we should use list instead of vector for 2 reasons.
//1. vector is continuous memory, insert() will result in re-allocate a whole new memory (bad performance)
//2. memory re-allocate will cause the original key-value stored in m_map invalid.

private:
    int max_size;
    //store key
    list<int>node_list;
    unordered_map<int, Node*>value_map;
};