# React

## El salto de paradigma más grande

Hasta acá vieron paradigmas imperativos y orientados a objetos (Java, C) y bases de datos relacionales, en los primeros dos años de la carrera. El salto más grande de esta unidad es el modelo **declarativo, basado en componentes** de React — y conecta directo con el eje funcional de todo el curso: un componente de React es, en esencia, **una función pura de `props`/`state` a JSX**. Mismos props y mismo state, mismo resultado visual — la misma idea de "función pura" de JS Funcional, aplicada a interfaces de usuario en vez de a transformaciones de datos.

De acá en adelante, todo el código de la unidad se escribe en **TypeScript**, recién visto en el tema anterior — empezando por los `props` tipados de cada componente.

## ¿Qué es React?

React es una **librería** de JavaScript/TypeScript para construir interfaces de usuario — no un framework completo (a diferencia de Angular): se enfoca únicamente en la capa de vista — cómo se ve la pantalla y cómo se actualiza cuando cambian los datos — y se combina con otras librerías para todo lo demás (ruteo, llamadas HTTP, manejo de formularios, componentes visuales...). Buena parte de este apunte es, justamente, ese "combinar piezas".

Se usa tanto para la web como, con **React Native**, para apps móviles — mismo modelo mental, distinto renderer. Tampoco reemplaza HTML/CSS/JS: los combina. JSX (se ve más adelante) es JavaScript con una sintaxis parecida a HTML.

### Historia

- **2011** — Jordan Walke, ingeniero de Facebook, crea un prototipo interno ("FaxJS") para el feed de noticias.
- **2012** — Instagram lo adopta y lo pone a prueba en producción, a gran escala.
- **Mayo 2013** — se libera como **código abierto**, en la conferencia JSConf US.
- **Febrero 2019** (v16.8) — llegan los **Hooks**: `useState`/`useEffect` reemplazan a los componentes de clase como forma estándar de escribir componentes. De acá en más, este apunte usa siempre funciones — las clases todavía existen y se encuentran en código viejo, pero no se cubren acá.
- **Marzo 2022** (v18) — renderizado concurrente.
- **Diciembre 2024** (v19) — Server Components estables, `use()`.
- **Hoy** — lo mantiene Meta junto con una comunidad enorme.

Trece años de historia continua es mucho tiempo en el mundo del frontend. Su modelo central — **la UI como función del estado** — se popularizó tanto que hoy influye en el diseño de otros frameworks (Vue, Svelte), aunque cada uno lo resuelva a su manera. React no inventó los "componentes" — la idea ya existía en interfaces de escritorio hace décadas. Lo que sí instaló como estándar de la industria fue combinarlos con un DOM virtual y un flujo de datos unidireccional, que se explican más abajo.

### Cómo se compara

<div class="overflow-x-auto">

| | React | Vue | Angular | Svelte | Solid |
|---|---|---|---|---|---|
| Lanzamiento | 2013 | 2014 | 2016 (AngularJS: 2010) | 2016 | 2018 |
| ⭐ GitHub | ~230k | ~210k | ~95k | ~85k | ~36k |
| % de uso (State of JS 2025) | **85%** | 52% | 48% | 27% | 10% |
| % satisfacción (State of JS 2025) | 72% | 84% | 48% | 86% | **90%+** |

</div>

React lidera en adopción real. Angular es el único **framework completo** de la lista, pesado pero atractivo en proyectos empresariales grandes. Svelte y Solid, con mucha menos gente usándolos, son los que generan mayor satisfacción — Solid lleva cinco años consecutivos primero en ese ranking. Otra opción relevante fuera de esta tabla: **Preact**, una reimplementación de la API de React en solo ~3kb, usada cuando el tamaño del bundle es crítico.

