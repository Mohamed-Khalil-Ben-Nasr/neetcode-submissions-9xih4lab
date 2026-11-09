class TrieNode {
    public:
    unordered_map<char, TrieNode> children;
    bool endOfWord = false;
};
class WordDictionary {
private:
    TrieNode root;
    bool searchHelper(string word, int i, TrieNode* cur) {
        if (i == word.size()) {
            return cur->endOfWord;
        } 
        
        if (word[i] == '.') {
            for (auto& [c, child] : cur->children){
                if (searchHelper(word, i+1, &child)) {
                    return true;
                }
            }
            return false;
        }

        if (cur->children.find(word[i]) == cur->children.end()) {
            return false;
        }

        cur = &cur->children[word[i]];
        return searchHelper(word, i+1, cur);
    }

public:
    WordDictionary() {
        
    }
    
    void addWord(string word) {
        TrieNode* cur = &root;
        for (const char& c : word) {
            if (cur->children.find(c) == cur->children.end()) {
                cur->children[c] = TrieNode();
            }
            cur = &cur->children[c];
        }
        cur->endOfWord = true;
        return;
    }
    
    bool search(string word) {
        TrieNode* cur = &root;
        return searchHelper(word, 0, cur);
    }
};
