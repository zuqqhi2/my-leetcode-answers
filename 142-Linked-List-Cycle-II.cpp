/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Runner {
public:
    int time_count;
    int start_time;
    ListNode *current;

    Runner() : time_count(0) {}

    bool hasNext() { return this->current->next == NULL ? false : true; }

    void Step() {
        this->time_count += 1;
        if (this->time_count >= this->start_time) {
            this->current = this->current->next;
            this->time_count = this->start_time;
        }
    }
};

class Solution {
public:
    const int kNumRunners = 10000;
    ListNode *detectCycle(ListNode *head) {
        // If head is NULL, there is no loop.
        if (head == NULL) { return NULL; }
        // There is no loop when there is only 1 node.
        if (head->next == NULL) { return NULL; }

        // Initialize runners
        Runner runner[kNumRunners];
        for (int i = 0; i < kNumRunners; i++) {
            runner[i].start_time = i + 1;
            runner[i].current = head;
        }

        // Let runners race until fastest runner reaches to other runner.
        while (runner[0].hasNext()) {
            for (int i = 0; i < kNumRunners; i++) { runner[i].Step(); }
            for (int i = 1; i < kNumRunners; i++) {
                if (runner[0].current == runner[i].current) { return runner[0].current; }
            }
        }

        // There is no loop if
        return NULL;
    }
};

// Sample Testcase:
//   Input:
//     head object of a linked list(1:3 -> 2:2 -> 3:0 -> 4:-4 -> 2:2 -> ...)
//   Output:
//     loop head node object

// Performance Result:
//   Runtime: 1248 ms, faster than 5.65% of C++ online submissions for Linked List Cycle II.
//   Memory Usage: 10.1 MB, less than 19.38% of C++ online submissions for Linked List Cycle II.
