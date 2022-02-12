/**
 * @param {string} s
 * @return {string}
 */
var replaceDigits = function(s) {
    let res = '';
    for (let i = 0; i < s.length; i += 2) {
        res += s[i];
        if (i == s.length - 1) { continue; }
        res += String.fromCharCode(s.charCodeAt(i) + Number(s[i + 1]));
    }

    return res;
};


// Performance Result:
//   Coding Time: 00:12:23
//   Time Complexity: O(N)
//   Space Complexity: O(N)
//   Runtime: 92 ms, faster than 55.55%
//   Memory Usage: 42.4 MB, less than 7.57%
