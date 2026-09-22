# Autodescripción, realidad y distinción — crónica consolidada

**Estado:** propuesta doctrinal exploratoria, no canónica.  
**PR:** #12 — *Derive regime-local Exists-R under locally set-like connectivity*.  
**Versión consolidada:** 2026-09-22.

Este documento ya **no** intenta mantener simultáneamente todas las formulaciones producidas durante la exploración. Su función es doble:

1. conservar una **historia cronológica auditable** de cómo evolucionó la idea;
2. mantener una única sección de **estado actual normativo**, de modo que una tesis superada no pueda confundirse con una tesis vigente.

La versión acumulativa anterior se conserva íntegra en:

- [archivo pre-consolidación](archive/autodescripcion-realidad-distincion-pre-consolidacion-2026-09-22.md)

La revisión se controla en:

- [ledger de findings](autodescripcion-realidad-distincion-review-ledger.md)

La literatura relevante se mantiene en:

- [mapa de literatura y referencias](autodescripcion-realidad-distincion-references.md)

Las derivaciones técnicas detalladas se mantienen fuera del estado normativo en:

- [derivaciones técnicas de emergencia, cierre y proceso](work/autodescripcion-realidad-distincion-derivaciones-2026-09-22.md)

---

## 0. Convenciones de lectura

Cada etapa histórica usa uno de estos estados:

- **SURVIVES** — la idea sigue formando parte del estado actual.
- **OPEN** — la idea sigue en investigación y no puede usarse todavía como premisa cerrada.
- **SUPERSEDED** — la formulación fue útil históricamente, pero ya no debe leerse como vigente.
- **DEFERRED** — se conserva como línea de investigación, fuera del núcleo que debe resolverse primero.

Las etiquetas históricas [D], [A], [I], [H], [O], [C] se conservan solo cuando ayudan a localizar el origen de una idea. Ya no constituyen la taxonomía normativa del documento.

---

# I. Estado actual normativo

Esta es la única sección que debe usarse para responder “¿qué sostiene ahora la propuesta?”.

## 1. Objetivo conceptual — Exists-$R$ frente a No-$R$

La propuesta distingue ahora tres niveles que antes quedaban mezclados bajo el símbolo $R$.

### 1.1. Totalidad de régimen

Para un régimen ontológico $i$, llamamos:

$$
R_i
$$

a un dominio máximamente exhaustivo de ese régimen cuando:

$$
\operatorname{EClosed}_i(R_i)
$$

y:

$$
\forall X\in\mathfrak D_i^{\mathrm{proc}},
\quad
X\preceq_i R_i.
$$

$R_i$ no se identifica necesariamente con un conjunto universal, una sustancia, una suma mereológica o una última capa física. Es el **máximo ontológico interno** del régimen según el tipo procesual vigente.

### 1.2. Totalidad absoluta hipotética

Reservamos:

$$
R_{\mathrm{abs}}
$$

para una eventual totalidad global que dominase todos los regímenes.

La existencia de $R_{\mathrm{abs}}$ **no** forma parte del objetivo mínimo del programa actual.

### 1.3. Tesis objetivo

Definimos:

$$
\boxed{
\operatorname{ExistsR}
:=
\exists i\;\exists R_i
\left[
\operatorname{EClosed}_i(R_i)
\land
\forall X\in\mathfrak D_i^{\mathrm{proc}},
\;X\preceq_i R_i
\right].
}
$$

Y su negación:

$$
\boxed{
\operatorname{NoR}
:=
\neg\operatorname{ExistsR}.
}
$$

Por tanto, el objetivo fuerte actual es:

$$
\boxed{
\neg\operatorname{NoR}.
}
$$

No es necesario demostrar:

$$
\exists R_{\mathrm{abs}}.
$$

### 1.4. Alternativas compatibles con éxito

Las siguientes arquitecturas son compatibles con $\operatorname{ExistsR}$:

- **One-$R$:** un único régimen y un único máximo;
- **Indexed-$R$:** máximos exhaustivos indexados por régimen;
- **Many-$R$:** varios $R_i$ ontológicamente incomparables;
- **Cluster-$R$:** varios máximos o grupos de máximos relacionados bajo una estructura metaontológica adicional.

El programa fracasa respecto de su objetivo mínimo solo si vale No-$R$:

> ningún régimen admite una totalidad exhaustiva cerrada.

### 1.5. Consecuencia metodológica

La discusión sobre generalidad absoluta y $R_{\mathrm{abs}}$ sigue siendo filosóficamente relevante, pero ya no es condición previa para refutar No-$R$.

Basta demostrar $\operatorname{ExistsR}$ para **un solo régimen no vacío**.

**Estado:** Exists-$R$ = OPEN; $R_{\mathrm{abs}}$ = OPEN y opcional respecto del objetivo mínimo.

## 2. Consecuencias analíticas si $R$ existe

Si $R$ significa “todo lo real”, entonces:

$$
\operatorname{Real}(x) \Rightarrow x \preceq_{\mathrm{ont}} R.
$$

Y un supuesto “exterior real de $R$” contradice esa definición.

Estas afirmaciones son **analíticas/definicionales**, no resultados empíricos ni teoremas profundos.

Del mismo modo, si se define un operador $F$ que solo añade estructuras o posibilidades ya comprendidas en el alcance real de $R$, entonces:

$$
R = F(R)
$$

es un **corolario condicional de clausura**, no una prueba de existencia de $R$.

**Estado: SURVIVES, con retórica rebajada.**

## 3. Estado actual del programa emergentista

La propuesta ya dispone de una definición independiente y event-local de emergencia, un operador system-relative construido desde ella, pruebas de F1–F3 dentro de ese tipo y un punto fijo propio explícito.

Por tanto, REV-01, REV-02 y REV-04 están cerrados en sus criterios originales, mientras REV-03 permanece PARTIAL por alcance doctrinal.

El programa dispone ahora de un **teorema directo condicional de Exists-$R$**: PON + una firma semántica set-sized/finitaria + StructAdm construyen un máximo E-closed $R_i^*$ de cualquier régimen no vacío. Lo que todavía no está justificado es PON ni, por completo, la taxonomía $\Lambda_*$ que determina qué cuenta como mismo régimen.

Los bloqueadores activos relevantes pasan a ser:

- **REV-07:** justificación filosófica de la familia pre-régimen $\Lambda_*$ que individúa los regímenes;
- **REV-23:** PON — smallness por-token de la conectividad ontológica inmediata — como premisa de la ruta directa a Exists-$R$;
- **REV-20:** PSB/K1, ahora derivables de PON en la ruta directa;
- **REV-22:** aplicabilidad de Zorn, también resuelta condicionalmente por PON aunque la ruta directa no la necesita;
- **REV-15:** consecuencias metaontológicas discriminantes;

## 3.1. Resumen formal vigente

Las demostraciones, contraejemplos y modelos de trabajo que originaron este estado se han movido al [documento de derivaciones técnicas](work/autodescripcion-realidad-distincion-derivaciones-2026-09-22.md). Esta sección registra solo resultados vigentes.

| Finding | Estado | Resultado vigente |
|---|---|---|
| REV-01 | RESOLVED formal | Para un sistema fijo $M$, la relación de eventos emergentes induce $F_M$ como clausura reflexivo-transitiva; F1, F2 interna y F3 se derivan. Para la ruta de Zorn, F2 es redundante: F1 + F3 bastan para elevar cotas a puntos fijos. |
| REV-02 | RESOLVED tipado | La inhibición compara sistemas/operadores distintos, no entradas del mismo $F_M$. Una extensión conductualmente conservativa caracteriza cuándo un evento puede transportarse entre sistemas. |
| REV-03 | PARTIAL | Existe una definición de emergencia event-local, independiente de $R$, basada en macro-invariancia, testigo organizacional y capacidad dinámica habilitada. Sigue pendiente validar su alcance doctrinal en casos ricos. |
| REV-04 | RESOLVED mínimo | El toy de cuatro componentes produce un punto fijo propio explícito de $F_M$. Esto demuestra que el operador no es necesariamente «la unión de todo», pero no caracteriza todavía sistemas ricos. |
| REV-18 | RESOLVED tipado | Un dominio se toma como fragmento semántico positivo actual $X=(T_X,\Phi_X)$; incidencia es pertenencia al carrier semántico y `EClosed_i` es una propiedad del contenido, no de la serialización. No se reifica el dominio como entidad adicional. |
| REV-19 | RESOLVED tipado | El objeto primario queda fijado como fragmento procesual semántico $X=(T_X,\Phi_X)$; $\preceq_i^{\mathrm{proc}}$ es inclusión de contenido positivo actual. Admisibilidad ontológica se separa como $\operatorname{Adm}_i$ y queda en REV-18/20/09/07. |
| REV-20 | PARTIAL subordinado | Bajo StructAdm + COV, $K1_i\iff\mathrm{PSB}_i$; PON implica PSB. K1 deja de ser blocker independiente de la ruta directa. |
| REV-22 | PARTIAL subordinado | PON + firma set-sized/finitaria hace set-sized cada régimen y su poset de fragmentos, resolviendo condicionalmente la ruta A de Zorn. La ruta directa no necesita Zorn. |
| REV-09 | RESOLVED set-indexed | Con `Adm_i := StructAdm_i`, la unión de una cadena set-indexed de fragmentos positivos actuales sigue siendo well-formed y admisible; junto con el lema previo de preservación de `EClosed`, K2 queda demostrada dentro del alcance set-sized del teorema. La aplicabilidad class-sized queda en REV-22. |
| REV-10 | RESOLVED vigente | La ruta actual ya no usa la inferencia oculta de StageFactorization/presentabilidad criticada en H8. |
| REV-21 | RESOLVED formal | Los puntos fijos de $F_i$ son exactamente los subconjuntos forward-closed del grafo emergente; la degeneración al único punto fijo no vacío $\Sigma_i$ ocurre exactamente cuando el grafo es fuertemente conexo. |
| REV-23 | OPEN blocker | PON no está justificada: falta demostrar que cada token actual tiene set-many vecinos ontológicos inmediatos bajo $\bowtie$. PON es la premisa de smallness que hace constructible el régimen completo y, con ella, Exists-R. |

