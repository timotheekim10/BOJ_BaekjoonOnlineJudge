import Foundation

let nm = readLine()!.split(separator: " ").map {Int($0)!}
let n = nm[0]
let m = nm[1]

var graph = [[Int]](repeating: [], count: n + 1)
var pre = [Int](repeating: 0, count: n + 1)

for _ in 0..<m {
    let ab = readLine()!.split(separator: " ").map {Int($0)!}
    let a = ab[0]
    let b = ab[1]
    graph[a].append(b)
    pre[b] += 1
}

var ans = [Int](repeating: 0, count: n + 1)

var queue = [(Int, Int)]()
for i in 1...n {
    if pre[i] == 0 {
        queue.append((i, 1))
    }
}

var idx = 0
while idx < queue.count {
    let (node, cnt) = queue[idx]
    idx += 1
    ans[node] = cnt
    for i in graph[node] {
        pre[i] -= 1
        if pre[i] == 0 {
            queue.append((i, cnt + 1))
        }
    }
}

for i in 1...n {
    print(ans[i], terminator: " ")
}