Una encuesta mide percepción, no uso real — para eso conviene un dato más duro: el **% de sitios web** que usan cada uno, medido directamente sobre sitios reales (no una encuesta). Sobre todos los sitios que [W3Techs](https://w3techs.com/technologies/overview/javascript_library) releva (la mayoría, webs viejas, estáticas o con un CMS sin ningún framework de este tipo, por eso los números absolutos son chicos), React aparece en 6.1%, Vue en 0.6% y Angular en 0.2% — React, **10 veces más** que Vue y **30 veces más** que Angular.

<div class="practice-box">
<p class="practice-label">Para pensar</p>

Las dos tablas de esta sección miden cosas distintas: una, percepción de quienes ya eligieron un framework (encuesta); la otra, presencia real medida sobre sitios (dato duro). ¿Por qué ambas son válidas y ninguna alcanza sola para decidir qué framework aprender?
</div>

## Principales características

- **Declarativo** — se describe QUÉ se quiere ver, no los pasos para lograrlo.
- **Basado en componentes** — la UI se arma combinando piezas reutilizables.
- **DOM virtual** — actualiza la pantalla sin recalcular todo de cero.
- **Flujo de datos unidireccional** — los datos bajan, los eventos suben.
- **Ecosistema enorme** — se combina con otras librerías para todo lo demás.

### Por qué declarativo

```js
// Imperativo: hay que describir CÓMO llegar al resultado, paso a paso
const li = document.createElement('li')
li.textContent = 'Mouse'
li.classList.add('product-item')
document.querySelector('ul').appendChild(li)
```

```jsx
// Declarativo: se describe QUÉ se quiere ver, no los pasos para lograrlo
<ul>
  <li className="product-item">Mouse</li>
</ul>
```

Con manipulación directa del DOM (imperativo), cada cambio de estado obliga a escribir a mano los pasos para actualizar la pantalla — crear el elemento, asignarle sus propiedades, insertarlo en el lugar correcto. React invierte el problema: se describe la UI **en función del estado actual**, y React se encarga de calcular qué cambió y actualizar solo eso.

### Basado en componentes

Toda la interfaz se arma combinando piezas reutilizables e independientes — como piezas de LEGO que se ensamblan para construir una aplicación completa. Para verlo en código real, cualquier sitio hecho con React se puede inspeccionar con la extensión **React Developer Tools** (Chrome) — muestra el árbol de componentes tal cual está en el código fuente. Una pantalla típica, descompuesta así, se ve como un árbol:

```
App
├── Header                     (usuario, carrito)
├── Sidebar
│   └── CategoryList
│       ├── Category
│       ├── Category
│       └── Category
├── ProductGrid
│   └── ProductCard  × 9
└── Footer
```

Cada caja de esa pantalla — el header, el buscador, cada categoría de la barra lateral, cada tarjeta de producto — es, literalmente, un componente propio, con su propio pedazo de lógica y de markup.

### El árbol del DOM

```
html
├── head
│   ├── title
│   └── meta
└── body
    ├── h1
    ├── p
    │   └── a
    └── ul
        ├── li
        ├── li
        └── li
```

El **DOM** (*Document Object Model*) representa la página como un árbol de nodos — cada etiqueta HTML es un nodo, anidado según cómo esté anidado el HTML. El navegador guarda este árbol en memoria y lo usa para todo: pintar la pantalla, calcular estilos, responder a eventos. Modificarlo directamente (como en el ejemplo imperativo de arriba) es una operación relativamente **costosa**.

### El DOM virtual

- El **DOM virtual** es una representación en memoria (un objeto JS liviano) del árbol del DOM recién visto — no el DOM real del navegador, una copia mucho más barata de modificar.
- Cuando el estado cambia, React arma un DOM virtual nuevo y lo compara (*diff*) contra el anterior — sin tocar el DOM real todavía.
- Recién después aplica al DOM real **solo los cambios mínimos necesarios** (*reconciliation*), en vez de volver a dibujar toda la pantalla.

<div class="flow-row">
<div class="flow-box tone-brand">Cambia el estado</div>
<div class="flow-arrow"><span class="arrow-glyph">→</span></div>
<div class="flow-box">React arma un DOM virtual nuevo</div>
<div class="flow-arrow"><span class="arrow-glyph">→</span></div>
<div class="flow-box">Lo compara (<em>diff</em>) contra el anterior</div>
<div class="flow-arrow"><span class="arrow-glyph">→</span></div>
<div class="flow-box tone-green">Aplica al DOM real solo lo mínimo necesario</div>
</div>

Manipular directamente el DOM real es costoso — trabajar primero en memoria y aplicar el mínimo cambio necesario es la razón principal por la que React sigue siendo rápido incluso en interfaces grandes, con muchos componentes actualizándose seguido.

### Flujo de datos unidireccional

```tsx
function ProductCard({ name, onAddToCart }: { name: string; onAddToCart: () => void }) {
  return (
    <div>
      <span>{name}</span>
      <button onClick={onAddToCart}>Agregar</button>   {/* evento sube */}
    </div>
  )
}

function ProductList() {
  const handleAdd = () => console.log('agregado al carrito')
  return <ProductCard name="Mouse" onAddToCart={handleAdd} />   {/* dato baja */}
}
```

Los **datos bajan** (`props`) y los **eventos suben** (una función que el padre le pasa al hijo). El hijo nunca modifica el estado del padre — así el estado de algo vive en un solo lugar, y siempre es posible rastrear de dónde salió un cambio.

## JSX

### JSX: qué es realmente

```jsx
const nav = (
  <ul id="nav">
    <li>Inicio</li>
  </ul>
)
```

```js
// Lo mismo, compilado por Babel — esto es lo que corre en el navegador
const nav = React.createElement(
  'ul',
  { id: 'nav' },
  React.createElement('li', null, 'Inicio')
)
```

JSX no es HTML ni un lenguaje nuevo — es **azúcar sintáctica** sobre `React.createElement`. Un compilador (Babel, o Vite por debajo) lo traduce a JavaScript plano antes de que llegue al navegador. Escribir JSX a mano es muchísimo más legible que anidar llamadas a `createElement` — pero el resultado final, una vez compilado, es exactamente el mismo código.

<div class="practice-box">
<p class="practice-label">Para pensar</p>

Un `<div className="card"><h3>{name}</h3></div>` con dos niveles de anidamiento se traduce a dos llamadas anidadas a `React.createElement`. ¿Cómo se vería, escrito a mano con `createElement`, un componente con tres niveles de anidamiento? No hace falta escribirlo completo — alcanza con notar cuánto más difícil es de leer que el JSX equivalente.
</div>

## Componentes

### Componentes funcionales + props tipados

```tsx
interface GreetingProps {
  name: string
}

function Greeting({ name }: GreetingProps) {
  return <h1>Hola, {name}!</h1>
}

// Uso
<Greeting name="Ada" />
```

Un componente es una función que recibe `props` (un objeto) y devuelve JSX. `{ name }: GreetingProps` desestructura el prop directamente en la firma — el mismo patrón de destructuring en parámetros ya visto en JS Contemporáneo, ahora con el tipo declarado con la `interface` recién vista en TypeScript. Antes de los Hooks (2019), esto se escribía con clases: `class Greeting extends React.Component { render() { ... } }`. Todavía se puede usar y se encuentra en código viejo, pero prácticamente todo el código nuevo — y este apunte — usa funciones.

### ¿Qué encapsula un componente?

- Su propio **markup** (el JSX que devuelve) — cómo se ve.
- Su propio **estado interno**, si lo necesita (`useState`, `useReducer`) — nadie de afuera lo ve ni lo toca directamente.
- Su propia **lógica**: funciones auxiliares, efectos (`useEffect`), validaciones.
- Opcionalmente, sus propios **estilos** (un archivo CSS asociado, o una librería de estilos).

Por fuera, un componente bien diseñado se ve como una caja cerrada: solo expone sus `props` de entrada — cómo resuelve internamente lo que hace es un detalle de implementación, no algo que el resto de la app necesite conocer.

### Principios para diseñar un componente

<div class="card-grid card-grid-2">
<div class="info-card">
<h4>Una sola responsabilidad</h4>

Si hace demasiadas cosas distintas, conviene partirlo en varios.
</div>
<div class="info-card">
<h4>Props claras y mínimas</h4>

Es la interfaz pública del componente; menos props, más fácil de usar y testear.
</div>
<div class="info-card">
<h4>Estado en el lugar correcto</h4>

Si dos hermanos necesitan el mismo dato, ese estado vive en el padre común, no duplicado.
</div>
<div class="info-card">
<h4>Reutilizable, sin sobre-generalizar</h4>

Abstraer recién cuando aparece un segundo caso real de uso, no antes.
</div>
</div>

Los mismos principios de diseño de funciones (de JS Funcional) — piezas chicas, predecibles y componibles — aplicados a interfaz.

### Composición de componentes

```tsx
function App() {
  return (
    <>
      <Header />
      <div className="layout">
        <Sidebar />
        <ProductGrid>
          <ProductCard name="Mouse" price={18000} />
          <ProductCard name="Teclado" price={25000} />
        </ProductGrid>
      </div>
    </>
  )
}
```

Los componentes se combinan como funciones que llaman a otras funciones — cada caja del árbol de pantalla visto antes es, literalmente, un componente. Es la misma idea de composición de JS Funcional (`compose`/`pipe`), aplicada a piezas de interfaz en vez de a transformaciones de datos puras.

<div class="practice-box">
<p class="practice-label">Practicá</p>

Escribí una `interface UserCardProps { name: string; role: 'alumno' | 'profesor' }` (reutilizando el literal type visto en TypeScript) y un componente `UserCard` que muestre el nombre y, condicionalmente, un ícono o texto distinto según el `role`. Componé un `UserList` que renderice tres `UserCard` con datos distintos.
</div>

### Props vs. state: la diferencia

<div class="card-grid card-grid-2">
<div class="info-card">
<h4>props</h4>

Vienen de afuera (el padre). Son de solo lectura.
</div>
<div class="info-card tone-yellow" style="background:var(--vp-c-yellow-soft);border-color:#fcd34d">
<h4>state</h4>

Vive adentro del componente. Se modifica con su setter.
</div>
</div>

```tsx
interface CounterProps {
  step: number   // prop: lo decide quien usa el componente, de afuera
}

function Counter({ step }: CounterProps) {
  const [count, setCount] = useState(0)   // state: lo maneja el componente, por dentro
  return <button onClick={() => setCount(count + step)}>{count}</button>
}

<Counter step={5} />   // el padre elige step; Counter elige y controla count
```

Si algo puede cambiar por acción del propio componente, es `state`; si lo define quien lo usa desde afuera, es `props` — de solo lectura, no se puede reasignar.

## Estado: `useState`

### `useState`

```tsx
import { useState } from 'react'

function Counter() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <span>{count}</span>
      <button onClick={() => setCount(count + 1)}>+</button>
    </div>
  )
}
```

`useState(0)` declara una variable de estado (`count`, arranca en `0`) y su función para actualizarla (`setCount`). Llamar a `setCount` no solo cambia el valor — le avisa a React que tiene que volver a renderizar el componente con el nuevo estado. `useState` es un **hook**: una función especial de React que solo se puede llamar en el nivel superior de un componente (no dentro de un `if` o un `for`), y que engancha el componente al sistema de estado y re-render de React.

### Por qué no se puede mutar el estado

```tsx
const [items, setItems] = useState(['Mouse', 'Teclado'])

// ❌ mutar directamente no dispara un nuevo render
items.push('Monitor')

// ✅ crear un array nuevo, con spread — React lo detecta y re-renderiza
setItems([...items, 'Monitor'])
```

Mismo tema que en JS Funcional: React detecta cambios comparando **referencias**, no el contenido interno del objeto. Si se muta el array original, la referencia sigue siendo la misma — React no se entera de nada y la pantalla no se actualiza. Por eso el estado siempre se actualiza creando una copia nueva (spread, como en el ejemplo, o un `map`/`filter` que ya devuelven un array nuevo), nunca mutando el valor anterior.

<div class="practice-box">
<p class="practice-label">Practicá</p>

Escribí un componente `Cart` con `useState<string[]>([])` para una lista de productos en un carrito. Agregá un botón "Agregar Mouse" que use spread para agregar `'Mouse'` al array, y otro botón "Vaciar" que reemplace el estado por un array vacío. Mostrá la cantidad de ítems con `{items.length}`.
</div>

## Renderizado condicional y de listas

### Renderizado condicional

```tsx
interface Props {
  isLoggedIn: boolean
}

function Greeting({ isLoggedIn }: Props) {
  if (isLoggedIn) {
    return <h1>Bienvenida de nuevo!</h1>
  }
  return <h1>Por favor, iniciá sesión.</h1>
}

// Alternativa compacta, con operador ternario
function Badge({ isLoggedIn }: Props) {
  return <span>{isLoggedIn ? 'Conectado' : 'Desconectado'}</span>
}
```

JSX es JavaScript — así que "renderizado condicional" es, literalmente, usar `if`/`else` o el operador ternario para decidir qué JSX devolver. Nada nuevo que aprender más allá de lo que ya sabían.

### Listas: `map` de nuevo

```tsx
interface Product {
  name: string
  price: number
}

function ProductList({ products }: { products: Product[] }) {
  return (
    <ul>
      {products.map((p) => (
        <li key={p.name}>{p.name} — ${p.price}</li>
      ))}
    </ul>
  )
}
```

Otra conexión directa con JS Funcional: renderizar una lista es `map`-ear un array de datos a un array de elementos JSX. La única pieza nueva es `key`.

### `key`: por qué hace falta

```tsx
products.map((p) => <li key={p.name}>{p.name}</li>)
```

`key` le da a React una identidad estable por elemento de la lista — así, cuando la lista cambia (se agrega, se quita o se reordena un ítem), React puede saber **cuál** elemento del DOM corresponde a cuál dato, en vez de volver a crear todos desde cero. Tiene que ser única entre elementos hermanos y, idealmente, estable entre renders — un `id` real de los datos, no el índice del array como primera opción (el índice cambia si la lista se reordena, lo que puede causar bugs sutiles de estado mezclado entre ítems).

<div class="practice-box">
<p class="practice-label">Practicá</p>

Con el catálogo de `Product[]` ya usado, renderizá la lista completa con `map` y `key={p.name}`. Después agregá un `useState<boolean>` que alterne entre mostrar todos los productos o solo los que tienen `price > 20000` (renderizado condicional combinado con `filter`, ya visto en JS Funcional).
</div>

## Formularios controlados

### Input controlado

```tsx
import { useState } from 'react'

function SearchBox() {
  const [query, setQuery] = useState('')

  return (
    <input
      value={query}
      onChange={(e) => setQuery(e.target.value)}
      placeholder="Buscar producto..."
    />
  )
}
```

Un input **controlado** tiene su valor manejado por el estado de React (`value={query}`), no por el DOM directamente — cada tecla dispara `onChange`, que actualiza el estado, que a su vez actualiza el `value` mostrado. React queda como la única fuente de verdad del valor del campo, en vez de tener que leerlo del DOM cuando haga falta (que es como se hacía antes, con `document.querySelector(...).value`).

### Formulario con varios campos y filtro

```tsx
function ProductFilter({ products }: { products: Product[] }) {
  const [query, setQuery] = useState('')

  const filtered = products.filter((p) =>
    p.name.toLowerCase().includes(query.toLowerCase())
  )

  return (
    <div>
      <input value={query} onChange={(e) => setQuery(e.target.value)} />
      <ul>
        {filtered.map((p) => <li key={p.name}>{p.name}</li>)}
      </ul>
    </div>
  )
}
```

Todo lo visto hasta acá combinado: estado (`query`), `filter` de JS Funcional, y renderizado de lista con `key`. Este patrón — estado que dispara un filtro que dispara un re-render — es la base de casi cualquier UI interactiva.

<div class="practice-box">
<p class="practice-label">Practicá</p>

Extendé `ProductFilter` con un segundo input numérico para un precio máximo (`useState<number>`), y combiná ambos filtros (`query` y precio máximo) en el mismo `filter`. Los dos inputs deben ser controlados.
</div>

## Efectos: `useEffect`

### `useEffect`: para qué sirve

`useEffect` sirve para manejar **efectos secundarios**: código que interactúa con algo fuera del componente — pedidos de red, timers, suscripciones. La misma idea de "efecto" que se vio como opuesto de "pureza" en JS Funcional.

Un componente tiene un **ciclo de vida**: se **monta** (aparece en pantalla, una sola vez), se **actualiza** (se re-renderiza, cada vez que cambia su estado, sus props, o el estado de un padre — muchas veces a lo largo de su vida) y se **desmonta** (desaparece, por ejemplo al navegar a otra ruta). `useEffect` recibe una función y, opcionalmente, un array de **dependencias**, que decide en cuáles de esas etapas corre el efecto:

<div class="card-grid card-grid-3">
<div class="info-card">
<h4>Sin array</h4>

Corre después de <strong>cada</strong> render (cada actualización).
</div>
<div class="info-card tone-yellow" style="background:var(--vp-c-yellow-soft);border-color:#fcd34d">
<h4><code>[]</code></h4>

Corre <strong>una sola vez</strong>, al montar. Nunca de nuevo.
</div>
<div class="info-card">
<h4><code>[a, b]</code></h4>

Corre al montar, y de nuevo en cada actualización donde <code>a</code> o <code>b</code> cambiaron.
</div>
</div>

### `useEffect`: un timer simple

```tsx
function Clock() {
  const [seconds, setSeconds] = useState(0)

  useEffect(() => {
    const id = setInterval(() => setSeconds((s) => s + 1), 1000)
    return () => clearInterval(id)   // limpieza: corre al desmontar
  }, [])

  return <p>Pasaron {seconds} segundos</p>
}
```

Con `[]`, el `setInterval` se crea **una sola vez**, al montar — sin el array, se crearía un timer nuevo en cada render, acumulándolos. La función que `useEffect` **devuelve** es la **limpieza**: React la corre al desmontar el componente (acá, cancelando el timer para no dejarlo corriendo de más), o justo antes de volver a ejecutar el mismo efecto si sus dependencias cambiaron. Es el gancho del ciclo de vida donde se cancela cualquier cosa que el efecto haya dejado pendiente — un timer, una suscripción, un pedido en curso.

### `useEffect` + `fetch`: conectando con Asincronismo

```tsx
function ProductList() {
  const [products, setProducts] = useState<Product[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    async function loadProducts() {
      const res = await fetch('/api/products')
      setProducts(await res.json())
      setLoading(false)
    }
    loadProducts()
  }, [])   // [] — solo al montar el componente

  if (loading) return <p>Cargando...</p>
  return <ul>{products.map((p) => <li key={p.name}>{p.name}</li>)}</ul>
}
```

El mismo `async`/`await` de Asincronismo, ahora disparado desde `useEffect` con dependencias `[]` — "buscá los productos una vez, apenas se monta el componente". El estado `loading` maneja el intermedio entre "todavía no llegó la respuesta" y "ya se puede mostrar algo" — un patrón que va a reaparecer todo el tiempo al conectar con una API real (Node + Express, más adelante en la unidad).

Una nota importante: `useEffect` no puede recibir directamente una función `async` (React espera que la función de efecto devuelva nada o una función de limpieza, no una Promise) — por eso el patrón habitual es declarar una función `async` **adentro** del efecto y llamarla enseguida, como en el ejemplo.

<div class="practice-box">
<p class="practice-label">Practicá</p>

Escribí un componente `UserGreeting` que use `useEffect` con `[]` para simular una carga (con un `setTimeout` de un segundo envuelto en una Promise, como en Asincronismo) que resuelva con un nombre de usuario. Mientras carga, mostrá `"Cargando..."`; cuando termine, mostrá `"Hola, {nombre}!"`.
</div>

## Más hooks de la librería estándar

`useState` y `useEffect` alcanzan para la gran mayoría de los componentes de este curso — son, con diferencia, los dos hooks más usados en cualquier proyecto real. El resto sirve para casos puntuales, buenos de conocer aunque no aparezcan en cada componente.

### `useContext`: estado global sin *prop drilling*

```tsx
const UserContext = createContext<string | null>(null)

function App() {
  const [user] = useState('Ada')
  return <UserContext.Provider value={user}><Toolbar /></UserContext.Provider>
}
function Toolbar() {
  return <UserGreeting />   // no recibe "user" como prop
}
function UserGreeting() {
  const user = useContext(UserContext)
  return <span>Hola, {user}</span>
}
```

Sin `useContext`, `user` tendría que pasarse como prop a través de `Toolbar`, aunque no lo use, solo para llegar a `UserGreeting` (***prop drilling***). Un `Context.Provider` publica un valor que cualquier descendiente lee directo con `useContext`, sin importar cuántos niveles de anidamiento haya en el medio.

### `useRef`: valores que sobreviven sin re-renderizar

```tsx
function SearchInput() {
  const inputRef = useRef<HTMLInputElement>(null)

  const focusInput = () => inputRef.current?.focus()

  return (
    <>
      <input ref={inputRef} type="text" />
      <button onClick={focusInput}>Enfocar</button>
    </>
  )
}
```

`useRef` guarda un valor mutable (`.current`) que persiste entre renders — a diferencia de `useState`, cambiarlo **no** dispara un nuevo render. Dos usos típicos: acceder directamente a un elemento del DOM (como `inputRef` arriba) o guardar un valor que necesita sobrevivir renders sin ser parte de lo que se muestra en pantalla (un id de `setTimeout`, un contador interno).

### `useMemo` y `useCallback`: cachear entre renders

```tsx
function ProductList({ products, query }: { products: Product[]; query: string }) {
  // useMemo: cachea un VALOR calculado, se recalcula solo si products/query cambian
  const filtered = useMemo(
    () => products.filter((p) => p.name.includes(query)),
    [products, query]
  )

  // useCallback: cachea una FUNCIÓN, se recrea solo si products cambia
  const handleAdd = useCallback(
    (name: string) => console.log('agregado:', name),
    [products]
  )

  return <ul>{filtered.map((p) => <li key={p.name}>{p.name}</li>)}</ul>
}
```

Los dos resuelven el mismo problema — evitar recalcular algo caro (o recrear una función) en **cada** render — para un valor (`useMemo`) o una función (`useCallback`). Son optimizaciones puntuales: no hace falta envolver todo con esto, solo cuando un cálculo real es costoso o una función se pasa a un componente hijo optimizado con `memo`.

### `React.memo`: evitar renders de más

```tsx
const ProductCard = memo(function ProductCard({ name, price }: Product) {
  console.log('renderizando', name)
  return <div>{name} — ${price}</div>
})

function ProductGrid({ products }: { products: Product[] }) {
  const [clicks, setClicks] = useState(0)
  return (
    <div>
      <button onClick={() => setClicks(clicks + 1)}>Clicks: {clicks}</button>
      {products.map((p) => <ProductCard key={p.name} {...p} />)}
    </div>
  )
}
```

`memo` compara las props por igualdad superficial — si no cambiaron, React reusa el render anterior sin volver a ejecutar el componente. Sin `memo`, cada click en el botón (que ni toca `products`) re-renderiza los `ProductCard` igual. Mismo criterio que `useMemo`/`useCallback`: no conviene memoizar todo sin necesidad real — cada comparación también tiene un costo.

### `useReducer`: estado complejo

```tsx
type Action = { type: 'add'; name: string } | { type: 'clear' }

function cartReducer(state: string[], action: Action): string[] {
  switch (action.type) {
    case 'add': return [...state, action.name]
    case 'clear': return []
  }
}

function Cart() {
  const [items, dispatch] = useReducer(cartReducer, [])
  const add = () => dispatch({ type: 'add', name: 'Mouse' })
  return <button onClick={add}>Agregar ({items.length})</button>
}
```

Alternativa a `useState` para **varias transiciones de estado relacionadas**: en vez de un `setState` distinto por cada acción posible, toda la lógica se centraliza en un `reducer`. `dispatch({ type: 'add', ... })` no cambia el estado directamente — le manda una `Action` al reducer, que calcula y devuelve el **estado nuevo completo** según el `type`. Es la misma función `(estado, acción) => nuevo estado` que usa `Array.reduce`, ahora manejando el estado de un componente.

### Tu propio hook: custom hooks

```tsx
function useFetch<T>(url: string) {
  const [data, setData] = useState<T | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch(url).then((res) => res.json()).then((json) => {
      setData(json)
      setLoading(false)
    })
  }, [url])

  return { data, loading }
}

// Uso, en cualquier componente:
const { data: products, loading } = useFetch<Product[]>('/api/products')
```

Un **custom hook** es una función propia que empieza con `use` y combina otros hooks por dentro — acá, `useFetch` empaqueta el patrón `useState` + `useEffect` de la sección de `fetch` para poder reusarlo en cualquier componente sin repetir la lógica. Es la misma idea de extraer una función reutilizable de siempre, aplicada a lógica con estado.

## Probar y correr un proyecto React

### Crear un proyecto con Vite

```bash
npm create vite@latest
# seleccionar: React, luego TypeScript
```

**Vite** es hoy la herramienta más usada para arrancar un proyecto de React desde cero — reemplazó a *Create React App* (CRA), que Meta discontinuó oficialmente. Genera un proyecto mínimo con las configuraciones necesarias (bundler, dev server con recarga instantánea) sin tener que armarlas a mano.

### Primer componente propio

```tsx
// src/App.tsx — se borran los imports y el CSS de ejemplo
function App() {
  return (
    <>
      <h1>Hola, Programación III</h1>
    </>
  )
}

export default App
```

```bash
npm install
npm run dev   # abre http://localhost:5173
```

El proyecto generado por Vite trae un `App.tsx` de ejemplo con un contador y los logos de Vite/React — se borra ese contenido y se arranca desde un componente propio, mínimo. `npm run dev` levanta el servidor de desarrollo con recarga en caliente: guardar el archivo actualiza el navegador sin perder el estado de la app.

### Scaffolding recomendado

```
src/
├── components/   # piezas de UI reutilizables (ProductCard, Header...)
├── routes/       # una página/vista por ruta (con React Router)
├── hooks/        # custom hooks propios (useFetch, useAuth...)
├── services/     # llamadas a APIs externas (con Axios)
├── constants/    # valores fijos compartidos
├── configs/      # configuración de librerías (axios, i18n...)
├── styles/       # CSS/estilos globales
├── utils/        # funciones auxiliares sin estado
├── App.tsx
└── main.tsx
```

Ninguna de estas carpetas la exige React — es una convención de organización que aparece una y otra vez en proyectos reales, a medida que crecen más allá de un puñado de componentes. Empezar un proyecto nuevo con esta estructura desde el día uno ahorra una reorganización dolorosa más adelante.

## React Router DOM

React, por sí solo, no sabe qué mostrar según la URL — hace falta una librería de ruteo, y `react-router-dom` es la más usada.

```bash
npm install react-router-dom
```

Expone tres piezas centrales: `<BrowserRouter>` habilita el ruteo basado en la URL del navegador, `<Routes>` agrupa las rutas posibles, y cada `<Route path="..." element={...}/>` mapea una URL puntual a un componente.

### Armar las rutas

```tsx
import { Routes, Route, BrowserRouter } from 'react-router-dom'
import Layout from './components/Layout'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<Home />} />
          <Route path="products" element={<Products />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}
```

Envolver a las demás rutas en `<Route element={<Layout/>}>` define un **layout compartido**, con `<Outlet />` marcando dónde va cada página.

### Layout compartido con `<Outlet />`

```tsx
import { NavLink, Outlet } from 'react-router-dom'

function Layout() {
  return (
    <div>
      <nav>
        <NavLink to="/">Inicio</NavLink>
        <NavLink to="/products">Productos</NavLink>
      </nav>
      <main>
        <Outlet />   {/* la ruta activa: Home o Products */}
      </main>
    </div>
  )
}

export default Layout
```

`NavLink` navega sin recargar la página y marca automáticamente el link activo. `<Outlet />` es el "hueco" donde React Router inserta el componente de la ruta hija que corresponda a la URL actual — así el `<nav>` y el resto del layout se escriben una sola vez, en vez de repetirlos en cada página.

### Parámetros de ruta: `useParams`

```tsx
<Route path="products/:id" element={<ProductDetail />} />
```

```tsx
import { useParams } from 'react-router-dom'

function ProductDetail() {
  const { id } = useParams()   // "42", si la URL es /products/42
  const [product, setProduct] = useState<Product | null>(null)

  useEffect(() => {
    fetch(`/api/products/${id}`).then((res) => res.json()).then(setProduct)
  }, [id])

  return product ? <h1>{product.name}</h1> : <p>Cargando...</p>
}
```

`:id` en la ruta es un **parámetro dinámico** — cualquier valor en esa posición de la URL. `useParams()` lo devuelve como string, listo para usar (acá, para pedirle ese producto puntual a la API). Como `id` es dependencia del efecto, cambiarlo (navegar de `/products/1` a `/products/2` sin desmontar el componente) vuelve a disparar el `fetch`.

### Query params: `useSearchParams`

```tsx
// URL: /products?category=electronics
import { useSearchParams } from 'react-router-dom'

function Products() {
  const [searchParams, setSearchParams] = useSearchParams()
  const category = searchParams.get('category')   // "electronics" o null

  return (
    <button onClick={() => setSearchParams({ category: 'books' })}>
      Ver libros
    </button>
  )
}
```

A diferencia de `:id`, los **query params** (`?clave=valor`) son opcionales y no cambian qué componente se renderiza — típicos para filtros, orden, paginado. `useSearchParams` funciona parecido a `useState`, y además actualiza la URL — así el estado del filtro sobrevive a un refresh de página, o se puede compartir como link.

### Rutas protegidas (autenticadas)

```tsx
import { Navigate, Outlet } from 'react-router-dom'
import { getToken } from '../services/auth'

function RequireAuth() {
  return getToken() ? <Outlet /> : <Navigate to="/login" replace />
}

// En las rutas:
<Route element={<RequireAuth />}>
  <Route path="products" element={<Products />} />
  <Route path="profile" element={<Profile />} />
</Route>
```

`RequireAuth` es un componente "guardián": no renderiza contenido propio, solo decide — si hay token, deja pasar (`<Outlet />`, la ruta hija real); si no, redirige a `/login` con `<Navigate />`. Cualquier ruta anidada adentro queda protegida, sin repetir esta lógica en cada una.

### Ruta 404: catch-all

```tsx
<Routes>
  <Route element={<Layout />}>
    <Route path="/" element={<Home />} />
    <Route path="products" element={<Products />} />
  </Route>
  <Route path="*" element={<NotFound />} />   {/* cualquier otra URL */}
</Routes>
```

`path="*"` funciona como comodín: si ninguna ruta anterior coincidió con la URL, React Router cae acá. Sin esta ruta, una URL inexistente muestra una pantalla en blanco en vez de un mensaje claro.

<div class="practice-box">
<p class="practice-label">Practicá</p>

Sobre un proyecto de Vite con `react-router-dom` instalado, armá tres rutas (`/`, `/products`, `/products/:id`) dentro de un `<Layout>` compartido con `<nav>` y `<Outlet />`. Agregá una ruta `*` con un componente `NotFound` simple, y confirmá navegando a una URL inexistente que aparece tu mensaje en vez de una pantalla en blanco.
</div>

## ¿Qué es un middleware?

- Un **middleware** es una función que se ubica en el medio de un flujo (una request, una navegación) y puede inspeccionar, modificar o **cortar** el paso antes de que siga — llamando (o no) a `next()`.
- `RequireAuth`, recién visto, es exactamente esa idea aplicada a rutas del lado del cliente: intercepta la navegación y decide si continúa o redirige.
- Del lado del servidor (Node + Express, más adelante en la unidad) el mismo concepto valida un token **antes** de que la request llegue a la lógica real de la ruta.

```tsx
// Cliente (React Router)
function RequireAuth() {
  return getToken()
    ? <Outlet />
    : <Navigate to="/login" />
}
```

```js
// Servidor (Express)
function requireAuth(req, res, next) {
  const token = req.headers.authorization
  if (!isValid(token)) {
    return res.status(401)
      .json({ error: 'No autorizado' })
  }
  next()   // token OK: sigue
}

app.get('/products', requireAuth, (req, res) => {
  res.json(products)
})
```

Mismo chequeo de permiso ("¿tiene permiso?"), resuelto en un solo lugar en vez de repetirlo en cada endpoint o cada pantalla. La diferencia es qué pasa si la respuesta es "no": del lado del cliente, se **redirige** a otra pantalla; del lado del servidor, se **corta la request** con un código de error, antes de que llegue a tocar la base de datos.

## Herramientas de calidad: Prettier + ESLint

### Prettier: formateo automático

Cuando varias personas tocan el mismo código, cada quien indenta y comenta a su manera — Prettier elimina esa fricción formateando todo automáticamente, según reglas configurables una sola vez.

```bash
npm install --save-dev --save-exact prettier
```

```json
// .prettierrc
{ "semi": false, "singleQuote": true, "trailingComma": "es5" }
```

```tsx
// antes
function greet(name){
return "Hola "+name}

// después de Prettier
function greet(name) {
  return 'Hola ' + name
}
```

No cambia **qué hace** el código, solo su forma. Se integra con el editor (formatea al guardar) y con `git` (un *pre-commit hook* que lo corre antes de cada commit) — para que el estilo se mantenga consistente sin que nadie tenga que acordarse de revisarlo.

### ESLint: errores antes de correr nada

Antes de ejecutar una sola línea, conviene detectar problemas reales del código — variables sin usar, un hook llamado condicionalmente, un import roto. Para eso existe ESLint, un analizador estático.

```bash
npm create vite@latest   # ya viene con un .eslintrc básico incluido
```

```tsx
// ESLint marca esto en rojo, antes de ejecutar una sola línea:
function Item({ show }: { show: boolean }) {
  if (show) {
    useState(0)          // ❌ hook llamado condicionalmente
  }
  const [x] = useState(1) // ❌ 'x' nunca se usa
  return <p>Item</p>
}
```

Un proyecto de Vite ya trae una configuración razonable por defecto; se puede extender con más reglas. La diferencia con Prettier: Prettier corrige **formato** (no cambia si el código funciona); ESLint señala **errores reales** — por eso se usan juntos, sin pisarse.

## Consumir APIs: Axios

`fetch` nativo alcanza para pedidos simples, pero un proyecto real necesita algo más cómodo para manejar headers, tokens y errores en cada request — ahí entra Axios, un cliente HTTP basado en Promises.

```bash
npm install axios
```

```tsx
// services/api.ts
import axios from 'axios'
const api = axios.create({ baseURL: 'http://localhost:4000/' })
export default api

// uso: GET a /products
const res = await api.get<Product[]>('/products')
console.log(res.data)   // ya viene parseado, sin un segundo await
```

`axios.create()` arma una instancia con una configuración base (URL, headers) reusada en cada pedido — se importa este `api` en vez de `axios` directamente en cada archivo. A diferencia de `fetch`, `res.data` llega ya parseado, sin un `.json()`/`await` adicional. Más adelante (sección de Autenticación) se le suman **interceptores** para incorporar el token automáticamente.

### Variables de entorno con Vite: `.env`

Cada ambiente (desarrollo, producción) necesita apuntar a una URL de API distinta, sin hardcodearla en el código ni subir secretos al repositorio — para eso existen las variables de entorno.

```bash
# .env.development
VITE_API_URL=http://localhost:4000/

# .env.production
VITE_API_URL=https://mi-api.com/

# .env.local — nunca se commitea (está en .gitignore)
VITE_API_URL=http://192.168.0.5:4000/   # ej: probar desde el celular
```

```tsx
const api = axios.create({ baseURL: import.meta.env.VITE_API_URL })
```

Un proyecto Vite las lee de forma **nativa** — no hace falta instalar `dotenv` (útil en un proyecto Node "pelado", redundante acá). Toda variable que llegue al navegador debe empezar con `VITE_`, una medida de seguridad para no exponer por accidente una variable del sistema que no era pública. `.env.local` tiene **prioridad** sobre los demás y nunca se sube al repositorio — ahí van valores propios de cada máquina (o secretos), sin pisarle la configuración a nadie más del equipo.

## Librerías de componentes visuales

### Por qué usar una

- Ahorra construir desde cero botones, inputs, modales, tablas — con estados de foco, hover, disabled y accesibilidad ya resueltos.
- Da **consistencia visual** de forma casi automática: todos los botones de la app se ven y se comportan igual, sin coordinarlo a mano.
- Se personaliza (colores, tipografía) mediante un sistema de *theming*, en vez de sobreescribir CSS componente por componente.

Nada de esto es gratis: agrega peso al bundle y un estilo visual reconocible.

### Las más usadas, con números

<div class="overflow-x-auto">

| Librería | Descargas npm/semana | Estilo |
|---|---|---|
| **MUI** | ~5.8M | Material Design de Google, muy completa |
| **Ant Design** | ~3.1M | Enterprise, pensada para dashboards y formularios densos |
| **Chakra UI** | ~1.4M | Minimalista, muy personalizable |
| **shadcn/ui** | ~150k (*) | Componentes que se copian al proyecto, no una dependencia tradicional |

</div>

(*) shadcn/ui no se instala como paquete, se copian los componentes fuente al proyecto — su descarga real no se refleja en npmtrends. MUI lidera en volumen — la opción "segura" por defecto. Ant Design es una recomendación puntual de este apunte: su set de componentes es muy completo para pantallas de datos (tablas, formularios, filtros), justo el tipo de UI que necesita el proyecto integrador — por eso es la que se usa en los siguientes ejemplos.

### Ejemplo con Ant Design

```bash
npm install antd
```

```tsx
import { Button, Table } from 'antd'

function ProductTable({ products }: { products: Product[] }) {
  const columns = [
    { title: 'Nombre', dataIndex: 'name' },
    { title: 'Precio', dataIndex: 'price' },
  ]
  return (
    <>
      <Table dataSource={products} columns={columns} rowKey="name" />
      <Button type="primary">Agregar producto</Button>
    </>
  )
}
```

`Table` resuelve de una sola vez ordenamiento, paginado y estilos consistentes — lo mismo que armar a mano tomaría bastante código propio. `Button type="primary"` ya viene con el estilo de la marca del proyecto (definido una sola vez, en el tema de Ant Design), sin escribir CSS propio.

### Ant Design: formularios con validación

```tsx
import { Form, Input, Button } from 'antd'

function ProductForm() {
  const onFinish = (v: { name: string; price: number }) =>
    console.log('producto válido:', v)

  return (
    <Form onFinish={onFinish} layout="vertical">
      <Form.Item name="name" label="Nombre" rules={[{ required: true }]}>
        <Input />
      </Form.Item>
      <Form.Item name="price" label="Precio" rules={[{ required: true, type: 'number' }]}>
        <Input type="number" />
      </Form.Item>
      <Button type="primary" htmlType="submit">Guardar</Button>
    </Form>
  )
}
```

Comparado con el input controlado a mano (sección de formularios): acá no hace falta un `useState` por campo — `Form` maneja el estado internamente, y `rules` declara las validaciones (requerido, tipo numérico...) sin escribir el `if` a mano. `onFinish` solo se ejecuta si **todo** pasó la validación.

### Ant Design: tema propio con `ConfigProvider`

```tsx
import { ConfigProvider } from 'antd'

function App() {
  return (
    <ConfigProvider theme={{ token: { colorPrimary: '#e11d48' } }}>
      <ProductTable products={products} />
    </ConfigProvider>
  )
}
```

`ConfigProvider` envuelve la app (o una parte) y redefine los `tokens` de diseño de la librería — acá, el color primario. Todo `Button type="primary"`, todo link, todo estado de foco que dependa de ese color cambia de una sola vez, en un solo lugar, en vez de sobreescribir CSS componente por componente.

<div class="practice-box">
<p class="practice-label">Practicá</p>

Sobre un catálogo de productos, armá una tabla con `antd` (`Table` + columnas de nombre y precio) y un `Form` con validación para agregar un producto nuevo (nombre requerido, precio requerido y numérico). Envolvé la app en un `ConfigProvider` con un `colorPrimary` propio.
</div>

## Autenticación

### Cómo funciona la autenticación con tokens

- Un **token** (normalmente un *JWT*, *JSON Web Token*) es una cadena que certifica "quién sos" sin reenviar la contraseña en cada pedido. Lo genera el **backend**, una sola vez, justo después de un login exitoso.
- Tiene fecha de expiración: pasado ese tiempo deja de ser válido y hay que loguearse de nuevo (o usar un *refresh token*, un mecanismo más avanzado para renovarlo sin pedir la contraseña otra vez).
- El frontend no lo genera ni lo valida — solo lo guarda y lo reenvía en cada pedido a una ruta protegida.

```
Cliente  --  usuario + contraseña  -->  Backend
Cliente  <--        token          --   Backend

Cliente  -- Authorization: Bearer <token> -->  Backend (cada request)
```

### Dónde guardar el token

<div class="overflow-x-auto">

| Método | Sobrevive un refresh | Riesgo principal |
|---|---|---|
| **Cookie `httpOnly`** | ✅ | Requiere que el backend la setee — JS del navegador no puede leerla, por diseño |
| **`localStorage`** | ✅ | Legible por cualquier script — vulnerable si hay una vulnerabilidad XSS |
| **`sessionStorage`** | ❌ (se borra al cerrar la pestaña) | Mismo riesgo que `localStorage`, ventana de exposición más corta |
| **Memoria (estado/Context)** | ❌ (se pierde al refrescar) | El más seguro contra XSS, pero necesita un refresh token para sostener la sesión |

</div>

No hay una respuesta única — es un balance entre seguridad y comodidad. La cookie `httpOnly` es la opción más recomendada hoy porque el propio navegador impide que JavaScript la lea, así que un ataque XSS no puede robarla directamente — pero exige que el backend coopere (fijarla en la respuesta, con los flags correctos). Para el proyecto integrador de este curso, `localStorage` es una opción razonable para empezar, dada su simplicidad.

### `localStorage`, en código

```ts
// services/auth.ts
const TOKEN_KEY = 'auth_token'

export function saveToken(token: string) {
  localStorage.setItem(TOKEN_KEY, token)
}

export function getToken(): string | null {
  return localStorage.getItem(TOKEN_KEY)
}

export function clearToken() {
  localStorage.removeItem(TOKEN_KEY)
}
```

`localStorage` es una API nativa del navegador — no hace falta ninguna librería para usarla.

### Axios: incorporar y leer el token

```tsx
import axios from 'axios'
import { getToken, clearToken } from './auth'

const api = axios.create({ baseURL: import.meta.env.VITE_API_URL })

api.interceptors.request.use((config) => {
  const token = getToken()
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

api.interceptors.response.use(
  (res) => res,
  (error) => {
    if (error.response?.status === 401) clearToken()
    return Promise.reject(error)
  }
)
```

El interceptor de **request** agrega el token con `getToken()` antes de que salga cada pedido, sin repetirlo en cada llamada; el de **response** detecta un `401` ("token vencido o inválido") y desloguea automáticamente.

<div class="practice-box">
<p class="practice-label">Practicá</p>

Escribí `services/auth.ts` con `saveToken`/`getToken`/`clearToken` sobre `localStorage`. Armá una instancia de Axios con un interceptor de request que agregue el header `Authorization` si hay token guardado, y probá (simulando la respuesta) que sin token la ruta protegida de tu API de prueba devuelve `401`.
</div>

## Testing de componentes

### React Testing Library: por qué

- Librería para testear componentes de React — hoy el estándar de facto, viene incluida por default en un proyecto creado con Vite + plantilla de testing.
- Su filosofía: testear el componente **como lo usa una persona real** (qué texto ve, qué botón puede clickear), no los detalles internos de implementación (qué hook usa, cuántas veces se renderizó).
- Un test que sobrevive a un refactor interno del componente, mientras la UI resultante no cambie, es una señal de que está bien escrito. Contraste: si un test se rompe porque se cambió `useState` por `useReducer` sin cambiar nada visible en pantalla, el test estaba mal enfocado desde el principio.

### Un test simple

```tsx
import { render, screen, fireEvent } from '@testing-library/react'
import { Counter } from './Counter'

test('incrementa el contador al hacer click', () => {
  render(<Counter />)

  const button = screen.getByRole('button', { name: '+' })
  fireEvent.click(button)

  expect(screen.getByText('1')).toBeInTheDocument()
})
```

`render` monta el componente en un DOM virtual de prueba. `screen.getByRole` busca el botón igual que lo encontraría alguien usando un lector de pantalla — por su rol y su texto, no por un `id` interno. `fireEvent.click` simula la interacción. El `expect` final verifica lo que **ve** la persona usuaria (el texto "1" en pantalla), no una variable interna del componente.

### Testear un input controlado

```tsx
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { SearchBox } from './SearchBox'

test('filtra al escribir en el buscador', async () => {
  const user = userEvent.setup()
  render(<SearchBox />)

  const input = screen.getByPlaceholderText('Buscar producto...')
  await user.type(input, 'mouse')

  expect(input).toHaveValue('mouse')
})
```

`userEvent` (en vez de `fireEvent`) simula la interacción **como la haría una persona real** — tecla por tecla, con los eventos intermedios que dispara un navegador de verdad, no solo el evento final. Es la API recomendada hoy para escribir tests nuevos; `fireEvent` sigue existiendo para casos puntuales que `userEvent` no cubre.

### Testear algo asíncrono

```tsx
import { render, screen } from '@testing-library/react'
import { ProductList } from './ProductList'

test('muestra los productos después de cargar', async () => {
  render(<ProductList />)

  expect(screen.getByText('Cargando...')).toBeInTheDocument()

  const item = await screen.findByText('Mouse')   // espera a que aparezca
  expect(item).toBeInTheDocument()
})
```

`ProductList` (la del `useEffect` + `fetch`) primero muestra "Cargando..." y después los productos — el test necesita **esperar** ese cambio. `findByText` es la versión asíncrona de `getByText`: reintenta hasta encontrar el elemento (o falla, pasado un timeout), en vez de fallar apenas se ejecuta, antes de que la respuesta llegue.

<div class="practice-box">
<p class="practice-label">Practicá</p>

Escribí un test para `ProductFilter` (la sección de formularios) que renderice el componente, escriba `"mouse"` en el input con `userEvent`, y confirme con `screen.getByText` que solo aparece el producto esperado en la lista filtrada.
</div>

## Cheat sheet

<div class="card-grid card-grid-2">
<div>

**Componentes, JSX y estado**

| Forma | Ejemplo |
|---|---|
| Componente | `function C({ x }: Props) { ... }` |
| Props tipados | `interface Props { x: string }` |
| Condicional / Lista | `{cond ? <A/> : <B/>}`, `{items.map(i => <li key={i.id}>)}` |
| Input controlado | `<input value={v} onChange={...}/>` |
| Estado | `const [s, setS] = useState(init)` |

</div>
<div>

**Hooks y herramientas**

| Hook / Tool | Para qué |
|---|---|
| `useEffect(fn, deps)` | Efectos: fetch, timers, suscripciones |
| `useContext`, `useRef` | Contexto global, referencias al DOM |
| `useMemo`/`useCallback`/`useReducer` | Cachear valor/función, estado complejo |
| `memo` | Evitar renders de más si las props no cambian |
| `useParams`, `useSearchParams` | Parámetros de ruta y query params |
| `RequireAuth` + `<Outlet/>` | Ruta protegida (patrón middleware) |
| Vite / Axios / Testing Library | Scaffolding, HTTP, testear componentes |

</div>
</div>

## Referencias y recursos

- [react.dev — Learn](https://react.dev/learn) — documentación oficial, ya orientada a hooks y componentes funcionales
- [react.dev — Keeping Components Pure](https://react.dev/learn/keeping-components-pure) — conecta directo con el eje funcional del curso
- [react.dev — Referencia de Hooks](https://react.dev/reference/react/hooks) — todos los hooks de la librería estándar
- [vite.dev](https://vite.dev/) — la herramienta recomendada hoy para arrancar un proyecto de React
- [reactrouter.com](https://reactrouter.com/) — documentación oficial de React Router
- [testing-library.com/react](https://testing-library.com/docs/react-testing-library/intro/) — React Testing Library
- [axios-http.com](https://axios-http.com/) — documentación de Axios
- [ant.design](https://ant.design/) y [mui.com](https://mui.com/) — las dos librerías de componentes visuales más usadas hoy
- [prettier.io](https://prettier.io/) y [eslint.org](https://eslint.org/) — formateo y análisis estático
- [2025.stateofjs.com](https://2025.stateofjs.com/en-US/libraries/front-end-frameworks/) — encuesta anual sobre el ecosistema JS
- [w3techs.com — JavaScript Library Usage](https://w3techs.com/technologies/overview/javascript_library) — medición directa de adopción sobre sitios reales

## Cierre

El objetivo de este tema es entender el modelo mental de React (UI como función del estado) y manejar con soltura componentes, props tipados, `useState` y `useEffect` — la base de cualquier interfaz interactiva. Alrededor de esa base se fue sumando todo lo que hace falta para un proyecto real: ruteo con páginas protegidas, herramientas de calidad, un cliente HTTP con autenticación, una librería de componentes visuales, y tests que verifican la app como la usaría una persona real. El resto de la unidad (Node + Express, MongoDB) construye el backend que un componente como `ProductList` va a terminar consumiendo con Axios, cerrando el circuito completo de una aplicación full-stack.