### Corrección histórica importante sobre F2

Durante la exploración se sostuvo temporalmente que sin F2 no podía elevarse una cota $U$ de una cadena de puntos fijos a una cota fija. Ese diagnóstico fue **erróneo** y queda marcado `SUPERSEDED` en el documento técnico.

Si:

$$
X\preceq U
$$

y F1 da:

$$
U\preceq F(U),
$$

entonces, por transitividad:

$$
X\preceq F(U).
$$

F2 no interviene. F3 garantiza después:

$$
F(F(U))=F(U).
$$

Por tanto, la monotonía interna de $F_M$ sigue siendo verdadera, pero **no es necesaria para ese paso de Zorn**.

### Alcance de los cierres formales

Los cierres de REV-01 y REV-04 son deliberadamente limitados:

- REV-01 demuestra propiedades formales de una clausura reflexivo-transitiva; esas propiedades valdrían para cualquier relación binaria del mismo tipo. El contenido específicamente emergentista reside en la definición y justificación de $\mathcal E_M$, todavía PARTIAL bajo REV-03.
- REV-04 demuestra la existencia de un punto fijo propio en un toy mínimo. No demuestra por sí solo que $F_M$ siga siendo discriminante en sistemas con redes densas o fuertemente conectadas de eventos emergentes. Esa cuestión se registra separadamente en el ledger.

### Blockers ontológicos actuales

Para la ruta directa, el cuello de botella ya no es K1/K2/K3: es justificar la identidad de régimen y su smallness local sin introducir una totalidad por definición:

1. **REV-07:** justificar filosóficamente $\Lambda_*$ como criterio de identidad de régimen;
2. **REV-23:** justificar PON —que cada token tenga set-many vecinos ontológicos inmediatos—.

REV-20 y REV-22 quedan como consecuencias/alternativas de esta smallness: PON implica PSB/K1 y además hace set-sized cada régimen y su poset de fragmentos.

---

## 3.2. Localidad ontológica de la emergencia

La propuesta adopta provisionalmente una separación fuerte entre **emergencia interna a una realidad ontológica concreta** y **metaontología de la pluralidad de realidades**.

Fijado un régimen ontológico $i$, la maquinaria emergentista se indexa:

$$
\mathcal E_i,
\qquad
\mathfrak D_i^{\mathrm{proc}},
\qquad
\preceq_i,
\qquad
\mathfrak K_i,
$$

y, cuando exista una representación system-relative apropiada:

$$
F_i.
$$

El teorema emergentista pregunta únicamente por la estructura interna de ese régimen:

$$
K1_i+K2_i+K3_i
\Rightarrow
\exists R_i\in\mathfrak K_i:
\forall X\in\mathfrak D_i^{\mathrm{proc}},
\quad
X\preceq_i R_i.
$$

### Objetivo fuerte real: refutar No-$R$

Para esta propuesta no es necesario demostrar un único $R_{\mathrm{abs}}$.

Definimos el rival fuerte:

$$
\operatorname{NoR}
:=
\neg\exists i\;\exists R_i\in\mathfrak D_i^{\mathrm{proc}}
\left[
\operatorname{EClosed}_i(R_i)
\land
\forall X\in\mathfrak D_i^{\mathrm{proc}},
\;X\preceq_i R_i
\right].
$$

Así, basta encontrar **un solo régimen no vacío** $i$ para el que se justifiquen las premisas del teorema:

$$
K1_i+K2_i+K3_i
$$

y sus condiciones fundacionales/tipadas, para obtener:

$$
\boxed{
\exists R_i
\Rightarrow
\neg\operatorname{NoR}.
}
$$

Que además exista un único régimen, múltiples regímenes, Cluster-$R$, Indexed-One-$R$ o alguna estructura metaontológica ulterior es una cuestión separada. Ninguna de esas alternativas restaura No-$R$ una vez que existe al menos un $R_i$ exhaustivo en su régimen.

### Qué significa aquí «cerrado»

La conclusión inmediata del teorema actual es:

$$
\boxed{
\operatorname{EClosed}_i(R_i)
}
$$

porque $R_i\in\mathfrak K_i$.

No debe escribirse todavía, sin una precisión adicional de tipos:

$$
R_i=F_i(R_i).
$$

Esa igualdad solo estará justificada si se construye un operador sobre **el mismo tipo de dominios procesuales**:

$$
F_i^{\mathrm{proc}}:
\mathfrak D_i^{\mathrm{proc}}
\to
\mathfrak D_i^{\mathrm{proc}}
$$

con:

$$
\operatorname{Fix}(F_i^{\mathrm{proc}})
=
\mathfrak K_i.
$$

En ese caso sí:

$$
R_i\in\mathfrak K_i
\Rightarrow
F_i^{\mathrm{proc}}(R_i)=R_i.
$$

Hasta entonces, la forma tipada y sustantiva de la tesis es «$R_i$ existe y es E-closed», no una igualdad entre objetos de tipos distintos.


Por tanto:

$$
\boxed{
R_i
=
\text{máximo ontológico interno del régimen }i
}
$$

no:

$$
\boxed{
R_i
=
\text{máximo de todas las realidades ontológicas}.
}
$$

### Emergencia local no implica monismo global

Si existen dos regímenes $i\neq j$, puede ocurrir:

$$
R_i\parallel R_j
$$

sin que falle ninguna de las teorías internas:

$$
\mathcal E_i
\qquad\text{y}\qquad
\mathcal E_j.
$$

Así:

$$
\boxed{
\text{emergencia local}
\not\Rightarrow
\text{One-R global}.
}
$$

La posibilidad de Strong Many-R queda, por tanto, **desacoplada** del teorema de emergencia.

### K3 queda estrictamente indexada

La condición de amalgamación se interpreta desde ahora como:

$$
K3_i:
\forall X,Y\in\mathfrak D_i^{\mathrm{proc}}\;
\exists Z\in\mathfrak D_i^{\mathrm{proc}}:
X\preceq_i Z
\land
Y\preceq_i Z.
$$

K3_i excluye incomparabilidad fuerte **dentro de $i$**, pero no entre $i$ y $j$.

No se permite inferir:

$$
K3_i\;\forall i
\Rightarrow
K3_{\mathrm{abs}}.
$$

Ni tampoco:

$$
\forall i\,\exists R_i
\Rightarrow
\exists R_{\mathrm{abs}}.
$$

El problema One-R/Many-R queda como problema metaontológico independiente.

### Meta-notación sin colector ontológico

Puede usarse informalmente:

$$
\mathscr R=\{R_i\}_{i\in I}
$$

solo como **metanotación** para hablar de varios regímenes. Esta escritura no afirma que exista un objeto ontológico $\mathscr R$, un conjunto universal de realidades ni una realidad superior que contenga a todas.

En particular:

$$
\boxed{
\text{hablar pluralmente de }R_i
\not\Rightarrow
\exists R_{\mathrm{abs}}.
}
$$

### Exhaustividad interna y verdad absoluta

Se abandona la identificación histórica:

$$
\operatorname{VA}(o)=R_i.
$$

Se distinguen:

$$
\operatorname{Truth}_i
$$

como verdad/exhaustividad relativa a todo lo que constituye el régimen $i$, de una hipotética:

$$
\operatorname{Truth}_{\mathrm{abs}},
$$

cuya existencia y coherencia permanecen abiertas.

Por tanto:

$$
\boxed{
\text{exhaustividad interna}
\neq
\text{absolutidad global}.
}
$$

Esto neutraliza la antigua solución verbal de llamar «Verdad Absoluta indexada» a un máximo relativo.

### Consecuencia metodológica

REV-18, REV-19, REV-20 y REV-09 deben resolverse **por régimen $i$**. Ninguna de sus soluciones necesita primero resolver One-R/Many-R.

REV-07 queda reducido a una obligación más precisa: justificar independientemente qué hace que dos dominios pertenezcan al mismo régimen $i$ y por qué ese régimen satisface K3_i, sin definir «mismo régimen» como «amalgamable».

---

## 3.3. Admisibilidad estructural mínima

El predicado abstracto $\operatorname{Adm}_i$ se concreta normativamente como **well-formedness de contenido ontológico positivo actual**.

Un dominio procesual:

$$
X=(T_X,\Phi_X)
$$

es admisible cuando:

1. todos sus tokens pertenecen al mismo régimen $i$;
2. todos los tokens y hechos incluidos son actuales;
3. todo hecho incluye en $T_X$ sus relata;
4. todo evento incluye source y target únicos;
5. la precedencia/dependencia incluida es acíclica/coherente;
6. el fragmento contiene solo contenido positivo: una extensión puede añadir hechos sin retractar los anteriores.

Es decir:

$$
\boxed{
\operatorname{Adm}_i(X)
:=
\operatorname{StructAdm}_i(X).
}
$$

Esta elección tiene una lectura ontológica deliberadamente austera:

> un dominio no es una entidad adicional dentro de la realidad; es un **fragmento semántico de alcance ontológico actual**.

Por tanto, un máximo $R_i$ del poset de dominios no introduce una sustancia, conjunto universal o colector físico adicional: representa el alcance exhaustivo del contenido actual del régimen dentro del tipo formal elegido.

