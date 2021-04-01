print("du ide")


# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
if int(user_input)%2 == 1:
	print("odd")
else:
	print("even")
  
  
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = list(input() for _ in range(2))
print(user_input);
aa = int(user_input[0]) >> int(user_input[1]);
bb = int(user_input[0]) << int(user_input[1]);
print (str(aa))
print (str(bb))
