/**
 * IntFreq have an integer value and its frequency
 */
typedef struct _intfreq {
    int value;
    int frequency;
} IntFreq;

/**
 * Original Heap tree class having integer value and it's frequency as node value
 */
class BinHeapTree {
private:
    IntFreq *int_freqs;
    int size; // Size of int_freqs

    // Swap int_freqs element between idx1 and idx2
    void swap(int idx1, int idx2) {
        IntFreq temp = this->int_freqs[idx1];
        this->int_freqs[idx1] = this->int_freqs[idx2];
        this->int_freqs[idx2] = temp;
    }

public:
    // Create initial heap tree
    BinHeapTree(unordered_map<int, int> int_freq_map) {
        // Initialize
        this->size = 0;
        this->int_freqs = new IntFreq[int_freq_map.size()];
        for (auto itr = int_freq_map.begin(); itr != int_freq_map.end(); itr++) {
            // Insert new integer
            this->push(itr->first, itr->second);
        }
    }

    // Free allocated memory of int_freqs
    ~BinHeapTree() {
        delete[] this->int_freqs;
    }

    // Insert new element to heap
    void push(int value, int freq) {
        this->int_freqs[this->size] = { value, freq };
        this->size += 1;
        if (this->size <= 1) { return; }

        // Reconstruction
        int inserted_idx = this->size - 1;
        int cur_inserted_idx = inserted_idx;
        while (cur_inserted_idx != 0) {
            // if child freq is higher than parent one, swap them
            int cur_parent_idx = (cur_inserted_idx - 1) / 2;
            if (this->int_freqs[cur_parent_idx].frequency < this->int_freqs[cur_inserted_idx].frequency) {
                this->swap(cur_parent_idx, cur_inserted_idx);
            }
            cur_inserted_idx = cur_parent_idx;
        }
    }

    int pop() {
        // 1st element is always max
        int max_freq_num = this->int_freqs[0].value;

        // Re-organize
        this->int_freqs[0] = this->int_freqs[this->size - 1];
        int cur_parent_idx = 0;
        int cur_child_idx = 2 * cur_parent_idx + 1;
        while (cur_child_idx < this->size - 1) {
            // Use highest child for swapping with parent
            if (cur_child_idx != this->size - 2
                && this->int_freqs[cur_child_idx].frequency < this->int_freqs[cur_child_idx + 1].frequency) {
                cur_child_idx += 1;
            }
            // if child freq is higher than parent one, swap them
            if (this->int_freqs[cur_parent_idx].frequency < this->int_freqs[cur_child_idx].frequency) {
                this->swap(cur_parent_idx, cur_child_idx);
            }
            // Go to next level
            cur_parent_idx = cur_child_idx;
            cur_child_idx = 2 * cur_parent_idx + 1;
        }
        // Reduce tree size
        this->size -= 1;

        return max_freq_num;
    }

    // This is for debug
    void printHeapTree() {
        printf("[%d: %d", this->int_freqs[0].value, this->int_freqs[0].frequency);
        for (int cur_idx = 1; cur_idx < this->size; cur_idx++) {
            printf(", %d: %d", this->int_freqs[cur_idx].value, this->int_freqs[cur_idx].frequency);
        }
        printf("]\n");
    }
};

class Solution {
public:
    /**
     * Time Complexity : O(nlogn)
     * Space Complexity: O(n)
     */
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Create integer and its frequency pairs
        unordered_map<int, int> int_freq_map;
        for (int cur_idx = 0; cur_idx < nums.size(); cur_idx++) {
            // Initialize for new integer
            if (int_freq_map.find(nums[cur_idx]) == int_freq_map.end()) {
                int_freq_map[nums[cur_idx]] = 1;
            } else {
                int_freq_map[nums[cur_idx]] += 1;
            }
        }

        // Create heap tree
        BinHeapTree heap(int_freq_map);

        // Pop k most frequent elements from heap
        vector<int> result;
        for (int num = 0; num < k; num++) result.push_back(heap.pop());

        return result;
    }
};

// Sample Testcase:
//   Input:
//     nums = [1,1,1,2,2,3]
//     k = 2
//   Output:
//     [1, 2]

// Performance Result:
//   Coding Time: 1:38:20
//   Runtime: 24 ms, faster than 60.89% of C++ online submissions for Top K Frequent Elements.
//   Memory Usage: 11.8 MB, less than 13.26% of C++ online submissions for Top K Frequent Elements.
