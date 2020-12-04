from anabasi import app
from flask import redirect, flash, url_for, render_template, request, send_from_directory
from flask_login import current_user, login_user, logout_user
from anabasi.models import User
from anabasi import db
from anabasi.forms import LoginForm, NewUser
from anabasi.services.pbiembedservice import PbiEmbedService
from anabasi.utils import Utils
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os

global id_utente_per_modifiche
id_utente_per_modifiche = None


@app.route("/")
def homepage():
    utente1 = User.query.all()
    #email = utente1.username
    posts = [{"title": "primo post", "body": "random body"},
             {"title": "secondo post", "body": "random body"}]
    bolean = True
    return render_template("index.html", utente1 = utente1 )

@app.route("/login_admin")
def login_admin():
    return render_template("login_admin.html")


@app.route("/schermata_amministratore", methods=["POST", "GET"])
def schermata_amministratore():
    if current_user.is_authenticated and current_user.id == 1:
        print(current_user.id)
        form = NewUser()
        utenti = User.query.all()
        if form.validate_on_submit():
            nuovo_utente = User(name = form.nome.data, username = form.username.data, password = generate_password_hash(form.password.data))
            db.session.add(nuovo_utente)
            db.session.commit()
            return redirect(url_for('schermata_amministratore'))
    else:
        return redirect(url_for('login'))
    return render_template("schermata_amministratore.html", form=form, utenti = utenti)

@app.route("/dettaglio_utente/<int:id_utente>", methods=["POST", "GET"])
def dettaglio_utente(id_utente):
    if current_user.is_authenticated and current_user.id == 1:
        utente_istanza = User.query.get_or_404(id_utente)
        
        utente_attuale = User.query.filter_by(id = id_utente).first()
        global id_utente_per_modifiche
        id_utente_per_modifiche = id_utente
        print(id_utente_per_modifiche)
        return render_template("render_utente.html", post=utente_istanza, utente_attuale = utente_attuale)
    else:
        return redirect(url_for('login'))
@app.route("/login", methods=["POST", "GET"])

def login():
    if current_user.is_authenticated and current_user.id != 1:
        return redirect(url_for('utente', id_u = current_user.id, lin= "n"))
    elif current_user.is_authenticated and current_user.id == 1:
        return redirect(url_for('schermata_amministratore'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username= form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            
            print("errore")
            flash("errore")
            return redirect(url_for('login'))
        elif user.id == 1 and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('schermata_amministratore'))
        else:
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('utente', id_u = current_user.id, lin = "n"))
     
       
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))



@app.route("/disattiva_av/<int:anabasi_servizio>", methods=['POST', 'GET'])
def disattiva_av(anabasi_servizio):
    print(id_utente_per_modifiche)
    utente = User.query.filter_by(id = id_utente_per_modifiche).first()
    print(utente.username)
    if anabasi_servizio == 1:
        if utente.anabasi_finanaza == True:
            utente.anabasi_finanaza = False
            utente.link_anabasi_fina = None
            
            db.session.commit()
        else:
            utente.anabasi_finanaza = True
            db.session.commit()
    elif anabasi_servizio == 2:
        if utente.anabasi_co_an == True:
            utente.anabasi_co_an = False
            utente.link_anabasi_co_an = None
            db.session.commit()
        else:
            utente.anabasi_co_an = True
            db.session.commit()
    elif anabasi_servizio == 3:
        if utente.anabasi_vendite == True:
            utente.anabasi_vendite = False
            utente.link_anabasi_vend = None
            db.session.commit()
        else:
            utente.anabasi_vendite = True
            db.session.commit()
    elif anabasi_servizio == 4:
        if utente.anabasi_produco == True:
            utente.anabasi_produco = False
            utente.link_anabasi_produco = None
            db.session.commit()
        else:
            utente.anabasi_produco = True
            db.session.commit()
    elif anabasi_servizio == 5:
        if utente.anabasi_logistica == True:
            utente.anabasi_logistica = False
            utente.link_anabasi_logistica = None
            db.session.commit()
        else:
            utente.anabasi_logistica = True
            db.session.commit()
    elif anabasi_servizio == 6:
        if utente.anabasi_crisi == True:
            utente.anabasi_crisi = False
            utente.link_anabasi_crisi = None
            db.session.commit()
        else:
            utente.anabasi_crisi = True
            db.session.commit()
        
    return redirect(url_for("dettaglio_utente", id_utente= id_utente_per_modifiche))

