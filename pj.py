import requests

s=requests.Session()
login_url = "http://pjb.ecust.edu.cn/pingce/login.php"
p = s.post(login_url, {'action':"login", 'sno':"10142045",'password':"101535"})
o = s.get("http://pjb.ecust.edu.cn/pingce/list.php")
o.encoding = "gbk"
print o.text