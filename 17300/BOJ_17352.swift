import Foundation

let n = Int(readLine()!)!
var parent = Array(0...n)

func find_parent(x: Int) -> Int {
    if parent[x] == x {
        return x
    }
    parent[x] = find_parent(x: parent[x])
    return parent[x]
}

func union_parent(x: Int, y: Int) {
    let a = find_parent(x: x)
    let b = find_parent(x: y)
    
    if a < b {
        parent[b] = a
    } else {
        parent[a] = b
    }
}

for _ in 0..<(n-2) {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    let island1 = input[0]
    let island2 = input[1]
    union_parent(x: island1, y: island2)
}

for i in 2...n {
    if find_parent(x: 1) != find_parent(x: i) {
        print(1, i)
        break
    }
}
