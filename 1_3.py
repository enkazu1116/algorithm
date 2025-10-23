# 入力内容の定義
card_max, sum = map(int, input().split())
red_card = list(map(int, input().split()))
blue_card = list(map(int, input().split()))

Answer = False

for choice_red_card in red_card:
  for choice_blue_card in blue_card:
    if (choice_red_card + choice_blue_card == 30):
      Answer = True

if (Answer == True):
  print('Yes')
else:
  print('No')