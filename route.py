from directory import Directory
from fichier import Fichier
from render_figure import RenderFigure
from user import User
from news import News
from remedes import Remedes

from storage import Storage
from mypic import Pic
from javascript import Js
from stylesheet import Css
import re
import traceback
import sys

class Route():
    def __init__(self):
        self.Program=Directory("mon petit guide de python")
        self.Program.set_path("./")
        self.mysession={"notice":None,"email":None,"name":None}
        self.dbUsers=User()
        self.dbNews=News()
        self.dbRemedes=Remedes()
        self.dbStorage=Storage()
        self.render_figure=RenderFigure(self.Program)
        self.getparams=("id",)
    def set_my_session(self,x):
          print("set session",x)
          self.Program.set_my_session(x)
          self.render_figure.set_session(self.Program.get_session())
    def set_redirect(self,x):
          self.Program.set_redirect(x)
          self.render_figure.set_redirect(self.Program.get_redirect())
    def render_json(self,x,y):
          self.Program.set_json(Fichier(("./"+x),y).lire())
          return self.render_figure.render_my_json(self.Program.get_json())
    def set_json(self,x):
          self.Program.set_json(x)
          self.render_figure.set_json(self.Program.get_json())
    def set_notice(self,x):
          print("set session",x)
          self.Program.set_session_params({"notice":x})
          self.render_figure.set_session(self.Program.get_session())
    def set_session(self,x):
          print("set session",x)
          self.Program.set_session(x)
          self.render_figure.set_session(self.Program.get_session())
    def get_this_route_param(self,x,params):
          print("set session",x)
          return dict(zip(x,params["routeparams"]))
          
    def logout(self,search):
        self.Program.logout()
        self.set_redirect("/")
        return self.render_figure.render_redirect()
    def login(self,s):
        search=self.get_post_data()(params=("email","password"))
        self.user=self.dbUsers.getbyemailpw(search["email"],search["password"])
        print("user trouve", self.user)
        if self.user["email"] != "":
          self.set_session(self.user)
          self.set_json("{\"redirect\":\"/welcome\"}")
        else:
          self.set_json("{\"redirect\":\"/\"}")
        print("session login",self.Program.get_session())
        return self.render_figure.render_json()
    def datastorage(self,search={}):
        return self.render_figure.render_figure("data/new.html")
    def new_datastorage(self,params={}):
        myparams=self.get_post_data()(params=("text","lat","lon","image",))
        self.user=self.dbStorage.create(myparams)
        if self.user["storage_id"]:
          self.set_notice(self.user["notice"])
          self.set_json("{\"redirect\":\"/mystorage/"+self.user["storage_id"]+"\"}")
        else:
          self.set_json("{\"redirect\":\"/datastorage\"}")
        return self.render_figure.render_json()
    def new(self,search={}):
        return self.render_figure.render_figure("news/new.html")
    def createnew(self,params={}):
        myparams=self.get_post_data()(params=("text","lat","lon","image",))

        self.user=self.dbNews.create(myparams)
        if self.user["news_id"]:
          self.set_notice(self.user["notice"])
          self.set_json("{\"redirect\":\"/seemynews/"+self.user["news_id"]+"\"}")
        else:
          self.set_json("{\"redirect\":\"/new\"}")
        return self.render_figure.render_json()
    def welcome(self,search):
        return self.render_figure.render_figure("welcome/index.html")
    def delete_user(self,params={}):
        getparams=("id",)
        myparam=self.post_data(self.getparams)
        self.render_figure.set_param("user",User().deletebyid(myparam["id"]))
        self.set_redirect("/welcome")
        return self.render_figure.render_redirect()
    def edit_user(self,params={}):
        getparams=("id",)
        myparam=self.post_data(getparams)
        self.render_figure.set_param("user",User().getbyid(myparam["id"]))
        return self.render_figure.render_figure("welcome/edituser.html")
    #remedes
    def newremede(self,search={}):
        return self.render_figure.render_figure("remede/new.html")
    def createremede(self,params={}):
        myparams=self.get_post_data()(params=("image","text","lat","lon",))
        self.user=self.dbRemedes.create(myparams)
        if self.user["remede_id"]:
          self.set_notice(self.user["notice"])
          self.set_json("{\"redirect\":\"/seemyremede/"+self.user["remede_id"]+"\"}")
        else:
          self.set_json("{\"redirect\":\"/newremede\"}")
        return self.render_figure.render_json()
    def showremede(self,params={}):
        print("action see my new")
        getparams=("id",)
        print("get param, action see my storage",getparams)
        myparam=self.get_this_route_param(getparams,params)
        print("m params see my new")
        print(myparam)
        self.render_figure.set_param("remede",self.dbRemedes.getbyid(myparam["id"]))
        return self.render_figure.render_figure("remede/show.html")
    def allremedes(self,params={}):
        self.render_figure.set_param("mystorages",self.dbStorage.getall())
        return self.render_figure.render_figure("data/all.html")
    def seestorage(self,params={}):
        print("action see my new")
        getparams=("id",)
        print("get param, action see my storage",getparams)
        myparam=self.get_this_route_param(getparams,params)
        print("m params see my new")
        print(myparam)
        self.render_figure.set_param("storage",self.dbStorage.getbyid(myparam["id"]))
        return self.render_figure.render_figure("data/show.html")
    def seenew(self,params={}):
        print("action see my new")
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        print("m params see my new")
        print(myparam)
        self.render_figure.set_param("news",News().getbyid(myparam["id"]))
        return self.render_figure.render_figure("news/shownews.html")
    def seeuser(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        self.render_figure.set_param("user",User().getbyid(myparam["id"]))
        return self.render_figure.render_figure("welcome/showuser.html")
    def mystorages(self,params={}):
        self.render_figure.set_param("mystorages",self.dbStorage.getall())
        return self.render_figure.render_figure("data/all.html")
    def mynews(self,params={}):
        self.render_figure.set_param("mynews",News().getall())
        return self.render_figure.render_figure("news/allnews.html")
    def myusers(self,params={}):
        self.render_figure.set_param("users",User().getall())
        return self.render_figure.render_figure("welcome/users.html")
    def set_post_data(self,x):
        self.post_data=x
    def get_post_data(self):
        return self.post_data
    def update_user(self,params={}):
        myparam=self.post_data(self.getparams)
        self.user=self.dbUsers.update(params)
        self.set_session(self.user)
        self.set_redirect(("/seeuser/"+params["id"][0]))
        return self.render_figure.render_redirect()
    def save_user(self,params={}):
        #print("My  f unc",self.post_data)
        myparam=self.get_post_data()(params=("businessaddress","gender","profile","metier", "otheremail", "password","zipcode", "email", "mypic","postaladdress","nomcomplet","password_confirmation"))
        #print("My p  a r a m",myparam)
        self.user=self.dbUsers.create(myparam)
        if self.user["email"]:
          self.set_session(self.user)
          self.set_json("{\"redirect\":\"/welcome\"}")
          return self.render_figure.render_json()
        else:
          self.set_json("{\"redirect\":\"/e\"}")
          return self.render_figure.render_json()
    def data_reach(self,search):
        return self.render_figure.render_figure("welcome/datareach.html")
    def voirtoutcequejaiajoute(self,data):

        print("tout")
        tout=self.dbNews.getall()+self.dbStorage.getall()+self.dbRemedes.getall()
        print("tout")
        print(tout,"tout")
        self.render_figure.set_param("tout",tout)
        return self.render_json("welcome","hey.json")
    def run(self,redirect=False,redirect_path=False,path=False,session=False,params={},url=False,post_data=False):
        if post_data:
            self.set_post_data(post_data)
        if url:
            print("url : ",url)
            self.Program.set_url(url)
        self.set_my_session(session)

        if redirect:
            self.redirect=redirect
        if redirect_path:
            self.redirect_path=redirect
        if not self.render_figure.partie_de_mes_mots(balise="section",text=self.Program.get_title()):
            self.render_figure.ajouter_a_mes_mots(balise="section",text=self.Program.get_title())
        if path and path.endswith("jpg"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("png"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith(".jfif"):
            self.Program=Pic(path)
        elif path and path.endswith(".css"):
            self.Program=Css(path)
        elif path and path.endswith(".js"):
            self.Program=Js(path)
        elif path:
            print("link route ",path)
            ROUTES={
                    "^/voirtoutcequejaiajoute$":self.voirtoutcequejaiajoute,
                    "^/newremede$":self.newremede,
                    "^/createremede$":self.createremede,
                    "^/seemyremede/([0-9]+)$":self.showremede,
                    "^/allremedes$":self.allremedes,
                    "^/datastorage$":self.new_datastorage,
                    "^/new_datastorage$":self.datastorage,
                    "^/allmynews$":self.mynews,
                    "^/alldatastorage$":self.mystorages,
                    '^/logmeout$':self.logout,
                    '^/save_user$':self.save_user,
                    '^/update_user$':self.update_user,
                    '^/new$':self.new,
                    '^/createnew$':self.createnew,

                    "^/seemynews/([0-9]+)$":self.seenew,
                    "^/mystorage/([0-9]+)$":self.seestorage,
                    "^/seeuser/([0-9]+)$":self.seeuser,
                    "^/edituser/([0-9]+)$":self.edit_user,
                    "^/deleteuser/([0-9]+)$":self.delete_user,
                    '^/login$':self.login,

                    '^/welcome$':self.myusers,

                    '^/$': self.welcome,
                    }
            REDIRECT={"/save_user": "/welcome"}
            for route in ROUTES:
               print("pattern=",route)
               mycase=ROUTES[route]
               x=(re.match(route,path))
               print(True if x else False)
               if x:
                    params["routeparams"]=x.groups()
                    try:
                        html=mycase(params)
                    except Exception as e:
                        print("erreur"+str(e),traceback.format_exc())
                        html=("<p>une erreur s'est produite dans le code server  "+(traceback.format_exc())+"</p><a href=\"/\">retour à l'accueil</a>").encode("utf-8")
                        print(html)
                    self.Program.set_html(html=html)
                    return self.Program
               else:
                    self.Program.set_html(html="<p>la page n'a pas été trouvée</p><a href=\"/\">retour à l'accueil</a>")
        return self.Program
