import Foundation

let w = readLine()!
var result = [".", ".", "#", ".", "."]

for (i, x) in w.enumerated() {
    var s = "#"
    if (i + 1) % 3 == 0 {
        s = "*"
        let endIdx: String.Index = result[2].index(result[2].startIndex, offsetBy: result[2].count-1)
        result[2] = String(result[2][..<endIdx]) + s
    }
    result[0] += ".\(s).."
    result[1] += "\(s).\(s)."
    result[2] += ".\(x).\(s)"
    result[3] += "\(s).\(s)."
    result[4] += ".\(s).."
}

for line in result {
    print(line)
}
