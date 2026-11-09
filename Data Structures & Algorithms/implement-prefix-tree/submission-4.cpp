class TrieNode {
public:
    unordered_map<char, TrieNode> children;
    bool endOfWord;
};

class PrefixTree {
private:
    TrieNode root;

public:
    PrefixTree() {
    }
    
    void insert(string word) {
        TrieNode* cur = &root;
        for (const char& c : word) {
            if (cur->children.find(c) == cur->children.end()){
                (cur->children[c]) = TrieNode();
            }
            cur = &(cur->children[c]);
        }
        cur->endOfWord = true;
        return;
    }
    
    bool search(string word) {
        TrieNode* cur = &root;
        for (const char& c: word) {
            if (cur->children.find(c) == cur->children.end()) {
                return false;
            }
            cur = &(cur->children[c]);
        }
        return cur->endOfWord;
    }
    
    bool startsWith(string prefix) {
        TrieNode* cur = &root;
        for (const char& c : prefix) {
            if (cur->children.find(c) == cur->children.end()){
                return false;
            }
            cur = &(cur->children[c]);
        }
        return true;
    }
};
