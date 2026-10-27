days = int(input())
attend_people = int(input())

# left = [None, None, None]という形でリストができる
left = [ None ] * attend_people
right = [ None ] * attend_people

for people in range(attend_people):
  left[people], right[people] = map(int, input().split())

# 初期値と終端を設定
# 例 days = 7の場合、0は初期値, 8は7日目の翌日
BeforeRs = [0] * (days + 2)
for p in range(attend_people):
  BeforeRs[left[p]] += 1
  BeforeRs[right[p] + 1] -= 1 # 減少の始まり

Answer = [ None ] * (days + 2)
Answer[0]  = 0
for d in range(1, days + 1):
  Answer[d] = Answer[d - 1] + BeforeRs[d]

for d in range(1, days + 1):
	print(Answer[d])