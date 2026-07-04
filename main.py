from flask import Flask, render_template
from pokedex import POKEDEX


app = Flask(__name__)

@app.route ("/")
def index ():
    return render_template("index.html")


@app.route ("/api/health")
def health ():
    return {"status":"ok"}

@app.route("/pokemon/<name>")

def get_pokemon(name):
    pokemon_found =  find_pokemon_by_name(name)

    if pokemon_found:
        return render_template("pokemon.html", pokemon=pokemon_found)
    else:
        return render_template("not-found.html",name=name), 404

def find_pokemon_by_name(name):
    for pokemon in POKEDEX:
        if pokemon["name"].lower() == name.lower():
            return pokemon
    return None

@app.route("/api/pokemon/<name>")
def get_pokemon_json(name):
    pokemon = find_pokemon_by_name(name)

    if pokemon:
        return pokemon
    else:
        return {"error":"unknown Pokemon"}, 404