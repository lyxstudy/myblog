Date: 2016-4-7
Title: Dogwood and Brich 数据库对比
Slug: something-interesting-2
Tags:  edx

----------
针对edx平台的升级数据库迁移是重中之重，但往往有很多有些人忽视这方面的问题，导致平台升级出现各种坑。下面针对dogwood和brich两个版本的数据进行对比，希望能给折腾数据的小伙伴一点帮助：

## Mysql 数据库对比 ##


- auth\_user表last_login字段dogwood允许为空长度为6，brich不允许null长度为0。

- auth\_userprofile表dogwood比brich多了两个字段:bio和profile\_image\_uploaded_at;
city字段dogwood为null,brich不为null。

- student\_courseenrollment表created字段dogwood长度为6，brich长度为0。

### 对比如下： ###
Brich\_auth\_user

![Brich_auth_user](http://7xofqa.com1.z0.glb.clouddn.com/Brich_auth_user.png)

Dogwood\_auth\_user

![Dogwood_auth_user](http://7xofqa.com1.z0.glb.clouddn.com/Dogwood_auth_user.png)

Brich\_auth\_userprofile

![Brich_auth_userprofile](http://7xofqa.com1.z0.glb.clouddn.com/Brich_auth_userprofile.png)

Dogwood\_auth\_userprofile

![Dogwood_auth_userprofile](http://7xofqa.com1.z0.glb.clouddn.com/Dogwood_auth_userprofile.png)

Brich\_student\_courseenrollmen

![Brich_student_courseenrollmen](http://7xofqa.com1.z0.glb.clouddn.com/Brich_student_courseenrollment.png)

Dogwood\_student\_courseenrollment

![Dogwood_student_courseenrollment](http://7xofqa.com1.z0.glb.clouddn.com/Dogwood_student_courseenrollment.png)


## Mongo数据对比 ##
cs\_comments\_service\_development数据库中contents表新版比老版多一个key:context,value:string,并且course_id规则不一样。

Users表中default\_sort_key的value不一样，Dogwood为data,Brich为votes。

Brich\_mongo:users

![Brich_mongo_users](http://7xofqa.com1.z0.glb.clouddn.com/Brich_mongo_users.png)

Dogwood\_mongo:users

![Dogwood_mongo_users](http://7xofqa.com1.z0.glb.clouddn.com/Dogwood_mongo_users.png)

Brich:cs\_comments\_service\_development

![Brich_cs_comments](http://7xofqa.com1.z0.glb.clouddn.com/Brich_cs_comments.png)

Dogwood:cs\_comments\_service\_development

![Dogwood_cs_comments](http://7xofqa.com1.z0.glb.clouddn.com/Dogwood_cs_comments.png)