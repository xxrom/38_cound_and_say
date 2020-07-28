class Solution:
  def countNextSameChars(self, char: str, index: int, fullStr: str):
    ans = 1
    i = index + 1

    while i < len(fullStr) and fullStr[i] == char:
      ans += 1
      i += 1

    return ans


  def sayIterate(self, currentI: int, endI: int ):
    print(self.ans)

    if currentI > endI:
      return self.ans

    newAns = ''
    i = 0

    while i < len(self.ans):
      char = self.ans[i]

      countChar = self.countNextSameChars(char, i, self.ans)
      newAns += str(countChar) + char

      i += countChar

    self.ans = newAns

    return self.sayIterate(currentI + 1, endI)


  def countAndSay(self, n: int) -> str:
    self.ans = '1'

    return self.sayIterate(2, n)

my = Solution()
n = 5
rightAns = '111221'
ans = my.countAndSay(n)
print("ans", ans, ans == rightAns)

# Runtime: 32 ms, faster than 88.18% of Python3 online submissions for Count and Say.
# Memory Usage: 13.8 MB, less than 60.92% of Python3 online submissions for Count and Say.