### Consecuencias demostradas

Con esta definición:

- **incidencia:** $q\trianglelefteq_i X$ significa exactamente $q\in T_X$; esto cierra REV-18 en su problema de tipos;
- **extensión por evento:** añadir el footprint de un evento emergente actual preserva StructAdm, por lo que OEA se deriva;
- **extensión por enlace:** añadir el footprint de una relación actual de $\Lambda_*$ preserva StructAdm, por lo que la EEA relevante se deriva;
- **unión binaria:** la unión de dos fragmentos del mismo régimen sigue siendo StructAdm; por tanto K3$_i$ se deriva directamente una vez fijada la identidad del régimen;
- **uniones de cadenas set-indexed:** preservan StructAdm; combinadas con la preservación formal de EClosed, demuestran K2$_i$ en el alcance set-sized.

La razón de coherencia es que solo se acumulan hechos positivos **actuales**. Un conflicto funcional o un ciclo finito de precedencia no puede aparecer por unir hechos que son conjuntamente verdaderos en el mismo régimen; si apareciese, la propia semántica de actualidad/proceso sería inconsistente.

### Cobertura

Para todo token o hecho actual de aridad finita del régimen existe un footprint well-formed set-sized que lo contiene. Por tanto:

$$
\mathrm{COV}_i:
\quad
\forall q\text{ actual en }i
\;\exists X\in\mathfrak D_i^{\mathrm{proc}}:
q\trianglelefteq_i X.
$$

Si $R_i$ domina todos los dominios admisibles, COV$_i$ implica que $R_i$ contiene todo contenido actual del régimen representable por la firma procesual.

### Precio conceptual

Este paso adopta como tesis metodológica que **todo fragmento positivo actual y well-formed cuenta como dominio legítimo** para el teorema. Si en el futuro se exige una noción más fuerte de dominio —por ejemplo cierre causal o nomológico previo— REV-18/REV-09 deberán reabrirse.

---

## 3.4. Construcción de K1 y smallness local

Con StructAdm, la cofinalidad K1 ya no necesita asumirse globalmente.

Definimos:

$$
\operatorname{Pend}_i(X)
$$

como las obligaciones emergentes actuales cuyo source ya está en $X$ pero cuyo evento/target/footprint todavía no está completamente incorporado.

Una ronda satisface todas las obligaciones pendientes de un dominio; las nuevas obligaciones activadas se procesan en la ronda siguiente.

Como la emergencia se propaga por caminos finitos, la unión de las rondas:

$$
X_0
\preceq_i
X_1
\preceq_i
\cdots
\preceq_i
X_\omega
$$

es E-closed siempre que cada ronda maneje un conjunto de obligaciones.

### PSB — Pointwise Set-like Branching

La condición suficiente más local es:

$$
\mathrm{PSB}_i:
\quad
\forall s,
\;
\operatorname{Out}_i(s)
=
\{e\mid \operatorname{Emergent}_i(e)\land\operatorname{src}(e)=s\}
\text{ es set-sized}.
$$

Para cualquier conjunto de sources $S$, Replacement + Union dan:

$$
\bigcup_{s\in S}\operatorname{Out}_i(s)
$$

como conjunto. Por tanto PSB implica que cada ronda y todo cono de alcanzabilidad emergente finita generado desde un dominio set-sized permanecen set-sized.

Con StructAdm, las extensiones de un evento y las uniones set-indexed preservan admisibilidad. Así:

$$
\boxed{
\operatorname{StructAdm}_i
+
\mathrm{PSB}_i
\Rightarrow
K1_i.
}
$$

El documento técnico contiene la construcción completa por rondas.

### Estado de REV-20

REV-20 permanece **PARTIAL** y queda reducido a una única cuestión estructural.

Con StructAdm, COV y dominios set-sized se demuestra además la conversa:

$$
K1_i
\Rightarrow
\mathrm{PSB}_i,
$$

porque una extensión E-closed de un fragmento que contiene $s$ debe contener todos los eventos emergentes actuales salientes de $s$, y su carrier es un conjunto.

Por tanto:

$$
\boxed{
K1_i
\iff
\mathrm{PSB}_i.
}
$$

La pregunta restante es exactamente:

> ¿puede un único estado actual ser source de proper-class many eventos emergentes actuales?

El potencialismo ordinario de «siempre hay una extensión más» no basta para negar K1; dentro de esta arquitectura, debe aparecer una ramificación propia-clase local.

PSB es independiente de REV-22: resuelve la smallness **local del cierre de cada dominio**, mientras REV-22 pregunta por la smallness/aplicabilidad global de Zorn sobre la colección de dominios.

## 4. Núcleo matemático — ruta directa a Exists-$R$ y ruta Zorn

### 4.0. Teorema directo de totalidad de régimen

La ruta principal ya no necesita Zorn.

Definimos el vecindario ontológico inmediato:

$$
N(q)
:=
\{r\mid q\bowtie r\}.
$$

y la condición:

$$
\mathrm{PON}:
\quad
\forall q,
\;
N(q)\text{ es set-sized}.
$$

PON afirma que ningún token actual tiene proper-class many vecinos ontológicos inmediatos bajo las relaciones que constituyen co-régimen.

Como:

$$
q\sim r
$$

significa que existe un camino **finito** de $\bowtie$ entre ambos, PON implica que la clase de equivalencia:

$$
T_i
:=
[q]_{\sim}
$$

es set-sized. Se prueba construyendo los niveles finitos de vecindad y tomando su unión sobre $\omega$.

Fijada además una firma semántica procesual $\mathcal L_i$ set-sized y de aridad finita, la colección de todos los átomos posibles sobre $T_i$ es un conjunto. Por Separation, también lo es la colección de todos los hechos **actualmente verdaderos** del régimen:

$$
\Phi_i^{\mathrm{all}}.
$$

Definimos entonces:

$$
\boxed{
R_i^*
:=
(T_i,\Phi_i^{\mathrm{all}}).
}
$$

Por StructAdm, $R_i^*$ es un dominio admisible.

Para cualquier:

$$
X=(T_X,\Phi_X)
\in
\mathfrak D_i^{\mathrm{proc}},
$$

se tiene:

$$
T_X\subseteq T_i
$$

y:

$$
\Phi_X\subseteq\Phi_i^{\mathrm{all}}.
$$

Por tanto:

$$
\boxed{
\forall X\in\mathfrak D_i^{\mathrm{proc}},
\quad
X\preceq_i R_i^*.
}
$$

Además, si un evento emergente actual tiene source en $T_i$, sus relaciones source/event/target son enlaces procesuales actuales; evento y target pertenecen a la misma clase $[q]_{\sim}$ y sus hechos están en $\Phi_i^{\mathrm{all}}$. Luego:

$$
\boxed{
\operatorname{EClosed}_i(R_i^*).
}
$$

Así:

$$
\boxed{
\mathrm{PON}
+
\text{firma set-sized/finitaria}
+
\operatorname{StructAdm}
\Rightarrow
\operatorname{ExistsR}.
}
$$

y por tanto:

$$
\boxed{
\neg\operatorname{NoR}.
}
$$

#### No circularidad

El argumento no presupone un objeto $R_i$. Parte de un token $q$, demuestra que su componente de conectividad finita es un conjunto y, solo entonces, forma mediante Separation el conjunto de hechos actuales sobre ese carrier. El máximo se **construye** como contenido semántico; no se introduce por definición como entidad ontológica adicional.

#### Papel de la emergencia

En esta ruta, la emergencia **no produce la existencia** del máximo. La existencia se sigue de la conectividad ontológica localmente set-like. La emergencia aporta la propiedad adicional:

$$
\operatorname{EClosed}_i(R_i^*).
$$

Por tanto, debe evitarse la afirmación fuerte «la emergencia demuestra que existe R» salvo que se precise esta dependencia.

#### Relación con Zorn

K1/K2/K3 y Zorn permanecen como una segunda ruta estructural y como análisis de qué propiedades de los dominios bastan para maximalidad. Pero, bajo PON, ya no son necesarios para demostrar Exists-$R$.

---
**Convención normativa:** durante toda esta sección se fija un régimen ontológico $i$. Para aligerar notación se escribe:

$$
\mathfrak D:=\mathfrak D_i^{\mathrm{proc}},
\qquad
\mathfrak K:=\mathfrak K_i,
\qquad
\preceq:=\preceq_i.
$$

Toda cuantificación de K1–K3 y todo máximo obtenido en esta sección son **internos a $i$**. El resultado se denota $R_i$; no se infiere la existencia de $R_{\mathrm{abs}}$.

Las secciones anteriores producen dos niveles distintos que no deben confundirse:

1. **nivel system-relative:** para un sistema fijo que representa el régimen $i$, la emergencia independiente $\mathcal E_i$ induce un operador concreto $F_i$ sobre su espacio de configuraciones, y F1–F3 se derivan;
2. **nivel ontológico local:** el teorema habla de dominios $(\mathfrak D_i^{\mathrm{proc}},\preceq_i)$, para los que REV-18 todavía exige justificar el puente semántico.

La forma operator-free del argumento permite ver exactamente qué parte de la estructura de $F_i$ es necesaria.

### 4.1. Forma operator-free

Sea:

$$
(\mathfrak D,\preceq)
$$

un poset **set-sized** no vacío y sea:

$$
\mathfrak K\subseteq\mathfrak D
$$

una familia de dominios que llamaremos **cerrados**.

Supongamos:

**K1 — cofinalidad**

$$
\forall X\in\mathfrak D\;
\exists Y\in\mathfrak K:
X\preceq Y.
$$

**K2 — inductividad de los cerrados**

