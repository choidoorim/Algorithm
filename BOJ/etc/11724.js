const readline = require('readline');
const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let input = []

r1.on("line", (data) => {
    input.push(data.toString());
}).on("close", () => {
    let [n, m] = input.shift().split(' ').map(Number);
    let visited = Array(n + 1).fill(false);

    let graph = Array.from(Array(n + 1), () => Array());
    for (let i of input) {
        let [x, y] = i.split(' ').map(Number);
        graph[x].push(y)
        graph[y].push(x)
    }

    const bfs = (start) => {
        let q = [start]
        while (q.length > 0) {
            start = q.shift()
            for (let i of graph[start]){
                if (visited[i] === false) {
                    visited[i] = true
                    q.push(i)
                }
            }
        }
    }

    let cnt = 0
    for (let j = 1; j < n + 1; j++) {
        if (visited[j] === false) {
            bfs(j)
            cnt += 1
        }
    }

    console.log(cnt)
})