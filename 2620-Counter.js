/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    var value = n;
    return function() {
        let prev = value;
        value += 1;
        return prev;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */

// Performance Result:
//   Coding Time: 00:02:04
//   Time Complexity: O(1)
//   Space Complexity: O(1)
//   Runtime: 48 ms, faster than 14.66%
//   Memory Usage: 53.20 MB, less than 73.84%