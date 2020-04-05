#if 1
//BFS -> queue
//refer http://fisherlei.blogspot.com/2013/12/leetcode-clone-graph-solution.html
/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
class Solution {
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        unordered_map<UndirectedGraphNode *, UndirectedGraphNode *>node_map;
        queue<UndirectedGraphNode *>q;

        if (!node) return 0;

        q.push(node);
        node_map[node] = new UndirectedGraphNode(node->label);

        while (!q.empty())
        {
            UndirectedGraphNode *curr = q.front();
            UndirectedGraphNode *new_curr = node_map[curr];
            q.pop();
            for (auto n : curr->neighbors)
            {
                if (!node_map.count(n))
                {
                    node_map[n] = new UndirectedGraphNode(n->label);
                    q.push(n);
                }
                new_curr->neighbors.push_back(node_map[n]);
            }
        }
        return node_map[node];
    }
};
#else 
//recursive solution
//DFS
class Solution {
public:
    unordered_map<UndirectedGraphNode *,UndirectedGraphNode *> created;
    ///although it takes O(n) space but it is the efficent way to search available in C++11...for C++4.8 use map...
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        //not required ..only to be in safe side
        if(!node)return node;
        ///if this node is already created then just return the reference of the new node created earlier
        if(created.count(node))return created[node];
        ///otherwise create a new node and mark corresponding node in original graph created.
        UndirectedGraphNode * t=new UndirectedGraphNode(node->label);
        created[node]=t;
        for(int i=0;i<node->neighbors.size();i++){
            //do recursively for all its neighbors...:)
            t->neighbors.push_back(cloneGraph(node->neighbors[i]));
        }
        return t;
    }
};
#endif

