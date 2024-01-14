from datetime import  datetime
from  time import gmtime, strftime

localSaat = datetime.now()
strftime("%a,   %Y %H:%M:%S", gmtime())
strftime("%d",gmtime())
strftime("%b",gmtime())

print(help(dir(gmtime())))






print(strftime("%a, %d %b %Y %H:%M:%S"))