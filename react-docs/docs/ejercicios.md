# React — Guía de ejercicios

A diferencia de otras guías de la unidad, acá **no hay ejercicios sueltos**: es la construcción incremental de una sola aplicación — un catálogo de productos — donde cada ejercicio agrega una pieza nueva sobre lo que ya se armó en el anterior, en el mismo proyecto. El orden sigue, paso a paso, la misma progresión vista en clase.

Esto **no es el proyecto integrador** de la materia (ese tiene su propia consigna y se trabaja aparte) — es una app chica, acotada, pensada solo para practicar todo lo visto en este módulo de forma conectada, no para entregar.

Un solo proyecto de Vite (`npm create vite@latest` → template `react-ts`) alcanza para toda la guía. El dominio es el mismo catálogo (`interface Product { name: string; price: number; stock: number }`) usado en TypeScript.

## 1. Preparar el proyecto

1. Crear el proyecto: `npm create vite@latest catalogo -- --template react-ts`.
2. Instalar dependencias y confirmar que levanta: `npm install && npm run dev` (`http://localhost:5173`).
3. Borrar el contenido de ejemplo de `App.tsx` (el contador, los logos) y dejar un `<h1>Catálogo</h1>` mínimo.
4. Crear las carpetas `src/components/`, `src/routes/`, `src/hooks/`, `src/services/` (todavía vacías) — se van a ir llenando a medida que avanza la guía.

## 2. Layout base

1. Crear `components/Header.tsx`: un componente sin props todavía, que muestre el título "Mi Catálogo".
2. Crear `components/Footer.tsx`: un componente estático con un texto de copyright.
3. Componer los dos dentro de `App.tsx`, con un `<main>` en el medio para el contenido que se va a ir agregando.

## 3. El catálogo, en su forma más simple

1. Declarar `interface Product { name: string; price: number; stock: number }` en `src/types.ts` (o donde prefieras) y un array `products: Product[]` con al menos cinco productos, como datos de ejemplo.
2. Crear `components/ProductCard.tsx` con `interface ProductCardProps { product: Product }` que muestre nombre y precio.
3. Crear `components/ProductList.tsx` que reciba `products: Product[]` y renderice un `ProductCard` por cada uno, con `map` y `key={p.name}`.
4. Usar `ProductList` dentro de `App`, pasándole el array de ejemplo.

## 4. Renderizado condicional: stock

1. Agregar `stock` al `interface Product` (si no lo tenías ya) y a los datos de ejemplo, con algún producto en `0`.
2. Crear `components/StockBadge.tsx` que reciba `stock: number` y muestre `"Sin stock"` o `"Disponible"` según corresponda.
3. Usar `StockBadge` dentro de cada `ProductCard`.

## 5. Filtrar por stock

1. En `ProductList`, agregar `useState<boolean>(false)` para un flag `onlyAvailable`.
2. Agregar un botón que alterne (*toggle*) ese estado.
3. Cuando `onlyAvailable` es `true`, filtrar los productos (con `filter`) para mostrar solo los que tienen `stock > 0`, antes de mapearlos.

## 6. Buscador controlado

1. Crear `components/SearchBox.tsx`: un `<input>` controlado, con `value`/`onChange` manejados por un `useState<string>('')` que recibe como prop la función para actualizar el estado del padre (o que declara su propio estado y lo expone con un callback `onSearch`, a elección).
2. Usarlo dentro de `ProductList`, combinando el texto buscado con el filtro de stock del ejercicio 5 en un único `filter` (`p.name.toLowerCase().includes(query.toLowerCase())`).
3. Mostrar la cantidad de resultados encontrados.

## 7. Carga simulada con `useEffect`

1. Escribir una función `fetchProducts(): Promise<Product[]>` en `services/products.ts` que simule una llamada a una API (un `setTimeout` de 1 segundo envuelto en una Promise, como en Asincronismo) y resuelva con el catálogo de ejemplo.
2. En `ProductList` (o en `App`, a elección), reemplazar el array estático por `useState<Product[]>([])` y `useState<boolean>(true)` para `loading`.
3. Dentro de un `useEffect` con dependencias `[]`, declarar una función `async` interna que llame a `fetchProducts`, guarde el resultado en el estado y ponga `loading` en `false`.
4. Mientras `loading` es `true`, mostrar `"Cargando..."` en vez del catálogo.

## 8. Tu propio hook: `useFetch`

1. Extraer la lógica del ejercicio 7 a un hook genérico `hooks/useFetch.ts`: `function useFetch<T>(fetcher: () => Promise<T>)`, que devuelva `{ data, loading }`.
2. Usarlo en `ProductList` como `const { data: products, loading } = useFetch(fetchProducts)`.
3. Confirmar que el catálogo se sigue viendo exactamente igual — el hook no cambia el comportamiento, solo reorganiza el código para poder reusarlo.

## 9. "Actualizado hace..."

