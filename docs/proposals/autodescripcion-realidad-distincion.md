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

### 1.3. Target doctrinal revisado — alcance extensional no es todavía $R$

La lectura histórica:

$$
R:=\operatorname{Scope}(\operatorname{Real})
$$

queda **SUPERSEDED como definición completa de $R$**.

Conservamos ese concepto bajo otro nombre:

$$
\boxed{
\mathcal R_{\mathrm{ext}}
:=
\operatorname{Scope}(\operatorname{Real}),
}
$$

el **alcance extensional absoluto** de todo aquello sobre lo que Real cuantifique legítimamente.

$\mathcal R_{\mathrm{ext}}$ responde únicamente a:

> ¿qué cosas son reales?

El $R$ doctrinal fuerte responde además a:

> ¿pertenecen todas esas cosas a una misma genealogía ontológica cerrada?

Por decisión doctrinal, una Realidad no es una mera pluralidad exhaustiva. Es el alcance generado por una **base/origen ontológico común** y cerrado bajo las relaciones ontológicas generativas pertinentes.

### 1.4. Primitivas genealógicas

Una base de origen puede ser singular, plural o estructurada. Se escribe:

$$
\mathcal O_i
$$

sin presuponer que sea un set, un instante inicial o una «primera causa» temporal.

Introducimos:

$$
\operatorname{OntOrigin}_i(\mathcal O_i),
$$

«$\mathcal O_i$ es una base ontológica originaria admisible para el índice $i$», y una relación generativa independiente:

$$
\operatorname{GenStep}_i(a,b),
$$

«$b$ deriva ontológicamente de $a$ mediante un paso generativo admisible».

Su clausura se denota:

$$
\operatorname{Generated}^{*}_i(\mathcal O_i,x).
$$

La estrella no compromete todavía a clausura finita: puede realizarse mediante la Ruta A finita o mediante una clausura generalizada/transfinita si esta última se justifica.

**Restricción de no circularidad:** OntOrigin, GenStep y las reglas que generan $\operatorname{Generated}^{*}$ deben especificarse sin usar $R_i$, CoReal, Presents, OntTotal, SemTotal ni la extensión final que se pretende obtener.

### 1.5. $R_i$ — realidad indexada como clausura genealógica

Definimos la condición genealógica:

$$
\operatorname{GeneTotal}_i(\mathcal O_i,R_i)
$$

cuando:

$$
\operatorname{OntOrigin}_i(\mathcal O_i)
$$

y:

$$
\forall x[
\operatorname{Within}_i(x,R_i)
\Longleftrightarrow
\operatorname{Generated}^{*}_i(\mathcal O_i,x)
].
$$

Así:

$$
\boxed{
R_i
=
\operatorname{Scope}
\bigl(
\operatorname{Cl}^{\mathrm{ont}}_i(\mathcal O_i)
\bigr)
}
$$

se entiende como abreviatura doctrinal, no como identidad conjuntista.

La existencia local fuerte pasa a ser:

$$
\boxed{
\operatorname{ExistsRegR}
:=
\exists i\;\exists\mathcal O_i\;\exists R_i\;
\operatorname{GeneTotal}_i(\mathcal O_i,R_i).
}
$$

Y la versión semánticamente testimoniada:

$$
\boxed{
\operatorname{WitnessedRegR}
:=
\exists i,S_i,\mathcal O_i,R_i[
\operatorname{SemTotal}_i(S_i)
\land
\operatorname{Presents}_i(S_i,R_i)
\land
\operatorname{GeneTotal}_i(\mathcal O_i,R_i)
].
}
$$

Por tanto:

$$
\operatorname{WitnessedRegR}
\Rightarrow
\operatorname{ExistsRegR},
$$

pero la existencia ontológica de $R_i$ ya no depende conceptualmente de que exista primero un $S_i$: $S_i$ **presenta** una genealogía ontológica cuya existencia debe justificarse por REV-07.

### 1.6. CoReal pasa a derivarse de genealogía común

Una vez justificada una base $\mathcal O_i$:

$$
\boxed{
\operatorname{CoReal}_i(x,y)
:\Longleftrightarrow
\operatorname{Generated}^{*}_i(\mathcal O_i,x)
\land
\operatorname{Generated}^{*}_i(\mathcal O_i,y).
}
$$

Así, la conectividad bajo $\Lambda_*$ o una clausura candidata $\mathcal C_*$ ya no **define primariamente** co-realidad. Debe reconstruir correctamente la clausura genealógica.

Esto invierte la carga de REV-07:

$$
\text{origen + generación}
\longrightarrow
\text{co-realidad}
\longrightarrow
\text{tests sobre }\Lambda_*/\mathcal C_*.
$$

No:

$$
\Lambda_*
\longrightarrow
\text{co-realidad por definición}.
$$

Dos regiones causalmente desconectadas pueden pertenecer al mismo $R_i$ si derivan de la misma base ontológica.

### 1.7. $R$ absoluto — genealogía común de todo lo real

Definimos el target absoluto mediante una base $\mathcal O_{\mathrm{abs}}$:

$$
\operatorname{AbsGeneTotal}(\mathcal O_{\mathrm{abs}},R_{\mathrm{abs}})
$$

si:

$$
\operatorname{OntOrigin}_{\mathrm{abs}}(\mathcal O_{\mathrm{abs}})
$$

y:

$$
\forall x[
\operatorname{Real}(x)
\Longleftrightarrow
\operatorname{Generated}^{*}_{\mathrm{abs}}
(\mathcal O_{\mathrm{abs}},x)
],
$$

y $R_{\mathrm{abs}}$ realiza exactamente ese alcance:

$$
\forall x[
\operatorname{Within}_{\mathrm{abs}}(x,R_{\mathrm{abs}})
\Longleftrightarrow
\operatorname{Generated}^{*}_{\mathrm{abs}}
(\mathcal O_{\mathrm{abs}},x)
].
$$

El objetivo doctrinal queda:

