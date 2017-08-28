#sum all the numbers in a .txt file
import re
print(sum(int(i) for i in re.findall("[0-9]+", open('regex_sum_25302.txt').read())))
