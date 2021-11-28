from fastapi import FastAPI
from INMUEBLES.inmuebles import consultar_inmuebles

app = FastAPI(
    title='Prueba',
    description='Estamos haciendo una prueba con FASTAPI',
    version='1.0.1'
)


@app.get('/')
@app.get('/{year}')
@app.get('/{year}/{city}')
@app.get('/{year}/{city}/{state}')
def main(year='0', city='0', state='0'):
    response = consultar_inmuebles(year, city, state)
    return response
