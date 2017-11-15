#coding:utf-8--

import requests

#执行API调用，并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print ("Status code: ", r.status_code)

#api响应存储在变量中，返回的是Json格式，所以用json()方法把返回信息转化为Python字典
response_dict = r.json()
#print type(reponse_dict)

#处理结果（只有三个键值对）:指出项目总数
print ("Total repostories:", response_dict['total_count'])

#探索有关仓库的信息
repo_dicts = response_dict['items']
#print type(repo_dicts)
print ("Repostories returned:",len(repo_dicts))

#研究第一个库
repo_dict = repo_dicts[0]
#print type(repo_dict)
# print("\nKeys:%d" %(len(repo_dict)))
# for key in repo_dict.keys():
#     print key

print ("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print ('Name:',repo_dict['name'])
    print ('Owner:',repo_dict['owner']['login'])
    print ('Stars:',repo_dict['stargazers_count'])
    print ('Repository:',repo_dict['html_url'])
    print ('Description:',repo_dict['description'])