1. Cerca del buscador, agregar un componente `components/LastUpdated.tsx` con `useState<number>(0)` para segundos transcurridos.
2. Con `useEffect` y `setInterval`, incrementar ese contador cada segundo — **no olvidar** la función de limpieza (`clearInterval`) que el efecto debe devolver, para que el timer se cancele si el componente se desmonta.
3. Mostrar `"Actualizado hace {segundos}s"` junto al catálogo.

## 10. Usuario global, sin *prop drilling*

1. Crear un `UserContext = createContext<string | null>(null)` en `context/UserContext.ts`.
2. En `App`, envolver todo en un `<UserContext.Provider value="Ada">` (por ahora, un nombre fijo — se reemplaza por un usuario real en el ejercicio 21).
3. En `Header`, leer el valor con `useContext(UserContext)` y mostrarlo (`"Hola, {user}"`), sin que `App` se lo pase como prop.

## 11. Foco automático en el buscador

1. En `SearchBox`, declarar `const inputRef = useRef<HTMLInputElement>(null)` y conectarlo al `<input>` con `ref={inputRef}`.
2. Con un `useEffect` con `[]`, llamar a `inputRef.current?.focus()` para que el cursor arranque ahí apenas se monta la pantalla.
3. Agregar un botón "Limpiar" que vacíe el estado del buscador y vuelva a enfocar el input con la misma ref.

## 12. Optimizar el filtrado

1. En el componente que hace el filtro combinado (ejercicio 6), envolver el cálculo de la lista filtrada en `useMemo`, con `products` y `query` (y el flag de stock) como dependencias.
2. Si `ProductCard` recibe alguna función como prop (por ejemplo, para el carrito del ejercicio 13 — se puede completar este paso después de ese), envolverla en `useCallback`.
3. Envolver `ProductCard` con `memo`, y confirmar con un `console.log` al principio del componente que **no** se re-renderiza cuando cambia algo que no le afecta (por ejemplo, el contador de "actualizado hace..." del ejercicio 9).

## 13. Carrito con `useReducer`

1. Declarar `type CartAction = { type: 'add'; product: Product } | { type: 'remove'; name: string } | { type: 'clear' }`.
2. Escribir `cartReducer(state: Product[], action: CartAction): Product[]` que maneje los tres casos.
3. En `App` (o en un `CartContext`, si querés combinarlo con el ejercicio 10), usar `useReducer(cartReducer, [])` y agregar un botón "Agregar al carrito" en cada `ProductCard` que haga `dispatch({ type: 'add', product })`.
4. Mostrar la cantidad de ítems del carrito en el `Header`.

## 14. Rutear la app

1. Instalar `react-router-dom`.
2. Crear `components/Layout.tsx` con un `<nav>` (usando `NavLink`, con links a `/` y `/products`) y un `<main>` con `<Outlet />`.
3. En `App` (o en un `main.tsx`/`AppRoutes.tsx` separado), armar `<BrowserRouter>` con `<Routes>`: una ruta raíz (`element={<Layout />}`) que agrupe `path="/"` (una `Home` simple, con un título de bienvenida) y `path="products"` (el catálogo armado en los ejercicios anteriores).
4. Confirmar que navegar entre "Inicio" y "Productos" no recarga la página, y que el `<nav>` no se repite ni se pierde.

## 15. Detalle de producto y filtro por categoría

1. Agregar `category: string` al `interface Product` y a los datos de ejemplo (con al menos dos categorías distintas).
2. Crear la ruta `products/:id` con un componente `ProductDetail` que use `useParams` para leer el `id` y busque (o "pida", si extendiste `fetchProducts` para aceptarlo) ese producto puntual.
3. En la ruta `/products`, agregar un filtro por categoría usando `useSearchParams` (un botón o `<select>` por categoría que actualice el query param `?category=...`).
4. Cada `ProductCard` debe linkear (`<Link to={`/products/${...}`}>` o `useNavigate`) a su propio detalle.

## 16. Ruta 404

1. Crear un componente `NotFound` simple, con un mensaje claro y un link de vuelta a `/`.
2. Agregar `<Route path="*" element={<NotFound />} />` al final de las rutas.
3. Confirmar navegando a una URL inventada (por ejemplo `/no-existe`) que aparece tu mensaje, no una pantalla en blanco.

## 17. Prettier + ESLint

1. Instalar Prettier (`npm install --save-dev --save-exact prettier`) y crear un `.prettierrc` propio (elegir `semi`, `singleQuote`, `trailingComma` a gusto).
2. Correr `npx prettier --write .` sobre todo el proyecto y revisar el diff — ¿qué cambió?
3. Revisar el `.eslintrc` que Vite ya generó al crear el proyecto (ejercicio 1) y agregarle una regla propia (por ejemplo, prohibir `console.log` con `"no-console": "warn"`).

## 18. Axios

