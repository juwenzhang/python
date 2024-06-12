# git的使用一



首先在使用之前我们都是有一点对于如何上传原地从仓库是有点迷茫的

下面就是开始来进行上传的步骤



## 1.首先现在githup的官网上进行创建一个新仓库

就是有一个create new的提示的那个 ，在那里有：  +   和搜索符号的



## 2.然后在本地上对远程的仓库进行克隆

git clone 仓库网址

后面的操作就是实现我们的将需要进行上传的文件或者文件夹复制到这个目录下面



## 3.后面的操作

git add 文件名   进行添加到缓存区

git commit -m "描述"   进行提交

git branch -M main 需要进行提交的分支

git push -u origin main  提交到我们的远程仓库





# git的使用二



首先先在我们的本地需要写项目的空文件夹下面进行初始化项目  git init    ===>  就会有一个默认是被隐藏的 .git 的文件夹

然后进行：  git add -A  就是进行提交所有的需要上传的文件夹

后面：  git commit -m "描述"   就是进行提交变化

然后：  git remote add origin 仓库网址   就是指定我们的需要进行提交的远程仓库

然后：  git branch -M main  

最后：  git push -u origin main  推送到远程githup仓库