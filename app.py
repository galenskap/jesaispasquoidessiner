import sqlite3
#import cherrypy
from bottle import Bottle, run, view, debug, template

app = Bottle()

@app.route('/')
def objets_list():
    conn = sqlite3.connect('generateur.db')
    c = conn.cursor()
    c.execute("SELECT texte FROM objets WHERE status LIKE '1' ORDER BY RANDOM() LIMIT 1")
    objet = c.fetchall()
    c.execute("SELECT texte FROM situations WHERE status LIKE '1' ORDER BY RANDOM() LIMIT 1")
    situation = c.fetchall()
    output = template('views/rand', objet=objet[0], situation=situation[0])
    return output

@app.route('/list')
def objets_list():
    conn = sqlite3.connect('generateur.db')
    c = conn.cursor()
    c.execute("SELECT id, texte FROM objets WHERE status LIKE '1'")
    objets = c.fetchall()
    c.execute("SELECT id, texte FROM situations WHERE status LIKE '1'")
    situations = c.fetchall()
    output = template('views/list', objets=objets, situations=situations)
    return output

# static files
@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/static/')


#run(host='0.0.0.0', port=80, server='cherrypy')
