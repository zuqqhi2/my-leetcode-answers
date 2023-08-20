func countStudents(students []int, sandwiches []int) int {
    for {
        isTaken := false
        for i, v := range students {
            if v == sandwiches[0] {
                if i + 1 >= len(students) {
                    students = students[:i]
                } else {
                    students = append(students[:i], students[i+1:]...)
                }
                sandwiches = sandwiches[1:]
                isTaken = true
                break
            }
        }
        if !isTaken {
            break
        }
    }

    return len(students)
}

// Performance Result:
//   Coding Time: 00:18:25
//   Time Complexity: O(n^2)
//   Space Complexity: O(1)
//   Runtime: 2 ms, faster than 75.00%
//   Memory Usage: 2.2 MB, less than 100.00%
