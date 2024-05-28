import Foundation

let input = readLine()!.split(separator: " ").map {Int($0)!}
let n = input[0]
let m = input[1]

let arr1 = readLine()!.split(separator: " ").map {Int($0)!}

let arr2 = readLine()!.split(separator: " ").map {Int($0)!}

var ans = 0
for i in arr1[..<m] {
    if !arr2.contains(i) {
        ans += 1
    }
}
print(ans)
