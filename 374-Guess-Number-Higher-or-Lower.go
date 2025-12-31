/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * func guess(num int) int;
 */

func guessNumber(n int) int {
	left, right, mid := 1, n, n/2
	for left <= right {
		mid = (left + right) >> 1
		if g := guess(mid); g == -1 {
			right = mid - 1
		} else if g == 1 {
			left = mid + 1
		} else {
			break
		}
	}
	return mid
}

// Performance Result:
//   Coding Time: 00:19:32
//   Time Complexity: O(log N)
//   Space Complexity: O(1)
//   Runtime: 1 ms, faster than 68.54%
//   Memory Usage: 3.81 MB, less than 14.08%