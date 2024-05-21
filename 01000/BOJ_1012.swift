import Foundation

let dx = [1, -1, 0, 0]
let dy = [0, 0, 1, -1]

func bfs(graph: inout [[Int]], sx: Int, sy: Int) {
    var q = [(sx, sy)]
    var p = [[sx, sy]]
    graph[sx][sy] = 0
    while !q.isEmpty {
        let (x, y) = q.removeFirst()
        for i in 0..<4 {
            let nx = x + dx[i]
            let ny = y + dy[i]
            if 0<=nx && nx<graph.count && 0<=ny && ny<graph[0].count && graph[nx][ny]==1 {
                q.append((nx, ny))
                graph[nx][ny] = 0
            }
        }
    }
}

let t = Int(readLine()!)!

for _ in 0 ..< t {
    let input = readLine()!.split(separator: " ").map {Int($0)!}
    let m = input[0]
    let n = input[1]
    let k = input[2]
    
    var graph = Array(repeating: Array(repeating: 0, count: m), count: n)
    for i in 0..<k {
        let cabbage = readLine()!.split(separator: " ").map {Int($0)!}
        graph[cabbage[1]][cabbage[0]] = 1
    }
    
    var ans = 0
    
    for i in 0..<n {
        for j in 0..<m {
            if graph[i][j] == 1 {
                bfs(graph: &graph, sx: i, sy: j)
                ans += 1
            }
        }
    }
    
    print(ans)
}
