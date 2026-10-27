# Aの個数
N = int(input())

# 整数Xの値
X = int(input())

# 複数の数値入力を受け付けるリスト
list_A = list(map(int, input().split()))

Answer = False

for one_A in list_A:
  if (one_A == X):
    Answer = True

if (Answer):
  print('Yes')
else:
  print('No')