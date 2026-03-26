---
theme: bricks
title: Programación III - Cálculo Lambda (In progress)
info: |
  Cálculo Lambda - Programación III
  INSPT - UTN
author: Gastón Larriera
keywords: cálculo lambda, programación funcional, INSPT, UTN
transition: slide-left
mdc: true
---

# Cálculo Lambda

---
layout: center
---

# Ideador

---
layout: center
---

# Alonzo Church

<div class="mt-6 text-left max-w-md mx-auto">

- Lógico - Matemático
- 1930
- Computación teórica
- Profesor de Alan Turing

</div>

---
layout: center
---

# Fundamentos

---
layout: default
---

# Sistema Formal

- Definición de función
- Aplicación de función
- Recursividad

---
layout: default
---

# Función computable

- Expresada
- Evaluada

---
layout: default
---

# ≠ Máquina de Turing

- Reglas de transformación
- Implementación real

---
layout: center
---

# Programas como expresiones

---
layout: default
---

# Programa funcional

- Expresión
  - Algoritmo
  - Entradas

---
layout: default
---

# Reglas de conversión

**Reducción**

$$E[P] \to E[P'], \text{ siempre y cuando } P \to P'$$

---
layout: default
---

# Ejemplo

$$
(7 + 4) \times (8 + 5 \times 3)
$$

<v-clicks>

$$\to 11 \times (8 + 5 \times 3)$$

$$\to 11 \times (8 + 15)$$

$$\to 11 \times 23$$

$$\to 253$$

</v-clicks>

---
layout: default
---

# Ejemplo

```
primero (ordenar (unir (a, ordenar (b))))
→ primero (ordenar (unir (a, b)))
→ primero (ordenar (a, b))
→ primero (a, b)
→ "conejo"
```

---
layout: center
---

# Definición Formal

---
layout: default
---

# Elementos

- Variable
- Abstracción
- Aplicación

---
layout: default
---

# Sintaxis

$$\langle expresión\ \lambda \rangle ::= \langle variable \rangle\ |\ (\lambda \langle variable \rangle . \langle expresión\ \lambda \rangle)\ |\ (\langle expresión\ \lambda \rangle\ \langle expresión\ \lambda \rangle)$$

---
layout: default
---

# Ejemplos

```
x
(λx.x)
((λx.x) y)
((λx.(x y)) ((λy.(y y)) z))
(((λx.(x y)) (λy.(y y))) z)
```

---
layout: default
---

# Convenciones

$$(((\lambda x.\ (\lambda y.\ (y\ x)))\ a)\ b)$$

<v-click>

Se puede abreviar como:

$$\lambda x\ y.\ y\ x\ \ a\ \ b$$

</v-click>

---
layout: center
---

# Variables Libres y Ligadas

---
layout: default
---

# Funciones Matemáticas...

- $f(x) = x^2 + 2$
- $f(z, w) = z + w^2 + 2$

---
layout: default
---

# Variables Libres y Ligadas

La variable **x** ocurre **ligada** en la expresión N si y solo si:

- $N = \lambda z.M$ siendo $x = z$ o cuando x ocurre ligada en M
- $N = M\ P$ donde x ocurre ligada en M y/o en P

<div class="mt-4">

La variable **x** ocurre **libre** en la expresión N si y solo si:

- $N = \lambda z.M$ siendo $x \neq z$ y donde x ocurre libre en M
- $N = M\ P$ donde x ocurre libre en M y en P

</div>

---
layout: default
---

# Ejemplo

| Expresión | Libres | Ligadas |
|---|---|---|
| $\lambda z.x\ y$ | x, y | — |
| $\lambda x.x\ y$ | y | x |
| $\lambda y.x\ y$ | x | y |
| $\lambda x\ y.x\ y$ | — | x, y |
| $(\lambda z.z\ x\ y)\ (\lambda x.x)$ | x, y | z, x |

---
layout: center
---

# Reglas de conversión

---
layout: default
---

# Regla de conversión Alfa (α)

*Sustitución de variables*

$$\lambda x.\ M =_\alpha \lambda y.\ M[y/x]$$

---
layout: default
---

# Ejemplos α

```
λx.x                   → λy.y
λx.y x                 → λz.y z
λx.z x x (λu x.x u) v x
    → λy.z y y (λu x.x u) v y
λx y.x z y             → ?
```

---
layout: default
---

# Regla de conversión Beta (β)

*Aplicación de un valor en una entrada*

$$\beta\text{-redex} \Rightarrow (\lambda x.M)\ N$$

---
layout: default
---

# Ejemplo β-redex

```
(λx.x x) z
(λx.x x) (λy.y y)
(λx.x) (λy.y y) z
(λx.(λu.u) (λv.x v)) ((λt.t t) w)
```

<div class="mt-4">

```
x (λy.y y)    ← NO ES UNA β-redex
x (λy.y y)    ← FORMA NORMAL
```

</div>

---
layout: default
---

# Regla de conversión Beta (β)

*Aplicación de un valor en una entrada*

Consiste en realizar la **reducción** de una β-redex

---
layout: default
---

# Ejemplos β

```
(λx.x) z =β z

(λx.(λu.u) (λv.x v)) ((λt.t t) w)
  =β (λu.u) (λv.(λt.t t) w v)
  =β λv.(λt.t t) w v
  ...

(λz w.w z w) w x =β ?

(λx.x x) (λy.y y) =β ?
```

---
layout: default
---

# Regla de conversión Eta (η)

*Extensionalidad*

$$\eta\text{-redex} \Rightarrow \lambda v.M\ v$$

$$\text{Conversión} \Rightarrow \lambda v.M\ v =_\eta M$$

---
layout: default
---

# Ejemplos η

```
(λx.f x) y  =η f y

(λx v.x v) ((λt.t t) w)
  =β λv.((λt.t t) w) v
  ...
  =η w y

(λv.w x y v) z  =η ?

λx.x t x  =η ?
```

---
layout: center
---

# Estrategias de Reducción

---
layout: default
---

# Call-by-name

Consiste en ir reduciendo siempre la β-redex más **externa desde la izquierda** y que **no esté ubicada dentro de una abstracción lambda**, hasta llegar a una expresión en forma normal de cabecera.

```
(λu.u (λt.t) ((λy.y) u)) ((λz.z) x)
  =β (λz.z) x (λt.t) ((λy.y) ((λz.z) x))
  =β x (λt.t) ((λy.y) ((λz.z) x))
```

---
layout: default
---

# Orden normal

Consiste en ir reduciendo siempre la β-redex más **externa desde la izquierda**.

```
(λu.u (λt.t) ((λy.y) u)) ((λz.z) x)
  =β (λz.z) x (λt.t) ((λy.y) ((λz.z) x))
  =β x (λt.t) ((λy.y) ((λz.z) x))
  =β x (λt.t) ((λz.z) x)
  =β x (λt.t) x
```

<div class="mt-2 text-green-600 font-semibold">

(+) Si tiene, siempre permite llegar a su forma normal

</div>

---
layout: default
---

# Call-by-value

Consiste en ir reduciendo siempre la β-redex más **interna desde la izquierda** y que **no esté ubicada dentro de una abstracción lambda**.

```
(λu.u (λt.t) ((λy.y) u)) ((λz.z) x)
  =β (λu.u (λt.t) ((λy.y) u)) x
  =β x (λt.t) ((λy.y) x)
  =β x (λt.t) x
```

---
layout: default
---

# Orden aplicativo

Consiste en ir reduciendo siempre la β-redex más **interna desde la izquierda**.

```
(λu.u (λt.t) ((λy.y) u)) ((λz.z) x)
  =β (λu.u (λt.t) u) ((λz.z) x)
  =β (λu.u (λt.t) u) x
  =β x (λt.t) x
```

<div class="mt-2">

(*) Permite llegar a su forma normal de cabecera

</div>

---
layout: default
---

# Comparación

<div class="text-sm">

**Call-by-name**

```
(λu.(λt.t) ((λy.y) w)) ((λv.v) r) ((λz.z z) (λx.x x))
  =β (λt.t) ((λy.y) w) ((λz.z z) (λx.x x))
  =β (λy.y) w ((λz.z z) (λx.x x))
  =β w ((λz.z z) (λx.x x))
```

Se llega a la **forma normal de cabecera**

</div>

<div class="text-sm mt-2">

**Orden normal**

```
... =β w ((λz.z z) (λx.x x))
    =β w ((λx.x x) (λx.x x)) ...
```

Se produce un **ciclo infinito**

</div>

---
layout: default
---

# Comparación (cont.)

<div class="text-sm">

**Call-by-value**

```
(λu.(λt.t) ((λy.y) w)) ((λv.v) r) ((λz.z z) (λx.x x))
  =β (λu.(λt.t) ((λy.y) w)) r ((λz.z z) (λx.x x))
  =β (λt.t) ((λy.y) w) ((λz.z z) (λx.x x))
  =β (λt.t) w ((λz.z z) (λx.x x))
  =β w ((λz.z z) (λx.x x))
  =β w ((λx.x x) (λx.x x)) ...  → ciclo infinito
```

</div>

<div class="text-sm mt-4">

**Orden aplicativo**

```
(λu.(λt.t) ((λy.y) w)) ((λv.v) r) ((λz.z z) (λx.x x))
  =β (λu.(λt.t) w) ((λv.v) r) ((λz.z z) (λx.x x))
  =β (λu.w) ((λv.v) r) ((λz.z z) (λx.x x))
  =β (λu.w) r ((λz.z z) (λx.x x))
  =β w ((λz.z z) (λx.x x))
  =β w ((λx.x x) (λx.x x)) ...  → ciclo infinito
```

</div>

---
layout: center
---

# Funciones Lógicas

---
layout: default
---

# Funciones Lógicas

Mediante abstracciones es posible definir representaciones de los valores verdadero y falso, y funciones lógicas aplicables sobre ellos.

```
// Si p entonces q, si no r
If = λp.λq.λr.p q r
```

```javascript
// Analogía con un lenguaje
if (p) {
  q;
} else {
  r;
}
```

---
layout: default
---

# Otras representaciones

```
True  = λx.λy.x
False = λx.λy.y
Not   = λp.p False True
And   = λp.λq.p q False
Or    = λp.λq.p True q
```

---
layout: center
---

# Funciones Numéricas y Relaciones

---
layout: default
---

# Números de Church

También mediante abstracciones se pueden definir numerales y funciones numéricas y relacionales aplicables sobre ellos.

```
0 = λf.λx.x
1 = λf.λx.f x
2 = λf.λx.f (f x)
3 = λf.λx.f (f (f x))
4 = λf.λx.f (f (f (f x)))
5 = λf.λx.f (f (f (f (f x))))
```

---
layout: default
---

# Operaciones

<div class="text-sm">

```
Succ   = λn.λf.λx.f (n f x)
Pred   = λn.λf.λx.n (λg.λh.h (g f)) (λu.x) (λu.u)
Add    = λm.λn.λf.λx.m f (n f x)
Sub    = λm.λn.n Pred m
Mul    = λm.λn.λf.λx.m (n f) x
Pow    = λm.λn.λf.λx.n m f x
```

```
Fibo   = λn.n (λf.λa.λb.f b (Add a b))
              (λx.λy.x) (λf.λx.x) (λf.λx.f x)

IsZero = λn.n (λz.(λx.λy.y)) (λx.λy.x)
```

</div>

---
layout: default
---

# Ejemplo — IsZero

Averiguar si el número **4** es cero

```
IsZero = λn.n (λz.(λx.λy.y)) (λx.λy.x)
4      = λf.λx.f (f (f (f x)))
0      = λf.λx.x
```

---
layout: default
---

# Resolución — IsZero 4

<div class="text-sm">

```
// IsZero 4
(λn.n (λz.λx.λy.y) (λx.λy.x)) (λf.λx.f (f (f (f x))))

=β (λf.λx.f (f (f (f x)))) (λz.λx.λy.y) (λx.λy.x)

=β (λx.(λz.λx.λy.y) ((λz.λx.λy.y) ((λz.λx.λy.y)
    ((λz.λx.λy.y) x)))) (λx.λy.x)

=β (λz.λx.λy.y) ((λz.λx.λy.y) ((λz.λx.λy.y)
    ((λz.λx.λy.y) (λx.λy.x))))

=β λx.λy.y    // False
```

</div>

---
layout: default
---

# Ejemplo — Add 2 1

```
Add = λm.λn.λf.λx.m f (n f x)
2   = λf.λx.f (f x)
1   = λf.λx.f x
```

---
layout: default
---

# Resolución — Add 2 1

<div class="text-sm">

```
// Add 2 1
(λm.λn.λf.λx.m f (n f x)) (λf.λx.f (f x)) (λf.λx.f x)

=β (λn.λf.λx.(λf.λx.f (f x)) f (n f x)) (λf.λx.f x)
=β (λf.λx.(λf.λx.f (f x)) f ((λf.λx.f x) f x))
=β (λf.λx.(λx.f (f x)) ((λf.λx.f x) f x))
=β (λf.λx.(f (f ((λf.λx.f x) f x))))
=β (λf.λx.(f (f ((λx.f x) x))))
=β (λf.λx.(f (f (f x))))

// En los números de Church es 3
```

</div>

---
layout: center
---

# Combinadores

---
layout: default
---

# Cálculo de combinadores SKI

Las expresiones lambda que no contienen ninguna variable libre se denominan **combinadores**.

<div class="mt-4">

| Combinador | Definición | Nombre |
|---|---|---|
| **S** | $\lambda x.\lambda y.\lambda z.x\ z\ (y\ z)$ | Fusión *(Verschmelzungsfunktion)* |
| **K** | $\lambda x.\lambda y.x$ | Constancia *(Konstanzfunktion)* |
| **I** | $\lambda x.x$ | Identidad *(Identitätsfunktion)* |

</div>

<div class="mt-4 text-sm opacity-80">

El cálculo de combinadores SKI es lo suficientemente potente como para codificar cualquier función computable.

</div>

---
layout: default
---

# Otros combinadores

```
B = λx.λy.λz.x (y z)
C = λx.λy.λz.x z y
D = λx.λy.λz.λv.x y (x v z)
M = λx.x x
K' = λx.λy.y
Y = λf.(λx.f (x x)) (λx.f (x x))    // Punto fijo
Ω = (λx.x x) (λx.x x)
```

---
layout: default
---

# Recursividad

Se representa utilizando un combinador de punto fijo, en este caso utilizamos **Y**:

```
Fact = Y (λf.λx.If (IsZero x) 1 (Mul x (f (Pred x))))
```

---
layout: center
---

# Pares y Listas

---
layout: default
---

# Par ordenado

Un par ordenado está compuesto de dos elementos, denominados **primero** y **segundo**.

$$(a, b) = \lambda s.s\ a\ b$$

```
// Función para construir pares ordenados
Pair = λx.λy.λs.s x y
```

---
layout: default
---

# First y Second

<div class="text-sm">

```
First = λp.p True
```

```
// Ejemplo → First (Pair p q)
(λp.p (λx.λy.x)) ((λx.λy.λs.s x y) p q)
  =β (λp.p (λx.λy.x)) ((λy.λs.s p y) q)
  =β (λp.p (λx.λy.x)) (λs.s p q)
  =β (λs.s p q) (λx.λy.x)
  =β (λx.λy.x) p q
  =β (λy.p) q
  =β p
```

```
Second = λp.p False
```

```
// Ejemplo → Second (Pair p q)
...  =β q
```

</div>

---
layout: default
---

# Listas

<div class="text-sm">

```
// Lista vacía
Nil = Pair True True
// O también
Nil = λz.z

// La lista (a b c)
(False . (a . (False . (b . (False . (c . (λz.z)))))))
```

```
// Verificar si una lista está vacía
Null = First

// Construir un nodo de cabeza x y cola y
Cons = λx.λy.Pair False (Pair x y)

// Obtener la cabeza y la cola de una lista
Head = λz.First (Second z)
Tail = λz.Second (Second z)
```

</div>

---
layout: center
---

# ¡Muchas Gracias!