$$
\boxed{
\operatorname{ExistsR}
:=
\operatorname{ExistsAbsR}
:=
\exists\mathcal O_{\mathrm{abs}}\exists R_{\mathrm{abs}}\;
\operatorname{AbsGeneTotal}
(\mathcal O_{\mathrm{abs}},R_{\mathrm{abs}}).
}
$$

Ésta es una tesis sustantiva. Puede ser falsa aun cuando exista perfectamente el alcance extensional $\mathcal R_{\mathrm{ext}}$ de todo lo real.

En particular:

$$
\boxed{
\operatorname{ExistsExtScope}
\not\Rightarrow
\operatorname{ExistsR}.
}
$$

AG y comprensión plural pueden ayudar a formular/realizar $\mathcal R_{\mathrm{ext}}$ o el scope de una clausura ya identificada, pero **no demuestran un origen ontológico común**.

### 1.8. No hay puente automático local → absoluto

Aunque existan genealogías indexadas:

$$
\operatorname{ExistsRegR}
\not\Rightarrow
\operatorname{ExistsR}.
$$

El salto absoluto exige justificar que todo lo real pertenece a una única genealogía ontológica última, o que las genealogías indexadas tienen una base superior común.

Por tanto REV-26 deja de ser principalmente un problema de formar la pluralidad «todo lo real». Su núcleo pasa a ser la **Common-Origin Thesis** absoluta.

### 1.9. One-$R$, Indexed-$R$ y Many-$R$

- **One-$R$ fuerte:** existe una base ontológica absoluta $\mathcal O_{\mathrm{abs}}$ cuya clausura contiene exactamente todo lo real.
- **Indexed-$R$:** existen una o más clausuras genealógicas $R_i$ justificadas localmente, sin tesis de origen absoluto común.
- **Many-$R$ fuerte:** existen al menos dos genealogías ontológicas últimas y no existe ninguna base ontológica superior admisible cuya clausura las integre a ambas.
- **Cluster-$R$:** varias genealogías aparentemente separadas resultan derivables de una base ontológica común de orden superior; pasan entonces a pertenecer a una realidad más amplia.

Una pluralidad de representaciones, horizontes o regiones causalmente desconectadas no basta para Many-$R$.

**Decisión REV-26e:** RESOLVED doctrinal. El target no es el mero $\mathcal R_{\mathrm{ext}}=Scope(Real)$, sino una Realidad entendida como **unidad genealógica ontológicamente cerrada**. Esta estructura no se añade para hacer no trivial la prueba: constituye el criterio doctrinal de qué cuenta como una realidad.

## 2. Consecuencias analíticas y tesis sustantiva

Para el mero alcance extensional:

$$
\mathcal R_{\mathrm{ext}}
=
\operatorname{Scope}(\operatorname{Real}),
$$

es analítico que:

$$
\operatorname{Real}(x)
\Rightarrow
x\prec \mathcal R_{\mathrm{ext}}
$$

bajo la semántica de scope adoptada.

También es analítico que un supuesto «real fuera del alcance de todo lo real» contradiga esa definición.

Pero **esas consecuencias pertenecen a $\mathcal R_{\mathrm{ext}}$, no demuestran $R$**.

La tesis doctrinal fuerte añade:

$$
\exists\mathcal O_{\mathrm{abs}}\;
\forall x[
\operatorname{Real}(x)
\Longleftrightarrow
\operatorname{Generated}^{*}_{\mathrm{abs}}
(\mathcal O_{\mathrm{abs}},x)
].
$$

Ésta no es analítica: puede haber una pluralidad exhaustiva de cosas reales sin que todas deriven de una base ontológica común.

Por tanto quedan separados:

$$
\boxed{
\text{exhaustividad extensional}
\neq
\text{unidad genealógica ontológica}.
}
$$

Un operador de cierre solo tiene fuerza ontológica para $R$ si sus reglas generativas se justifican independientemente de la totalidad que pretende producir. La mera identidad formal:

$$
R=F(R)
$$

sigue siendo, por sí sola, un corolario de clausura y no una prueba de origen común.

**Estado: la parte extensional conserva su carácter analítico; la existencia genealógica de $R$ es una tesis sustantiva abierta.**

## 3. Estado actual del programa emergentista

La propuesta ya dispone de una definición independiente y event-local de emergencia, un operador system-relative construido desde ella, pruebas de F1–F3 dentro de ese tipo y un punto fijo propio explícito.

Por tanto, REV-01, REV-02 y REV-04 están cerrados en sus criterios originales, mientras REV-03 permanece PARTIAL por alcance doctrinal.

El programa dispone de dos construcciones semánticas condicionales. La ruta finita usa el régimen candidato $[q]_{\sim}$, PON y $\operatorname{StructAdm}_i$. La ruta generalizada es deliberadamente pre-ontológica: usa $T_q^{\mathcal C}$, `CFragAdm_C`, CSet/CWF/CProcStable y smallness/Separation relativas a la clausura; solo tras CS/CC/CRType puede reindexarse como un régimen. Ninguna ruta demuestra por sí sola $\operatorname{ExistsRegR}$ y, con mayor razón, tampoco $\operatorname{ExistsAbsR}$.

Los bloqueadores activos relevantes pasan a ser:

