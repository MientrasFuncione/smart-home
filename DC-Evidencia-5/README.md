# Modulo Programador - ( Tercera Instancia )

<img width="762" height="538" alt="Image" src="https://github.com/user-attachments/assets/0881eaad-d24d-44c9-80da-11234da90e66" />

### Introducción

A partir de la instancia anterior, donde utilizabamos un programacion estructura, en  esta instancia tenemos como objetivo lograr implementa una Programacion Orientada a Objetos, aplicando los conceptos fundamentales como abstracción, encapsulamiento, herencia, agregación, etc.

Con respecto al modelo entidad relacion tuvimos cambios debido a la inconsistencia del mismo, donde decimos solo implementar las Entidades Usuario, Dispositivo y Automatización.

---

### Diagrama de Clases

![UML-diagrama de clases.png](attachment:a7daa178-3dc2-4ca2-8b92-e8efbcb29c96:UML-diagrama_de_clases.png)

En el diagrama de clases presentado podemos visualizar tres tablas las cuales nos ayudan a conceptualizar, analizar y comunicar la estructura del sistema de manera efecticva 

Cabe aclarar que el diagrama de UML puede ser mejorado integrando integrando nuevas tablas como dispositivos especificos como “Luces” donde busquemos un comportamiento diferente al de los demas objetos como un prendido automatico a determinada hora.

En este caso no lo vimos necesario, debido a que la automatizacion establecida anteriormente fue modificada, por una de uso general.

La automatizacion permite activar automaticamente todos los dispositivos conectados al mismo tiempo, por esta razón no fue necesario implementar mas tablas.

---

### Principios Aplicados

- **Abstraccion**

Una clase es una abstracción de un objeto del mundo real, donde seleccionamos solo lo relevante y ocultamos detalles inncesarios.

Nos permite enfocarnos en que hace un objeto, sin tener en cuenta su comportamiento interno.

En este caso Dispositivo, Usuario y Automatización.

- **Encapsulamiento**

Al declarar los atributos como privados evita que otros objetos o clases modifiquen directamente estos atributos.

En la clase Usuario podes ver los atributos contraseña como atributo privado y rol como atributo protegido. En el caso de constraseña, se establece como privado para que no se pueda acceder a el desde otras partes del código. A esto sumarle la prevención de modificación desde otras clases.

- Agregación

La agregación representa una relación “tiene un”, donde una clase contiente o agrupa a otras clases, tener en cuenta que las partes pueden existir independientemente de todo.
En este caso Usuario existe independientemente de si existe Dispositivo, cosa que como nuestra relacion es n:m un Dispositivo sigue existiendo idependiente del usuario, ya que puede ser accedido por otros usuarios.

Lo mismo pasa con la Automatizacion, al ser una automatizacion que se aplica a todos los dispositivos, su existencia no depende de un dispositivo y viceversa.

---

### Consideraciones

Debido a que este diagrama puede ser mejorado explicaremos ideas para aplicar.
Como comentamos anteriormente la automatizacion es general, pero podemos tambien agregar comportamientos independientes para cada dispositivos, esto asi, haciendo que nuevos conceptos como “Herencia” y “Poliformismo”.

- Herencia

Podemos agregar al diagrama, los dispositivos de manera individual, como “Luces”, “Aire” o “Aspiradora”, en donde cada dispositivo herede de Usuario sus atributos y metodos, y logrando que cada dispositivo tenga su propio comportamiento.

- Poliformismo

Podemos modificar algunos metodos de la tabla Usuario, haciendo que tenga un comportamiento diferente en cada dispositivo.