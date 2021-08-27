const readline = require('readline');
const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let input = []

r1.on("line", (data) => {
    input.push(data.toString())
}).on("close", () => {
    let n = parseInt(input.shift())
    let m = parseInt(input.shift())
    let graph = Array.from(Array(n + 1), () => Array())
    let visited = Array.from(Array(n + 1).fill(false))
    let cnt = 0;

    for (let i of input) {
        let [x, y] = i.split(' ').map(Number)
        graph[x].push(y)
        graph[y].push(x)
    }

    const bfs = (start) => {
        visited[start] = true
        let q = [start]
        while (q.length > 0) {
            let num = q.shift()
            for (let i of graph[num]) {
                if (visited[i] === false) {
                    visited[i] = true
                    q.push(i)
                    cnt += 1
                }
            }
        }
    }
    bfs(1)

    console.log(cnt)
})