- **REV-07:** origen y clausura ontológica del régimen: justificar $\operatorname{OntOrigin}_i$, $\operatorname{GenStep}_i$ y $\operatorname{Generated}^{*}_i$; $\Lambda_*$/$\mathcal C_*$ pasan a ser reconstrucciones candidatas de esa genealogía;
- **REV-23:** PON — smallness por-token de la ruta finita; la ruta generalizada puede sustituirlo por `CSet/TransClSmall`;
- **REV-24:** puente de presentación: dado un $R_i$ genealógico justificado por REV-07, demostrar que $S_i$ lo presenta adecuadamente mediante OA/MC/RA;
- **REV-25:** smallness de la firma y legitimidad del paso por Separation sobre «actualmente verdadero»;
- **REV-20:** PSB/K1, ahora derivables de PON en la ruta estructural;
- **REV-22:** aplicabilidad de Zorn, subordinada a las premisas de smallness aunque la ruta directa a $\operatorname{SemTotal}$ no lo necesita;
- **REV-15:** consecuencias metaontológicas discriminantes;
- **REV-26:** origen ontológico común absoluto — AG para formular el target, CO$_{abs}$ para la genealogía común y scope realization como capa formal auxiliar;

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
| REV-24 | OPEN blocker doctrinal local | El máximo semántico no produce un $R_i$. REV-07 debe justificar primero una realidad genealógica $\operatorname{GeneTotal}_i(\mathcal O_i,R_i)$; REV-24 queda reducido a OA/MC/RA para demostrar $\operatorname{Presents}_i(S_i,R_i)$. Su cierre fortalece `ExistsRegR` a `WitnessedRegR`; no crea la existencia local ni implica `ExistsR`. |
| REV-25 | OPEN blocker fundacional/semántico | El teorema usa smallness de la firma y un paso de Separation sobre los hechos «actualmente verdaderos». Deben justificarse la firma/aridades y la disponibilidad metateórica del predicado de actualidad. |
| REV-26 | OPEN blocker doctrinal/metaontológico | **Origen común absoluto.** El target doctrinal ya está fijado: $R$ es la clausura de una base ontológica común, no el mero scope extensional. AG sigue abierto; APC realiza scope pero no origen; el blocker principal es CO$_{abs}$/globalización genealógica: demostrar que todo lo real pertenece a una única clausura ontológica última. REV-26e queda RESOLVED doctrinal. |

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

La existencia ontológica y su representación quedan ahora separadas:

1. **REV-07:** justificar una base/origen ontológico $\mathcal O_i$, reglas $\operatorname{GenStep}_i$ independientes y una clausura $\operatorname{Generated}^{*}_i$ que realice un $R_i$;
2. **REV-23:** justificar PON solo si se conserva la reconstrucción finita por $\Lambda_*$;
3. **REV-24:** dado un $R_i$ genealógico ya justificado, demostrar OA/MC/RA y $\operatorname{Presents}_i(S_i,R_i)$;
4. **REV-25:** justificar la smallness de firma/aridades y el predicado de actualidad usado por Separation;
5. **REV-26:** justificar, para el $R$ absoluto, una base ontológica común cuya clausura genere exactamente todo lo real.

REV-20 y REV-22 quedan como consecuencias/alternativas de las premisas de smallness. El teorema semántico directo entrega $\operatorname{SemTotal}$; la existencia local depende de REV-07 y la existencia absoluta de REV-26, no de la maximalidad semántica.

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

### Objetivo real de esta maquinaria: presentación semántica

K1–K3 producen exactamente:

$$
\boxed{\operatorname{SemTotal}_i(S_i).}
$$

Eso no establece una genealogía ontológica.

La existencia local fuerte pertenece a REV-07:

$$
\operatorname{GeneTotal}_i(\mathcal O_i,R_i)
\Rightarrow
\operatorname{ExistsRegR}.
$$

Si REV-07 ha justificado esa genealogía, REV-24 intenta demostrar:

$$
\operatorname{SemTotal}_i(S_i)
+
\mathrm{OTB}_i
\Rightarrow
\operatorname{Presents}_i(S_i,R_i),
$$

y por tanto:

$$
\boxed{
\operatorname{ExistsRegR}
+
\operatorname{SemTotal}_i(S_i)
+
\mathrm{OTB}_i
\Rightarrow
\operatorname{WitnessedRegR}.
}
$$

La maquinaria semántica no crea el origen, la clausura ni el alcance ontológico.

El paso adicional desde genealogías indexadas al $R$ absoluto pertenece a REV-26.

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

La forma tipada del resultado semántico es «existe un máximo $S_i$ y es E-closed». La existencia ontológica de $R_i$ requiere REV-07 y su genealogía:

$$
\operatorname{GeneTotal}_i(\mathcal O_i,R_i).
$$

REV-24 solo debe justificar después:

$$
\operatorname{Presents}_i(S_i,R_i).
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

## 4. Núcleo formal vigente

Esta sección contiene solo los **enunciados normativos** necesarios para auditar la propuesta. Las demostraciones completas, contraejemplos, rutas alternativas y stress tests viven en [derivaciones técnicas](work/autodescripcion-realidad-distincion-derivaciones-2026-09-22.md).

La separación es deliberada: el documento normativo no debe volver a crecer por acreción técnica.

### 4.1. Ruta A — exhaustividad semántica sobre régimen finitamente conectado

Para un token actual $q$, la ruta finita usa:

$$
T_i:=[q]_{\sim},
$$

donde $\sim$ es la clausura por caminos finitos de la relación ontológica candidata $\bowtie$.

La hipótesis local de smallness es:

$$
\mathrm{PON}:\quad
\forall q,\;
N(q)=\{r\mid q\bowtie r\}
\text{ es set-sized}.
$$

Con:

$$
\mathrm{SigSmall}_i:
\quad
\mathcal L_i\text{ es set-sized}
\land
\forall\sigma\in\mathcal L_i,\;
\operatorname{ar}(\sigma)\text{ es set-sized},
$$

y $\mathrm{ActualSep}_i$, definimos:

$$
\Phi_i^{\mathrm{all}}
=
\{
\varphi\in
\operatorname{Atoms}_{\mathcal L_i}(T_i)
\mid
\operatorname{Actual}_i(\varphi)
\},
$$

$$
S_i^*:=(T_i,\Phi_i^{\mathrm{all}}).
$$

El resultado matemático vigente es:

$$
\boxed{
\mathrm{PON}
+
\mathrm{SigSmall}_i
+
\mathrm{ActualSep}_i
+
\operatorname{StructAdm}_i
\Rightarrow
\operatorname{SemTotal}_i(S_i^*).
}
$$

