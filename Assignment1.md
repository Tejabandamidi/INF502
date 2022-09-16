1. List all the branches in this repository and, for each branch, list the commits.

    - Use `git branch` to list the branches in this repository.
    - Use `git checkout` to explore each branch.
    - Use `git log --decorate` to explore the structure of commits.

```
C:\Users\hi\Desktop\INF502\handson\handson>git branch
* main
  math

C:\Users\hi\Desktop\INF502\handson\handson>git commit
On branch main
nothing to commit, working tree clean

C:\Users\hi\Desktop\INF502\handson\handson>git checkout

C:\Users\hi\Desktop\INF502\handson\handson>git commit
On branch main
nothing to commit, working tree clean

C:\Users\hi\Desktop\INF502\handson\handson>git checkout main
Already on 'main'

C:\Users\hi\Desktop\INF502\handson\handson>git commit
On branch main
nothing to commit, working tree clean

C:\Users\hi\Desktop\INF502\handson\handson>git log --decorate
commit 18931d12a8be7cac049b73c6bc8136e9482f3371 (HEAD -> main)
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:15:28 2019 -0700

    Making a small change here

commit 654b490a181dedf82dd6deda5f9848d6cca05918
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:12:14 2019 -0700

    Added a draft of A.py

commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:08:47 2019 -0700

     Creating all files (all empty)

C:\Users\hi\Desktop\INF502\handson\handson>git commit
On branch main
nothing to commit, working tree clean

```

2. Try `git log --graph --all` to see the commit tree. Paste the result here and write a paragraph to provide an interpretation of what you found.
```
C:\Users\hi\Desktop\INF502\handson\handson>git log --graph --all
* commit 18931d12a8be7cac049b73c6bc8136e9482f3371 (HEAD -> main)
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:15:28 2019 -0700
|
|     Making a small change here
|
| * commit e3c629dd524712aedea96d7dbaad1c50d12b5b5e (math)
|/  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
|   Date:   Wed Aug 14 23:13:48 2019 -0700
|
|       Adding some more knowledge to the function
|
* commit 654b490a181dedf82dd6deda5f9848d6cca05918
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:12:14 2019 -0700
|
|     Added a draft of A.py
|
* commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
  Date:   Wed Aug 14 23:08:47 2019 -0700

       Creating all files (all empty)

This is a tree structure. Small changes are done to the main branch and few more functions are added. Later, a draft of python file is added as "A.py".

```

3. Use `git diff BRANCH_NAME` to view the differences from a branch and the current branch. Summarize the difference from master to the other branch.

```
C:\Users\hi\Desktop\INF502\handson\handson>git diff math
diff --git a/A.py b/A.py
index 0afa98c..dc1e9bd 100644
--- a/A.py
+++ b/A.py
@@ -1,11 +1,3 @@
 #this is just an example, do not freak out
 def calculate_this(operator, num1, num2):
-   if operator == 'sum':
-      print num1 + num2
-      print 'That was easy buddy'
-   else:
-      if operator == 'subtraction':
-         print num1 - num2
-         print 'I could handle that...'
-      else:
-         print 'my knowledge is limited'
+   print 'my knowledge is limited'
diff --git a/B.py b/B.py
index e69de29..c63f94c 100644
--- a/B.py
+++ b/B.py
@@ -0,0 +1 @@
+# Another file that will receive a line of code... at least.

The default branch is called a 'Master' branch. While, other branches are evolved through the actions of the commits. As the current branch we are on is math, it is also our main branch. In other words, it is master branch.

```

4. Write a command sequence to merge the non-master branch into `master`.

```
git checkout master
git merge math

```


5. Write a command (or sequence) to (i) create a new branch called `math` (from the `master`) and (ii) change to this branch.

```
git checkout master
git branch math (fatal: a branch named 'math' already exists)
git checkout math

```
   
6. Edit B.py adding the following source code below the content you have there.
```
C:\Users\hi\Desktop\INF502\handson\handson>git add B.py

C:\Users\hi\Desktop\INF502\handson\handson>git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   B.py


C:\Users\hi\Desktop\INF502\handson\handson>git commit -m "B.py"
[main 35efccc] B.py
 1 file changed, 2 insertions(+)
```

7. Write a command (or sequence) to commit your changes.
```
git add B.py
git commit -m "addition of two lines to B.py on math branch"

```

8. Change back to the `master` branch and change B.py adding the following source code (commit your change to `master`):
```
print 'hello world!'

git checkout master
git add B.py
git commit -m "adding one line to B.py on master branch"
```

9. Write a command sequence to merge the `math` branch into `master` and describe what happened.
```
C:\Users\hi\Desktop\INF502\handson\handson>git merge math
Already up to date. 

git checkout master 
git merge math

```
   
10. Write a set of commands to abort the merge.
```
git merge --abort

```
   
11. Now repeat item 9, but proceed with the manual merge (editing B.py). All implemented methods are needed. Explain your procedure.
```
No errors are seen. None of the files are copied.

```

12. Write a command (or set of commands) to proceed with the merge and make `master` branch up-to-date.
```
git checkout master
git merge math
git rebase

```

13. Complete Part 2. Then, come back here and answer the following:
Report your experience of submitting the Part 2. Please, include the steps you followed, the commands you used, and the hurdles you faced (within the file you created for the **Part 1**).
```
In this assignment, part 2 made me learn and understand the working of github. Firstly, I created a markdown file with “.md” extension to fork the repo. Then, I included the details of my chosen paper. After this, I made a pull request for the repo to observe if it was saved. The difficulty I faced as a beginner was, It was a bit time taking task while working with git and github. Pull request was something I was confused about since it has to appear.
```

