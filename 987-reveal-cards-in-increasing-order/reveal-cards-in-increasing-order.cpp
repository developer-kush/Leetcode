class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        sort(deck.begin(), deck.end());

        deque<int> range;
        for (int i = 0; i < deck.size(); i++){
            range.push_back(i);
        }

        vector<int> order;

        for (int i = 0; i < deck.size(); i++){
            order.push_back(range.front());
            range.pop_front();
            if (range.size()){
                range.push_back(range.front());
                range.pop_front();
            }
        };

        vector<int> res(deck.size());
        for (int i = 0; i < deck.size(); i++) res[order[i]] = deck[i];
        return res;
    }
};