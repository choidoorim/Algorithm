function solution(progresses, speeds) {
    let answer = [];
    let days = 1;
    let count = 0;
    while (progresses.length > 0) {
        if (progresses[0] + (speeds[0] * days) >= 100) {
            progresses.shift()
            speeds.shift()
            count += 1
        } else {
            if (count > 0) {
                answer.push(count)
                count = 0
            }
            days += 1;
        }
    }

    answer.push(count)
    return answer;
}


console.log(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))