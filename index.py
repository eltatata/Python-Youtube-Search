import urllib
from urllib import parse, request
import re

# pedir al usuario la busqueda
text_user = input("cual es la busqueda que deseas realizar: ")

# covertir el texto normal a texto de busqueda
converted_text = parse.urlencode({'search_query': text_user})
HTML = request.urlopen(f"http://www.youtube.com/results?{converted_text}")
results = re.findall('watch\?v=(.{11})',HTML.read().decode('utf-8'))

# mostrar el resultado probablemente mas acertado
print("el resultado de la busqueda es:")
print(f"https://www.youtube.com/watch?v={results[0]} \n")

# mostrar todos los resultados encontrados
print("estos son los otros resultados")
for id in results:
  print(f"https://www.youtube.com/watch?v={id}")
