from flask import Flask
from helper import pets

app =Flask(__name__)

@app.route('/')
def index():
  return """
  <h1> Adopt a Pet! </h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
<li><a href="/animals/dogs">Dog</a></li>
<li><a href="/animals/cats">Cats</a></li>
<li><a href="/animals/rabbits">Rabbits</a></li>
  </ul>
  """
@app.route('/animals/<variable_name>')
def animals(variable_name):
  html = f'<h1>List of {variable_name}</h1>'
  html += '<ul>'
  for i, pet in enumerate(pets[variable_name]):
    html += f'<li><a href="/animals/{variable_name}/{i}">{pet["name"]}</a></li>'
  html += '</ul>'
  return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  html = f"<h1>{pet['name']}</h1>"
  html += f"<p>Age: {pet['age']}</p>"
  html += f"<p>Breed: {pet['breed']}</p>"
  html += f"<p>Descrription: {pet['description']}</p>"
  html += f'<img src="{pet["url"]}" alt="{pet["name"]}">'
  return html











