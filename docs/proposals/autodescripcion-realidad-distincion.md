# Autodescripción, realidad y distinción — crónica consolidada

**Estado:** propuesta doctrinal exploratoria, no canónica.  
**PR:** #12 — *Derive regime-local semantic exhaustivity and isolate the Exists-R bridge*.  
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

## 1. Objetivo conceptual — totalidad de régimen frente a Realidad Total

La auditoría de REV-24 obliga a separar dos preguntas que la versión anterior volvió a mezclar:

1. ¿existe un alcance ontológico exhaustivo **de algún régimen**?;
2. ¿existe el $R$ de la doctrina original, es decir, la **totalidad de todo lo real**?

Estas tesis no son equivalentes.

### 1.1. Exhaustividad semántica, presentación y totalidad ontológica

Para un régimen ontológico $i$:

$$
\operatorname{SemTotal}_i(S)
:=
\operatorname{EClosed}_i(S)
\land
\forall X\in\mathfrak D_i^{\mathrm{proc}},
\;X\preceq_i S.
$$

$\operatorname{SemTotal}_i(S)$ es una propiedad de un **objeto semántico** $S$.

Reservamos:

$$
\operatorname{OntTotal}_i(R)
$$

para una propiedad de **alcances ontológicos**: $R$ agota efectivamente el alcance ontológico del régimen $i$.

Y:

$$
\operatorname{Presents}_i(S,R)
$$

relaciona ambos tipos. No significa $S=R$ y no contiene por definición $\operatorname{OntTotal}_i(R)$.

### 1.2. Horizonte empírico $U_i$ y Muro

$U_i$ designa el horizonte físico/empírico accesible desde una posición interna. No se identifica por definición con $S_i$ ni con $R_i$.

$$
\operatorname{Rep}_i(U_i)\preceq_i S_i.
$$

El Muro mínimo exige:

$$
\boxed{
\operatorname{NoAccessibleExtension}_i(U_i)
\not\Rightarrow
\operatorname{ExhaustsOntScope}_i(U_i).
}
$$

La arquitectura permanece:

$$
U_i
\xrightarrow{\operatorname{Rep}_i}
S_i
\dashrightarrow_{\mathrm{REV\text{-}24}/\mathrm{OTB}_i}
R_i.
$$

