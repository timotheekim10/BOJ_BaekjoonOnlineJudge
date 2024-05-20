import Foundation

func backtracking(s: [Int], arr: inout [Int], k: Int, idx: Int) {
    if arr.count == 6 {
        print(arr.map { String($0) }.joined(separator: " "))
        return
    }
    
    for i in stride(from: idx, to: k, by: 1) {
        arr.append(s[i])
        backtracking(s: s, arr: &arr, k: k, idx: i+1)
        arr.removeLast()
    }
}

while true {
    let input = readLine()!.split(separator: " ").map {Int($0)!}
    let k = input[0]
    let s = Array(input[1...])
    if k == 0 {
        exit(0)
    }
    var arr: [Int] = []
    backtracking(s: s, arr: &arr, k: k, idx: 0)
    print()
}