Esto demuestra **exhaustividad semántica local al régimen candidato**. No demuestra $\operatorname{ExistsRegR}$ ni $\operatorname{ExistsAbsR}$.

PON pertenece solo a esta instanciación finita. No es una condición doctrinal general de existencia.

### 4.2. Ruta B — clausura integrativa generalizada pre-ontológica

Si la clausura finita es insuficiente, se permite una clausura candidata:

$$
\mathcal C_*:A\mapsto\mathcal C_*(A),
$$

generada por reglas integrativas especificadas mediante CGI/CMin sin usar $\operatorname{CoReal}$, $R_i$, $S_i$, $\operatorname{Presents}$, $\operatorname{OntTotal}$ ni el resultado final de la propia clausura.

Para un seed $q$:

$$
T_q^{\mathcal C}:=\mathcal C_*(\{q\}).
$$

Mientras CS/CC no estén justificadas, este carrier **no se denomina régimen** y no recibe índice ontológico $i$.

El teorema semántico closure-relative usa únicamente:

$$
\mathrm{CSet}
+
\mathrm{CWF}
+
\mathrm{CProcStable}
+
\mathrm{SigSmall}_{\mathcal C}
+
\mathrm{ActualSep}_{\mathcal C}.
$$

Con esas premisas se construye $S_q^{\mathcal C}$ y:

$$
\boxed{
\mathrm{CSet}
+
\mathrm{CWF}
+
\mathrm{CProcStable}
+
\mathrm{SigSmall}_{\mathcal C}
+
\mathrm{ActualSep}_{\mathcal C}
\Rightarrow
\operatorname{SemTotal}_{\mathcal C}(S_q^{\mathcal C}).
}
$$

Este teorema es deliberadamente **pre-ontológico**. No contiene $\operatorname{StructAdm}_i$, SameRegime, CS, CC ni $\operatorname{CoReal}$ entre sus premisas.

Solo después se investigan:

$$
\mathrm{CS}:\quad
x\in T_q^{\mathcal C}
\Rightarrow
\operatorname{CoReal}(x,q),
$$

$$
\mathrm{CC}:\quad
\operatorname{CoReal}(x,q)
\Rightarrow
x\in T_q^{\mathcal C},
$$

junto con CRType y la realización de scope. Si esas obligaciones se cierran, la construcción puede reindexarse como $S_i^{\mathcal C}$.

FID es solamente una condición suficiente de la Ruta A; un fallo de FID no implica $\neg\operatorname{ExistsRegR}$ ni $\neg\operatorname{ExistsAbsR}$.

### 4.3. REV-24 — presentación semántica de una realidad genealógica

$S_i$ y $R_i$ son tipos distintos, y la nueva definición genealógica separa además **existencia ontológica** de **presentación semántica**.

REV-07 debe justificar primero alguna:

$$
\operatorname{GeneTotal}_i(\mathcal O_i,R_i).
$$

REV-24 pregunta después si un máximo semántico $S_i$ presenta adecuadamente esa realidad.

#### REV-24a — Ontological Anchoring (OA)

$$
\mathrm{OA}_i(S;\mathcal O_i):
\quad
\forall a\in T_S\;
\exists x[
\operatorname{Generated}^{*}_i(\mathcal O_i,x)
\land
\operatorname{Den}_i(a,x)
].
$$

OA impide que el carrier semántico sobreincluya contenido ajeno a la genealogía.

En Ruta A, una vez justificado que $\Lambda_*$ reconstruye la clausura genealógica y usando denotación canónica, la antigua obligación RS se reinterpreta como soundness respecto de $\operatorname{Generated}^{*}_i$.

#### REV-24b — Membership Completeness (MC)

$$
\mathrm{MC}_i(S;\mathcal O_i):
\quad
\forall x[
\operatorname{Generated}^{*}_i(\mathcal O_i,x)
\Rightarrow
\exists a\in T_S\;
\operatorname{Den}_i(a,x)
].
$$

MC impide que $S_i$ omita contenido de la clausura ontológica.

En Ruta A, RC se reinterpreta como:

$$
\operatorname{Generated}^{*}_i(\mathcal O_i,x)
\Rightarrow
x\in[q]_{\sim}.
$$

En Ruta B, CC se reinterpreta como:

$$
\operatorname{Generated}^{*}_i(\mathcal O_i,x)
\Rightarrow
x\in T_q^{\mathcal C}.
$$

FID sigue siendo únicamente una vía suficiente para la implementación finita.

#### REV-24c — Representational Adequacy (RA)

$\mathrm{RA}_i(S,R_i)$ debe garantizar que la presentación preserva y refleja no solo miembros, sino la estructura genealógica/procesual relevante:

- identidades;
- relaciones de generación;
- dependencias constitutivas relevantes;
- procesos que mantienen la clausura;
- invariancia bajo recodificaciones fieles.

RA permanece OPEN y debe coordinarse con REV-25.

#### REV-24d — Scope Realization

El finding histórico REV-24d queda **MOVED/SUPERSEDED como parte del puente semántico**. La realización de scope ya no es algo que $S_i$ deba producir: forma parte de establecer $\operatorname{GeneTotal}_i(\mathcal O_i,R_i)$ en REV-07.

La ruta plural sigue siendo una posible formalización no reificante del alcance:

$$
\exists rr_i\;
\forall x[
x\prec rr_i
\Longleftrightarrow
\operatorname{Generated}^{*}_i(\mathcal O_i,x)
],
$$

condicionada a la lógica plural adoptada.

#### Esquema OTB local revisado

El objetivo de REV-24 pasa a ser:

$$
\boxed{
\operatorname{GeneTotal}_i(\mathcal O_i,R_i)
+
\operatorname{SemTotal}_i(S_i)
+
\mathrm{OA}_i(S_i;\mathcal O_i)
+
\mathrm{MC}_i(S_i;\mathcal O_i)
+
\mathrm{RA}_i(S_i,R_i)
\Rightarrow
\operatorname{Presents}_i(S_i,R_i).
}
$$

