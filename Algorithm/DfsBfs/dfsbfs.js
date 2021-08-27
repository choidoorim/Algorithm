const readline = require('readline');
const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let input = []
let graph = []
let visited_DFS = []
let visited_BFS = []
let dfs_result = []
let bfs_result = []

r1.on("line", (data)=> {
    input.push(data.toString())
}).on("close", ()=>{
    let [n, m, num] = input.shift().split(' ').map(el => parseInt(el))

    graph = Array.from(Array(n + 1), () => Array())

    for (i of input) {
        let [x, y] = i.split(' ').map(el => parseInt(el))
        graph[x].push(y)
        graph[y].push(x)
    }

    // 작은 수 부터 방문하기 때문에 정렬
    for (let i = 0; i < graph.length; i++) {
        graph[i].sort()
    }

    visited_DFS = Array(n + 1).fill(false)
    visited_BFS = Array(n + 1).fill(false)

    const dfs = (start, graph, visited) => {
        visited[start] = true
        dfs_result.push(start)
        for (let i of graph[start]) {
            if (visited[i] === false) {
                dfs(i, graph, visited)
            }
        }
    }

    const bfs = (start, graph, visited) => {
        visited[start] = true
        let q = [start]
        while (q.length > 0) {
            start = q.shift()
            bfs_result.push(start)
            for (let i of graph[start]) {
                if (visited[i] === false) {
                    q.push(i);
                    visited[i] = true;
                }
            }
        }
    }
    dfs(num, graph, visited_DFS)
    bfs(num, graph, visited_BFS)
    console.log(dfs_result);
    console.log(bfs_result);
    process.exit()
})