Para toda cadena $\mathcal C\subseteq\mathfrak K$ existe $U\in\mathfrak K$ tal que:

$$
\forall X\in\mathcal C,\quad X\preceq U.
$$

**K3 — directedness/amalgamación**

$$
\forall X,Y\in\mathfrak D\;
\exists Z\in\mathfrak D:
X\preceq Z
\land
Y\preceq Z.
$$

**Alcance de K3.** En esta sección K3 significa siempre $K3_i$. Es una condición fuerte sobre la unidad interna del régimen $i$, pero **no** una premisa sobre todas las realidades.

Dentro de $i$:

$$
X\parallel_i Y
\Rightarrow
\neg K3_i.
$$

Por eso REV-07 no desaparece: todavía hay que justificar independientemente qué determina la pertenencia a un mismo $i$ y por qué sus dominios son jointly embeddable.

Lo que queda prohibido es usar K3_i para concluir One-R global:

$$
\boxed{
K3_i
\not\Rightarrow
K3_{\mathrm{abs}}.
}
$$

El teorema obtiene un máximo interno $R_i$. La cuestión de si distintos $R_i$ tienen una extensión común pertenece exclusivamente a la metaontología One-R/Many-R.

### 4.2. Teorema de máximo cerrado cofinal

**Teorema.** Bajo K1–K3 existe:

$$
R\in\mathfrak K
$$

tal que:

$$
\boxed{
\forall X\in\mathfrak D,\quad X\preceq R.
}
$$

**Demostración.**

K1 y la no-vacuidad de $\mathfrak D$ implican $\mathfrak K\neq\varnothing$.

Por K2, toda cadena en $\mathfrak K$ tiene una cota superior en $\mathfrak K$. Por Zorn existe un $R\in\mathfrak K$ maximal.

Sea $X\in\mathfrak D$. Por K3 existe $Y\in\mathfrak D$ con:

$$
R\preceq Y
\land
X\preceq Y.
$$

Por K1 existe $Z\in\mathfrak K$ con:

$$
Y\preceq Z.
$$

Luego $R\preceq Z$. Como ambos pertenecen a $\mathfrak K$ y $R$ es maximal:

$$
Z=R.
$$

Por tanto:

$$
X\preceq Y\preceq R.
$$

Como $X$ era arbitrario, $R$ es un **máximo de todo $\mathfrak D_i^{\mathrm{proc}}$**. Normativamente se identifica este resultado como $R_i$; no como un máximo de otros regímenes. $\square$

### 4.3. Cobertura de lo real

Si además:

$$
\operatorname{Real}(x)
\Rightarrow
\exists X\in\mathfrak D:
x\preceq X,
$$

entonces:

$$
\operatorname{Real}(x)
\Rightarrow
x\preceq R.
$$

La inferencia es simplemente:

$$
x\preceq X\preceq R.
$$

### 4.4. Cómo se recupera esta forma desde un operador

Sea ahora:

$$
F:\mathfrak D\to\mathfrak D
$$

con solo:

$$
\text{F1: }X\preceq F(X),
$$

y:

$$
\text{F3: }F(F(X))=F(X).
$$

Definamos:

$$
\mathfrak K:=\operatorname{Fix}(F).
$$

Entonces F1 + F3 implican automáticamente K1:

para cualquier $X\in\mathfrak D$,

$$
X\preceq F(X)
$$

y:

$$
F(F(X))=F(X),
$$

por lo que:

$$
F(X)\in\mathfrak K.
$$

Además, si una cadena $\mathcal C\subseteq\operatorname{Fix}(F)$ tiene una cota $U\in\mathfrak D$, F1 da:

$$
U\preceq F(U).
$$

Así, para cada $X\in\mathcal C$:

$$
X\preceq U\preceq F(U).
$$

Y F3 da:

$$
F(U)\in\operatorname{Fix}(F).
$$

Por tanto la cota fija se obtiene con:

$$
\boxed{F1+F3,}
$$

sin usar F2.

Esta es la corrección exacta al argumento archivado: **la monotonía F2 era redundante para la ruta de Zorn**.

### 4.5. Papel de $F_M$

El operador system-relative construido en REV-01:

$$
F_M:\mathcal P(\Sigma_M)\to\mathcal P(\Sigma_M)
$$

sigue siendo útil y no queda superseded.

Para $F_M$:

- F1 se deriva por reflexividad;
- F2 interna se deriva por inclusión de conjuntos bajo un mismo sistema $M$;
- F3 se deriva por transitividad del cierre emergente.

El contraejemplo del inhibidor de REV-02 compara:

$$
F_M
\quad\text{con}\quad
F_N,
$$

no dos entradas del mismo operador. Por tanto no refuta la monotonía interna de $F_M$.

La extensión conductualmente conservativa de REV-02 sigue siendo útil para saber cuándo un evento puede transportarse entre sistemas, pero:

$$
\boxed{
\hookrightarrow_{\mathrm{cons}}
\text{ no es el orden ontológico } \preceq_{\mathrm{ont}}.
}
$$

Una incorporación real puede cambiar capacidades previas sin dejar de ser ontológicamente real.

### 4.6. Qué queda demostrado y qué no

**Demostrado matemáticamente:**

1. F2 no es necesaria para el teorema abstracto de maximalidad/exhaustividad;
2. F1 + F3 convierten cotas arbitrarias de cadenas de puntos fijos en cotas fijas;
3. la forma operator-free K1–K3 basta para obtener un máximo de $\mathfrak D$;
4. el $F_M$ concreto de REV-01 satisface F1–F3 dentro de su propio tipo.

**No demostrado ontológicamente:**

1. que un dominio ontológico $X\in\mathfrak D$ sea representable por un subconjunto de $\Sigma_M$;
2. que $\subseteq$ represente $\preceq_{\mathrm{ont}}$;
3. que la noción de cierre inducida por $F_M$ produzca una familia $\mathfrak K$ ontológicamente cofinal;
4. que las cadenas ontológicas relevantes tengan las cotas requeridas;
5. que K3/directedness sea legítima independientemente de “mismo índice”.

Estas cargas quedan trazadas así:

- **REV-18:** significado ontológico de $\operatorname{EClosed}$;
- **REV-19:** elección del tipo temporal del dominio;
- **REV-20:** K1/cofinalidad de dominios E-closed;
- **REV-09/REV-10:** K2/inductividad y sus supuestos de compactitud/presentabilidad;
- **REV-07:** K3/directedness no circular.

### 4.7. Relación con teoría estándar de puntos fijos

El teorema clásico de Tarski afirma que los puntos fijos de una función monótona sobre un retículo completo forman un retículo completo. Los closure operators estándar son extensivos, monótonos e idempotentes.

Nuestra observación es más modesta: **para esta ruta concreta de Zorn, una vez que existe un operador extensivo e idempotente y las cadenas de puntos fijos tienen cotas en el poset ambiente, la monotonía no es necesaria para levantar esas cotas a puntos fijos**.

La versión operator-free de K1–K3 hace transparente esa dependencia.

### 4.8.1. Aplicabilidad fundacional al régimen real

La restricción set-sized de Zorn pertenece al teorema abstracto. Para aplicarlo a un régimen ontológico real hay tres rutas posibles.

**Ruta A — smallness directa**

$$
\mathfrak D_i^{\mathrm{proc}}
\text{ es set-sized}.
$$

**Ruta B — esqueleto cofinal set-sized**

Existe:

$$
\mathfrak C_i
\subseteq
\mathfrak D_i^{\mathrm{proc}}
$$

set-sized y cofinal:

$$
\forall X\in\mathfrak D_i^{\mathrm{proc}}
\;\exists Y\in\mathfrak C_i:
X\preceq_i Y.
$$

Si dentro de $\mathfrak C_i$ se preservan cofinalidad cerrada, cotas de cadenas cerradas y directedness, Zorn produce un máximo de $\mathfrak C_i$ que, por cofinalidad, domina también todo $\mathfrak D_i^{\mathrm{proc}}$.

Por tanto:

$$
\boxed{
\text{esqueleto cofinal set-sized}
\Rightarrow
\text{Zorn puede producir un }R_i
\text{ máximo del régimen}.
}
$$

La demostración completa está en el documento técnico.

**Ruta C — teoría de clases**

Especificar explícitamente una teoría de clases y un principio de maximalidad suficientemente fuerte. Esta ruta no se presupone.

La aplicabilidad fundacional se registra como REV-22. No puede cerrarse suponiendo smallness a partir de la existencia del propio $R_i$.

### 4.8. Estado normativo

- **REV-01:** RESOLVED en su ataque original. F1–F3 se derivan para $F_M$, y F2 resulta además redundante para el teorema abstracto.
- **REV-02:** RESOLVED en el sentido tipado correcto: la inhibición muestra no-monotonía entre sistemas/operadores, no dentro de un único $F_M$.
- **REV-04:** RESOLVED mediante el punto fijo propio explícito del toy.
- **REV-18:** OPEN y ahora es el blocker principal del enlace entre la teoría de emergencia y la ontología global.

---

## 5. Identidad independiente de régimen — REV-07

La identidad de una realidad ontológica ya no se define por K3 ni por existencia de una cota común.

### 5.1. Familia pre-régimen de enlaces ontológicos

Antes de conocer cualquier régimen $i$, se fija una familia candidata de tipos de relación:

$$
\Lambda_*.
$$

El subíndice `*` indica que esta familia debe definirse sin usar $i$, $R_i$, `SameRegime`, K3, `EClosed` ni una totalidad global.

Un tipo $\lambda$ solo puede pertenecer a $\Lambda_*$ si sus instancias relevantes cumplen:

