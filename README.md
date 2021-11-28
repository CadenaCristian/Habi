# Habi
1. En la creación del primer service me base en la idea de usa url dinamicas como las que se usan en Django, pero sin usar ningun Framework.
2. No describo un objeto JSON, ya que me parecio que no era necesario, se pueden manejar los parametros por medio de la URL y usarlos para filtrar.
3. A continuación escribire los comandos que se necesitra para compilar este proyecto (despues de haberlo clonado).
- se puede o no usar un entorno virtual eso es a elección, en caso de usarlo debe de activarse previamente y luego ejecutar el siguiente comando: pip install -r libs.txt 
- Luego de ubicarse en la ruta donde se clono el proyecto ejecute el siguiente comando para levantar el backend:  uvicorn main:app --reload
- Luego de eso puede colocar la siguiente url en cualquier aplicativo para hacer peticiones ya sea postman, thunder client u otro: http://localhost:8000/