**Motivación física limitada.** Static-patch observables, gravitational dressing y reconstrucción holográfica motivan distinguir acceso, representación y alcance, pero no demuestran ninguna identificación $U_i=S_i=R_i$ ni ninguna tesis de totalidad. Véase el [mapa de literatura, §13](autodescripcion-realidad-distincion-references.md#13-horizontes-observables-gravitatorios-y-reconstrucción-holográfica).

### 1.3. Target audit — $R_i$ local no es el $R$ absoluto

La formulación original de esta propuesta definía:

$$
R:=\operatorname{Scope}(\operatorname{Real}),
$$

es decir, la totalidad de **todo lo real**. Esa noción corresponde, bajo una semántica de generalidad absoluta, a lo que ahora escribimos:

$$
R_{\mathrm{abs}}.
$$

La formulación intermedia:

$$
\exists i\exists R_i\,\operatorname{OntTotal}_i(R_i)
$$

es más débil: basta una totalidad indexada de un régimen. Por tanto queda **SUPERSEDED** el uso de esa fórmula como definición sin matices de `ExistsR`.

### 1.4. Existencia de totalidad de régimen

Definimos:

$$
\boxed{
\operatorname{ExistsRegR}
:=
\exists i\;\exists R_i\;
\operatorname{OntTotal}_i(R_i).
}
$$

Y la versión semánticamente testimoniada:

$$
\boxed{
\operatorname{WitnessedRegR}
:=
\exists i\;\exists S_i\;\exists R_i
[
\operatorname{SemTotal}_i(S_i)
\land
\operatorname{Presents}_i(S_i,R_i)
\land
\operatorname{OntTotal}_i(R_i)
].
}
$$

Entonces:

$$
\operatorname{WitnessedRegR}
\Rightarrow
\operatorname{ExistsRegR}.
$$

Esta es la conclusión que puede perseguir directamente la maquinaria $S_i$/REV-24.

Para aislar la realización plural de un régimen respecto de un seed actual $q$ definimos:

$$
\operatorname{RegScope}_q(rr)
:\Longleftrightarrow
\forall x[
x\prec rr
\Longleftrightarrow
(\operatorname{Actual}(x)\land\operatorname{CoReal}(x,q))
].
$$

Bajo comprensión plural, actualidad de $q$ y reflexividad de `CoReal`, REV-24d proporciona condicionalmente un $rr$ que satisface $\operatorname{RegScope}_q(rr)$. Esto es un resultado sobre **realización de alcance local**; no demuestra por sí mismo Realidad Total.

Definimos también:

$$
\operatorname{NoRegR}
:=
\neg\operatorname{ExistsRegR}.
$$

### 1.5. Existencia de Realidad Total

Para la tesis original reservamos:

$$
\boxed{
\operatorname{ExistsAbsR}
:=
\exists R_{\mathrm{abs}}\;
\operatorname{AbsTotal}(R_{\mathrm{abs}}).
}
$$

donde $\operatorname{AbsTotal}$ significa que el alcance agota **todo lo real**, no solo un régimen previamente indexado.

En una formalización plural con generalidad absoluta, el objetivo tendría la forma:

$$
\exists rr_{\mathrm{abs}}\;
\forall x[
x\prec rr_{\mathrm{abs}}
\Longleftrightarrow
\operatorname{Real}(x)
].
$$

Esta fórmula requiere precisamente aquello que está en disputa: una cuantificación suficientemente general sobre `Real` y una instancia legítima de comprensión plural absoluta. No se obtiene de la comprensión local aplicada a $\operatorname{CoReal}(-,q)$.

Reservamos el nombre doctrinal desnudo:

$$
\boxed{
\operatorname{ExistsR}:=\operatorname{ExistsAbsR}
}
$$

mientras se mantenga la definición original de $R$ como totalidad de todo lo real.

Y:

$$
\boxed{
\operatorname{NoR}
:=
\neg\operatorname{ExistsAbsR}.
}
$$

### 1.6. No hay puente automático local → absoluto

En particular:

$$
\boxed{
\operatorname{ExistsRegR}
\not\Rightarrow
\operatorname{ExistsAbsR}.
}
$$

y:

$$
\boxed{
\operatorname{WitnessedRegR}
\not\Rightarrow
\operatorname{ExistsAbsR}.
}
$$

Para llegar desde regímenes indexados a Realidad Total hace falta un **Globalization Bridge** independiente: por ejemplo, justificar generalidad ontológica absoluta, una clausura que abarque todos los regímenes o alguna estructura real común que los integre. Esta deuda se registra como REV-26.

Si, por el contrario, la semántica correcta de `real` es irreduciblemente indexada y no existe cuantificación global legítima, entonces la doctrina debe decidir explícitamente si abandona $R$ absoluto en favor de Indexed-/Many-$R$. Esa decisión tampoco la toma la maquinaria semántica.

### 1.7. One-$R$, Many-$R$ y Cluster-$R$

Solo después de separar los targets tiene sentido distinguir:

- **One-$R$ absoluto:** existe un único $R_{\mathrm{abs}}$;
- **Indexed-$R$:** existen uno o más $R_i$ exhaustivos de sus índices sin tesis global adicional;
- **Many-$R$ fuerte:** existen totalidades indexadas ontológicamente incomparables y ninguna totalidad global legítima;
- **Cluster-$R$:** varios $R_i$ quedan relacionados por una estructura real común que puede abrir una ruta de globalización.

**Estado actual:** la ruta matemática/REV-24 trabaja sobre `ExistsRegR`/`WitnessedRegR`. El objetivo doctrinal original `ExistsR = ExistsAbsR` permanece OPEN y requiere además REV-26. No se considerará refutado No-$R$ absoluto demostrando solo un $R_i$ local.


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

El programa dispone de teoremas directos condicionales de exhaustividad semántica de régimen: la ruta finita usa PON y la ruta generalizada usa `CSet/CProcStable`; ambas requieren además smallness de firma, Separation aplicable a actualidad y StructAdm. Estos resultados demuestran $\operatorname{SemTotal}$; no demuestran por sí solos $\operatorname{ExistsRegR}$ y, con mayor razón, tampoco $\operatorname{ExistsAbsR}$.

Los bloqueadores activos relevantes pasan a ser:

- **REV-07:** justificación filosófica de la familia pre-régimen $\Lambda_*$, incluida la elección de conectividad por caminos finitos;
- **REV-23:** PON — smallness por-token de la ruta finita; la ruta generalizada puede sustituirlo por `CSet/TransClSmall`;
- **REV-24:** puente no circular entre exhaustividad semántica y una totalidad ontológica de régimen;
- **REV-25:** smallness de la firma y legitimidad del paso por Separation sobre «actualmente verdadero»;
- **REV-20:** PSB/K1, ahora derivables de PON en la ruta estructural;
- **REV-22:** aplicabilidad de Zorn, subordinada a las premisas de smallness aunque la ruta directa a $\operatorname{SemTotal}$ no lo necesita;
- **REV-15:** consecuencias metaontológicas discriminantes;
- **REV-26:** Globalization Bridge — relación entre `ExistsRegR` y el $R$ absoluto de la doctrina;

## 3.1. Resumen formal vigente

Las demostraciones, contraejemplos y modelos de trabajo que originaron este estado se han movido al [documento de derivaciones técnicas](work/autodescripcion-realidad-distincion-derivaciones-2026-09-22.md). Esta sección registra solo resultados vigentes.

| Finding | Estado | Resultado vigente |
|---|---|---|
| REV-01 | RESOLVED formal | Para un sistema fijo $M$, la relación de eventos emergentes induce $F_M$ como clausura reflexivo-transitiva; F1, F2 interna y F3 se derivan. Para la ruta de Zorn, F2 es redundante: F1 + F3 bastan para elevar cotas a puntos fijos. |
| REV-02 | RESOLVED tipado | La inhibición compara sistemas/operadores distintos, no entradas del mismo $F_M$. Una extensión conductualmente conservativa caracteriza cuándo un evento puede transportarse entre sistemas. |
| REV-03 | PARTIAL | Existe una definición de emergencia event-local, independiente de $R$, basada en macro-invariancia, testigo organizacional y capacidad dinámica habilitada. Sigue pendiente validar su alcance doctrinal en casos ricos. |
| REV-04 | RESOLVED mínimo | El toy de cuatro componentes produce un punto fijo propio explícito de $F_M$. Esto demuestra que el operador no es necesariamente «la unión de todo», pero no caracteriza todavía sistemas ricos. |
| REV-18 | RESOLVED tipado | Un dominio se toma como fragmento semántico positivo actual $X=(T_X,\Phi_X)$; incidencia es pertenencia al carrier semántico y `EClosed_i` es una propiedad del contenido, no de la serialización. No se reifica el dominio como entidad adicional. Este cierre no identifica exhaustividad semántica con totalidad ontológica; esa deuda queda en REV-24. |
| REV-19 | RESOLVED tipado | El objeto primario queda fijado como fragmento procesual semántico $X=(T_X,\Phi_X)$; $\preceq_i^{\mathrm{proc}}$ es inclusión de contenido positivo actual. Admisibilidad ontológica se separa como $\operatorname{Adm}_i$ y queda en REV-18/20/09/07. |
| REV-20 | PARTIAL subordinado | Bajo StructAdm + COV, $K1_i\iff\mathrm{PSB}_i$; PON implica PSB. K1 deja de ser blocker independiente de la ruta directa. |
| REV-22 | PARTIAL subordinado | PON + las condiciones de smallness de REV-25 hacen set-sized cada régimen y su poset de fragmentos, resolviendo condicionalmente la ruta A de Zorn. La ruta directa a $\operatorname{SemTotal}$ no necesita Zorn. |
| REV-09 | RESOLVED set-indexed | Con `Adm_i := StructAdm_i`, la unión de una cadena set-indexed de fragmentos positivos actuales sigue siendo well-formed y admisible; junto con el lema previo de preservación de `EClosed`, K2 queda demostrada dentro del alcance set-sized del teorema. La aplicabilidad class-sized queda en REV-22. |
| REV-10 | RESOLVED vigente | La ruta actual ya no usa la inferencia oculta de StageFactorization/presentabilidad criticada en H8. |
| REV-21 | RESOLVED formal | Los puntos fijos de $F_i$ son exactamente los subconjuntos forward-closed del grafo emergente; la degeneración al único punto fijo no vacío $\Sigma_i$ ocurre exactamente cuando el grafo es fuertemente conexo. |
| REV-23 | OPEN para ruta finita | PON no está justificada. Hace set-sized el componente finitamente conectado, pero la ruta generalizada puede sustituirla por `CSet/TransClSmall`. Ninguna de estas smallness conditions implica por sí sola `ExistsRegR` ni `ExistsAbsR`. |
| REV-24 | OPEN blocker doctrinal local | El máximo semántico no produce un $R_i$. El puente local se descompone en REV-24a/OA, REV-24b/MC, REV-24c/RA y REV-24d/SR. Su cierre puede producir `WitnessedRegR/ExistsRegR`, no `ExistsAbsR`. |
| REV-25 | OPEN blocker fundacional/semántico | El teorema usa smallness de la firma y un paso de Separation sobre los hechos «actualmente verdaderos». Deben justificarse la firma/aridades y la disponibilidad metateórica del predicado de actualidad. |
| REV-26 | OPEN blocker doctrinal/metaontológico | **Target alignment / Globalization Bridge.** La existencia de una totalidad de régimen no implica Realidad Total. Justificar `ExistsAbsR` exige generalidad absoluta/comprensión adecuada o una estructura real que globalice todos los regímenes; alternativamente, adoptar explícitamente una semántica irreduciblemente indexada y revisar la doctrina de $R$. |

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

Para la ruta directa, el cuello de botella ya no es K1/K2/K3. Hay cuatro obligaciones independientes:

1. **REV-07:** justificar filosóficamente $\Lambda_*$ como criterio de identidad de régimen y, en particular, por qué la clausura relevante usa caminos finitos;
2. **REV-23:** justificar PON —que cada token tenga set-many vecinos ontológicos inmediatos—;
3. **REV-24:** justificar OA/MC/RA y la relación tipada $\operatorname{Presents}_i(S_i,R_i)$ sin presuponer totalidad;
4. **REV-25:** justificar la smallness de la firma/aridades y el predicado de actualidad usado por Separation.

REV-20 y REV-22 quedan como consecuencias/alternativas de las premisas de smallness. Incluso si REV-07, REV-23 y REV-25 se cierran, el teorema directo solo entrega $\operatorname{SemTotal}$ hasta cerrar REV-24.

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

El teorema de máximo pregunta únicamente por la estructura interna del poset semántico del régimen:

$$
K1_i+K2_i+K3_i
\Rightarrow
\exists S_i\in\mathfrak K_i:
\forall X\in\mathfrak D_i^{\mathrm{proc}},
\quad
X\preceq_i S_i.
$$

Como $S_i\in\mathfrak K_i$, además:

$$
\operatorname{EClosed}_i(S_i).
$$

Por tanto K1–K3 producen exactamente:

$$
\boxed{\operatorname{SemTotal}_i(S_i).}
$$

### Objetivo fuerte de esta maquinaria: `WitnessedRegR`

K1–K3 producen exactamente:

$$
\boxed{\operatorname{SemTotal}_i(S_i).}
$$

REV-24 intenta añadir un alcance ontológico de **ese régimen**:

$$
\mathrm{OTB}_i(S_i):
\quad
\operatorname{SemTotal}_i(S_i)
\Rightarrow
\exists R_i[
\operatorname{Presents}_i(S_i,R_i)
\land
\operatorname{OntTotal}_i(R_i)
].
$$

Por tanto la ruta correcta de esta maquinaria es:

$$
\boxed{
K1_i+K2_i+K3_i
+\mathrm{OTB}_i
\Rightarrow
\operatorname{WitnessedRegR}
\Rightarrow
\operatorname{ExistsRegR}.
}
$$

Esta cadena **no** contiene:

$$
\operatorname{ExistsAbsR}
$$

ni:

$$
\neg\operatorname{NoR}.
$$

El paso adicional es REV-26. El antiguo bloque que identificaba `ExistsR` con $\exists i\exists R_i\,OntTotal_i(R_i)$ queda SUPERSEDED por el target audit de §1.3–1.6.

$\mathrm{OTB}_i$ sigue siendo una abreviatura del problema local a demostrar, descompuesto en REV-24a/OA, REV-24b/MC, REV-24c/RA y REV-24d/SR.


### Qué significa aquí «cerrado»

La conclusión inmediata del teorema actual es:

$$
\boxed{
\operatorname{EClosed}_i(S_i)
}
$$

porque $S_i\in\mathfrak K_i$.

No debe escribirse todavía, sin una precisión adicional de tipos:

$$
S_i=F_i(S_i).
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
S_i\in\mathfrak K_i
\Rightarrow
F_i^{\mathrm{proc}}(S_i)=S_i.
$$

Hasta cerrar REV-24, la forma tipada y sustantiva de la tesis es «existe un máximo semántico $S_i$ y es E-closed». REV-24 debe justificar la existencia de un alcance ontológico distinto $R_i$ tal que:

$$
\operatorname{Presents}_i(S_i,R_i)
\land
\operatorname{OntTotal}_i(R_i).
$$

Por tanto no se identifica por mera maximalidad:

$$
\boxed{
S_i
\neq_{\mathrm{justified}}
R_i
}
$$

mientras REV-24 permanezca abierto.

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

Ni tampoco, incluso suponiendo cerrados los puentes REV-24 pertinentes:

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

Por tanto, un máximo $S_i$ del poset de dominios no introduce una sustancia, conjunto universal o colector físico adicional: representa exhaustivamente el contenido semántico del régimen dentro del tipo formal elegido. REV-24 no autoriza a renombrarlo como $R_i$; debe justificar una relación $\operatorname{Presents}_i(S_i,R_i)$ con un alcance ontológico distinto.

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

Si un máximo semántico domina todos los dominios admisibles, COV$_i$ implica que contiene todo contenido actual del régimen representable por la firma procesual. Esta conclusión es $\operatorname{SemTotal}$; identificarla con totalidad ontológica requiere además REV-24.

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

### 4.0. Teorema directo de exhaustividad semántica de régimen

La ruta directa al máximo semántico ya no necesita Zorn.

Definimos el vecindario ontológico inmediato:

$$
N(q):=\{r\mid q\bowtie r\}.
$$

y:

$$
\mathrm{PON}:\quad \forall q,\;N(q)\text{ es set-sized}.
$$

Como $q\sim r$ significa que existe un camino **finito** de $\bowtie$ entre ambos, PON implica que:

$$
T_i:=[q]_{\sim}
$$

es set-sized, construyendo los niveles finitos de vecindad y tomando su unión sobre $\omega$.

La elección de clausura por caminos finitos hace trabajo ontológico real: el teorema totaliza exactamente el componente finitamente conectado. REV-07 permanece abierto respecto de por qué esa es la noción correcta de co-régimen y qué ocurre ante dependencias esencialmente transfinitarias.

Definimos además:

$$
\mathrm{SigSmall}_i:
\quad
\mathcal L_i\text{ es set-sized}
\land
\forall\sigma\in\mathcal L_i,\;
\operatorname{ar}(\sigma)\text{ es set-sized}.
$$

La aridad finita es un caso suficiente de $\mathrm{SigSmall}_i$, pero no es matemáticamente necesaria. Bajo $\mathrm{SigSmall}_i$, la colección de todos los átomos posibles sobre el set $T_i$ es un conjunto.

Para aplicar Separation a «actualmente verdadero» exigimos además $\mathrm{ActualSep}_i$: el predicado de actualidad relevante debe estar disponible en la metateoría como condición definible sobre ese conjunto de átomos. Entonces:

$$
\Phi_i^{\mathrm{all}}
=
\{\varphi\in\operatorname{Atoms}_{\mathcal L_i}(T_i)
\mid \operatorname{Actual}_i(\varphi)\}
$$

es un conjunto.

Definimos:

$$
\boxed{S_i^*:=(T_i,\Phi_i^{\mathrm{all}}).}
$$

Por StructAdm, $S_i^*$ es un dominio admisible. Para cualquier $X=(T_X,\Phi_X)\in\mathfrak D_i^{\mathrm{proc}}$ se tiene $T_X\subseteq T_i$ y $\Phi_X\subseteq\Phi_i^{\mathrm{all}}$. Por tanto:

$$
\forall X\in\mathfrak D_i^{\mathrm{proc}},
\quad X\preceq_i S_i^*.
$$

Además, si un evento emergente actual tiene source en $T_i$, sus relaciones source/event/target son enlaces procesuales actuales; evento y target pertenecen a la misma clase $[q]_{\sim}$ y sus hechos están en $\Phi_i^{\mathrm{all}}$. Luego:

$$
\operatorname{EClosed}_i(S_i^*).
$$

Así:

$$
\boxed{
\mathrm{PON}
+\mathrm{SigSmall}_i
+\mathrm{ActualSep}_i
+\operatorname{StructAdm}
\Rightarrow
\operatorname{SemTotal}_i(S_i^*).
}
$$

Este es el resultado matemático directo. No contiene todavía ninguna inferencia a un objeto de tipo ontológico.

### REV-24 — descomposición del puente semántica → ontología

El puente no se expresa ya como $\operatorname{OntTotal}_i(S_i^*)$, porque $S_i^*$ es semántico y $R_i$ es ontológico. El objetivo de REV-24 es establecer, sin circularidad:

$$
\boxed{
\operatorname{SemTotal}_i(S_i)
+
\mathrm{OA}_i(S_i;q)
+
\mathrm{MC}_i(S_i;q)
+
\mathrm{RA}_i(S_i)
+
\mathrm{SR}_i(q)
\Rightarrow
\exists R_i
[
\operatorname{Presents}_i(S_i,R_i)
\land
\operatorname{OntTotal}_i(R_i)
].
}
$$

Esta caja es un **esquema objetivo, no un teorema ya demostrado**. Abreviamos por $\mathrm{OTB}_i$ una justificación suficiente de ese esquema. REV-24a/b/c controlan adecuación de la presentación; REV-24d controla la existencia del objeto de tipo alcance.

#### REV-24a — OA: anclaje ontológico

Para mantener la misma base ontológica independiente que usa MC, OA se formula también respecto de un token semilla actual $q$ y $\operatorname{CoReal}$:

$$
\mathrm{OA}_i(S;q):
\quad
\forall a\in T_S\;
\exists x\,
[
\operatorname{Actual}(x)
\land
\operatorname{CoReal}(x,q)
\land
\operatorname{Den}_i(a,x)
].
$$

OA expresa **soundness del carrier**: ningún elemento semántico de $S$ debe denotar contenido ajeno al alcance ontológico cuya presentación se pretende.

Para el candidato directo:

$$
T_i=[q]_{\sim}
$$

y se dispone de la denotación canónica:

$$
\mathrm{CD}_i:
\quad
x\in T_i
\Rightarrow
\operatorname{Den}_i(x,x).
$$

Por tanto:

$$
\boxed{
\mathrm{RS}_{\Lambda}
+
\mathrm{CD}_i
\Rightarrow
\mathrm{OA}_i(S_i^*;q).
}
$$

En efecto, si $a\in T_i=[q]_{\sim}$, RS proporciona $\operatorname{CoReal}(a,q)$ y CD proporciona $\operatorname{Den}_i(a,a)$.

Esta derivación descarga condicionalmente el anclaje de **tokens**. El anclaje y fidelidad de los hechos $\Phi_i^{\mathrm{all}}$ no quedan resueltos por ello y permanecen en REV-24c/REV-25.

#### REV-24b — MC: completitud de pertenencia

Para evitar una variable intermedia de pertenencia no justificada, MC se formula directamente respecto de la relación ontológica objetivo $\operatorname{CoReal}$ y de un token semilla actual $q$:

$$
\mathrm{MC}_i(S;q):
\quad
\forall x,
[
\operatorname{Actual}(x)
\land
\operatorname{CoReal}(x,q)
\Rightarrow
\exists a\in T_S\;\operatorname{Den}_i(a,x)
].
$$

$\operatorname{CoReal}(x,q)$ significa que $x$ y $q$ co-pertenecen al mismo régimen ontológico en el sentido que la doctrina pretende capturar. Debe recibir contenido independientemente de $S_i$, $R_i$, K3 y de la propia conectividad $[q]_{\sim}$.

Si posteriormente resulta útil escribir una extensión del régimen relativa a $q$, puede introducirse solo como abreviatura derivada:

$$
\operatorname{Reg}^{\mathrm{ont}}_q(x)
:\Longleftrightarrow
\operatorname{Actual}(x)
\land
\operatorname{CoReal}(x,q),
$$

sin añadir contenido nuevo.

##### Soundness y completeness de $\Lambda_*$

El criterio formal candidato generado por $\Lambda_*$ es:

$$
\operatorname{Reg}^{\Lambda}(x;q)
:\Longleftrightarrow
x\in[q]_{\sim}.
$$

Se distinguen dos obligaciones:

$$
\mathrm{RS}_{\Lambda}:
\quad
\operatorname{Reg}^{\Lambda}(x;q)
\Rightarrow
\operatorname{CoReal}(x,q),
$$

**soundness de régimen**: la clausura de $\Lambda_*$ no incorpora tokens que no co-pertenecen realmente;

y:

$$
\mathrm{RC}_{\Lambda}:
\quad
\operatorname{CoReal}(x,q)
\Rightarrow
\operatorname{Reg}^{\Lambda}(x;q),
$$

**completeness de régimen**: ningún modo ontológicamente genuino de co-pertenencia queda fuera de la clausura finita.

Estas direcciones hacen trabajos distintos. Para la construcción directa:

$$
T_i=[q]_{\sim}.
$$

Además, el carrier usa los propios tokens actuales como elementos semánticos; por tanto dispone de la denotación canónica:

$$
\mathrm{CD}_i:
\quad
x\in T_i
\Rightarrow
\operatorname{Den}_i(x,x).
$$

Entonces $\mathrm{RC}_{\Lambda}$, sin necesitar $\mathrm{RS}_{\Lambda}$, basta para la cobertura:

$$
\boxed{
\mathrm{RC}_{\Lambda}
+
\mathrm{CD}_i
\Rightarrow
\mathrm{MC}_i(S_i^*;q).
}
$$

En efecto, si $\operatorname{CoReal}(x,q)$, RC da $x\in[q]_{\sim}=T_i$ y CD proporciona un representante $a=x$ con $\operatorname{Den}_i(a,x)$.

$\mathrm{RS}_{\Lambda}$ cumple la obligación complementaria: evita que el carrier contenga tokens ajenos al alcance ontológico pretendido. Así, bajo RS + RC:

$$
\operatorname{CoReal}(x,q)
\Longleftrightarrow
x\in[q]_{\sim},
$$

pero solo RC interviene en la demostración de MC.

Los seis criterios actuales de §5 están orientados principalmente a $\mathrm{RS}_{\Lambda}$. El verdadero cuello de botella de completitud es $\mathrm{RC}_{\Lambda}$.

La pregunta queda reducida a:

> ¿existe algún modo actual de co-pertenencia ontológica que no pueda descomponerse en una cadena finita de relaciones integradoras token-specific pertenecientes a $\Lambda_*$?

Dependencias de límite, integración esencialmente global, relaciones infinitarias no reducibles a incidencias locales o una ontología holista fuerte son contraejemplos candidatos. Si alguno funciona, $\mathrm{RC}_{\Lambda}$ falla y la construcción actual totaliza solo un subalcance.

Si una relación infinitaria de aridad set-sized puede representarse mediante un **token de relación actual** enlazado por incidencias a sus relata, cada relatum queda a distancia finita del token relacional y no se requiere por ello una clausura transfinita. Una aridad o vecindad proper-class vuelve a chocar con REV-23.

Esta reducción **no cierra REV-24b**. Si $\operatorname{CoReal}$ no puede caracterizarse independientemente de $\Lambda_*$, RC sería una estipulación y no una prueba.

##### FID significa profundidad finita, no generación local finita

El stress test físico obliga a precisar FID. No se exige que todo contenido global sea generado por un número finito de observables locales, ni que toda relación integradora tenga aridad finita.

La tesis relevante es únicamente que la **profundidad del testigo ontológico** sea finita. Una instancia relacional actual $g$ puede tener set-many relata y actuar como nodo de incidencia:

$$
\operatorname{Inc}(x,g)
\land
\operatorname{Inc}(y,g).
$$

Si $g$ satisface los criterios independientes de admisibilidad de $\Lambda_*$, entonces $x$ e $y$ quedan conectados por un camino de longitud dos aunque $g$ sea una relación global o infinitaria. Por tanto:

$$
\boxed{
\text{aridad infinita set-sized}
\not\Rightarrow
\neg\mathrm{FID}.
}
$$

Lo que sí falsaría FID sería **integración sin testigo finitamente alcanzable**:

$$
\operatorname{CoReal}(x,q)
\land
\neg\exists\text{ cadena finita de instancias relacionales actuales admisibles}
\Rightarrow
\neg\mathrm{FID}.
$$

Esto impide confundir «no local» con «no finitamente conectable».

##### Stress test físico: gauge, superselección y completaciones

Tres familias conocidas fuerzan esta cautela:

1. **Gauge/gravedad.** Las restricciones de gauge obstaculizan la factorización ingenua de subsistemas; formulaciones con fronteras introducen edge/boundary data para describir el pegado. Esto desafía una ontología de subsistemas puramente local, pero por sí solo no refuta FID: esos grados de libertad pueden funcionar como testigos relacionales extendidos si se consideran ontológicamente reales.
2. **Superselección y pérdida de aditividad.** Hay QFTs donde ciertos operadores de una región no son generados por las álgebras de regiones menores; en ejemplos discutidos por Casini–Huerta–Magán–Pontello aparecen operadores que no pertenecen a la unión de ningún número finito de regiones locales y emergen al completar/tomar doble conmutante. Esto refuta cualquier lectura de FID como «todo es finitariamente generado por partes locales», pero no una lectura por testigos relacionales.
3. **AQFT/cuasilocalidad.** El álgebra cuasilocal es un $C^*$-inductive limit/completion de las álgebras locales; la unión local es densa, no tiene por qué coincidir con el álgebra completa. Por tanto existen candidatos matemáticos cuyo estatuto es esencialmente de límite. Si una ontología física trata uno de esos elementos como token actual co-real con tokens locales, pero no reconoce ninguna instancia relacional actual que testimonie la relación de límite, obtenemos exactamente un contraejemplo candidato a FID.

La salida «introducir un token $g$ que representa el límite» solo es legítima si $g$ satisface un criterio independiente de admisibilidad. No puede crearse un nodo relacional ad hoc únicamente para forzar conectividad. Llamamos a esa condición:

$$
\mathrm{WA}(g)
$$

(**Witness Admissibility**), que exige al menos:

- actualidad independiente del argumento de totalización;
- carácter ontológico, no mera relación entre descripciones;
- relata identificables sin usar $R_i$ o $\operatorname{CoReal}$;
- rol integrador justificable;
- invariancia bajo recodificación fiel;
- incidencia set-sized o una revisión explícita de REV-23;
- ausencia de definición circular del tipo «$g$ existe porque sus relata son co-reales».

Así, un límite, constraint global, Wilson loop, edge mode o relación infinitaria puede salvar FID **solo si** su instancia cumple WA.

Véase el [mapa de literatura](autodescripcion-realidad-distincion-references.md#identidad-de-régimen-y-relaciones-de-worldmate) para los precedentes usados en este stress test.

##### Contraejemplo matemático: conectividad sin caminos

FID no es una consecuencia lógica de una noción genérica de unidad. La curva seno del topólogo proporciona un contraesquema matemático estándar: existe un espacio $X$ que es **conexo pero no conexo por caminos**.

Tomemos una interpretación de prueba:

$$
\operatorname{CoReal}_X(x,q)
:\Longleftrightarrow
x\text{ y }q\text{ pertenecen a la misma componente conexa de }X,
$$

y:

$$
\operatorname{AdmIntRel}_X(x,y)
:\Longleftrightarrow
\text{existe un camino en }X\text{ de }x\text{ a }y.
$$

En la curva seno del topólogo existen $q,x\in X$ con:

$$
\operatorname{CoReal}_X(x,q)
$$

pero:

$$
\neg\operatorname{AdmIntRel}_X(q,x).
$$

Además, ninguna cadena finita de pares path-connected puede salvar la situación: los caminos se concatenan, por lo que una cadena finita:

$$
q=z_0,\dots,z_n=x
$$

con cada $\operatorname{AdmIntRel}_X(z_k,z_{k+1})$ produciría un camino de $q$ a $x$, contradicción.

Por tanto existe un modelo matemático coherente con:

$$
\boxed{
\operatorname{CoReal}_X(x,q)
\land
\neg\mathrm{FID}_X.
}
$$

Esto **no** prueba que la co-realidad física o metafísica tenga estructura topológica de este tipo. Sí prueba algo metodológicamente importante: FID no puede presentarse como verdad lógica derivada de «unidad» o «conectividad» sin una premisa ontológica adicional.

##### Contraejemplo metafísico candidato: dependencia a distancia transfinita

La literatura sobre regressos de grounding distingue entre que exista un fundamento y que cada entidad llegue a él mediante una cadena **finita**. Puede haber una secuencia:

$$
E_1
\succ E_{1/2}
\succ E_{1/4}
\succ\cdots
$$

tal que cada miembro dependa del siguiente y, sin embargo, la estructura completa esté ultimadamente anclada en un fundamento $F$ al que solo se llega atravesando infinitos intermediarios.

Si las instancias de dependencia inmediata son los únicos testigos WA-admisibles y una caracterización independiente de co-realidad coloca $E_1$ y $F$ dentro del mismo entramado ontológico, entonces:

$$
\operatorname{CoReal}(E_1,F)
$$

pero no existe ninguna cadena **finita** de $\operatorname{AdmIntRel}$ desde $E_1$ hasta $F$. En ese modelo:

$$
\neg\mathrm{FID}.
$$

Esto tampoco prueba que nuestra realidad contenga dependencia de longitud transfinita. Sí muestra que FID excluye una familia metafísica reconocible y, por tanto, debe defenderse o sustituirse; no puede presentarse como neutral respecto de infinitismo/fundacionalismo.

##### Dos rutas para REV-24b

La construcción vigente por caminos finitos es por tanto una **instanciación**, no la única arquitectura posible.

**Ruta A — finite-witness closure.**

Se mantiene:

$$
T_i=[q]_{\sim}
$$

y se intenta justificar:

$$
\mathrm{FID}+\mathrm{LA}
\Rightarrow
\mathrm{RC}_{\Lambda}.
$$

Esta ruta es fuerte y simple cuando toda integración dispone de profundidad finita de testigos WA-admisibles.

**Ruta B — generalized integrative closure.**

Si FID falla, puede introducirse un operador pre-régimen independiente:

$$
\mathcal C_*:A\mapsto\mathcal C_*(A),
$$

generado por reglas integrativas admisibles que pueden incluir, si se justifican independientemente, reglas de límite/globales además de enlaces finitos. Debe definirse sin usar $R_i$, $S_i$, `Presents` ni `OntTotal`.

Para impedir que esta generalización trivialice el problema definiendo simplemente:

$$
\mathcal C_*(\{q\})
:=
\{x\mid\operatorname{CoReal}(x,q)\},
$$

se exige una **independencia generativa** explícita. Sea $\mathfrak G_*$ una familia de reglas integrativas pre-régimen. Cada regla debe especificarse sin usar:

$$
\operatorname{CoReal},
R_i,
S_i,
\operatorname{Presents},
\operatorname{OntTotal}
\text{ ni el resultado final de }\mathcal C_*.
$$

Y $\mathcal C_*$ debe ser la **menor clausura** generada por esas reglas. Esquemáticamente:

$$
\mathrm{CMin}:
\quad
A\subseteq\mathcal C_*(A)
$$

y para toda estructura $B$ que contiene $A$ y es cerrada bajo todas las reglas de $\mathfrak G_*$:

$$
\mathcal C_*(A)\subseteq B.
$$

Llamamos a la restricción de independencia:

$$
\mathrm{CGI}
$$

(**Closure-Generation Independence**). Bajo CGI+CMin, CS y CC vuelven a ser afirmaciones sustantivas que pueden fallar; no quedan satisfechas por definición.

Para un seed $q$:

$$
T_i^{\mathcal C}:=\mathcal C_*(\{q\}).
$$

La ruta requiere al menos:

$$
\mathrm{CS}:\quad
x\in T_i^{\mathcal C}
\Rightarrow
\operatorname{CoReal}(x,q),
$$

$$
\mathrm{CC}:\quad
\operatorname{CoReal}(x,q)
\Rightarrow
x\in T_i^{\mathcal C},
$$

y:

$$
\mathrm{CSet}:\quad
T_i^{\mathcal C}\text{ es set-sized}.
$$

CS hace para la clausura general el trabajo de RS; CC hace el trabajo de RC. Bajo denotación canónica:

$$
\mathrm{CS}+\mathrm{CD}_i
\Rightarrow
\mathrm{OA}_i,
$$

y:

$$
\mathrm{CC}+\mathrm{CD}_i
\Rightarrow
\mathrm{MC}_i.
$$

Para reutilizar el teorema semántico directo se exige además que la clausura sea estable bajo los eventos procesuales que generan `EClosed`. Con CSet, `SigSmall`, `ActualSep` y esa estabilidad, la construcción de $S_i^*$ puede repetirse sobre $T_i^{\mathcal C}$.

Formalmente, definiendo $S_i^{\mathcal C}$ sobre $T_i^{\mathcal C}$ y restringiendo los fragmentos admisibles al carrier de esa clausura:

$$
\boxed{
\mathrm{CSet}
+
\mathrm{CProcStable}
+
\mathrm{SigSmall}_i
+
\mathrm{ActualSep}_i
+
\operatorname{StructAdm}
\Rightarrow
\operatorname{SemTotal}_{i,\mathcal C}(S_i^{\mathcal C}).
}
$$

La demostración es la misma construcción directa: todos los fragmentos relativos a la clausura se incluyen en $S_i^{\mathcal C}$ y `CProcStable` proporciona `EClosed`. CS/CC no hacen trabajo en la maximalidad semántica; hacen el trabajo ontológico de justificar que la clausura elegida coincide con el régimen pretendido.

Así, un contraejemplo a FID no implica ni:

$$
\neg\operatorname{ExistsRegR}
$$

ni, por sí solo:

$$
\neg\operatorname{ExistsAbsR}.
$$

Implica únicamente que la **ruta finita** $[q]_{\sim}$ no basta para caracterizar el régimen. La PR no adoptará FID como axioma doctrinal mientras la ruta de clausura generalizada permanezca abierta.

##### Requisito de independencia para $\operatorname{CoReal}$

Para que $\mathrm{RC}_{\Lambda}$ cuente como apoyo ontológico y no como una tautología encubierta, cualquier caracterización candidata $C(x,q)$ de co-realidad debe satisfacer:

$$
\mathrm{IR}_{\mathrm{CoReal}}:
\quad
C(x,q)
\text{ no puede definirse usando }
\Lambda_*,
\sim,
S_i,
R_i,
K3_i,
\operatorname{Presents}_i
\text{ ni }\operatorname{OntTotal}_i.
$$

Después debe poder argumentarse, y no estipularse:

$$
C(x,q)
\Rightarrow
x\in[q]_{\sim}.
$$

El criterio de falsación queda igualmente claro:

$$
\boxed{
C(x,q)
\land
x\notin[q]_{\sim}
\Rightarrow
\neg\mathrm{RC}_{\Lambda}.
}
$$

Por tanto REV-24b admite contraejemplos reales: basta un caso de co-pertenencia justificado independientemente que escape de la clausura de $\Lambda_*$.

##### Candidatos examinados para $C(x,q)$

Ninguno se adopta todavía como definición universal:

1. **conexión espaciotemporal:** es un precedente metodológico fuerte —Lewis usa una noción de mundo como totalidad máxima espaciotemporalmente conectada—, pero resulta demasiado estrecha para una propuesta que admite relaciones ontológicas no espaciotemporales y posibles estructuras físicas no separables;
2. **conexión causal:** es también demasiado estrecha; co-realidad no debería depender de que exista una cadena causal efectiva entre cualesquiera dos regiones del mismo alcance;
3. **dependencia/grounding:** amplía correctamente el espacio de enlaces, pero usar cualquier ground común como conector puede colapsar regímenes mediante fundamentos, leyes o abstracta compartidos; por eso $\Lambda_*$ exige dependencia token-specific e integradora;
4. **no-separabilidad física:** la literatura cuántica muestra que el estado de un todo puede no supervenir en los estados de sus subsistemas, por lo que constituye un test importante contra una ontología puramente local; pero no es condición necesaria de co-realidad para sistemas separables;
5. **ser partes del mismo todo máximo:** captura directamente la intuición buscada, pero presupone precisamente la unidad ontológica que REV-24b intenta justificar y por ello es circular como definición de $\operatorname{CoReal}$;
6. **relación natural/integrativa actual:** es el candidato más cercano a la arquitectura de $\Lambda_*$, pero si «integrativa» se define simplemente como «la relación que hace co-reales a sus relata», vuelve a introducir la conclusión.

La conclusión provisional no es que $\operatorname{CoReal}$ sea imposible de caracterizar, sino que REV-24b ha quedado localizado en una pregunta metafísica genuina y falsable. Véase el [mapa de literatura](autodescripcion-realidad-distincion-references.md#identidad-de-régimen-y-relaciones-de-worldmate).

#### REV-24c — RA: adecuación representacional

$\mathrm{RA}_i(S)$ exige que la representación no solo nombre miembros reales, sino que preserve y refleje las identidades y relaciones ontológicas relevantes para el uso que se haga de $S$:

$$
\mathrm{RA}_i(S)
$$

incluye, como mínimo, fidelidad de denotación e invariancia bajo recodificaciones fieles; cualquier exigencia de completitud factual adicional debe declararse por separado y coordinarse con REV-25.

#### REV-24d — SR: realización de alcance

Incluso si OA y MC fijan exactamente qué contenido ontológico corresponde al carrier de $S_i$, queda una obligación de **tipo** distinta: justificar que ese perfil de pertenencia determina un alcance ontológico $R_i$ sin identificar $R_i$ con un conjunto, una suma mereológica o el propio objeto semántico.

Introducimos una relación tipada:

$$
\operatorname{Within}_i(x,R),
$$

que significa que el token ontológico $x$ queda dentro del alcance $R$. No se presupone que $R$ sea un conjunto y $\operatorname{Within}$ no se identifica con pertenencia conjuntista.

La obligación de realización de alcance relativa a $q$ es:

$$
\mathrm{SR}_i(q):
\quad
\exists R_i\;
\forall x\,
[
\operatorname{Within}_i(x,R_i)
\Longleftrightarrow
(\operatorname{Actual}(x)\land\operatorname{CoReal}(x,q))
].
$$

SR **no está demostrada** por OA, MC, FID ni por teoría de conjuntos. Si la metateoría permite libremente un objeto-alcance para cualquier predicado, SR sería una forma de comprensión de alcances y ese compromiso debe declararse. Si no lo permite, hay que justificar por qué el perfil `CoReal(-,q)` admite realización como alcance.

Esta obligación evita dos atajos:

1. definir $R_i$ como el set $\{x\mid\operatorname{CoReal}(x,q)\}$ y declarar resuelto el problema de tipos;
2. tratar el cuantificador $\exists R_i$ como mera notación para un predicado sin explicitar la lógica de segundo orden/plural o la ontología de scopes utilizada.

REV-24d queda por tanto abierta y es lógicamente posterior a la adecuación de `CoReal`/REV-24b.

##### Ruta plural — realización sin objeto colector

Existe una ruta formal que respeta mejor la cautela anti-reificación. En una lógica plural, escribimos $rr_i$ para **unas cosas**, no para una entidad singular que las colecta, y $x\prec rr_i$ para «$x$ es una de ellas».

Sea:

$$
\varphi_q(x)
:=
\operatorname{Actual}(x)
\land
\operatorname{CoReal}(x,q).
$$

El esquema estándar de comprensión plural tiene la forma:

$$
\exists x\,\varphi_q(x)
\Rightarrow
\exists rr_i\;
\forall x\,
[x\prec rr_i\Longleftrightarrow\varphi_q(x)].
$$

Si $q$ es actual y `CoReal` es reflexiva, la antecedente está satisfecha. Por tanto, bajo comprensión plural:

$$
\boxed{
\mathrm{PluralComp}
+
\operatorname{Actual}(q)
+
\operatorname{CoReal}(q,q)
\Rightarrow
\exists rr_i\;
\forall x[
x\prec rr_i
\Longleftrightarrow
(\operatorname{Actual}(x)\land\operatorname{CoReal}(x,q))
].
}
$$

Esta conclusión realiza el **alcance plural** del régimen sin postular un set universal ni una suma mereológica. En esta lectura, la notación doctrinal $R_i$ puede entenderse como abreviatura de ese alcance plural $rr_i$; el cuantificador `\exists R_i` usado en fórmulas anteriores es entonces notación esquemática de un cuantificador de tipo scope/plural, no un existencial singular de primer orden.

Esto no es ontológicamente gratuito. La comprensión plural es un principio explícito y discutido; versiones críticas de la lógica plural restringen precisamente la comprensión cuando el dominio es extensionally indefinite. Por ello:

- para un régimen local cuya extensión `CoReal(-,q)` sea independientemente determinada, la ruta plural es un candidato serio a cerrar SR;
- para $R_{\mathrm{abs}}$, no se presupone una pluralidad universal de absolutamente todo. Esa generalización permanece dentro del debate de generalidad absoluta.

**Estado de REV-24d: PARTIAL.** La derivación plural está disponible condicionalmente; falta decidir/adoptar la lógica de scopes de la propuesta y justificar que la instancia de comprensión requerida sea legítima para los regímenes considerados.

#### Relación Presents

$\operatorname{Presents}_i(S,R)$ es la relación tipada resultante entre una presentación semántica y un alcance ontológico. No es identidad, no implica por definición $\operatorname{OntTotal}_i(R)$ y no puede definirse usando «$R$ es todo lo real del régimen» como atajo.

La descomposición hace visible una posibilidad importante: la **existencia de un alcance ontológico** puede requerir menos que una descripción semántica completa de todos sus hechos. Si REV-24b pudiera justificarse a partir de una individuación ontológica independiente del régimen, parte del trabajo sobre $R_i$ podría desacoplarse de la exhaustividad factual de $S_i$. Esto se registra como línea de investigación; no se toma todavía como demostración de $\operatorname{ExistsRegR}$ y mucho menos de $\operatorname{ExistsAbsR}$.

Solo si REV-24a/b/c producen efectivamente el esquema puente, la ruta doctrinal toma la forma:

$$
\boxed{
\mathrm{PON}
+\mathrm{SigSmall}_i
+\mathrm{ActualSep}_i
+\operatorname{StructAdm}
+\mathrm{OTB}_i
\Rightarrow
\operatorname{WitnessedRegR}
\Rightarrow
\operatorname{ExistsRegR}.
}
$$

#### No circularidad formal

La construcción de $S_i^*$ no presupone una totalidad ontológica. Parte de un token, construye su componente de conectividad finita y forma después el conjunto de hechos actuales sobre ese carrier. Precisamente por ello prueba exhaustividad **dentro del tipo semántico** y deja visible el paso adicional a ontología.

#### Papel de la emergencia

La emergencia no produce la existencia del máximo semántico. Las premisas de identidad y smallness permiten construirlo; la teoría de emergencia aporta $\operatorname{EClosed}_i(S_i^*)$. Tampoco resuelve $\mathrm{OTB}_i$. No debe afirmarse que «la emergencia demuestra que existe R».

#### Relación con Zorn

K1/K2/K3 y Zorn permanecen como una segunda ruta estructural. Bajo las premisas de smallness ya no son necesarios para construir $S_i^*$; tampoco resuelven por sí mismos REV-24.

---
**Convención normativa:** durante toda esta sección se fija un régimen ontológico $i$. Para aligerar notación se escribe:

$$
\mathfrak D:=\mathfrak D_i^{\mathrm{proc}},
\qquad
\mathfrak K:=\mathfrak K_i,
\qquad
\preceq:=\preceq_i.
$$

Toda cuantificación de K1–K3 y todo máximo obtenido en esta sección son **internos a $i$**. Formalmente el resultado es un máximo semántico $S_i$; REV-24 debe justificar si $S_i$ presenta algún alcance ontológico $R_i$. En ningún caso se infiere la existencia de $R_{\mathrm{abs}}$.

Las secciones anteriores producen dos niveles distintos que no deben confundirse:

1. **nivel system-relative:** para un sistema fijo que representa el régimen $i$, la emergencia independiente $\mathcal E_i$ induce un operador concreto $F_i$ sobre su espacio de configuraciones, y F1–F3 se derivan;
2. **nivel semántico de régimen:** el teorema habla de dominios $(\mathfrak D_i^{\mathrm{proc}},\preceq_i)$ ya tipados por REV-18; REV-24 exige justificar aparte el paso desde su máximo semántico a totalidad ontológica.

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

El teorema obtiene un máximo semántico interno $S_i$. Solo tras REV-24 podrá usarse como presentación justificada de algún alcance ontológico $R_i$; no se identifica con él. La cuestión de si distintos $R_i$ tienen una extensión común pertenece a la metaontología One-R/Many-R.

### 4.2. Teorema de máximo cerrado cofinal

**Teorema.** Bajo K1–K3 existe:

$$
S\in\mathfrak K
$$

tal que:

$$
\boxed{
\forall X\in\mathfrak D,\quad X\preceq S.
}
$$

**Demostración.**

K1 y la no-vacuidad de $\mathfrak D$ implican $\mathfrak K\neq\varnothing$.

Por K2, toda cadena en $\mathfrak K$ tiene una cota superior en $\mathfrak K$. Por Zorn existe un $S\in\mathfrak K$ maximal.

Sea $X\in\mathfrak D$. Por K3 existe $Y\in\mathfrak D$ con:

$$
S\preceq Y
\land
X\preceq Y.
$$

Por K1 existe $Z\in\mathfrak K$ con:

$$
Y\preceq Z.
$$

Luego $S\preceq Z$. Como ambos pertenecen a $\mathfrak K$ y $S$ es maximal:

$$
Z=S.
$$

Por tanto:

$$
X\preceq Y\preceq S.
$$

Como $X$ era arbitrario, $S$ es un **máximo de todo $\mathfrak D_i^{\mathrm{proc}}$**. Este $S$ es precisamente el máximo semántico $S_i$ del régimen fijado. Obtener un $R_i$ ontológico presentado por $S_i$ requiere REV-24/$\mathrm{OTB}_i$. $\square$

### 4.3. Cobertura representacional y límite del puente

En el tipo semántico vigente, la cobertura que sí puede usarse sin cambiar de nivel es:

$$
\forall q\text{ representable y actual en }i,
\quad
\exists X\in\mathfrak D_i^{\mathrm{proc}}:
q\trianglelefteq_i X.
$$

Combinada con la maximalidad de $S_i$, esta condición implica que todo contenido actual **representable por el formalismo** aparece en $S_i$.

No debe escribirse sin más:

$$
\operatorname{Real}(x)\Rightarrow x\preceq S_i,
$$

porque $S_i$ es, por REV-18, un fragmento semántico y esa fórmula mezclaría otra vez el tipo ontológico con el semántico. Para obtener una afirmación sobre todo lo real hace falta una tesis independiente de adecuación representacional —que ningún contenido ontológico relevante queda fuera del carrier/firma y que la representación preserva el alcance que se quiere llamar totalidad—. Esa es precisamente parte del criterio de cierre de REV-24.

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

1. que la representación semántica sea exhaustiva respecto de todo contenido ontológico relevante del régimen;
2. que un máximo semántico presente adecuadamente un alcance $R_i$ que satisfaga $\operatorname{OntTotal}_i(R_i)$ —REV-24—;
3. que la noción de cierre inducida por $F_M$ produzca una familia $\mathfrak K$ con el contenido ontológico pretendido;
4. que las cadenas ontológicas relevantes tengan las cotas requeridas en cualquier fortalecimiento del tipo de dominio;
5. que K3/directedness y la clausura finita de `SameRegime` sean legítimas independientemente de la conclusión.

Estas cargas quedan trazadas así:

- **REV-18:** tipado semántico de $\operatorname{EClosed}$, ya resuelto en su alcance;
- **REV-24:** puente tipado $S_i\to R_i$ mediante OA/MC/RA y $\operatorname{Presents}_i$;
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
\text{Zorn puede producir un }S_i
\text{ máximo del poset semántico del régimen}.
}
$$

La demostración completa está en el documento técnico.

**Ruta C — teoría de clases**

Especificar explícitamente una teoría de clases y un principio de maximalidad suficientemente fuerte. Esta ruta no se presupone.

La aplicabilidad fundacional se registra como REV-22 y depende también de REV-25. No puede cerrarse suponiendo smallness a partir de la existencia del propio máximo.

### 4.8. Estado normativo

- **REV-01:** RESOLVED en su ataque original. F1–F3 se derivan para $F_M$, y F2 resulta además redundante para el teorema abstracto.
- **REV-02:** RESOLVED en el sentido tipado correcto: la inhibición muestra no-monotonía entre sistemas/operadores, no dentro de un único $F_M$.
- **REV-04:** RESOLVED mediante el punto fijo propio explícito del toy.
- **REV-18:** RESOLVED en su alcance de tipado semántico. **REV-24** es ahora el blocker específico del paso de exhaustividad semántica a totalidad ontológica.

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

El criterio de cierre restante se separa ahora en las dos direcciones exigidas por REV-24b:

1. justificar qué roles integradores pertenecen legítimamente a $\Lambda_*$;
2. demostrar $\mathrm{RS}_{\Lambda}$: la conectividad bajo $\Lambda_*$ no fusiona entidades que no co-pertenecen ontológicamente;
3. demostrar $\mathrm{RC}_{\Lambda}$: toda co-pertenencia ontológica relevante queda capturada por una cadena finita de enlaces admisibles —o justificar una generalización explícita si existen relaciones esencialmente globales/infinitarias—;
4. demostrar que $\sim$ es suficientemente invariante bajo representaciones fieles;
5. comprobar que la taxonomía de enlaces no colapsa regímenes por hubs abstractos ni fragmenta indebidamente una realidad.

$\mathrm{RC}_{\Lambda}$ es compartido por REV-07 y REV-24b: mientras permanezca abierto, $[q]_{\sim}$ es un **candidato** a alcance de régimen, no una certificación de totalidad ontológica.

Como antecedente metodológico, Lewis usa conexión espaciotemporal para determinar worldmates sin definir primero una cota común; aquí ese patrón se generaliza y no compromete a la propuesta con modal realism ni con una reducción de toda unidad ontológica a espaciotiempo.

**Estado: PARTIAL — REV-07.**


## 6. Generalidad absoluta, No-$R$ y potencialismo — REV-26

REV-26 es el blocker que separa una totalidad indexada de régimen de la Realidad Total original.

### 6.1. AG — generalidad absoluta

Llamamos:

$$
\mathrm{AG}
$$

a la condición metalingüística de que el cuantificador usado en:

$$
\operatorname{Real}(x)
$$

pueda recorrer **absolutamente todo lo real**, sin una restricción contextual/indexada oculta.

AG no afirma que exista un set o dominio-objeto de todas las cosas. Es una tesis sobre el alcance legítimo de la cuantificación.

### 6.2. APC$_{Real}$ — comprensión plural absoluta relevante

La instancia de comprensión plural necesaria es:

$$
\mathrm{APC}_{Real}:
\quad
(\exists x\,\operatorname{Real}(x))
\Rightarrow
\exists rr_{\mathrm{abs}}\;
\forall x[
x\prec rr_{\mathrm{abs}}
\Longleftrightarrow
\operatorname{Real}(x)
].
$$

Esta fórmula no postula un conjunto de todas las cosas: $rr_{\mathrm{abs}}$ es una variable plural. Pero la legitimidad de aplicar comprensión a un dominio absolutamente general sigue siendo una cuestión filosófica real; critical plural logic y las objeciones por extensibilidad indefinida impiden tratarla como gratuita.

### 6.3. Teorema condicional de existencia absoluta

Si la doctrina adopta la semántica plural de alcance ya usada en REV-24d, entonces:

$$
\boxed{
\mathrm{AG}
+
\mathrm{APC}_{Real}
+
\exists x\,\operatorname{Real}(x)
\Rightarrow
\operatorname{ExistsAbsR}.
}
$$

**Demostración.** APC$_{Real}$ produce unas cosas $rr_{\mathrm{abs}}$ tales que, para todo $x$, $x$ es una de ellas si y solo si $x$ es real. Bajo la lectura de $R$ como **alcance ontológico** y no como megaobjeto/set, esa pluralidad realiza exactamente el scope de `Real`. Por tanto existe Realidad Total en el sentido plural-scope adoptado. $\square$

Este resultado es deliberadamente austero. No usa:

- emergencia;
- $F$;
- Zorn;
- PON;
- $S_i$;
- REV-24;
- causalidad;
- ni una hipótesis física sobre nuestro universo.

Por tanto, si el objetivo es **solo la existencia de $R$ como alcance de todo lo real**, la carga decisiva no está en la maquinaria emergentista: está en AG + APC$_{Real}$ + la semántica plural de scope.

### 6.4. Qué no demuestra este teorema

No demuestra que $R$ sea:

- único como objeto —no se ha postulado objeto alguno—;
- estructuralmente conectado;
- un régimen de $\operatorname{CoReal}$;
- emergente o E-closed;
- cognoscible desde dentro;
- representable por un único $S_i$;
- ni que One-$R$ sea la metaontología correcta en el sentido fuerte.

Tampoco demuestra AG o APC$_{Real}$: **condiciona `ExistsAbsR` a ellas**.

### 6.5. Ruta restrictionist/expansionist

El rival fuerte no necesita sostener que «hay un objeto real fuera de $R$». Puede negar que exista una cuantificación/pluralidad absolutamente exhaustiva.

Dos estrategias quedan abiertas:

1. **restricción/contextualismo:** todo uso efectivo de `Real` está indexado a un dominio/contexto $c$;
2. **expansionismo/extensibilidad indefinida:** para todo dominio legítimo $D_c$ existe una expansión legítima $D_{c'}$ que permite cuantificar sobre más.

En esa semántica, la propia fórmula APC$_{Real}$ puede carecer de una instancia absolutamente general legítima. Entonces no obtenemos:

$$
\operatorname{ExistsAbsR}.
$$

Pero de ello tampoco se sigue automáticamente `NoR` como una proposición ordinaria formulada desde un supuesto metalenguaje absolutamente general: el restrictionist debe explicar cómo expresa su propia tesis sin reintroducir la generalidad que niega.

### 6.6. Globalización desde regímenes indexados

Existe una segunda ruta posible, independiente de AG directa. Supóngase que tenemos totalidades de régimen $R_i$. Para obtener $R_{\mathrm{abs}}$ hace falta una estructura real $G$ capaz de abarcar **todos** los índices relevantes sin que quede otro índice real fuera de su alcance.

Esquemáticamente:

$$
\mathrm{GB}:
\quad
\{R_i\}_{i\in I}
\leadsto
R_{\mathrm{abs}}.
$$

Pero GB no puede definirse simplemente como «hay un scope que contiene todos los $R_i$», porque eso presupone la conclusión. Debe venir de una semántica global legítima o de una estructura ontológica común independientemente justificada.

Si cada supuesto conjunto de índices admite siempre un índice adicional no cubierto, obtenemos una versión metaontológica del expansionismo y GB falla.

### 6.7. Estado de REV-26

- **REV-26a / AG:** OPEN.
- **REV-26b / APC$_{Real}$:** OPEN.
- **REV-26c / GB:** OPEN como ruta alternativa desde `ExistsRegR`.

Por tanto:

$$
\boxed{
\operatorname{ExistsRegR}
\not\Rightarrow
\operatorname{ExistsAbsR}
}
$$

pero también:

$$
\boxed{
\mathrm{AG}
+
\mathrm{APC}_{Real}
+
\operatorname{NonEmptyReality}
\Rightarrow
\operatorname{ExistsAbsR}.
}
$$

**Estado del debate:** REV-11 permanece RESOLVED como corrección de carga argumentativa; REV-26 concentra ahora el problema de existencia del $R$ doctrinal original.


## 7. One-$R$, Many-$R$ y niveles de exhaustividad

La maquinaria de emergencia queda desacoplada de este problema.

Para cada régimen ontológico $i$ cuya unidad se justifique independientemente, el programa puede intentar obtener primero:

$$
S_i
$$

como máximo semántico interno de:

$$
(\mathfrak D_i^{\mathrm{proc}},\preceq_i).
$$

Solo si REV-24 proporciona $\mathrm{OTB}_i$ puede demostrarse la existencia de un alcance ontológico $R_i$ relacionado con el máximo semántico mediante:

$$
\operatorname{Presents}_i(S_i,R_i)
\land
\operatorname{OntTotal}_i(R_i).
$$

$S_i$ no «se convierte» en $R_i$: permanece como su presentación semántica.

Esto deja dos niveles de pluralidad distintos:

- pluralidad formal de máximos semánticos $S_i$;
- pluralidad ontológica de $R_i$, condicionada al cierre de REV-24 para los regímenes correspondientes.

### 7.1. La pluralidad no crea automáticamente un absoluto

Puede escribirse metalingüísticamente:

$$
\mathscr S=\{S_i\}_{i\in I}.
$$

Esa expresión no introduce un conjunto universal ontológico, una suma de realidades, un suprarégimen ni un $R_{\mathrm{abs}}$.

Incluso si para cada régimen se cerrase REV-24 y existieran correspondientes $R_i$, seguiría sin valer por mera lógica:

$$
\forall i\,\exists R_i
\Rightarrow
\exists R_{\mathrm{abs}}.
$$

El problema One-$R$/Many-$R$ continúa siendo metaontológico e independiente.

### 7.2. Monismo interno y pluralismo externo

En el nivel puramente formal puede ocurrir:

$$
\forall i\;
\forall X\in\mathfrak D_i^{\mathrm{proc}}:
X\preceq_i S_i
$$

junto con incomparabilidad entre máximos de regímenes distintos.

Si además REV-24 se cerrase para dos regímenes $i\neq j$, podría plantearse la posibilidad ontológica:

$$
R_i\parallel R_j.
$$

Esto puede describirse como **monismo interno + pluralismo externo**, pero no se adopta como tesis demostrada.

Tampoco se permite inferir pluralidad ontológica a partir de mera pluralidad de representaciones, observadores o reconstrucciones. La literatura holográfica sobre quantum error correction proporciona un precedente técnico para representaciones redundantes/no triviales del mismo contenido físico. Se usa aquí solo como cautela metodológica: One-$R$/Many-$R$ debe resolverse por estructura ontológica, no contando descripciones. Véase [§13 del mapa de literatura](autodescripcion-realidad-distincion-references.md#13-horizontes-observables-gravitatorios-y-reconstrucción-holográfica).

### 7.3. Retirada de «Verdad Absoluta indexada»

La fórmula histórica:

$$
\operatorname{VA}(o)=R_i
$$

queda **SUPERSEDED**, no solo suspendida.

Un máximo semánticamente exhaustivo dentro de $i$ puede denominarse, si resulta útil:

$$
\operatorname{Truth}_i
$$

o **verdad exhaustiva interna del formalismo de régimen $i$**. Esa nomenclatura no añade $\operatorname{OntTotal}_i$.

No se denomina «Verdad Absoluta» porque:

$$
\boxed{
\operatorname{Truth}_i
\neq
\operatorname{Truth}_{\mathrm{abs}}
\text{ por mera definición}.
}
$$

La existencia, coherencia y semántica de $\operatorname{Truth}_{\mathrm{abs}}$ quedan abiertas junto con la cuestión One-$R$/Many-$R$.

**Concesión doctrinal explícita.** La arquitectura formal vigente ya no contiene una inferencia desde emergencia/clausura local hacia una realidad total. El máximo semántico $S_i$ permanece separado de la tesis ontológica $R_i$ por REV-24.

### 7.4. Consecuencia para los antiguos índices

Los $i$ del teorema ya no se definen como «subconjuntos dirigidos maximales» para fabricar K3. Deben corresponder a regímenes cuya identidad ontológica tenga un criterio independiente.

La función histórica $\operatorname{VA}(o)=R_i$ permanece retirada. La pregunta que sigue abierta es más fundamental:

> ¿qué hace que dos dominios pertenezcan al mismo régimen ontológico $i$, y qué justificaría que dos candidatos semánticos exhaustivos correspondan a totalidades ontológicas distintas en vez de a partes de un régimen mayor?

Esa obligación queda repartida entre REV-07 —identidad de régimen— y REV-24 —puente semántica→ontología—.

**Estado:** la teoría emergentista local es neutral respecto de One-$R$/Many-$R$.

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

REC y el Muro deben mantenerse separados porque tienen **estatus y dirección lógica distintos**.

### 10.1. REC — consecuencia estructural de una totalidad real

$\operatorname{REC}_i(R_i)$ (R Enigmatic Certification) no se adopta como una premisa independiente para demostrar que $R_i$ existe. Es una consecuencia estructural —en gran medida analítica una vez fijado el significado de totalidad ontológica— de un candidato que ya satisface:

$$
\operatorname{OntTotal}_i(R_i).
$$

Introducimos, de forma tipada, la abreviatura:

$$
\operatorname{REC}_i(R_i)
:=
\neg\exists x\,
[
\operatorname{Real}(x)
\land
\operatorname{OutsideOntScope}_i(x,R_i)
\land
\operatorname{CertifiesTotality}_i(x,R_i)
].
$$

Por tanto, la dirección válida es:

$$
\boxed{
\operatorname{OntTotal}_i(R_i)
\Rightarrow
\operatorname{REC}_i(R_i).
}
$$

La razón es estructural: si existiera un certificador **real y ontológicamente exterior** al alcance exhaustivo atribuido a $R_i$, ese mismo testigo mostraría que el candidato no era ontológicamente total.

Así, para cualquier candidato $C$:

$$
\boxed{
\operatorname{ExternalRealCertification}_i(C)
\Rightarrow
\neg\operatorname{OntTotal}_i(C).
}
$$

Una certificación externa exitosa no certifica que $C$ sea $R_i$: descarta esa identificación y amplía el alcance ontológico relevante.

REC no significa que $R_i$ sea incognoscible, indescriptible o indemostrable por cualquier vía. Excluye específicamente un **punto de certificación real situado ontológicamente fuera de una totalidad genuina**.

Por ello REC solo se atribuye propiamente a un candidato después de disponer de $\operatorname{OntTotal}_i$. No se atribuye por mera clausura a $U_i$ ni a un máximo semántico $S_i$.

### 10.2. Muro — subdeterminación desde un horizonte o candidato

El Muro es una restricción epistemológica distinta. Su forma mínima dice que la ausencia de una extensión accesible no certifica exhaustividad ontológica:

$$
\boxed{
\operatorname{NoAccessibleExtension}_i(U_i)
\not\Rightarrow
\operatorname{ExhaustsOntScope}_i(U_i).
}
$$

Y, en el nivel semántico:

$$
\boxed{
\operatorname{SemTotal}_i(S_i)
\not\Rightarrow
\exists R_i[
\operatorname{Presents}_i(S_i,R_i)
\land
\operatorname{OntTotal}_i(R_i)
].
}
$$

Una sandbox o cuasisingularidad puede por tanto **imitar epistemológicamente** el comportamiento que un observador esperaría de REC —no aparece ningún certificador exterior accesible— sin poseer REC en sentido ontológico. Si realmente existe un exterior, el dominio era parcial aunque ese exterior fuese inaccesible desde dentro.

La asimetría queda resumida así:

$$
\boxed{
\begin{array}{rcl}
\text{exterior real que certifica un candidato}
&\Rightarrow&
\text{el candidato no era ontológicamente total}
\\
\text{ningún exterior accesible}
&\not\Rightarrow&
\text{el candidato es ontológicamente total}.
\end{array}
}
$$

La primera línea es la consecuencia estructural asociada a REC. La segunda es el Muro.

La versión fuerte del Muro —que ninguna evidencia puramente interna pueda **jamás** discriminar la metaontología última— no se da por demostrada y permanece dentro de REV-15.

### 10.3. Estatuto del teorema semántico

La distinción normativa correcta sigue siendo:

$$
\boxed{
\text{existencia condicional de un máximo semántico }S_i
\neq
\text{certificación ontológica de }R_i.
}
$$

Si para algún régimen $i$ se justifican K1$_i$, K2$_i$ y K3$_i$, el teorema puede demostrar que existe un máximo E-closed $S_i$ aunque ningún observador interno pueda identificarlo empíricamente.

Por tanto, el Muro no bloquea el paso formal:

$$
K1_i+K2_i+K3_i
\Rightarrow
\exists S_i\;\operatorname{SemTotal}_i(S_i).
$$

Pero ese paso **no es todavía**:

$$
K1_i+K2_i+K3_i
\Rightarrow
\exists R_i.
$$

La segunda inferencia requiere además REV-24/$\mathrm{OTB}_i$.

### Acceso causal y reconstruibilidad

El Muro tampoco debe identificar «causalmente accesible» con «representable/reconstruible». En AdS/CFT, Dong–Harlow–Wall demuestran reconstrucción de operadores del bulk en el entanglement wedge, que puede extenderse más allá de la causal wedge. Almheiri–Dong–Harlow relacionan esta redundancia reconstructiva con quantum error correction.

Esto proporciona un precedente físico concreto para admitir, en modelos donde esas hipótesis aplican:

$$
\operatorname{Reconstructible}_i(x)
\land
\neg\operatorname{DirectCausalAccess}_i(x).
$$

La propuesta **no universaliza** este resultado a toda ontología ni lo usa para probar el Muro. Solo muestra que acceso causal directo y alcance representacional son nociones físicamente separables; por tanto, la ausencia de acceso causal adicional no certifica el alcance de $R_i$. Véase el [mapa de literatura, §13](autodescripcion-realidad-distincion-references.md#13-horizontes-observables-gravitatorios-y-reconstrucción-holográfica).

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

El criterio de cierre de REV-20 exige una justificación **estructural y no enumerativa**. La evidencia empírica puede motivar o apoyar sus premisas, pero no sustituir la cuantificación universal requerida.

### Alcance del Muro

El Muro deja abiertas simultáneamente estas posibilidades:

- existe un máximo semántico $S_i$ pero no puede identificarse desde dentro;
- una cuasisingularidad es indistinguible localmente de $S_i$;
- existe o no existe algún alcance $R_i$ tal que $\operatorname{Presents}_i(S_i,R_i)\land\operatorname{OntTotal}_i(R_i)$;
- existen otros regímenes y, si REV-24 se cierra en ellos, otros $R_j$;
- existe o no existe un $R_{\mathrm{abs}}$.

Nada de ello resta valor lógico a una demostración condicional de $\exists S_i\;\operatorname{SemTotal}_i(S_i)$. Tampoco sustituye la justificación ontológica que exige REV-24.

**Estado:** REC queda clasificado como consecuencia estructural condicionada a $\operatorname{OntTotal}$, en línea con REV-06. REV-15 permanece OPEN para las consecuencias discriminantes y para cualquier versión fuerte del Muro. El Muro se conserva como límite epistemológico, no como puente ni a `ExistsRegR` ni a `ExistsAbsR`.

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

- Muro: **DEFERRED** históricamente como epistemología. **Corrección normativa posterior (§10):** REC no es otra versión del Muro; queda reclasificado como consecuencia estructural condicionada a `OntTotal`.
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
