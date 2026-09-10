# Promblem - implement trie 
# Approach - trie 
# Leetcode and diffculty level - 208 & easy 
class Trie {
public:

    struct TrieNode {
        TrieNode* children[26];
        bool isEnd;

        TrieNode() {
            isEnd = false;

            for(int i = 0; i < 26; i++) {
                children[i] = nullptr;
            }
        }
    };

    TrieNode* root;

    Trie() {
        root = new TrieNode();
    }

    void insert(string word) {

        TrieNode* curr = root;

        for(char c : word) {

            int index = c - 'a';

            if(curr->children[index] == nullptr) {
                curr->children[index] = new TrieNode();
            }

            curr = curr->children[index];
        }

        curr->isEnd = true;
    }

    bool search(string word) {

        TrieNode* curr = root;

        for(char c : word) {

            int index = c - 'a';

            if(curr->children[index] == nullptr)
                return false;

            curr = curr->children[index];
        }

        return curr->isEnd;
    }

    bool startsWith(string prefix) {

        TrieNode* curr = root;

        for(char c : prefix) {

            int index = c - 'a';

            if(curr->children[index] == nullptr)
                return false;

            curr = curr->children[index];
        }

        return true;
    }
};
