import mechanize
from bs4 import BeautifulSoup
names,gpa = [],[]
print('Enter the roll numbers seperated by spaces')
a=raw_input()
rolls=a.split(' ')
index=0
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
        gpa[index]= float(gpa[index].encode('ascii'))
        index+=1
index=0

import numpy as np
import matplotlib.pyplot as plt

print(names)
print(gpa)
x, y = np.array(range(0,len(rolls))), gpa
plt.xticks(x,rolls)
plt.bar(x,y)
plt.ylim(0,10)
plt.show()