Por tanto REV-24 **no demuestra la existencia de $R_i$**. Si REV-07 ya ha establecido $\operatorname{GeneTotal}_i$, entonces:

$$
\operatorname{ExistsRegR}
$$

ya es una conclusión ontológica; REV-24 permite fortalecerla a:

$$
\operatorname{WitnessedRegR}.
$$

Esta separación elimina definitivamente la lectura según la cual una estructura semántica «promueve» o crea ontológicamente $R_i$.

### 4.4. Ruta Zorn — resultado auxiliar

La ruta operator-free se conserva como resultado estructural auxiliar.

Sea $(\mathfrak D,\preceq)$ un poset set-sized no vacío y $\mathfrak K\subseteq\mathfrak D$. Si:

- K1: $\mathfrak K$ es cofinal en $\mathfrak D$;
- K2: toda cadena de $\mathfrak K$ tiene una cota superior en $\mathfrak K$;
- K3: $\mathfrak D$ es directed;

entonces existe $S\in\mathfrak K$ tal que:

$$
\boxed{
\forall X\in\mathfrak D,\quad
X\preceq S.
}
$$

El resultado es semántico. Zorn no proporciona $R_i$, no resuelve REV-24 y no es necesario para las dos construcciones directas anteriores cuando sus premisas de smallness están disponibles.

Para un operador extensivo e idempotente, F1 + F3 bastan para elevar cotas a puntos fijos en esta ruta concreta; F2 es redundante para ese paso. La demostración completa permanece en work/.

### 4.5. Estado normativo del núcleo formal

**Demostrado condicionalmente:**

1. Ruta A: PON + $\mathrm{SigSmall}_i$ + $\mathrm{ActualSep}_i$ + $\operatorname{StructAdm}_i$ producen $\operatorname{SemTotal}_i(S_i^*)$.
2. Ruta B: CSet + CWF + CProcStable + $\mathrm{SigSmall}_{\mathcal C}$ + $\mathrm{ActualSep}_{\mathcal C}$ producen $\operatorname{SemTotal}_{\mathcal C}(S_q^{\mathcal C})$ sin suponer todavía que la clausura sea un régimen.
3. K1–K3 producen un máximo semántico bajo las condiciones fundacionales declaradas.
4. En Ruta A, RS + CRType + CD descargan condicionalmente OA del carrier; RC + CD descargan condicionalmente MC.

**No demostrado:**

1. la existencia/adecuación de una base $\mathcal O_i$ y de su clausura ontológica —REV-07—;
2. la adecuación de $\Lambda_*$ o $\mathcal C_*$ como reconstrucción de esa genealogía;
3. REV-24c/RA y, por tanto, la presentación completa por $S_i$;
4. $\operatorname{ExistsRegR}$ sin cerrar la obligación genealógica de REV-07;
5. $\operatorname{ExistsR}$ sin CO$_{abs}$ / REV-26.

Esta separación es normativa. Cualquier detalle técnico nuevo debe incorporarse primero al documento work/; el normativo solo se amplía cuando cambie uno de estos enunciados, dependencias o estados.

---

## 5. Identidad genealógica de régimen — REV-07

La identidad de una realidad indexada queda anclada primariamente en **origen + clausura ontológica**, no en K3, maximalidad semántica ni conectividad elegida ad hoc.

### 5.1. Criterio primario

Para un índice $i$, REV-07 debe justificar:

$$
\operatorname{OntOrigin}_i(\mathcal O_i)
$$

y una relación generativa independiente:

$$
\operatorname{GenStep}_i(a,b),
$$

cuyas reglas no usan $R_i$, CoReal, SameRegime, K3, SemTotal, Presents ni la extensión final de la clausura.

La clausura genealógica es:

$$
\operatorname{Generated}^{*}_i(\mathcal O_i,x).
$$

Una realidad indexada existe cuando puede realizarse un alcance:

$$
\operatorname{GeneTotal}_i(\mathcal O_i,R_i)
$$

tal que:

$$
\forall x[
\operatorname{Within}_i(x,R_i)
\Longleftrightarrow
\operatorname{Generated}^{*}_i(\mathcal O_i,x)
].
$$

La base $\mathcal O_i$ no tiene por qué ser un único token ni un primer instante temporal. Bases distintas pueden ser representacionalmente equivalentes si generan exactamente la misma clausura.

### 5.2. Co-realidad derivada

Una vez fijada la genealogía:

$$
\operatorname{CoReal}_i(x,y)
:\Longleftrightarrow
\operatorname{Generated}^{*}_i(\mathcal O_i,x)
\land
\operatorname{Generated}^{*}_i(\mathcal O_i,y).
$$

Por tanto SameRegime deja de ser una noción obtenida por conectividad formal. La conectividad es ahora una **hipótesis de reconstrucción** de una unidad genealógica previamente caracterizada.

Para dominios procesuales:

$$
\operatorname{SameRegime}(X,Y)
$$

significa que los tokens ontológicos representados por ambos pertenecen a la misma clausura genealógica.

Esto sigue sin implicar K3:

$$
\boxed{
\operatorname{SameRegime}(X,Y)
\not\Rightarrow
K3_i(X,Y).
}
$$

La identidad ontológica y la amalgamabilidad semántica continúan separadas.

### 5.3. Ruta A — reconstrucción mediante $\Lambda_*$

La familia pre-régimen:

$$
\Lambda_*
$$

se conserva como implementación candidata, pero ya no define CoReal por decreto.

Sus tipos de enlace deben seguir cumpliendo:

1. actualidad;
2. carácter ontológico;
3. sensibilidad token-specific;
4. rol generativo/integrador;
5. independencia respecto de $R_i$/SameRegime;
6. invariancia bajo recodificación fiel.

La clausura finita:

$$
[q]_{\sim}
$$

es adecuada solo si reconstruye la genealogía:

$$
\mathrm{RS}_{\Lambda}^{\mathrm{gen}}:
\quad
x\in[q]_{\sim}
\Rightarrow
\operatorname{Generated}^{*}_i(\mathcal O_i,x),
$$

y:

$$
\mathrm{RC}_{\Lambda}^{\mathrm{gen}}:
\quad
\operatorname{Generated}^{*}_i(\mathcal O_i,x)
\Rightarrow
x\in[q]_{\sim}.
$$

FID + LA sigue siendo una vía suficiente hacia RC para esta ruta, no una verdad doctrinal general.

### 5.4. Ruta B — clausura generativa generalizada

Si la genealogía no admite reconstrucción por caminos finitos, la clausura candidata:

$$
\mathcal C_*
$$

debe generarse mediante reglas independientes CGI/CMin.

La adecuación ontológica se reescribe:

$$
\mathrm{CS}^{\mathrm{gen}}:
\quad
x\in T_q^{\mathcal C}
\Rightarrow
\operatorname{Generated}^{*}_i(\mathcal O_i,x),
$$

$$
\mathrm{CC}^{\mathrm{gen}}:
\quad
\operatorname{Generated}^{*}_i(\mathcal O_i,x)
\Rightarrow
x\in T_q^{\mathcal C}.
$$

La Ruta B puede incorporar reglas globales, de límite o transfinitas si se justifican sin usar la clausura final como premisa.

### 5.5. Directedness sigue siendo posterior

Con:

$$
\operatorname{Adm}_i:=\operatorname{StructAdm}_i,
$$

y una vez fijada legítimamente la genealogía del régimen, la unión semántica positiva de dos fragmentos del mismo régimen proporciona una cota común; por tanto se deriva:

$$
\boxed{K3_i.}
$$

Así K3 no individua el régimen: es una propiedad del poset semántico **después** de que REV-07 haya justificado la genealogía.

### 5.6. Scope realization

La realización no reificante de:

$$
\operatorname{Generated}^{*}_i(\mathcal O_i,-)
$$

puede expresarse pluralmente:

$$
\exists rr_i\;
\forall x[
x\prec rr_i
\Longleftrightarrow
\operatorname{Generated}^{*}_i(\mathcal O_i,x)
].
$$

Esta instancia sigue dependiendo de la lógica plural/scope adoptada. El finding histórico REV-24d se mueve aquí: la realización de alcance pertenece a la existencia ontológica de $R_i$, no a su presentación por $S_i$.

### 5.7. Qué sigue abierto

REV-07 permanece **PARTIAL**. Para cerrarlo hay que justificar:

1. qué cuenta como $\operatorname{OntOrigin}_i$ sin definirlo como «lo que genera $R_i$»;
2. qué relaciones cuentan como $\operatorname{GenStep}_i$;
3. cómo se construye $\operatorname{Generated}^{*}_i$ sin circularidad;
4. si la base/origen debe satisfacer minimalidad, irredundancia o alguna forma de prioridad;
5. cómo tratar bases múltiples que generan la misma clausura;
6. qué ruta —$\Lambda_*$ finita o $\mathcal C_*$ generalizada— reconstruye adecuadamente esa genealogía;
7. qué principio de scope/pluralidad realiza la clausura sin setificarla.

**Estado: PARTIAL — REV-07. La existencia de $R_i$ se concentra aquí; REV-24 queda reservado a la presentación semántica de un $R_i$ ya justificado.**

## 6. Genealogía absoluta, generalidad y No-$R$ — REV-26

REV-26 ya no pregunta si puede formarse la mera pluralidad de todo lo real. Esa pluralidad corresponde a $\mathcal R_{\mathrm{ext}}$.

La cuestión doctrinal es:

> ¿existe una base/origen ontológico común cuya clausura genere exactamente todo lo real?

### 6.1. REV-26e — decisión doctrinal

**RESOLVED.**

La lectura minimalista:

$$
R=\operatorname{Scope}(\operatorname{Real})
$$

queda SUPERSEDED como target completo.

El concepto se conserva como:

$$
\mathcal R_{\mathrm{ext}}.
$$

El $R$ doctrinal exige unidad genealógica:

$$
R
=
\operatorname{Scope}
\bigl(
\operatorname{Cl}^{\mathrm{ont}}
(\mathcal O_{\mathrm{abs}})
\bigr).
$$

Esta propiedad no se introduce para hacer no trivial la prueba: expresa el criterio doctrinal elegido de qué cuenta como una Realidad.

### 6.2. REV-26a — AG: generalidad absoluta

AG sigue siendo necesaria para que:

$$
\forall x\;\operatorname{Real}(x)
$$

tenga la lectura de **absolutamente todo lo real**.

AG no postula una colección universal. Es una tesis sobre alcance cuantificacional.

Sin AG, la afirmación «la clausura de $\mathcal O_{\mathrm{abs}}$ contiene todo lo real» no tiene una única lectura absoluta y debe sustituirse por una semántica indexada/metalingüística.

**Estado: OPEN.**

### 6.3. Alcance extensional y APC$_{Real}$

La comprensión plural absoluta:

$$
\mathrm{APC}_{Real}:
\quad
(\exists x\,\operatorname{Real}(x))
\Rightarrow
\exists rr_{\mathrm{ext}}\;
\forall x[
x\prec rr_{\mathrm{ext}}
\Longleftrightarrow
\operatorname{Real}(x)
]
$$

realiza $\mathcal R_{\mathrm{ext}}$ en una semántica plural clásica.

Por tanto, bajo AG:

$$
\mathrm{AG}
+
\mathrm{APC}_{Real}
+
\operatorname{NonEmptyReality}
\Rightarrow
\operatorname{ExistsExtScope}.
$$

Pero ahora queda explícito:

$$
\boxed{
\operatorname{ExistsExtScope}
\not\Rightarrow
\operatorname{ExistsR}.
}
$$

APC$_{Real}$ resuelve, como mucho, la **realización extensional** del alcance. No demuestra origen común ni clausura generativa.

