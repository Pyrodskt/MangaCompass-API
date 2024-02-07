from flask import Flask, request
import flask
import json
import file_buffer

app = Flask(__name__)
#A enlever => a des fins de tests en local (cors policy déclanchée car même origine)
app.config['CORS_HEADERS'] = 'Content-Type'


def filter_by_name(search_string):
    # fonction de filtre sur les titres dans les données, retourne l'objet
    data = file_buffer.get_file_data()
    ret = []
    for i in data['datas']:
        if search_string.lower() in i['title'].lower():
            ret.append(i)
    return ret 

def update_manga_data(title, new_datas):
    # update du current chap a lire.
    content = file_buffer.get_file_data()
    for i in content['datas']:
        if i['title'] == title:
            i['current'] = new_datas
            file_buffer.save_file(content)
            return 200
    
# route principale pr tous les mangas
@app.route("/mangas", methods=["GET"])
def mangas():
    response = flask.jsonify(message=file_buffer.get_file_data())
    response.headers.add('Access-Control-Allow-Origin', "*")
    return response

# route secondaire pour rechercher par titre
@app.route('/manga/<title>', methods=["GET", "POST"])
def manga(title):
        
    if request.method == "GET":
        response = flask.jsonify(message=filter_by_name(title))
        response.headers.add('Access-Control-Allow-Origin', "*")

    if request.method == "POST":
        params = request.args.get('current')
        update_manga_data(title, params)
        response = flask.jsonify(message="Success")
        response.headers.add('Access-Control-Allow-Origin', "*")
        
    
    return response
        
    

# route tertiaire pour ajouter des mangas dans la liste
@app.route('/add/manga', methods=["GET", "POST", "OPTIONS"])
def add_manga():
    print(request.form)
    title = request.form.get('title')
    url = request.form.get('url')
    old_data = file_buffer.get_file_data()
    if filter_by_name(title):
        response = flask.jsonify(message='Denied')
        response.headers.add('Access-Control-Allow-Origin', "*")
        return response
    else:
        old_data["datas"].append({"title": title, "url": url, "current": "", "list": []})
        file_buffer.save_file(content=old_data, filename='data/data.json')
        response = flask.jsonify(message='Data added successfully ')
        response.headers.add('Access-Control-Allow-Origin', "*")
        return response
    
if __name__ == "__main__":
    app.run("0.0.0.0", 5000)

app.run()