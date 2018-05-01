import mechanize
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt

names,gpa = [],[]
urls = ['http://gvpce.ac.in/results/B.Tech%20I%20Semester%20Regular%20(R-2015)_December%202015/btechsearch.asp',
'http://gvpce.ac.in/results/B.Tech%20II%20Semester%20(Regular)%20(R-2015)_May%202016%20(For%202015%20Admitted%20Batch)/btechsearch.asp',
'http://gvpce.ac.in/results/B.Tech%20III%20Semester%20(R-2015)%20Regular%20Results-October-2016/btechsearch.asp',
'http://gvpce.ac.in/results/B.Tech%20IV%20Sem%20Regular%20%20(R-2015)%20(For%202015%20%20Batch)%20Result_April,%202017/btechsearch.asp',
'http://gvpce.ac.in/results/B.Tech%20V%20Sem%20Regular%20(R-2015)%20(For%202015%20batch)%20Result_October-%202017/btechsearch.asp']
credits = [22,27,24,24,26]
urllen = len(urls)
rolls,sem = raw_input("Enter you roll number"),input("Enter the semester you want result for")
br = mechanize.Browser()
br.open(urls[sem-1])
br.select_form(nr=0)
br.form['u_input']=rolls
br.submit()
soup = BeautifulSoup(br.response().read(),"html5lib")
names.append(soup("td",{'colspan':'4'})[1].text)
gpa.append(soup("td",{'colspan':'4'})[2].text)
br.close()
gpa[0]= float(gpa[0].encode('ascii'))
print("Your gpa is ")
print(gpa[0])
