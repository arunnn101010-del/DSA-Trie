# Promblem - search suggestion system 
# approach - dfs + tree 
# Leetcode and diffculty level - 1268 & easy 
class Solution {
public:

    struct TrieNode {
        TrieNode* children[26];
        bool isEnd;

        TrieNode() {
            isEnd = false;

            for(int i = 0; i < 26; i++)
                children[i] = nullptr;
        }
    };

    TrieNode* root;

    void insert(string word) {

        TrieNode* curr = root;

        for(char c : word) {

            int index = c - 'a';

            if(curr->children[index] == nullptr)
                curr->children[index] = new TrieNode();

            curr = curr->children[index];
        }

        curr->isEnd = true;
    }

    void dfs(TrieNode* curr, string& path,
             vector<string>& result) {

        if(result.size() == 3)
            return;

        if(curr->isEnd)
            result.push_back(path);

        for(int i = 0; i < 26; i++) {

            if(curr->children[i] != nullptr) {

                path.push_back('a' + i);

                dfs(curr->children[i], path, result);

                path.pop_back();
            }
        }
    }

    vector<vector<string>> suggestedProducts(
        vector<string>& products,
        string searchWord) {

        root = new TrieNode();

        sort(products.begin(), products.end());

        for(string product : products)
            insert(product);

        vector<vector<string>> ans;

        TrieNode* curr = root;
        string path = "";

        for(char c : searchWord) {

            int index = c - 'a';

            if(curr != nullptr &&
               curr->children[index] != nullptr) {

                curr = curr->children[index];

                path.push_back(c);

                vector<string> result;

                dfs(curr, path, result);

                ans.push_back(result);
            }
            else {

                curr = nullptr;

                ans.push_back({});
            }
        }

        return ans;
    }
};