REV-26b permanece PARTIAL como cuestión lógica/fundacional de scope, pero deja de ser el núcleo ontológico de la existencia de $R$.

### 6.4. REV-26c — Common-Origin / Genealogical Globalization Bridge

Definimos la tesis de origen absoluto común:

$$
\mathrm{CO}_{\mathrm{abs}}:
\quad
\exists\mathcal O_{\mathrm{abs}}\;
[
\operatorname{OntOrigin}_{\mathrm{abs}}
(\mathcal O_{\mathrm{abs}})
\land
\forall x(
\operatorname{Real}(x)
\Longleftrightarrow
\operatorname{Generated}^{*}_{\mathrm{abs}}
(\mathcal O_{\mathrm{abs}},x)
)
].
$$

Éste es el blocker ontológico principal de REV-26.

La dirección:

$$
\operatorname{Generated}^{*}_{\mathrm{abs}}
(\mathcal O_{\mathrm{abs}},x)
\Rightarrow
\operatorname{Real}(x)
$$

es **soundness genealógica**: la clausura no fabrica contenido ontológicamente espurio.

La dirección:

$$
\operatorname{Real}(x)
\Rightarrow
\operatorname{Generated}^{*}_{\mathrm{abs}}
(\mathcal O_{\mathrm{abs}},x)
$$

es **exhaustividad genealógica**: nada real queda fuera de la genealogía común.

Además, las reglas de $\operatorname{Generated}^{*}_{\mathrm{abs}}$ deben satisfacer independencia generativa: no pueden definirse como «las reglas necesarias para alcanzar todo lo real».

### 6.5. Globalización desde genealogías indexadas

Si existen:

$$
\operatorname{GeneTotal}_i(\mathcal O_i,R_i)
$$

para varios índices, eso no produce automáticamente $\mathrm{CO}_{\mathrm{abs}}$.

Una ruta válida de globalización debe justificar una base superior:

$$
\mathcal O_{\mathrm{abs}}
$$

tal que las genealogías indexadas sean subclausuras o derivados de su clausura:

$$
\forall i\;
\operatorname{Cl}^{\mathrm{ont}}_i(\mathcal O_i)
\preceq_{\mathrm{gen}}
\operatorname{Cl}^{\mathrm{ont}}_{\mathrm{abs}}
(\mathcal O_{\mathrm{abs}}).
$$

Esta relación de inclusión genealógica no puede definirse meramente como inclusión extensional de scopes. Debe conservar la dependencia/origen relevante.

Si no existe ninguna base superior admisible, tenemos un candidato a Many-$R$ fuerte.

### 6.6. Scope realization del $R$ genealógico

Una vez justificada $\mathrm{CO}_{\mathrm{abs}}$, una instancia adecuada de comprensión plural puede realizar el alcance generado:

$$
\exists rr_{\mathrm{abs}}\;
\forall x[
x\prec rr_{\mathrm{abs}}
\Longleftrightarrow
\operatorname{Generated}^{*}_{\mathrm{abs}}
(\mathcal O_{\mathrm{abs}},x)
].
$$

Bajo $\mathrm{CO}_{\mathrm{abs}}$, este scope coincide extensionalmente con $\mathcal R_{\mathrm{ext}}$, pero la igualdad extensional **no borra la diferencia explicativa**:

- $\mathcal R_{\mathrm{ext}}$ se caracteriza por ser todo lo real;
- $R$ se caracteriza por ser la clausura de una genealogía ontológica común.

Por tanto:

$$
\boxed{
\mathrm{AG}
+
\mathrm{CO}_{\mathrm{abs}}
+
\mathrm{ScopeRealization}_{\mathrm{abs}}
\Rightarrow
\operatorname{ExistsR}.
}
$$

El contenido sustantivo está en $\mathrm{CO}_{\mathrm{abs}}$ y en la adecuación de la clausura, no en la mera formación plural del scope.

### 6.7. REV-26d — No-$R$

Bajo AG, la negación doctrinal es ahora:

$$
\operatorname{NoR}_{\mathrm{AG}}
:=
\neg
\exists\mathcal O_{\mathrm{abs}},R_{\mathrm{abs}}\;
\operatorname{AbsGeneTotal}
(\mathcal O_{\mathrm{abs}},R_{\mathrm{abs}}).
$$

Equivalentemente, puede fallar porque:

1. no existe origen/base absoluta admisible;
2. existe una base candidata pero su clausura no es sound;
3. existe una base candidata pero su clausura no es exhaustiva respecto de todo lo real;
4. la realización de scope requerida por la formalización adoptada falla.

Si AG se rechaza, No-$R$ no debe formularse fingiendo un cuantificador absoluto. Se conserva la alternativa metalingüística NoAbsFinality: toda interpretación candidata de cierre genealógico admite una expansión ontológicamente legítima que no queda absorbida por su genealogía.

### 6.8. Estado de REV-26

- **REV-26a / AG:** OPEN.
- **REV-26b / scope realization / APC:** PARTIAL y auxiliar; ya no decide la existencia sustantiva.
- **REV-26c / CO$_{\mathrm{abs}}$ + genealogical globalization:** OPEN y blocker ontológico principal.
- **REV-26d / No-$R$ semantics:** OPEN.
- **REV-26e / target doctrinal:** RESOLVED — $R$ es una unidad genealógica ontológicamente cerrada, no el mero alcance extensional.

Por tanto:

$$
\boxed{
\operatorname{ExistsRegR}
\not\Rightarrow
\operatorname{ExistsR}
}
$$

y:

$$
\boxed{
\operatorname{ExistsExtScope}
\not\Rightarrow
\operatorname{ExistsR}.
}
$$

El objetivo fuerte queda concentrado en demostrar una genealogía ontológica común absoluta, no en demostrar que podemos formar la expresión «todo lo real».

## 7. One-$R$, Many-$R$ y niveles de exhaustividad

La distinción relevante ya no es «un scope extensional o varios». Es **una genealogía ontológica última o varias genealogías irreducibles**.

