# In[1] 导入库
import pandas as pd

# In[2] 读取文件
df = pd.read_excel('xxx课表.xlsx')
CourseName = df['课程名称']
Teacher = df['主讲教授员']
Time = df['上课时间']
Place = df['教授室']
Score = df['学分']

# In[3] 格式调整
# 时间
Cn2Arabic = {'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'日':7}
Week = [] # 星期
WeekNum = [] # 周数
Begin = [] # 开始节数
End = [] # 结束节数
for t in Time:
    t = t.split(' ')
    # print(t)
    # 星期
    week = t[1][-1]
    week = Cn2Arabic[week]
    Week.append(week)
    # print(week)
    # 周数
    weeknum = t[0]
    weeknum = weeknum.replace('(','')
    weeknum = weeknum.replace(')','')
    weeknum = weeknum.replace(',','、')
    WeekNum.append(weeknum)
    # 节数
    # print(weeknum)
    section = t[2]
    section = section.replace('第','')
    section = section.replace('节','')
    section = section.split('-')
    # 开始节数
    begin = int(section[0])
    Begin.append(begin)
    # 结束节数
    end = int(section[1])
    End.append(end)
    # print(begin,end)
# 老师
TmpTeacher = Teacher
Teacher = []
for t in TmpTeacher:
    t = t.replace(',','')
    Teacher.append(t)
# 地点
TmpPlace = Place
Place = []
for p in TmpPlace:
    p = p[-7:]
    Place.append(p)
# In[4] 导出
WakeUp = pd.DataFrame({'课程名称':list(CourseName),
                       '星期':Week,
                       '开始节数':Begin,
                       '结束节数':End,
                       '老师':Teacher,
                       '地点':Place,
                       '周数':WeekNum,
                       '学分':list(Score)})
WakeUp.to_csv('xxx课表.csv',index=False,encoding='utf-8-sig')