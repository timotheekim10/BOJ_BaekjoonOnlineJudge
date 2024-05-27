import Foundation

var dict: [Int:Int] = [:]
let n = Int(readLine()!)!
var arr1 = readLine()!.split(separator: " ").map {Int($0)!}
for i in arr1 {
    if dict.keys.contains(i) {
        dict[i]! += 1
    } else {
        dict[i] = 1
    }
}
let m = Int(readLine()!)!
var arr2 = readLine()!.split(separator: " ").map {Int($0)!}
for i in arr2 {
    if dict.keys.contains(i) {
        print(dict[i]!, terminator: " ")
    } else {
        print(0, terminator: " ")
    }
}