@app.route("/add_link", methods=['POST', 'GET'])
def add_link():
    print(request.form)
    servizi = ["anabasi_finanaza", "anabasi_vendite", "anabasi_co_an", "anabasi_produco"]
    utente = User.query.filter_by(id = id_utente_per_modifiche).first()
    if request.form.get("workset_id") != None and request.form.get("workset_id") != '':
        utente.link_workset = request.form.get("workset_id")
        db.session.commit()
    if request.form.get("anabasi_finanaza") != None and request.form.get("anabasi_finanaza") != '' :
        utente.link_anabasi_fina = request.form.get("anabasi_finanaza")
        db.session.commit()
        
    if request.form.get("anabasi_vendite") != None and request.form.get("anabasi_vendite") != '':
        utente.link_anabasi_vend = request.form.get("anabasi_vendite")
        db.session.commit()
        
    if request.form.get("anabasi_co_an") != None and request.form.get("anabasi_co_an") != '':
        utente.link_anabasi_co_an = request.form.get("anabasi_co_an")
        db.session.commit()
    print(request.form.get("anabasi_finanaza"))
    
    if request.form.get("anabasi_produco") != None and request.form.get("anabasi_produco") != '':
        utente.link_anabasi_produco = request.form.get("anabasi_produco")
        db.session.commit()
        
    if request.form.get("anabasi_logistica") != None and request.form.get("anabasi_logistica") != '':
        utente.link_anabasi_logistica = request.form.get("anabasi_logistica")
        db.session.commit()
    
    if request.form.get("anabasi_crisi") != None and request.form.get("anabasi_crisi") != '':
        utente.link_anabasi_crisi = request.form.get("anabasi_crisi")
        db.session.commit()
     
    return redirect(url_for("dettaglio_utente", id_utente= id_utente_per_modifiche))

@app.route('/getembedinfo/<link>/<wor>', methods=['GET'])
def get_embed_info(link, wor):
    
    
    #config_result = Utils.check_config(app)
    #if config_result is not None:
     #   return json.dumps({'errorMsg': config_result}), 500
    print("id utente embed")
    
    print(current_user.id)
    try:
        
        embed_info = PbiEmbedService().get_embed_params_for_single_report(wor, link)
        
        print("sono link"+ link)
        link = "n"
        print("sono lini 2"+ link)
        return embed_info
    except Exception as ex:
        return json.dumps({'errorMsg': str(ex)}), 500

@app.route('/utente<int:id_u>/<lin>')
def utente(id_u, lin):
    
    if current_user.is_authenticated and current_user.id == id_u:
        utente_connesso = User.query.filter_by(id = id_u).first()
        diz = {"anabasi finanaza": utente_connesso.anabasi_finanaza,"anabasi co an": utente_connesso.anabasi_co_an, "anabasi vendite": utente_connesso.anabasi_vendite, "anabasi produco": utente_connesso.anabasi_produco, "anabasi logistica":utente_connesso.anabasi_logistica, "anabasi crisi": utente_connesso.anabasi_crisi}
        num = 0
        l = lin
        
        #print(diz)
        #print(utente_connesso.__dict__)
        return render_template("pagina_cliente.html", utente=utente_connesso, serv = diz, li = l, num=num)
    else:
        return redirect(url_for('login'))

@app.route('/link_o/<servizio_richiesto>')
def link_o(servizio_richiesto):
    recupera_link = {"anabasi finanaza":current_user.link_anabasi_fina,"anabasi co an":current_user.link_anabasi_co_an,"anabasi vendite":current_user.link_anabasi_vend,"anabasi produco":current_user.link_anabasi_produco,"anabasi logistica":current_user.link_anabasi_logistica,"anabasi crisi":current_user.link_anabasi_crisi}
    for s in recupera_link:
        if s == servizio_richiesto:
            
            link = recupera_link[s]
            print(link)
    print('link_o')
    
    return redirect(url_for('utente', id_u = current_user.id, lin = link))
    
'''
def verifica_servizi_disp(utente_c):
    servizi_0 = ["anabasi_finanaza", "anabasi_vendite", "anabasi_co_an", "anabasi_produco", "anabasi_logistica", "anabasi_crisi"]
    servizi = {"anabasi_finanaza": "link_anabasi_fina"}
    for ser in servizi_0:
        if exec("utente_connesso.%s"%ser) == 1:
            print("l utente ha questo servizio disponibile")  
'''