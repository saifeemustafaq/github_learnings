# In general scenario, you do add commit push in three lines:

`git add .`

`git commit -m "message"`

`git push origin master`

---

# Simplify this by making a bat file

1. Create a .bat file (eg. push.bat) in the directory where you will be using git.
2. write the following lines as it is in the ***push.bat*** file.

   `git add .`  
   `git commit -m "message"`  
   `git push origin master`  
   
   or you can replace `"message"` with `%1` so that when you type `push.bat "message"`, whatever is written after the `push.bat` will replace the `%1`
   
3. save the file

## If you are using ***cmd***
navigate to the directory  
in the command line type `push.bat` or `push.bat "message"`

## If you are using ***Powershell or VSCode Terminal***
navigate to the directory
in the command line type `.\push.bat` or `.\push.bat "message"`
