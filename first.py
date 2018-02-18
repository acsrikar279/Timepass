import mechanize
from bs4 import BeautifulSoup
names,gpa = [],[]
print('Enter the roll numbers seperated by spaces')
a=raw_input()
rolls=a.split(' ')
for i in rolls:
        br = mechanize.Browser()
        br.open('http://gvpce.ac.in/results/B.Tech%20V%20Sem%20Regular%20(R-2015)%20(For%202015%20batch)%20Result_October-%202017/btechsearch.asp')
        br.select_form(nr=0)
        br.form['u_input']=i
        br.submit()
        soup = BeautifulSoup(br.response().read(),"html5lib")
        names.append(soup("td",{'colspan':'4'})[1].text)
        gpa.append(soup("td",{'colspan':'4'})[2].text)
        br.close()
print(names)
print(gpa)
'''
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = tuple(rolls)
y_pos = np.arange(len(objects))
performance = marks
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
 
plt.show()
'''
