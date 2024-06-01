import Foundation

let n = Int(readLine()!)!
var dp = Array(repeating: 0, count: n)
let arr = readLine()!.split(separator: " ").map {Int($0)!}
dp[0] = arr[0]
for i in 1..<n {
    dp[i] = max(arr[i], arr[i] + dp[i-1])
}
print(dp.max()!)