### 7.1. Relación entre $R_i$ y $S_i$

REV-07 intenta justificar primero:

$$
\operatorname{GeneTotal}_i(\mathcal O_i,R_i).
$$

Después el programa semántico puede construir:

$$
S_i
$$

y REV-24 intenta establecer:

$$
\operatorname{Presents}_i(S_i,R_i).
$$

Por tanto:

$$
R_i
\not\equiv
S_i,
$$

y la existencia de $R_i$ no depende de que $S_i$ sea construido antes.

La arquitectura vigente es:

$$
\boxed{
\mathcal O_i
\xrightarrow{\operatorname{Cl}^{\mathrm{ont}}}
R_i
\xleftarrow{\operatorname{Presents}_i}
S_i.
}
$$

La flecha izquierda es ontológica/generativa; la derecha es semántica/representacional.

### 7.2. One-$R$ fuerte

One-$R$ fuerte exige:

$$
\exists\mathcal O_{\mathrm{abs}}
$$

tal que:

$$
\forall x[
\operatorname{Real}(x)
\Longleftrightarrow
\operatorname{Generated}^{*}_{\mathrm{abs}}
(\mathcal O_{\mathrm{abs}},x)
].
$$

No exige que todos los contenidos estén causalmente conectados entre sí ni que exista un único camino local entre cualesquiera dos. Dos regiones causalmente aisladas pueden pertenecer al mismo $R$ si derivan de la misma base ontológica.

Tampoco exige unicidad literal de la representación del origen. Puede haber dos bases:

$$
\mathcal O,\mathcal O'
$$

que sean ontológicamente equivalentes para este propósito si generan exactamente la misma clausura. La unicidad relevante es la de la **genealogía/clausura última**, no necesariamente la de una descripción particular de su base.

### 7.3. Indexed-$R$ y Many-$R$ fuerte

Indexed-$R$ significa que existen una o más genealogías locales:

$$
\operatorname{GeneTotal}_i(\mathcal O_i,R_i)
$$

sin haber demostrado todavía un origen común absoluto.

Many-$R$ fuerte requiere más:

$$
\exists i\neq j
$$

con genealogías últimas $R_i,R_j$ y:

$$
\neg\exists\mathcal O_k
$$

tal que una clausura genealógica admisible de $\mathcal O_k$ integre a ambas preservando su estructura de derivación.

Así:

$$
\boxed{
R_i\parallel_{\mathrm{causal}}R_j
\not\Rightarrow
\text{Many-}R.
}
$$

y también:

$$
\boxed{
\text{existencia de }\mathcal R_{\mathrm{ext}}
\not\Rightarrow
\text{One-}R.
}
$$

El scope extensional de todo lo real puede existir incluso si las cosas reales pertenecen a genealogías ontológicas últimas distintas.

### 7.4. Cluster-$R$

Cluster-$R$ es una situación provisional: varias genealogías consideradas inicialmente independientes resultan tener una base ontológica superior común.

Si:

$$
\operatorname{Cl}^{\mathrm{ont}}_i(\mathcal O_i)
$$

y:

$$
\operatorname{Cl}^{\mathrm{ont}}_j(\mathcal O_j)
$$

son ambas derivables de:

$$
\mathcal O_k,
$$

entonces el candidato correcto a realidad más amplia es:

$$
R_k
=
\operatorname{Scope}
(
\operatorname{Cl}^{\mathrm{ont}}_k(\mathcal O_k)
).
$$

### 7.5. Retirada de «Verdad Absoluta indexada»

La fórmula histórica:

$$
\operatorname{VA}(o)=R_i
$$

permanece **SUPERSEDED**.

Un máximo semántico interno puede denominarse:

$$
\operatorname{Truth}_i,
$$

pero:

$$
\operatorname{Truth}_i
\neq
R_i
$$

y:

$$
\operatorname{Truth}_i
\neq
\operatorname{Truth}_{\mathrm{abs}}
$$

por mera definición.

La cuestión absoluta depende ahora de la genealogía de REV-26, no del número de máximos semánticos.

### 7.6. Consecuencia para los índices

Los índices $i$ no se fabrican a partir de K3 ni de máximos semánticos. Deben corresponder a genealogías ontológicas justificadas por REV-07.

La pregunta primaria pasa a ser:

> ¿qué base ontológica y qué reglas de generación hacen que ciertos contenidos pertenezcan a la misma clausura genealógica?

Y solo después:

> ¿qué estructura semántica $S_i$ presenta adecuadamente esa realidad?

**Estado:** la teoría emergentista/semántica local sigue siendo neutral respecto de One-$R$/Many-$R$ hasta que REV-07 y REV-26 resuelvan la estructura genealógica.

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
\exists\mathcal O_i\exists R_i\;
\operatorname{GeneTotal}_i(\mathcal O_i,R_i).
}
$$

Y, aun suponiendo una genealogía ontológica ya justificada:

$$
\operatorname{SemTotal}_i(S_i)
\not\Rightarrow
\operatorname{Presents}_i(S_i,R_i).
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

Pero ese paso **no es**:

$$
K1_i+K2_i+K3_i
\Rightarrow
\exists R_i.
$$

La existencia de $R_i$ requiere una genealogía de REV-07. REV-24/$\mathrm{OTB}_i$ entra solo después para justificar que $S_i$ presenta ese $R_i$.

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
- existe o no existe una genealogía $\operatorname{GeneTotal}_i(\mathcal O_i,R_i)$ y, si existe, $S_i$ la presenta o no adecuadamente;
- existen otras genealogías $R_j$ si REV-07 las justifica, con independencia de que sus presentaciones semánticas cierren REV-24;
- existe o no existe un $R_{\mathrm{abs}}$.

Nada de ello resta valor lógico a una demostración condicional de $\exists S_i\;\operatorname{SemTotal}_i(S_i)$. Tampoco sustituye la justificación genealógica de REV-07 ni la adecuación representacional de REV-24.

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
