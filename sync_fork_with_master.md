`C:\Users\saifuddin>cd gite`  

---

`C:\Users\saifuddin\gite>git clone https://github.com/SaifuddinSaifee/sem6feedback-it.git`  
Cloning into 'sem6feedback-it'...  
remote: Enumerating objects: 69, done.  
remote: Counting objects: 100% (69/69), done.  
remote: Compressing objects: 100% (54/54), done.  
remote: Total 69 (delta 13), reused 37 (delta 8), pack-reused 0  
Receiving objects: 100% (69/69), 347.60 KiB | 645.00 KiB/s, done.  
Resolving deltas: 100% (13/13), done.  

---

`C:\Users\saifuddin\gite>dir`  
 Volume in drive C has no label.  
 Volume Serial Number is 6EE4-4EE3  

 Directory of C:\Users\saifuddin\gite  

05/26/2020  01:39 PM    <DIR>          .  
05/26/2020  01:39 PM    <DIR>          ..  
05/26/2020  01:39 PM    <DIR>          sem6feedback-it  
               0 File(s)              0 bytes  
               3 Dir(s)  463,599,042,560 bytes free  

---

`C:\Users\saifuddin\gite>cd sem6feedback-it`  

---

`C:\Users\saifuddin\gite\sem6feedback-it>git remote add upstream https://github.com/saifeemustafaq/sem6feedback-it`  

---

`C:\Users\saifuddin\gite\sem6feedback-it>git fetch upstream`  
remote: Enumerating objects: 24, done.  
remote: Counting objects: 100% (23/23), done.  
remote: Compressing objects: 100% (7/7), done.  
remote: Total 14 (delta 5), reused 11 (delta 4), pack-reused 0  
Unpacking objects: 100% (14/14), 2.91 KiB | 2.00 KiB/s, done.  
From https://github.com/saifeemustafaq/sem6feedback-it  
 * [new branch]      master                 -> upstream/master  
 * [new branch]      saifeemustafaq-patch-1 -> upstream/saifeemustafaq-patch-1  

---

`C:\Users\saifuddin\gite\sem6feedback-it>git pull upstream master`  
From https://github.com/saifeemustafaq/sem6feedback-it  
 * branch            master     -> FETCH_HEAD  
Updating a079d5f..b976d8a  
Fast-forward  
 README.md          | 38 ++++----------------------------------  
 css/style.css      | 24 ++++++++++++++++++++++++  
 index.html         | 45 +++++++++++++++++++++++++++++----------------  
 javascript/demo.js | 32 ++++++++++++++++++++++++++++----  
 4 files changed, 85 insertions(+), 54 deletions(-)  

---

`C:\Users\saifuddin\gite\sem6feedback-it>`  
