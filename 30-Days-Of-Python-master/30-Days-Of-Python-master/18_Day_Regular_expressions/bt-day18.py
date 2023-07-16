        #LEVEL 1
import re
#bài tập 1
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
word_lst = paragraph.split(' ')
word_lst = [word.strip('.') for word in word_lst]
count_dict = {}
for word in word_lst:
    if word in count_dict:
            count_dict[word] += 1
    else:
        count_dict[word] = 1
count_lst = [(counter, word) for word, counter in count_dict.items()]
print(sorted(count_lst, reverse=True))

#bài tập 2
txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction'
txt_lst = re.findall(r'-?\d+', txt)
numbers = list(map(int, txt_lst))
print(max(numbers) - min(numbers))

            #LEVEL 2
def is_valid_variabel(param):
    return bool(re.match(r'[a-zA-Z_][a-zA-Z0-9_]*$', param))


                #LEVEL 3
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
lst_str = re.sub(r'[;@%&$#!?]', "", sentence)
print(lst_str)
