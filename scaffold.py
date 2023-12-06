# -*- coding: utf-8 -*-

import sys
import os
import errno    
import os
from fichier import Fichier

def mkdir_p(path):
        try:
             os.makedirs(path)
        except OSError as exc:  # Python ≥ 2.5
             if exc.errno == errno.EEXIST and os.path.isdir(path):
                 pass
                 # possibly handle other errno cases here, otherwise finally:
             else:
                 raise
print(sys.argv[1])


filename=sys.argv[1].lower()
mkdir_p(filename)
myclass=(filename).capitalize()
modelname=(filename).capitalize()
marouteget="\"/%s\"" % filename
maroutenew="\"/%s_new\"" % filename
maroutecreate="\"/%s_create\"" % filename
marouteget2="\\\"/%s\\\"" % filename
myhtml="my"+filename+"html"
myfavdirectory=filename
index = 2 
createtable=""
columns="("
values="("
myparam=","
items=sys.argv
while index < (len(items)):

    try:
      print(index, items[index])
      paramname=items[index]
      print(items[(index+1)])
    except:
      myparam=""
    index += 1
    columns+="{paramname}{myparam}".format(myparam=myparam,paramname=paramname)
    values+=":{paramname}{myparam}".format(myparam=myparam,paramname=paramname)
    createtable+="""        {paramname} text{myparam}
    """.format(myparam=myparam,paramname=paramname)
columns+=")"
values+=")"
mystr="""# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class {modelname}(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute(\"\"\"create table if not exists {filename}(
        id integer primary key autoincrement,
"""
mystr+=createtable

mystr+="""                );\"\"\")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from {filename}")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

"""
mystr+="""        self.cur.execute("delete from {filename} where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from {filename} where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={myhash}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        print(myhash,myhash.keys())
        myid=None
        try:
          self.cur.execute("insert into {filename} {columns} values {values}",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={notice}
        azerty["{filename}_id"]=myid
        azerty["notice"]="votre {filename} a été ajouté"
        return azerty




"""
model="""    def new{filename}(self,search={}):
        return self.render_figure.render_figure("{filename}/new.html")
    def create{filename}(self,params={}):
        myparams=self.get_post_data()(params=("content",))
        self.user=self.db{myclass}.create(myparams)
        if self.user["{filename}_id"]:
            self.set_notice(self.user["notice"])
            self.set_json("{\"redirect\":\"/seemy{filename}/"+self.user["{filename}_id"]+"\"}")
        else:
            self.set_json("{\"redirect\":\"/new{filename}\"}")
            return self.render_figure.render_json()
    def show{filename}(self,params={}):
        print("action see my new")
        getparams=("id",)
        print("get param, action see my storage",getparams)
        myparam=self.get_this_route_param(getparams,params)
        print("m params see my new")
        print(myparam)
        self.render_figure.set_param("{filename}",self.db{myclass}.getbyid(myparam["id"]))
        return self.render_figure.render_figure("{filename}/show.html")
    def all{filename}s(self,params={}):
        self.render_figure.set_param("mystorages",self.db{myclass}.getall())
        return self.render_figure.render_figure("data/all.html")
"""
mesroutes="""                    "^/new{filename}$":self.new{filename},
                    "^/create{filename}$":self.create{filename},
                                        "^/seemy{filename}/([0-9]+)$":self.show{filename},
                                                            "^/all{filename}$":self.all{filename}s,
"""
matableinit="""        self.db{myclass}={myclass}()
"""
myimport="""from {filename} import {myclass}
"""
viewmymodel="""<p><%=news["content"]%></p>
"""
Fichier("./"+filename, "_"+filename+".html").ecrire(viewmymodel)
seeallmode="""<h1>toutes les breaking news</h1>
<%=render_collection(collection=params['mynews'], partial='news/_news.html', as_='news')%>
"""
Fichier("./"+filename, "voirtout.html").ecrire(newmodel)
newmodel="""<h1>ecrire 1 breaking news</h1>
<form action="/createnew" method="post">
<div class="field">
<label for="content">content</label>
<textarea name="content" id="content"></textarea>
</div>
<div class="field">
<label for="lat">latitude</label>
<input type="text" name="lat" id="lat"/>
</div>
<div class="action">
<input type="submit" value="submit" name="submit"/>
</div>
</form>
"""
Fichier("./"+filename, "new.html").ecrire(newmodel)
if not os.path.isfile(filename+".py"):
  f = open(filename+".py", "w") 
  res=(mystr.format(modelname=modelname,filename=filename,columns=columns,values=values,myhash={},notice={}))
  print(res)
  f.write(res)
  f.close()




index=[i for i in range(len(contents)) if "def run" in contents[i]][0]
contents.insert((index), model.format(myfavdirectory=myfavdirectory,myclass=filename,myhtml=myhtml))
indexinittable=[i for i in range(len(contents)) if "__init__" in contents[i]][0]
contents.insert((indexroute+1), matableinit.format(myfavdirectory=myfavdirectory,myclass=filename,myhtml=myhtml))
indexroute=[i for i in range(len(contents)) if "ROUTES={" in contents[i]][0]
contents.insert((indexroute+1), mesroutes.format(filename=filename, myclass=myclass))
with open("./route.py", "r") as f:
  contents = f.readlines()
#contents.insert(1, "global {myclass}\n".format(myclass=filename))
#contents.insert(1, "import {myclass}\n".format(myclass=filename))
#contents.insert(1, "from {myclass} import {myclass}page\n".format(myclass=filename))
#myrouteget="\"/{myclass}\":{myclass}func,\n"
#index=[i for i in range(len(contents)) if "myroutes = {" in contents[i]][0]
#contents.insert((index+1), myrouteget.format(myclass=filename))
#index=[i for i in range(len(contents)) if "def reloadmymodules" in contents[i]][0]
#contents.insert((index+1), "    reload({myclass})\n".format(myclass=filename))
#index=[i for i in range(len(contents)) if "__mots__={" in contents[i]][0]
#contents.insert((index+1), "    \"/{myclass}\":{\"partiedemesmots\":\"{myclass}\"},\n".replace("{myclass}",filename))

#with open("./script.py", "w") as f:
#    contents = "".join(contents)
#    f.write(contents)

#os.system("mkdir %s" % myfavdirectory)
#pathhtml="%s/%s.html" % (myfavdirectory, myhtml)
#os.system("touch %s" % pathhtml)

#if os.path.isfile(pathhtml):
#    with open(pathhtml, "w") as f:
#        urlayout="""<h1>Layout de la route {myclass}</h1>
#<p><a href="{marouteget}">nous sommes ici (essayez ce lien)</a></p>
#<p>Entrez du texte sur cette page</p>
#"""
#          f.write(urlayout.format(marouteget=marouteget,myclass=filename))
#
#  #print("ma route get %s a été ajoutée. Maintenant vous pouvez essayer d'y acceder" % marouteget)