1. **actualidad:** la relación está efectivamente instanciada, no meramente posible;
2. **carácter ontológico:** obtiene entre los relata, no solo entre descripciones o modelos;
3. **sensibilidad a los relata:** la instancia es token-specific, no mero compartir universal, tipo, propiedad, ley o ecuación;
4. **rol integrador:** pertenece a una familia causal/procesual, constitutiva, de dependencia ontológica o espaciotemporal cuando corresponda;
5. **localidad semántica:** verificarla no requiere cuantificar sobre $R_i$, $R_{\mathrm{abs}}$, K3 o la pertenencia previa al régimen;
6. **invariancia representacional:** una recodificación fiel no puede cambiar si el enlace existe.

En particular, no bastan:

- semejanza;
- isomorfismo;
- compartir leyes;
- instanciar la misma propiedad universal;
- posibilidad contrafáctica de interacción;
- ser descritos conjuntamente por una teoría o modelo.

Esto evita que universales, leyes o tipos actúen como hubs abstractos que fusionen regímenes por mera clasificación.

### 5.2. Enlace y co-régimen

Si existe una instancia actual admisible de algún $\lambda\in\Lambda_*$ entre $q$ y $r$, escribimos:

$$
q\bowtie_* r.
$$

Para calcular conectividad usamos su simetrización:

$$
q\bowtie r
\iff
q\bowtie_* r
\lor
r\bowtie_* q.
$$

Y definimos:

$$
q\sim r
$$

como la clausura reflexivo-transitiva de $\bowtie$.

Las clases:

$$
[q]_{\sim}
$$

son candidatos a regímenes ontológicos.

Para un dominio procesual no vacío:

$$
\operatorname{Tok}(X)
:=
\{q\mid q\trianglelefteq X\},
$$

se define:

$$
\operatorname{Reg}(X)=i
$$

cuando todos sus tokens pertenecen a la misma clase $i$.

### 5.3. SameRegime no implica K3

Ahora:

$$
\operatorname{SameRegime}(X,Y)
\iff
\operatorname{Reg}(X)=\operatorname{Reg}(Y),
$$

pero no se infiere:

$$
\exists Z\,[X\preceq_i Z\land Y\preceq_i Z].
$$

El [documento técnico](work/autodescripcion-realidad-distincion-derivaciones-2026-09-22.md) contiene un contraejemplo mínimo donde dos dominios pertenecen al mismo régimen porque sus tokens están ontológicamente enlazados y, sin embargo, la familia de dominios admisibles no contiene una cota común.

Por tanto:

$$
\boxed{
\operatorname{SameRegime}(X,Y)
\not\Rightarrow
K3_i(X,Y).
}
$$

Esto elimina la circularidad conceptual original entre identidad de régimen y amalgamabilidad.

### 5.4. Alcance actual de $\Lambda_*$

Los roles integradores admitidos provisionalmente son:

$$
\Lambda_*
\subseteq
\Lambda_{\mathrm{proc}}
\cup
\Lambda_{\mathrm{causal}}
\cup
\Lambda_{\mathrm{constit}}
\cup
\Lambda_{\mathrm{dep}}
\cup
\Lambda_{\mathrm{st}}.
$$

Esta expresión no afirma que todas esas relaciones sean primitivas ni que estén presentes en toda ontología. Solo delimita los tipos de enlace que pueden optar a conectar tokens en un régimen.

Dos cautelas importantes:

- una correlación estadística no basta por sí sola;
- una relación física no clásica, como el entrelazamiento, cuenta solo si una ontología física independiente la trata como relación real token-specific y satisface los criterios anteriores.

### 5.5. K3_i se deriva de admisibilidad estructural

Con la definición normativa:

$$
\operatorname{Adm}_i
:=
\operatorname{StructAdm}_i,
$$

la directedness interna deja de requerir OAM como premisa separada.

Sean:

$$
X,Y\in\mathfrak D_i^{\mathrm{proc}}.
$$

Como ambos pertenecen al mismo régimen, definimos su unión semántica:

$$
Z
:=
(T_X\cup T_Y,\Phi_X\cup\Phi_Y).
$$

StructAdm se preserva bajo esta unión porque solo se acumula contenido positivo actual y coherente del mismo régimen.

Por tanto:

$$
Z\in\mathfrak D_i^{\mathrm{proc}},
$$

y:

$$
X\preceq_i Z
\land
Y\preceq_i Z.
$$

Luego:

$$
\boxed{K3_i.}
$$

EEA también se deriva para footprints de enlaces de $\Lambda_*$: incorporar el otro extremo y el hecho relacional actual preserva StructAdm.

Así, la parte de directedness de REV-07 queda resuelta **una vez fijada la identidad del régimen**. Lo que permanece abierto en REV-07 ya no es K3, sino la justificación filosófica de qué relaciones pertenecen legítimamente a $\Lambda_*$.

### 5.6. Qué sigue abierto

REV-07 permanece **PARTIAL**.

Ya no falta una definición de régimen; falta justificar que la familia candidata $\Lambda_*$ sea filosóficamente adecuada.

El criterio de cierre restante es:

1. justificar qué roles integradores pertenecen legítimamente a $\Lambda_*$;
2. demostrar que $\sim$ es suficientemente invariante bajo representaciones fieles;
3. comprobar que la taxonomía de enlaces no colapsa regímenes por hubs abstractos ni fragmenta indebidamente una realidad.

Como antecedente metodológico, Lewis usa conexión espaciotemporal para determinar worldmates sin definir primero una cota común; aquí ese patrón se generaliza y no compromete a la propuesta con modal realism ni con una reducción de toda unidad ontológica a espaciotiempo.

**Estado: PARTIAL — REV-07.**


## 6. Generalidad absoluta, No-$R$ y potencialismo

No se asigna una carga privilegiada a ninguna de las dos posiciones.

- El **absolutista** debe justificar que puede hablar coherentemente de absolutamente todo.
- El **restrictionist/expansionist/potentialist** debe justificar su semántica de dominios siempre restringibles o expandibles.

La propuesta no toma el debate como resuelto.

**Estado del debate: OPEN. Finding REV-11: RESOLVED como corrección de carga argumentativa.**

## 7. One-$R$, Many-$R$ y niveles de exhaustividad

La maquinaria de emergencia queda desacoplada de este problema.

Para cada régimen ontológico $i$ cuya unidad se justifique independientemente, el programa puede intentar obtener:

$$
R_i
$$

como máximo interno de:

$$
(\mathfrak D_i^{\mathrm{proc}},\preceq_i).
$$

Esto es compatible tanto con:

$$
R_i\parallel R_j
$$

como con la posibilidad de que exista alguna relación ontológica ulterior entre ambos. La teoría local no decide cuál de las dos opciones es correcta.

### 7.1. La pluralidad no crea automáticamente un absoluto

Puede escribirse:

$$
\mathscr R=\{R_i\}_{i\in I}
$$

como abreviatura metalingüística. Esa expresión **no** introduce:

- un conjunto universal ontológico;
- una suma de realidades;
- un suprarégimen;
- un $R_{\mathrm{abs}}$.

En particular:

$$
\forall i\,\exists R_i
\not\Rightarrow
\exists R_{\mathrm{abs}}.
$$

Si algún argumento futuro demuestra que todos los $R_i$ admiten una extensión ontológica común, eso constituirá un resultado metaontológico adicional. No forma parte del teorema de emergencia.

### 7.2. Monismo interno y pluralismo externo

Una posibilidad coherente con el estado actual es:

$$
\forall i\;
\forall X\in\mathfrak D_i:
X\preceq_i R_i
$$

junto con:

$$
R_i\parallel R_j
\qquad
(i\neq j).
$$

Esto puede describirse como **monismo interno + pluralismo externo**.

No se adopta como tesis demostrada; se registra como posibilidad que el formalismo local no excluye.

### 7.3. Retirada de «Verdad Absoluta indexada»

La fórmula histórica:

$$
\operatorname{VA}(o)=R_i
$$

queda **SUPERSEDED**, no solo suspendida.

Un máximo exhaustivo dentro de $i$ puede denominarse, si resulta útil:

$$
\operatorname{Truth}_i
$$

o **verdad exhaustiva interna del régimen $i$**.

No se denomina «Verdad Absoluta» porque:

$$
\boxed{
\operatorname{Truth}_i
\neq
\operatorname{Truth}_{\mathrm{abs}}
\text{ por mera definición}.
}
$$

La existencia, coherencia y semántica de:

$$
\operatorname{Truth}_{\mathrm{abs}}
$$

quedan abiertas junto con la cuestión One-$R$/Many-$R$.


**Concesión doctrinal explícita.** Esta retirada es sustantiva, no terminológica. La arquitectura formal vigente ya no contiene una inferencia desde emergencia/clausura local hacia una única realidad total ni hacia una «Verdad Absoluta». La pieza histórica que pretendía conectar el formalismo con esa doctrina —$\operatorname{VA}(o)=R_i$— ha sido eliminada porque no estaba justificada.

En consecuencia, el programa actual demuestra o intenta demostrar propiedades **internas a cada régimen $i$**. Recuperar una tesis sobre $R_{\mathrm{abs}}$ o $\operatorname{Truth}_{\mathrm{abs}}$ exigiría un argumento metaontológico nuevo e independiente.

### 7.4. Consecuencia para los antiguos índices

Los $i$ del teorema ya no se definen como «subconjuntos dirigidos maximales» para fabricar K3. Deben corresponder a regímenes cuya identidad ontológica tenga un criterio independiente.

Por tanto, el antiguo problema de solapamiento de maximales dirigidos deja de ser un problema para la función:

$$
\operatorname{VA}(o)=R_i,
$$

porque esa función ha sido retirada.

Lo que permanece abierto es más fundamental:

> ¿qué hace que dos dominios pertenezcan a la misma realidad ontológica $i$, y qué haría que dos $R_i$ fueran realmente distintos en vez de partes de un régimen mayor?

Esa obligación queda en REV-07 y en la cuestión metaontológica One-$R$/Many-$R$.

**Estado:** la teoría emergentista local es neutral respecto de One-$R$/Many-$R$. La identificación «Verdad Absoluta indexada» queda retirada.


## 8. K2, localidad, compacidad y colímites

La ruta vigente ya no presenta localidad, compacidad lógica y colímites como «tres pruebas independientes».

Para dominios procesuales de un régimen fijo $i$, se ha demostrado formalmente que `EClosed_i` se preserva bajo uniones de cadenas compatibles. Esto elimina la antigua necesidad de hacer factorizar un testigo finito por algún estadio.

Por tanto:

- **REV-10: RESOLVED** para la ruta vigente; la premisa oculta de StageFactorization ya no se usa.
- **REV-09: PARTIAL**; falta demostrar que la unión/direct limit formal de una cadena de dominios procesuales admisibles sigue siendo un dominio ontológicamente admisible de $i$.

La compacidad lógica y la maquinaria categórica pueden seguir siendo herramientas futuras para justificar esa admisibilidad, pero no cuentan como resultados ontológicos por sí mismas.


## 9. Proceso, admisibilidad y extensiones diferidas

REV-19 permanece **RESOLVED en tipado y orden** y REV-18 queda **RESOLVED en el puente semántico mínimo**.

El objeto primario es:

$$
X=(T_X,\Phi_X),
$$

con orden:

$$
X\preceq_iY
\iff
T_X\subseteq T_Y
\land
\Phi_X\subseteq\Phi_Y.
$$

La admisibilidad vigente es StructAdm: fragmento positivo, actual, homogéneo de régimen y well-formed.

Con esta elección, REV-09 queda RESOLVED para cadenas set-indexed y K3$_i$ deja de requerir OAM como premisa: la unión de dos dominios del mismo régimen ya proporciona una cota común admisible.

Siguen fuera del núcleo demostrado:

- una teoría temporal concreta;
- branching como tesis física universal;
- meta-capacidades;
- AbsoluteBruteNovelty;
- fractalidad.

«Fractal» no participa en ninguna inferencia vigente.


## 10. REC, Muro y el estatuto de la demostración

REC($R$), el Muro de la singularidad y la indistinguibilidad entre una totalidad y una sandbox internamente cerrada son **restricciones epistemológicas**, no refutaciones de la existencia de $R_i$.

La distinción normativa es:

$$
\boxed{
\text{existencia demostrada condicionalmente}
\neq
\text{identificación/certificación empírica del máximo}.
}
$$

Si para algún régimen $i$ se justifican K1$_i$, K2$_i$ y K3$_i$, el teorema puede demostrar que existe un máximo E-closed $R_i$ aunque ningún observador interno pueda señalar qué dominio concreto es $R_i$ ni distinguir empíricamente una cuasisingularidad de la totalidad genuina.

Por tanto, el Muro no bloquea el paso:

$$
K1_i+K2_i+K3_i
\Rightarrow
\exists R_i.
$$

Sí restringe **cómo pueden justificarse las premisas**, especialmente REV-20.

### Restricción epistemológica sobre K1

K1$_i$ cuantifica sobre todos los dominios admisibles del régimen:

$$
\forall X\in\mathfrak D_i^{\mathrm{proc}}
\;\exists Y\in\mathfrak K_i:
X\preceq_i Y.
$$

Un observador interno no puede establecer esta universalidad inspeccionando una muestra finita o creciente de dominios. Por ello:

$$
\boxed{
\text{evidencia por muestreo}
\not\Rightarrow
K1_i.
}
$$

El criterio de cierre de REV-20 exige una justificación **estructural y no enumerativa**: una derivación desde la naturaleza de $\operatorname{Adm}_i$, de los fragmentos procesuales y del cierre emergente, o un principio ontológico independiente que implique K1$_i$.

La evidencia empírica puede motivar o apoyar las premisas estructurales, pero no sustituir la cuantificación universal requerida.

### Alcance del Muro

El Muro deja abiertas simultáneamente estas posibilidades:

- $R_i$ existe pero no puede identificarse desde dentro;
- una cuasisingularidad es indistinguible localmente de $R_i$;
- existen otros regímenes $R_j$ inaccesibles;
- existe o no existe un $R_{\mathrm{abs}}$.

Nada de ello resta valor lógico a una demostración condicional de $\exists R_i$.

**Estado:** REV-15 permanece OPEN en cuanto a consecuencias discriminantes; el Muro se conserva como límite epistemológico compatible con la prueba de existencia.

## 11. “Dios”

“Dios” puede conservarse en el corpus exergista como **nombre doctrinal/apofático** de la Verdad Absoluta, pero no añade ninguna inferencia.

Se mantiene:

$$
\operatorname{Total}(R)
\neq
\operatorname{Ground}(R)
$$

mientras no exista un argumento separado sobre fundamento.

**Estado: SURVIVES como nomenclatura; fuera del argumento formal — REV-16.**

---

# II. Historia cronológica de la propuesta

## Fase 1 — 21 Sep 2026, 12:36 UTC — Autodescripción y distinción

