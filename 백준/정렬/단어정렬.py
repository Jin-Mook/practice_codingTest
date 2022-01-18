# 단어의 길이가 50이하이기 때문에 길이가 51인 리스트를 만든다.
# 이후 각 원소별로 사전순으로 나열한 리스트를 만들어준다.
import sys
n = int(input())

word_list = [[] for _ in range(n+1)]

for _ in range(n):
  word = input()
  length = len(word)

  word_list[length].append(word)

for words in word_list:
  if words == []:
    continue
  set_words = set(words)
  words = list(set_words)
    
  words.sort()
  for word in words:
    print(word)

#  다른 사람 풀이
 
n = int(input())
word_list = []

for _ in range(n):
  word_list.append(sys.stdin.readline().strip())

set_list = set(word_list)
word_list = list(set_list)

word_list.sort()
word_list.sort(key= len)

print(word_list)

# 또 다른 사람 풀이
import sys
word=set()
for i in range(int(input())):
    word.add(sys.stdin.readline().rstrip())
word=list(word)
word.sort()
word.sort(key=lambda x:len(x))
print("\n".join(word))