# Modulo Programador - ( Tercera Instancia )

![Image](https://github.com/user-attachments/assets/b0e031df-5a4d-45e1-a7d6-bb44d33d5f00)

### Introducción

A partir de la instancia anterior, donde utilizabamos un programacion estructura, en  esta instancia tenemos como objetivo lograr implementa una Programacion Orientada a Objetos, aplicando los conceptos fundamentales como abstracción, encapsulamiento, herencia, agregación, etc.

Con respecto al modelo entidad relacion tuvimos cambios debido a la inconsistencia del mismo, donde decimos solo implementar las Entidades Usuario, Dispositivo y Automatización.

A partir de esta decisión, se simplifica el modelo y se enfoca en las entidades principales del sistema, evitando redundancias e inconsistencias. Esto permite que cada clase tenga una responsabilidad clara, facilitando la aplicación de los conceptos de la Programación Orientada a Objetos como **abstracción**, al modelar solo lo esencial de cada entidad; **encapsulamiento**, al proteger los datos y exponer solo los métodos necesarios; **herencia**, si en el futuro se crean clases derivadas; y **agregación**, para reflejar las relaciones entre Usuario, Dispositivo y Automatización. Esta estructura hace que el código sea más **modular, escalable y fácil de mantener**, en comparación con la programación estructurada anterior.

---

### Principios Aplicados

- **Asociación**

Una relación de asociación representa un vínculo entre dos o más clases que colaboran entre sí.

En este caso, las clases Usuario y Dispositivo cumplen con esta característica, estableciendo una asociación bidireccional. Lo mismo ocurre entre Dispositivo y Automatización.

Podemos entender que el Usuario conoce al Dispositivo, y según la multiplicidad, un Usuario puede tener cero o más Dispositivos, mientras que un Dispositivo puede ser controlado por varios Usuarios.

La asociación no implica propiedad ni dependencia, sino simplemente una interacción funcional o lógica entre las clases dentro del sistema.

- **Encapsulamiento**

Al declarar los atributos como **privados**, se evita que otras clases u objetos **accedan o modifiquen directamente** dichos valores.

En la clase **Usuario**, el atributo **contraseña** se define como **privado**, lo que impide su acceso directo desde fuera de la clase. Esto ayuda a **proteger la información sensible** y **evitar modificaciones indebidas** desde otras partes del código.

Por otro lado, el atributo **rol** se declara como **protegido**, permitiendo que solo la propia clase y sus **subclases** puedan accederlo, pero no cualquier objeto externo.

En conjunto, esta práctica promueve el principio de **encapsulamiento**, fundamental para mantener la **seguridad y consistencia** de los datos dentro del sistema.

- **Agregación**

La agregación representa una relación “tiene un”, donde una clase contiene o agrupa a otras clases.

Es importante tener en cuenta que las partes pueden existir independientemente del todo.

En este caso, aplicamos agregación desde los respectivos gestores, ya que forman parte del dominio del sistema, pero las clases que administran no dependen directamente de ellos para existir.

Por ejemplo, la clase GestiónUsuario se encarga de administrar varios Usuario, pero si se elimina GestiónUsuario, los usuarios seguirán existiendo en la base de datos.

Lo mismo sucede con GestiónDispositivo, que gestiona varios Dispositivo, los cuales también pueden existir de forma independiente

- **Principio de responsabilidad única**

El principio de responsabilidad única establece que cada clase debe tener una única funcion o motivo dentro del sistema. Encargandose asi de solo una tarea o proposito.
En este caso los dominios Usuario, Dispositivo, Automatización, se encargan de modelar los atributos y metodos individuales. Las clases de gestión se encargar exclusivamente de administrar los usuarios, los dispositivos y las automatizaciones, de esta forma facilita el mantenimiento y la escalabilidad, y sobre todo la lectura del código. 

---

### Consideraciones

Debido a que este diagrama puede ser mejorado explicaremos ideas para aplicar.
Como comentamos anteriormente la automatizacion es general, pero podemos tambien agregar comportamientos independientes para cada dispositivos, esto asi, haciendo que nuevos conceptos como “Herencia” y “Poliformismo”.

- Herencia

Podemos agregar al diagrama, los dispositivos de manera individual, como “Luces”, “Aire” o “Aspiradora”, en donde cada dispositivo herede de Usuario sus atributos y metodos, y logrando que cada dispositivo tenga su propio comportamiento.

- Poliformismo

Podemos modificar algunos metodos de la tabla Usuario, haciendo que tenga un comportamiento diferente en cada dispositivo.