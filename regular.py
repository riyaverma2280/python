import re
exp="[6-9]{1}\d{9}"
st="mob no. is 8264962680 and other number is 7087860049 and one more is 48759248789 "
print(re.findall(pattern=exp,string=st))

mail_exp="[a-zA-Z0-9.-]+@[a-zA-Z0-9]+.[a-zA-Z]{2,7}"