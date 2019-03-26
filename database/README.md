# INFORMACIÓN SOBRE EL USO DE LA BASE DE DATOS
Se usa SQLite para la implementación de la base de datos. Sin embargo, se usa la librería
de python SQLAlchemy. De esta manera, no se usan queries para obtener e insertar datos a la
db, sino que se utilizan las funciones ya implementadas por la librería.

Aquí una miniguía del uso de las principales funciones para insertar y leer datos para implementar
nuestra base de datos.

## LAS SESIONES
En el archivo database/crud.py, se usa la función `sessionmaker(bind=engine)`. Esta genera un
constructor de sesiones. Una sesión se usará para realizar una transacción con funciones que imitan
el comportamiento de las queries.

### QUERIES CON LA SESIÓN
`DBSession` almacena el constructor de sesiones dado por `sessionmaker(bind=engine)`.
Para crear una sesión solo basta usar el siguiente comando.

```python
    
    session = DBSession()

```

En una sessión se puede realizar un "query" de la siguiente manera.

```python

    # retorna todos los elementos de TABLA en forma de objetos, almacenados en una lista
    objetos = session.query(Product).all()

    # retorna la lista de todos los elementos que coinciden con el atributo indicado
    objetos = session.query(Product).filter(atributo=dato)

    # retorna un objeto elemento de la TABLA, el primero que coincida
    objeto = session.query(Product).filter(atributo=dato).first()

    # cierra la sesión
    session.close()
```

### INSERTAR DATOS
De la misma manera, usamos una sesión para insertar un elemento a una tabla determinada.

```python
    # crea una sesión
    session = DBSession()

    # crea un objeto elemento para insertar
    producto = Product(name="nombre", price="1.20", description="esto es una descripcion")

    # inserta el objeto, no es necesario especificar la tabla
    session.add(producto)

    # confirma la transacción
    session.commit()

    # cierra la sesión
    session.close()
```

**OBSERVACIÓN**: la tabla que se usa es la clase que la modela, en este caso es `class Product`.

