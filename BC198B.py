#input
N = input()

#0<=N=<10^9より先頭につく0の最大数は9個
for i in range(10):
     M = "0" * i + N #i個の０を文字列として
     if M==M[::-1]: #ひっくり返す
          print("Yes")
          exit()
print("No")

#スライス　文字列の部分を新しい文字列として取り出す
#s[i:j] ...s[i]からs[j-1]までの並び
#s[i:j:k] ...s[i]からs[j-1]までのkごと並び
#今回はM[::-1]で全てを逆向きに
