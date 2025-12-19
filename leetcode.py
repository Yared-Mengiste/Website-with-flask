# # # # # class Solution:
# # # # #     def convert_temperature(self, n: int) -> list[str]:
# # # # #         data: list[str] = []
# # # # #         for i in range(1, n):
# # # # #             if i % 3 == 0 and i % 5 == 0:
# # # # #                 data.append('FizzBuzz')
# # # # #             elif i % 3 == 0:
# # # # #                 data.append('Fizz')
# # # # #             elif i % 5 == 0:
# # # # #                 data.append('Buzz')
# # # # #             else:
# # # # #                 data.append(f'{i}')
# # # # #         return data
# # # # #
# # # # #
# # # # # def count(data: list[int]) -> int:
# # # # #     counter: int = 0
# # # # #     if len(data) > 1:
# # # # #         for i in range(len(data) - 1):
# # # # #             for j in range(i + 1, len(data)):
# # # # #                 if data[i] == data[j]:
# # # # #                     counter += 1
# # # # #
# # # # #     return counter
# # # # #
# # # # #
# # # # # ex = []
# # # # # print(bool(ex))
# # # ex2 = [1,1]
# # # ex3 = [1]
# # # ex4 = [1,2,3,1,1,3]
# # # ex5 = [1,2,3,1,8,3]
# # #
# # # # # # for i in range(len(ex4) - 1, 0, -1):
# # # # # #     print(ex4[i])
# # # # # x = 'yared'
# # # # # x.
# # # # #
# # # # # print(ex4 == ex5)
# # # # #
# # # # # # print(max(ex4))
# # # # # # print(min(ex4))
# # # # # #
# # # # # # print(count(ex))
# # # # # # print(count(ex2))
# # # # # # print(count(ex3))
# # # # # # print(count(ex4))
# # # # # #
# # # # # # b = Solution()
# # # # # # a: list = b.convert_temperature(32)
# # # # # #
# # # # # # print(a)
# # # # def check(s, t):
# # # #     temp_a = []
# # # #     temp_b = []
# # # #     s = s.lower()
# # # #     t = t.lower()
# # # #     if 1 <= len(s) <= 200 and len(t) >= 1 and len(t) <= 200:
# # # #         for i in s:
# # # #             if i == '#':
# # # #                 temp_a.pop(-1)
# # # #             elif not i == '#':
# # # #                 temp_a.append(i)
# # # #         print(temp_a)
# # # #         for i in t:
# # # #             if i == '#' and temp_b:
# # # #                 temp_b.pop(-1)
# # # #             elif not i == '#':
# # # #                 temp_b.append(i)
# # # #         print(temp_b)
# # # #         if temp_a == temp_b:
# # # #             return True
# # # #         else:
# # # #             return False
# # # #     else:
# # # #         return False
# # # #
# # # #
# # # # print("y#fo##f", "y#f#o##f".replace('#', '', 8))
# # # #
# # # #
# # # # def removeDuplicates(s):
# # # #     """
# # # #     :type s: str
# # # #     :rtype: str
# # # #     """
# # # #
# # # #     ina = '1'
# # # #     p = []
# # # #     if 1 <= len(s) and len(s) <= 10e5:
# # # #         i = 0
# # # #         while i < len(s):
# # # #             temp = s[i]
# # # #             got = False
# # # #             for j in s[i + 1: len(s)]:
# # # #                 if j == s[i]:
# # # #                     got = True
# # # #                     s = s.replace(j, '', 2)
# # # #                     break
# # # #             if not got:
# # # #                 i = i + 1
# # # #     return s
# # # #
# # # #
# # # # print(removeDuplicates('abbaca'))
# # #     # result = []
# # #     # operation_size = len(operations)
# # #     # if 1 <= operation_size and operation_size <= 10e3:
# # #     #     i = 0
# # #     #     while i < operation_size:
# # #     #         char = operations[i]
# # #     #         result_size = len(result)
# # #     #         if char.isdigit():
# # #     #             result.append(int(char))
# # #     #         elif char == '+':
# # #     #             if result_size > 1:
# # #     #                 result.append(result[-1] + result[-2])
# # #     #         elif char == 'C':
# # #     #             if result_size > 0:
# # #     #                 result.pop(-1)
# # #     #         elif char == 'D':
# # #     #             if result_size > 0:
# # #     #                 result.append(result[-1] * 2)
# # #     #
# # #     # return sum(result)
# # # b = '-2'
# # # print(b.isalpha())
# # #
# # def repeatedCharacter(s):
# #     """
# #     :type s: str
# #     :rtype: str
# #     """
# #     j = s
# #     letters = []
# #     repitition = []
# #     while len(s) > 0:
# #         letters.append(s[0])
# #         s = s.replace(s[0], '')
# #     print(letters)
# #     for letter in range(len(letters)):
# #         repitition.append(j.count(letters[letter]))
# #     print(repitition)
# #     return letters[repitition.index(max(repitition))]
# #
# #
# # a = list('aannnssmm')
# # print(a.count('j'))
# # print(repeatedCharacter(a))
# 
def leftRightDifference( nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    answer = []
    size = len(nums)
    if nums:
        left_sum = [0]
        right_sum = [0]
        for i in range(size - 1):
            left_sum.append(left_sum[i] + nums[i])
            right_sum.append(right_sum[i] + nums[size - i - 1])
        # right_sum.reverse()
        print(left_sum)
        print(right_sum)
        for i in range(size):
            answer.append(left_sum[i] - right_sum[size - 1 - i])
    return answer

data = [10, 4, 8, 3]
print(leftRightDifference(data))
print('a'.islower())
print(sum(data[0:3]))
