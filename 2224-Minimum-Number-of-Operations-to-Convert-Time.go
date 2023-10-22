import (
    "strings"
    "strconv"
)

func convertTime(current string, correct string) int {
    operations := [4]int{60, 15, 5, 1}
    numOperations := 0

    curTime := strings.Split(current, ":")
    curHour, _ := strconv.Atoi(curTime[0])
    curMin, _ := strconv.Atoi(curTime[1])

    targetTime := strings.Split(correct, ":")
    targetHour, _ := strconv.Atoi(targetTime[0])
    targetMin, _ := strconv.Atoi(targetTime[1])

    for _, op := range operations {
        for true {
            nextHour := curHour
            nextMin := curMin

            nextMin = nextMin + op
            if nextMin >= 60 {
                nextMin = nextMin - 60
                nextHour++
            }

            if nextHour * 100 + nextMin <= targetHour * 100 + targetMin {
                curHour = nextHour
                curMin = nextMin
                numOperations++
            } else {
                break
            }
        }
    }

    return numOperations
}


// Performance Result:
//   Coding Time: 00:21:09
//   Time Complexity: O(n)
//   Space Complexity: O(1)
//   Runtime: 2 ms, faster than 53.85%
//   Memory Usage: 2.04 MB, less than 7.69%