**Commit:** [7dfd137](https://github.com/Exergism-Commons/exergism/commit/7dfd1372b5a6c0921cae8e0041a9558007d6a7e3)

### Idea de partida

La propuesta comenzó preguntando cómo distinguir realidad, representación/modelo de la realidad, autodescripción interna y totalidad ontológica.

La intuición central era que una descripción interna nunca debía confundirse automáticamente con aquello que describe.

### Qué sobrevive

**SURVIVES:** distinción entre $R$ y cualquier modelo interno $\widehat R_o$.

---

## Fase 2 — 21 Sep, 16:55–17:20 — Supramedio, emergencia y primer cierre

**Commits:**

- [9cf0e1d](https://github.com/Exergism-Commons/exergism/commit/9cf0e1db296e59b2ca24274cb4c71ddb8fde98b0)
- [1a53931](https://github.com/Exergism-Commons/exergism/commit/1a539315a9c4ce41bdd006a8476e193a7184add2)
- [2bfef6d](https://github.com/Exergism-Commons/exergism/commit/2bfef6d2c11f935d0f8af7dd1830e2e88fb99175)
- [0d93f76](https://github.com/Exergism-Commons/exergism/commit/0d93f7697666d24f6691981c6c21afd342b284d8)

### Tesis de la etapa

Se introdujo:

$$
R=F(R)
$$

con $F$ entendido como cierre recursivo bajo emergencia. La emergencia se hizo multivaluada para evitar determinismo ficticio.

### Problema descubierto posteriormente

La revisión muestra que $\mathcal E$ nunca llegó a definirse de manera independiente, F1–F3 fueron exigidas, F2 puede ser falsa si un dominio mayor contiene inhibidores y $R=F(R)$ es analítico si $R$ ya significa todo lo real.

### Estado actual

**OPEN / SUPERSEDED EN PARTE.**

La idea de cierre sigue siendo un programa; la formulación original ya no cuenta como demostración.

Literatura relevante: Broad, Bedau, Kim, Humphreys y Crutchfield.

---

## Fase 3 — 21 Sep, 17:32–18:01 — Muro epistemológico y Many-$R$

**Commits:**

- [5285dab](https://github.com/Exergism-Commons/exergism/commit/5285dabbcb2b6076bc5c8ef66f61e3af0e5d6569)
- [66002e3](https://github.com/Exergism-Commons/exergism/commit/66002e3f5e902089507c6597378f95eb6353de2f)
- [f7bb704](https://github.com/Exergism-Commons/exergism/commit/f7bb704ac78ed16c82fffe8ea997cc88fa847da3)
- [002b956](https://github.com/Exergism-Commons/exergism/commit/002b956ce21b9383aebe5b3a3f8dd0a4f67e19ae)

### Tesis de la etapa

Se introdujeron cuasisingularidades, Muro de la singularidad, posibilidad Many-$R$ e intento de preservar la Verdad Absoluta de forma indexada.

### Qué se aprendió

La clausura interna no certifica totalidad absoluta.

### Problema posterior

“Verdad Absoluta indexada” puede convertir “absoluto” en “máximo relativo a un índice/observador”. Además, índices maximales pueden solaparse.

### Estado actual

- Muro/REC: **DEFERRED** como epistemología.
- Many-$R$: **OPEN**.
- $\operatorname{VA}(o)=R_i$: **SUPERSEDED/SUSPENDIDO**.

---

## Fase 4 — 21 Sep, 19:06–20:52 — No-$R$, generalidad absoluta e indexación

**Commits:**

- [0a469cc](https://github.com/Exergism-Commons/exergism/commit/0a469ccab67cae23af5dd46e27a1644839a23136)
- [ebc600e](https://github.com/Exergism-Commons/exergism/commit/ebc600e76dee76b6012b967600ad10bd8f20ea33)
- [3848096](https://github.com/Exergism-Commons/exergism/commit/38480965b1f7045342cdd21930ea27b46f60ba33)
- [f00e30c](https://github.com/Exergism-Commons/exergism/commit/f00e30cbf41c0e225f40b9607cb3ce252ec5225e)
- [668be27](https://github.com/Exergism-Commons/exergism/commit/668be2791b49d398912c8fbd4ee676891a2210f3)
- [4612443](https://github.com/Exergism-Commons/exergism/commit/461244357a816eec78cea239372c298ebf308d22)
- [6a6e5dd](https://github.com/Exergism-Commons/exergism/commit/6a6e5dd38189e150757111ca79c69aabaceef3c8)
- [9152537](https://github.com/Exergism-Commons/exergism/commit/915253710bdbc8f7bb358a1373155cbf0933414b)
- [a552d3c](https://github.com/Exergism-Commons/exergism/commit/a552d3c1d2b0f6bf19526cf1540e8c87d681ca3f)
- [275efff](https://github.com/Exergism-Commons/exergism/commit/275efff224b66c1b0cf9323e5039baab834a4f3d)

### Evolución

La pregunta dejó de ser solo “¿qué es $R$?” y pasó a:

> ¿puede existir una cuantificación absolutamente general que permita formar siquiera el alcance de todo lo real?

Se separaron generalidad semántica, totalizabilidad ontológica, unicidad y existencia indexada. También aparecieron Cluster-$R$, REC y ManyMany-$R$.

### Corrección de la revisión

Esta discusión reproduce problemas existentes en la literatura sobre **absolute generality** e **indefinite extensibility**. No hay una ventaja metodológica automática para el absolutista ni para el expansionista.

### Estado actual

**OPEN.**

Lectura obligatoria: Rayo & Uzquiano (2006), Fine, Glanzberg, Hellman, Linnebo, Shapiro & Wright, Uzquiano, Williamson y Studd (2019).

---

## Fase 5 — 21 Sep, 21:19–21:50 — Teorema de clausura maximal

**Commits:**

- [bb328bc](https://github.com/Exergism-Commons/exergism/commit/bb328bc48745dcbe245cf11a0dc0b6730e72f8cf)
- [85c04d0](https://github.com/Exergism-Commons/exergism/commit/85c04d08ac23bb2698e064bc378bcf5316394b45)
- [6a46940](https://github.com/Exergism-Commons/exergism/commit/6a46940b3ef8cb518bd4662623baf0eece55aa79)
- [d43ad00](https://github.com/Exergism-Commons/exergism/commit/d43ad00b33a44ed5c65b61775c7455f7bdf65e28)

### Tesis de la etapa

Se formalizó un poset de dominios, un operador de cierre y un argumento tipo Zorn:

$$
C0+F1+F2+F3+C1+C2+\operatorname{Max}
\Rightarrow
\text{punto fijo exhaustivo}.
$$

Luego C2 se intentó derivar de la definición del índice como régimen dirigido.

### Qué sí se obtuvo

Una plantilla matemática reconocible: con hipótesis de closure operator, cotas de cadenas y maximalidad, existe un máximo/punto fijo bajo condiciones adecuadas.

### Qué no se obtuvo

No se demostró que esas hipótesis describan la realidad ni la emergencia.

Convertir C2 en parte de SameIndex hizo la conclusión demasiado analítica respecto del índice.

### Estado actual

**SURVIVES como lema matemático condicional; puente ontológico OPEN.**

El uso de Zorn se limita de momento a estructuras set-sized. Para clases propias harían falta compromisos fundacionales adicionales.

---

## Fase 6 — 21 Sep, 21:58–22:52 — Ataque a C1

**Commits:**

- [9ab2e24](https://github.com/Exergism-Commons/exergism/commit/9ab2e2422c995e762213331e55e97508ee9556d4)
- [d272982](https://github.com/Exergism-Commons/exergism/commit/d272982c59000077bc7ccd5ce779e6448a2c7c70)
- [ed4b05c](https://github.com/Exergism-Commons/exergism/commit/ed4b05cf25f9f76c42271e7106d0c8b1501ec409)
- [94d25ca](https://github.com/Exergism-Commons/exergism/commit/94d25cad20ada19ed321797315a519e78a2d1f29)
- [ec244d1](https://github.com/Exergism-Commons/exergism/commit/ec244d187169b3a05fb58f91ca9b7053943aa684)

### Evolución

C1 pasó por tres formulaciones: localidad/testigos, compacidad lógica y colímites dirigidos. Se introdujo $\Omega_\infty$ para concentrar obstrucciones no compactas.

### Corrección posterior

Las tres formulaciones son herramientas matemáticas relacionadas, pero **no son tres pruebas ontológicas independientes**.

Además, la derivación por localidad escondía otra hipótesis: si un testigo compacto queda por debajo del límite dirigido, debe factorizar por algún estadio. Esa propiedad está relacionada con la teoría de objetos presentables y categorías accesibles de Adámek–Rosický.

### Estado actual

**OPEN.**

---

## Fase 7 — 21 Sep, 23:07 – 22 Sep, 10:30 — Actualidad, potencialismo, metaemergencia y proceso

**Commits:**

- [bb775f0](https://github.com/Exergism-Commons/exergism/commit/bb775f0b54edb1ec584acf92ea67047795e856d7)
- [d40c43d](https://github.com/Exergism-Commons/exergism/commit/d40c43dd084a3f860ad19df078cdade759c45412)
- [3f5257a](https://github.com/Exergism-Commons/exergism/commit/3f5257a5fd740e55dc093d5e2e68bdf9f980958d)
- [c21b4a0](https://github.com/Exergism-Commons/exergism/commit/c21b4a0bb2273e51dfe8c1938cea86c3f59730b1)
- [b306207](https://github.com/Exergism-Commons/exergism/commit/b3062072e4333a0500b5ec2a61b4e345c956a210)
- [43b0383](https://github.com/Exergism-Commons/exergism/commit/43b03839da5cd33d61f4146b5e0170d7998ba0be)

### Evolución

Se distinguieron dominios actuales frente a modelos posibles, potencialismo radical, posibilidad modal directa y meta-capacidades, clausura sincrónica frente a continuidad diacrónica, proceso/red de estados, branching no lineal y rechazo de identificar estadios con tiempo de Planck.

### Valor de esta fase

Aclaró varias confusiones reales:

$$
\text{novedad}
\neq
\text{exterior ontológico},
$$

$$
\text{branching}
\not\Rightarrow
\text{fractalidad}.
$$

### Problema metodológico

Estas extensiones se construyeron antes de resolver las premisas más básicas sobre $\mathcal E$, $F$, C1 y C2.

### Estado actual

**DEFERRED.**

Se reabrirán solo después de cerrar el núcleo.

---

## Fase 8 — 22 Sep 2026 — Auditoría externa y consolidación

### Revisión recibida

La revisión externa identificó problemas sustantivos y formales, entre ellos:

- F1–F3 postuladas;
- fallo potencial de F2 por inhibición;
- emergencia no independiente;
- ausencia de modelo $S=F(S)\neq R$;
- exceso de resultados analíticos presentados como teoremas;
- C2 introducida por definición;
- solapamiento de índices y problema de $\operatorname{VA}(o)$;
- dependencia común de H8/H10/H11;
- presentabilidad implícita;
- asimetría frente al potencialismo;
- H1/fractalidad sin criterio;
- ausencia de consecuencias discriminantes;
- nomenclatura “Dios” sin fuerza inferencial;
- Zorn/clases;
- problemas graves de renderizado, taxonomía y duplicación.

Todos están registrados de forma persistente en el [ledger](autodescripcion-realidad-distincion-review-ledger.md).

### Decisión metodológica

A partir de esta fase:

1. no se añade nueva metafísica al núcleo mientras existan REV-01–REV-04 abiertos;
2. toda formulación antigua queda en la cronología o el archivo, no en el estado actual;
3. toda referencia literaria relevante se registra;
4. todo finding requiere evidencia explícita para cerrarse.

**Estado: SURVIVES como política de trabajo.**

---

# III. Próxima secuencia de resolución

El orden de trabajo normativo es:

## A. Emergencia y cierre

1. **REV-03:** definición independiente de emergencia/transición.
2. **REV-02:** contraejemplo de inhibición y relación correcta de extensión.
3. **REV-01:** derivar o revisar F1–F3.
4. **REV-04:** modelo explícito $S=F(S)\neq R$.

Solo entonces se podrá afirmar que el formalismo habla de emergencia.

## B. Estructura del teorema

5. **REV-07:** criterio independiente de índice/amalgamación.
6. **REV-10:** presentabilidad/factorización.
7. **REV-09:** papel exacto de compacidad y colímites.
8. **REV-17:** fundamentos de maximalidad.

## C. Metaontología y doctrina

9. **REV-11:** generalidad absoluta vs expansionismo.
10. **REV-08/REV-14:** índices, solapamiento y Verdad Absoluta.
11. **REV-15:** consecuencias discriminantes / función regulativa.

## D. Extensiones diferidas

Solo al final:

- REC/Muro;
- proceso temporal;
- branching;
- novedad modal;
- fractalidad;
- nomenclatura teológica.

---

# IV. Qué cuenta como “resolución”

La propuesta no se considerará resuelta porque haya una narración filosóficamente atractiva.

Para el núcleo emergentista, una resolución positiva exige al menos:

1. una definición de $\mathcal E$ independiente de $R$;
2. una construcción de $F$ a partir de esa definición;
3. pruebas o contraejemplos de F1–F3;
4. un ejemplo explícito de cierre propio;
5. un puente no circular entre el formalismo y dominios ontológicos;
6. una especificación clara de C1/C2 sin ocultarlas en definiciones;
7. una declaración del compromiso fundacional usado por maximalidad;
8. una posición explícita —no presupuesta— sobre generalidad absoluta.

Si alguno de estos pasos falla, el resultado correspondiente debe registrarse como negativo en el ledger.

---

# V. Literatura mínima obligatoria por bloque

El [mapa completo](autodescripcion-realidad-distincion-references.md) contiene las referencias y su función. El núcleo mínimo es:

- **Generalidad absoluta:** Rayo & Uzquiano; Fine; Glanzberg; Hellman; Linnebo; Parsons; Shapiro & Wright; Uzquiano; Williamson; Studd; Dummett.
- **Cuantificación plural:** Boolos; Linnebo; Rayo.
- **Emergencia:** Broad; Bedau; Kim; Humphreys; Crutchfield; Bedau & Humphreys.
- **Grounding:** Fine; Correia & Schnieder; Schaffer; tradición del PSR.
- **Orden/puntos fijos:** Knaster, Tarski, Zorn; Abramsky & Jung.
- **Modelo/compacidad:** teoría de modelos de primer orden, compacidad y lema del diagrama.
- **Categorías/presentabilidad:** Adámek & Rosický; Paré & Rosický.
- **Proceso/tiempo:** Whitehead; Rescher; Belnap–Perloff–Xu; literatura de branching time.
- **Branching cuántico:** Everett, solo como referencia de no linealidad posible, no como prueba de fractalidad.
- **Fractales:** Mandelbrot, si el término vuelve a usarse con contenido matemático.

---

# VI. Registro cronológico de commits de la exploración

| Fecha UTC | Commit | Cambio |
|---|---|---|
| 2026-09-21 12:36 | [7dfd137](https://github.com/Exergism-Commons/exergism/commit/7dfd1372b5a6c0921cae8e0041a9558007d6a7e3) | propose reality self-description and distinction framework |
| 2026-09-21 16:55 | [9cf0e1d](https://github.com/Exergism-Commons/exergism/commit/9cf0e1db296e59b2ca24274cb4c71ddb8fde98b0) | derive reality closure from supramedium and emergence |
| 2026-09-21 16:56 | [1a53931](https://github.com/Exergism-Commons/exergism/commit/1a539315a9c4ce41bdd006a8476e193a7184add2) | fix proposal markdown rendering |
| 2026-09-21 17:06 | [2bfef6d](https://github.com/Exergism-Commons/exergism/commit/2bfef6d2c11f935d0f8af7dd1830e2e88fb99175) | simplify emergent closure notation around F |
| 2026-09-21 17:20 | [0d93f76](https://github.com/Exergism-Commons/exergism/commit/0d93f7697666d24f6691981c6c21afd342b284d8) | model emergence as non-deterministic and constitutively decomposable |
| 2026-09-21 17:32 | [5285dab](https://github.com/Exergism-Commons/exergism/commit/5285dabbcb2b6076bc5c8ef66f61e3af0e5d6569) | introduce R singularity wall and quasi-singularities |
| 2026-09-21 17:32 | [66002e3](https://github.com/Exergism-Commons/exergism/commit/66002e3f5e902089507c6597378f95eb6353de2f) | clarify singularity wall notation and math rendering |
| 2026-09-21 17:40 | [f7bb704](https://github.com/Exergism-Commons/exergism/commit/f7bb704ac78ed16c82fffe8ea997cc88fa847da3) | add Many-R as absolute ontological pluralism stress test |
| 2026-09-21 18:01 | [002b956](https://github.com/Exergism-Commons/exergism/commit/002b956ce21b9383aebe5b3a3f8dd0a4f67e19ae) | preserve R under Many-R through metaontological humility |
| 2026-09-21 19:06 | [0a469cc](https://github.com/Exergism-Commons/exergism/commit/0a469ccab67cae23af5dd46e27a1644839a23136) | formalize No-R and conditional existence of total reality |
| 2026-09-21 19:13 | [ebc600e](https://github.com/Exergism-Commons/exergism/commit/ebc600e76dee76b6012b967600ad10bd8f20ea33) | generalize R singularity wall across metaontological models |
| 2026-09-21 19:20 | [3848096](https://github.com/Exergism-Commons/exergism/commit/38480965b1f7045342cdd21930ea27b46f60ba33) | make absolute generality versus indexed existence the core fork |
| 2026-09-21 19:21 | [f00e30c](https://github.com/Exergism-Commons/exergism/commit/f00e30cbf41c0e225f40b9607cb3ce252ec5225e) | separate absolute generality from indexed ontological totality |
| 2026-09-21 19:28 | [668be27](https://github.com/Exergism-Commons/exergism/commit/668be2791b49d398912c8fbd4ee676891a2210f3) | add indexed monism and factual versus derived uniqueness |
| 2026-09-21 19:43 | [4612443](https://github.com/Exergism-Commons/exergism/commit/461244357a816eec78cea239372c298ebf308d22) | add Cluster-R and R Enigmatic Certification |
| 2026-09-21 19:44 | [6a6e5dd](https://github.com/Exergism-Commons/exergism/commit/6a6e5dd38189e150757111ca79c69aabaceef3c8) | align Cluster-R and REC across proposal summary |
| 2026-09-21 19:51 | [9152537](https://github.com/Exergism-Commons/exergism/commit/915253710bdbc8f7bb358a1373155cbf0933414b) | rule out ManyMany-R as a stable ontological category |
| 2026-09-21 20:18 | [a552d3c](https://github.com/Exergism-Commons/exergism/commit/a552d3c1d2b0f6bf19526cf1540e8c87d681ca3f) | decouple Absolute Truth from global uniqueness |
| 2026-09-21 20:52 | [275efff](https://github.com/Exergism-Commons/exergism/commit/275efff224b66c1b0cf9323e5039baab834a4f3d) | stress-test No-R and refine R as ontological scope |
| 2026-09-21 21:19 | [bb328bc](https://github.com/Exergism-Commons/exergism/commit/bb328bc48745dcbe245cf11a0dc0b6730e72f8cf) | tighten ontology while preserving R proof program |
| 2026-09-21 21:35 | [85c04d0](https://github.com/Exergism-Commons/exergism/commit/85c04d08ac23bb2698e064bc378bcf5316394b45) | derive maximal ontological closure theorem |
| 2026-09-21 21:44 | [6a46940](https://github.com/Exergism-Commons/exergism/commit/6a46940b3ef8cb518bd4662623baf0eece55aa79) | derive C2 from ontological index structure |
| 2026-09-21 21:50 | [d43ad00](https://github.com/Exergism-Commons/exergism/commit/d43ad00b33a44ed5c65b61775c7455f7bdf65e28) | reduce C1 to directed ontological continuity |
| 2026-09-21 21:58 | [9ab2e24](https://github.com/Exergism-Commons/exergism/commit/9ab2e2422c995e762213331e55e97508ee9556d4) | reduce C1 to locality and potentialism |
| 2026-09-21 22:04 | [d272982](https://github.com/Exergism-Commons/exergism/commit/d272982c59000077bc7ccd5ce779e6448a2c7c70) | derive C1 conditionally from logical compactness |
| 2026-09-21 22:06 | [ed4b05c](https://github.com/Exergism-Commons/exergism/commit/ed4b05cf25f9f76c42271e7106d0c8b1501ec409) | clarify logical compactness assumptions |
| 2026-09-21 22:13 | [94d25ca](https://github.com/Exergism-Commons/exergism/commit/94d25cad20ada19ed321797315a519e78a2d1f29) | isolate noncompact ontological obstructions |
| 2026-09-21 22:52 | [ec244d1](https://github.com/Exergism-Commons/exergism/commit/ec244d187169b3a05fb58f91ca9b7053943aa684) | add directed colimit route and grounded obstruction criterion |
| 2026-09-21 23:07 | [bb775f0](https://github.com/Exergism-Commons/exergism/commit/bb775f0b54edb1ec584acf92ea67047795e856d7) | separate actual domains and radical potentialism |
| 2026-09-21 23:19 | [d40c43d](https://github.com/Exergism-Commons/exergism/commit/d40c43dd084a3f860ad19df078cdade759c45412) | separate modal novelty from ontological growth |
| 2026-09-21 23:27 | [3f5257a](https://github.com/Exergism-Commons/exergism/commit/3f5257a5fd740e55dc093d5e2e68bdf9f980958d) | close emergence under modal meta-transformations |
| 2026-09-22 10:05 | [c21b4a0](https://github.com/Exergism-Commons/exergism/commit/c21b4a0bb2273e51dfe8c1938cea86c3f59730b1) | separate synchronic totality from diachronic persistence |
| 2026-09-22 10:19 | [b306207](https://github.com/Exergism-Commons/exergism/commit/b3062072e4333a0500b5ec2a61b4e345c956a210) | model diachronic reality as process continuity |
| 2026-09-22 10:30 | [43b0383](https://github.com/Exergism-Commons/exergism/commit/43b03839da5cd33d61f4146b5e0170d7998ba0be) | decouple process structure from Planck time and branching |

Los commits posteriores de consolidación mantienen este registro como historia y no reintroducen sus tesis superadas en el estado normativo.

---

# VII. Herramientas futuras

**DEFERRED:** Lean cuando haya un teorema sustantivo que formalizar; cualquier infraestructura RDF/OWL/SHACL/PROV-O/CiTO/nanopublications se reconsiderará solo si una necesidad concreta de trazabilidad o inferencia la justifica después de resolver REV-01–REV-04.

---

# VIII. Política de mantenimiento

A partir de esta consolidación:

- el documento principal tendrá **una sola sección de estado actual**;
- el historial se añade cronológicamente, sin reescribir el pasado como si siempre hubiéramos sostenido la formulación final;
- los findings viven en el ledger, no repartidos por comentarios;
- la bibliografía vive en el mapa de referencias;
- un resultado superado se marca SUPERSEDED, no se borra de la historia;
- no se duplica el teorema en tres resúmenes distintos;
- no se añaden más deudas de investigación sin asociarlas a un ID del ledger.

La siguiente tarea sustantiva es **REV-03 → REV-02 → REV-01 → REV-04**: definir emergencia independientemente, resolver la inhibición/monotonía, derivar o revisar F1–F3 y construir un cierre propio explícito.
