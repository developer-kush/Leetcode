class Solution {
public:

    bool isBipartite(vector<vector<int>>& graph) {
        unordered_map<int, int> visited;
        stack<pair<int, int>> st;

        for (int startNode=0; startNode < graph.size(); startNode ++){
            if (visited.find(startNode) != visited.end()) continue;

            visited[startNode] = 0;
            st.push({startNode, 0});
            while (!st.empty()){
                pair<int, int> curr = st.top(); st.pop();
                int node = curr.first, dist = curr.second;

                for (auto ne: graph[node]){
                    if (visited.find(ne)==visited.end()){
                        visited[ne] = dist+1;
                        st.push({ne, dist+1});
                    } else if ((visited.at(ne)-dist+1)&1) {
                        return false;
                    }
                }
            }
        }

        return true;
    }
};