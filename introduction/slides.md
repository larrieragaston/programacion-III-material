---
theme: default
title: Programación III - Introducción
info: |
  Presentación introductoria de la materia Programación III.
  INSPT - UTN
author: Gastón Larriera
keywords: programación funcional, INSPT, UTN
transition: slide-left
mdc: true
---

---
layout: center
---

# Programación III

<div class="abs-b mb-8 text-sm opacity-60">
INSPT - UTN
</div>

---
layout: center
---

# Presentación personal

---
layout: default
---

# Profesor: Gastón A. Larriera

- Técnico Superior en Informática
- Profesor en Disciplinas Industriales
- Ingeniero en Informática
- Software Engineer (MERCADOLIBRE)

---
layout: default
---

# Presentación de alumnos

- Nombre
- ¿Profesorado?
- Conocimientos de programación
- Trabajo

---
layout: center
---

# Contenidos de la materia

---
layout: default
---

# Primera parte

1. **Cálculo Lambda**
2. **Clojure**

---
layout: default
---

# Segunda parte

1. **Programación Web FullStack**
   1. Mongo
   2. Express
   3. React
   4. Node
2. **API Rest**
3. **JSON**
4. **JavaScript**
5. **HTML**
6. **CSS**

---
layout: center
---

# Condiciones de aprobación

---
layout: two-cols
---

# Condiciones de aprobación

::left::

## Regularidad

- 75% de asistencia
- 1er Parcial aprobado (6 o más)
- Actividades adicionales
- Proyecto web full stack JS (avance 40%)

**Final:** Proyecto web full stack JS - MERN (100%)

::right::

## Promoción

- 1er Parcial aprobado (8 o más)
- Proyecto web full stack JS (100%)

---
layout: center
---

# Vías de comunicación

---
layout: center
---

# Contacto

<div class="grid grid-cols-2 gap-12 mt-8">
<div class="text-left">

### Mail institucional
gaston.larriera@inspt.utn.edu.ar

</div>
<div class="text-left">

### Aula virtual
Programación III - 3.603

</div>
</div>

---
layout: center
---

# Programación Funcional

---
layout: default
---

# Ejercicio

Dado un listado de colores, decir si el color `'red'` está en el listado.

**¿Cómo resolver el problema?**

---
layout: default
---

# Java - Forma Imperativa

```java {all|2|3|4-8|9}
List<String> colors = Arrays.asList("blue", "green", "red", "yellow");
boolean hasRed = false;
for (String color : colors) {
    if (color.equals("red")) {
        hasRed = true;
        break;
    }
}
System.out.println("Has color red? " + hasRed);
```

---
layout: default
---

# Java 8 - Forma Declarativa

```java
System.out.println("Has color red?: " + colors.contains("red"));
```

<br>

### ¿Cuál es el problema?

<!-- TODO: acá podés expandir la reflexión sobre imperativo vs declarativo -->
