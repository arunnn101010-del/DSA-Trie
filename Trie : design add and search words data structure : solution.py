# Promblem - design add and search words data structure 
# Time and space complexity - 0(l) & 0(l*n) 
# Leetcode and diffculty level - 211 & medium 
class WordDictionary {
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

    WordDictionary() {
        root = new TrieNode();
    }

    void addWord(string word) {

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

    bool searchHelper(string& word, int i, TrieNode* curr) {

        if(i == word.size())
            return curr->isEnd;

        char c = word[i];

        if(c == '.') {

            for(int j = 0; j < 26; j++) {

                if(curr->children[j] != nullptr) {

                    if(searchHelper(word, i + 1,
                                    curr->children[j]))
                        return true;
                }
            }

            return false;
        }

        int index = c - 'a';

        if(curr->children[index] == nullptr)
            return false;

        return searchHelper(word, i + 1,
                            curr->children[index]);
    }

    bool search(string word) {

        return searchHelper(word, 0, root);
    }
};
