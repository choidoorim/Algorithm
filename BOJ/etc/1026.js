const readline = require('readline');
const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let input = []

r1.on("line", (data) => {
    input.push(data.toString())
}).on("close", () => {
    const n = parseInt(input.shift())
    let A = input.shift().split(' ').map(el => parseInt(el)).sort((a, b) => a - b)
    let B = input.shift().split(' ').map(el => parseInt(el)).sort((a, b) => b - a)
    let result = 0
    for (let i = 0; i < n; i++) {
        result += A[i] * B[i]
    }
    console.log(result)
})