1. Instalar `axios` y crear `services/api.ts` con `const api = axios.create({ baseURL: 'http://localhost:4000/' })`.
2. Reemplazar el `fetch` de `fetchProducts` (ejercicio 7) por `api.get<Product[]>('/products')`, ajustando el código para leer `res.data` en vez de `await res.json()`.
3. Confirmar que `useFetch` (ejercicio 8) sigue funcionando sin cambios — el hook no debería saber si por debajo hay `fetch` o Axios.

## 19. Variables de entorno

1. Crear `.env.development` con `VITE_API_URL=http://localhost:4000/`.
2. Cambiar `services/api.ts` para usar `baseURL: import.meta.env.VITE_API_URL` en vez del string hardcodeado.
3. Crear un `.env.local` (confirmar que Vite lo ignora en `.gitignore`) con una URL distinta, y verificar que **esa** es la que efectivamente se usa al correr `npm run dev` — `.env.local` tiene prioridad.

## 20. Ant Design: tabla, formulario y tema

1. Instalar `antd` y reemplazar `ProductList` (o crear una vista alternativa `/products-table`) por un `<Table>` de Ant Design, con columnas para nombre, precio y stock.
2. Agregar un `<Form>` de Ant Design (con `Form.Item` y `rules`) para cargar un producto nuevo — nombre y precio requeridos, precio numérico.
3. Envolver la app en un `ConfigProvider` con un `theme` propio (token `colorPrimary`, a elección) y confirmar que los botones `type="primary"` lo reflejan.

## 21. Login y rutas protegidas

1. Crear `services/auth.ts` con `saveToken`/`getToken`/`clearToken` sobre `localStorage` (como en el apunte).
2. Armar una pantalla `Login` simple (usuario/contraseña, sin validar contra un backend real — alcanza con simular un token fijo al enviar el formulario) que llame a `saveToken` y navegue a `/products`.
3. Agregar interceptors a la instancia de Axios del ejercicio 18: uno de **request** que agregue `Authorization: Bearer <token>` si hay token guardado, y uno de **response** que llame a `clearToken` ante un `401`.
4. Crear `RequireAuth` (como en el apunte) y proteger con él una ruta nueva `/profile` que muestre el nombre de usuario del `UserContext` (ejercicio 10) — reemplazá ahí el valor fijo `"Ada"` por el que quede guardado al loguearse.

## 22. Tests

1. Escribí un test simple sobre algún botón con contador propio del proyecto (el carrito del ejercicio 13, por ejemplo): renderizarlo, hacer click con `fireEvent`, y confirmar con `screen.getByText` que el contador se actualizó.
2. Escribí un test de `SearchBox` (ejercicio 6) usando `userEvent.setup()` y `user.type()`, confirmando con `toHaveValue` que el input refleja lo escrito.
3. Escribí un test asíncrono de `ProductList`: confirmar primero que aparece `"Cargando..."`, y después usar `await screen.findByText(...)` para esperar a que aparezca algún producto del catálogo simulado.

## 23. Checklist final

Compará tu proyecto contra esta lista — es, ítem por ítem, el objetivo que se planteó en las clases de "Manos a la obra":

- [ ] Un buscador (texto) y un filtro (stock o categoría) funcionando juntos.
- [ ] Una grilla de productos, cada uno como su propio componente.
- [ ] Al menos una ruta con parámetro dinámico (`/products/:id`) y una con query params.
- [ ] Una ruta protegida, que redirige a `/login` sin token.
- [ ] Al menos un componente de una librería visual (Ant Design) integrado.
- [ ] Al menos tres tests pasando (`npm run test`, o el comando que corresponda a tu configuración).

## Para pensar

- El `UserContext` del ejercicio 10 y el `AuthContext`/token del ejercicio 21 resuelven problemas parecidos ("¿quién es el usuario actual?"). ¿Los unificarías en un solo Context, o los dejarías separados? ¿Qué pasaría si `RequireAuth` necesitara leer el nombre de usuario además del token?
- `React.memo` (ejercicio 12) evita un re-render, pero agrega una comparación de props en cada render del padre. En una lista de 5 productos, ¿ese costo extra vale la pena? ¿Y en una de 5.000? ¿Cómo se podría medir la diferencia, en vez de asumirla?
- El interceptor de response (ejercicio 21) desloguea automáticamente ante un `401`. ¿Qué pasaría si el usuario estaba en `/profile` en ese momento — debería quedarse ahí mostrando un error, o redirigirse solo a `/login`? ¿Con qué pieza ya construida en esta guía resolverías eso?
- La guía completa evitó a propósito duplicar lógica: `useFetch` se reusa para todo el catálogo, `cartReducer` centraliza las transiciones del carrito, `api` es una única instancia de Axios. Elegí una de las tres y pensá qué tendrías que cambiar si mañana el backend real cambiara la forma de la respuesta (por ejemplo, productos paginados en vez de un array completo) — ¿cuántos archivos tocarías?
