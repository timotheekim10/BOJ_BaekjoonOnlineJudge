import Foundation

let arr = readLine()!.split(separator: " ").map {Int($0)!}
let n = arr[0]
let m = arr[1]
var graph: [[Int]] = []
for _ in stride(from: 0, to: n, by: 1) {
    graph.append(readLine()!.split(separator: " ").map {Int($0)!})
}
var dp: [[Int]] = Array(repeating: Array(repeating: 0, count: m+1), count: n+1)
for i in stride(from: 1, to: n+1, by: 1) {
    for j in stride(from: 1, to: m+1, by: 1) {
        dp[i][j] = graph[i-1][j-1] + max(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
    }
}
print(dp[n][m])
