"""
自分の答え
"""
# input
all_days, questions            = map(int, input().split())
list_num_people                 = list(map(int, input().split()))
first_day_start, first_day_end  = map(int, input().split())
last_day_start, last_day_end    = map(int, input().split())

list_sum = []
sum = 0
for index in range(len(list_num_people)):
  oneday_people = list_num_people[index]
  sum += oneday_people
  list_sum.append(sum)

answers_num = list_sum[first_day_end] - list_sum[first_day_start]
print(answers_num)

"""
正解ver
"""
# input
all_days, questions = map(int, input().split())
list_num_people = list(map(int, input().split()))

# make prefix sum with a leading 0 to handle 1-indexed ranges safely
prefix_sum = [0]
running_sum = 0
for oneday_people in list_num_people:
    running_sum += oneday_people
    prefix_sum.append(running_sum)

# answer each query
for _ in range(questions):
    L, R = map(int, input().split())  # 1-indexed
    # sum in [L, R] = prefix_sum[R] - prefix_sum[L - 1]
    print(prefix_sum[R] - prefix_sum[L - 1])
