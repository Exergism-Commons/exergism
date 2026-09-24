# Arqueología conceptual de PR #12 — rescate, linaje y estado vigente

**Fecha de consolidación:** 2026-09-25  
**Ámbito:** `doctrine/reality-self-description-distinction` / PR #12  
**Propósito:** impedir que una reformulación posterior haga parecer descartado trabajo anterior que en realidad fue absorbido, restringido o reasignado a otra capa.

Este documento **no es normativo**. El orden de autoridad sigue siendo:

1. `docs/proposals/autodescripcion-realidad-distincion.md`;
2. `docs/proposals/autodescripcion-realidad-distincion-review-ledger.md`;
3. derivaciones técnicas;
4. este mapa arqueológico.

La regla de mantenimiento es:

> ningún concepto histórico debe quedar simplemente “olvidado”: debe constar como **ACTIVE CORE**, **ACTIVE SUPPORT**, **CONDITIONAL ROUTE**, **SUPERSEDED** o **OPEN DEBT**, con un descendiente actual o una razón explícita de abandono.

---

## 1. Mapa ejecutivo de linajes

| Concepto histórico | Función original | Descendiente vigente | Estado actual |
|---|---|---|---|
| Autodescripción interna vs realidad | Evitar confundir modelo y realidad | `Presents_i`, REV-24, WitnessCovariance | **ACTIVE CORE** |
| Supramedio | Medio envolvente/global del que emergería cierre | host realization, SharedOntSpace, ContextEmbedding | **SUPERSEDED como primitivo; RESCUED estructuralmente** |
| ε / emergencia | Novedad organizacional y capacidad nueva | REV-03 + EpsilonAlignment + XR-ε | **ACTIVE CORE** |
| (R=F(R)) | Identificar realidad con cierre emergente | (F_M), `EClosed`, `SemTotal` | **SUPERSEDED ontológicamente; ACTIVE SUPPORT semántico** |
| Monotonía F2 como requisito de Zorn | Elevar cotas a fixed points | F1+F3 bastan | **SUPERSEDED** |
| Inhibición como contraejemplo a F2 | Mostrar no-monotonía | distinción entre sistemas (M
eq M') | **RESOLVED / ACTIVE SUPPORT** |
| C1 locality / compactness / colimits | Salvar cotas de cadenas | source-local EClosed; direct-limit solo auxiliar | **PARTIALLY RESCUED** |
| (Omega_infty) | Obstrucción no compacta | ninguna obligación vigente directa | **RETIRED** |
| Muro de singularidad | Límite epistemológico | InterfaceWall + REV-15 strong Muro | **ACTIVE OPEN DEBT** |
| REC | Certificación enigmática de totalidad | consecuencia posterior a RegimeTotal | **ACTIVE DOWNSTREAM** |
| VA(o)=R_i | Verdad Absoluta indexada | Truth_i + translation discipline | **SUPERSEDED** |
| Many-R | Pluralidad de realidades | REV-26 / typed metaontology | **ACTIVE NON-BLOCKING** |
| Cluster-R | Colapso/agrupación de candidatos | SharedOntSpace / ContextGenesis / pre-index diagnosis | **RESCUED / REFINED** |
| ManyMany-R | estrato superior estable de pluralidades | ninguno | **RETIRED** |
| No-R | alternativa absoluta | metasentence `NoR := not ExistsR`; NQ | **ACTIVE CORE** |
| Generalidad absoluta | cuantificar sobre todo | meta-quantification + REV-26a deferred | **DEFERRED** |
| Maximal closure / Zorn | Obtener totalidad | SemTotal route only | **CONDITIONAL SUPPORT** |
| Actualidad vs posibilidad | evitar convertir posibilidades en hechos | actual events, OnticRealization, NFA | **ACTIVE CORE** |
| Metaemergencia | emergencia de posibilidades/capacidades | no target vigente independiente | **RETIRED/UNSCOPED** |
| Proceso / branching | continuidad no snapshot | process fragments, ε, Interface traces, ContinuationProfile | **ACTIVE CORE** |
| Fractalidad | autosimilitud multiescalar | Cellular Reality + nesting + generation | **SUPERSEDED como inferencia; metaphor only** |
| Common-Ground Principle | colapsar candidatos por integración | countermodel; SharedOntSpace/Genesis split | **REFUTED como regla general** |
| (Omega_i) como ancla previa | identidad/persistencia | possible later canonicalization | **OPEN LATE OUTPUT** |
| Baking/trivialización | procesos complejos sustituidos por resultados | Interface/Memo/Bake + GenesisTrivialization | **ACTIVE CORE** |
| “No context proliferation” | evitar termostatos/caches como contextos | no-free-promotion + nested contextuality | **SUPERSEDED** |
| Witness constitutivo | certificar realidad | evidence witness vs OnticRealization | **SUPERSEDED** |
| RSP genérico | realización estructural → IA0 | εRSP para XR-ε | **NARROWED / fallback only** |

---

## 2. Fase por fase: qué murió y qué sobrevivió

### Fase 1 — autodescripción y distinción

**Sobrevive intacto el problema original**: un modelo interno o una representación no debe convertirse en aquello que representa.

Descendientes directos:

[
S_i
eq R_i,
qquad
operatorname{Presents}_i(S_i,R_i),
]

y, más tarde:

[
chi
eqarrho
eq C
]

para separar evidence witness, realization y contexto.

**Clasificación:** ACTIVE CORE.

### Fase 2 — supramedio, ε y primer cierre

Aquí hubo tres ideas distintas que después se mezclaron históricamente.

#### A. Supramedio

El supramedio como único medio envolvente con papel fundacional ya no participa en la arquitectura. Su función se descompuso en:

- host / realization layer;
- SharedOntSpace cuando un contexto común preexiste;
- ContextEmbedding para nesting;
- ContextGenesis cuando una interacción constituye un nuevo contexto.

**No debe resucitarse como un (R) global encubierto.**

#### B. Emergencia (arepsilon)

Fue rescatada casi íntegramente.

La definición event-local:

[
e=(s_0,P,s_1)inmathcal E_M
]

con actualización efectiva, Macro-invariance, OrgWitness y Enables sigue siendo válida y ahora alimenta:

[
operatorname{RealizedEmergence}
	o
arepsilon RSP
	o
IA0.
]

XR-ε reutiliza el toy path→cycle original **sin redefinir ε**.

**Clasificación:** ACTIVE CORE.

#### C. (R=F(R))

La identificación ontológica fue abandonada. Lo que sobrevivió fue el operador system-relative:

[
F_M
]

y luego:

[
operatorname{EClosed},
quad
operatorname{SemTotal}.
]

Su función actual es **semántica/presentacional**, no creadora de existencia.

**Clasificación:** SUPERSEDED ontológicamente / ACTIVE SUPPORT semántico.

---

## 3. La ruta emergentista semántica no debe confundirse con ExistsR

El arco:

[
mathcal E_M
	o
F_M
	o
EClosed
	o
SemTotal
]

resuelve preguntas sobre cierre y exhaustividad **dentro de un régimen ya tipado**.

El arco de existencia actual es distinto:

[
arepsilon	ext{-event actual}
+
TR	ext{-}M
+
operatorname{OnticRealization}
	o
ContextIndividuation
	o
RegimeTotal
	o
ExistsR.
]

REV-24 queda como puente posterior:

[
RegimeTotal
+
SemTotal
+
OTB
	o
Presents
+
WitnessedR.
]

**Regla de mantenimiento:** nunca volver a usar `SemTotal` o maximalidad para crear (R_i).

---

## 4. C1, compactness y colimits: qué quedó realmente

La antigua “C1” pasó por locality, compactness y colimits. El resultado arqueológico es:

- **locality** sí sobrevivió, primero porque un evento EClosed queda determinado por su source actual y después, de forma más general, como OR8/prefix-locality;
- **StageFactorization** quedó eliminada de la prueba vigente;
- **compactness lógica** no es un teorema ontológico;
- **direct limits/colimits** solo son herramientas posibles si una futura ruta usa embeddings en vez de inclusión;
- (Omega_infty) no desempeña ya ningún papel vigente.

**Clasificación:** locality ACTIVE; compactness/colimits CONDITIONAL TOOL; (Omega_infty) RETIRED.

---

## 5. Actualidad, posibilidad y proceso: Fase 7 fue absorbida, no descartada

La historia antigua la marcaba como DEFERRED, pero varias de sus intuiciones son ahora centrales.

### Rescatado

- actual transition (
eq) available transition;
- proceso (
eq) snapshot;
- branching permitido sin convertirlo en tesis física universal;
- estados/eventos actuales en fragmentos procesuales;
- capacidad disponible puede servir de OrgWitness sin ser actualizada;
- ContinuationProfile es dinámico y branching;
- InterfaceContract usa branching semantics;
- NFA separa modelabilidad de actualidad.

### No rescatado como tesis independiente

- meta-capacidades como nivel ontológico propio;
- potentialismo radical como refutación automática de cierre;
- branching cuántico/Everett como soporte de la ontología;
- tiempo de Planck como discretización del proceso.

**Clasificación:** process/actuality ACTIVE CORE; speculative physics RETIRED/DEFERRED.

---

## 6. Muro, REC y InterfaceWall

La genealogía conceptual correcta es:

[
	ext{Muro epistemológico temprano}
	o
	ext{separación REC/Muro}
	o
operatorname{InterfaceWall}
	o?
	ext{strong genealogical Muro}.
]

REC no es evidencia de existencia y no debe usarse para ExistsR.

InterfaceWall demuestra channel-relative underdetermination; REV-15 sigue abierto porque falta demostrar irreconstructibilidad **de principio**, no ignorancia contingente.

**Clasificación:** REC ACTIVE DOWNSTREAM; Muro ACTIVE OPEN DEBT.

---

## 7. Cluster-R, CommonGround y la arquitectura actual de integración

El viejo Cluster-R contenía una intuición correcta pero demasiado gruesa: candidatos aparentemente separados podían resultar integrables.

La descomposición vigente es:

- **SharedOntSpace:** el contexto común ya existía;
- **CommonGround:** además existe base/origen común;
- **ContextGenesis:** la interacción constituye un contexto nuevo;
- **ContextEmbedding:** un contexto local está realizado dentro de otro;
- **pre-index correction:** dos candidatos provisionalmente separados pueden resultar ser el mismo contexto.

El Common-Ground Principle fuerte fue atacado por contramodelo y **no** es regla universal.

**Clasificación:** Cluster-R RESCUED as typed split; CGP general REFUTED.

---

## 8. Fractal Reality → Cellular Reality → Generation

“Fractal” fue correctamente retirado de las inferencias por carecer de criterio matemático.

La intuición multiescalar sobrevivió de forma más precisa como:

[
	ext{nested contexts}
+
	ext{ContextEmbedding}
+
	ext{ContextGenesis}
+
operatorname{Generation}.
]

Las nuevas coordenadas son ortogonales:

[
	ext{embedding depth}

eq
	ext{generation depth}.
]

[
GenSig
]

conserva geometría genealógica sin reclamar autosimilitud fractal.

**Clasificación:** fractal inference SUPERSEDED; Cellular/Generation ACTIVE CORE.

---

## 9. (Omega_i): dos usos históricos que deben mantenerse separados

### Uso histórico fallido

[
Omega_i
	o
ContinuationProfile
	o
FaithfulContinuation.
]

SUPERSEDED.

### Uso actual permitido

[
	ext{generative structure}
+
{ContinuationProfile}
+
Bake/Prov
	o?
Omega_i.
]

Es una posible canonicalización **posterior**, nunca requisito para individuar o persistir.

GenerationSignature puede acabar formando parte de esa canonicalización, pero no se incluye por definición.

**Clasificación:** OPEN LATE OUTPUT.

---

## 10. Arcos actuales que organizan toda la PR

### A. Arco de emergencia actual

[
arepsilon
	o
RealizedEmergence
	o
arepsilon RSP
	o
IA0.
]

### B. Arco de individuación contextual

[
Ind_{mathcal T}
+
IndAdequate
	o
ContextIndividuation
	o
IndexAdmission.
]

### C. Arco genealógico de realidad

[
OntOrigin
+
OntProd
+
GenEvent
+
RegimeClosure
	o
RegimeTotal
	o
ExistsR.
]

### D. Arco de presentación semántica

[
mathcal E_i
	o
EClosed_i
	o
SemTotal_i
+
OTB_i
	o
Presents_i.
]

### E. Arco de interfaz/continuidad

[
SourceUnit
	o
InterfaceContract
	o
MemoState
	o
Bake
	o
ContinuationProfile
	o
FaithfulContinuation.
]

### F. Arco celular/generacional

[
ContextGenesis
+
ContextEmbedding
	o
nested contexts
+
Generation
+
GenSig.
]

### G. Arco de existencia fuerte

Ruta realizacional:

[
RealizedEmergence_{XR1}
+
arepsilon RSP
+
IndAdequate^{1	ext{--}10}
	o
ExistsR.
]

Ruta a priori:

[
NQ
	o?

eg NoR
	o
ExistsR.
]

NFA-T1 impide una tercera ruta puramente sintáctica que permanezca Null-compatible.

---

## 11. Deudas abiertas por capa

### Existencia / individuación

- (arepsilon)RSP sigue siendo un compromiso emergentista de suficiencia, no teorema de lógica pura.
- NQ: inadmisibilidad de Null sigue abierta.
- REV-07b/c/d siguen abiertos universalmente aunque XR-ε los descargue localmente en la instancia finita.

### Muro / reconstructibilidad

- REV-15: InterfaceWall → strong Muro.

### Canonicalización

- (Omega_i): posible output posterior.

### Presentación semántica

- REV-24 OA/MC/RA.
- REV-25 firma/Separation.
- REV-23/PON solo para la ruta finita correspondiente.
- REV-20/22 son rutas subordinadas/condicionales de smallness/maximalidad.

### Metaontología

- REV-26 One-R/Many-R y extensiones globales; no bloquea ExistsR.

---

## 12. Conceptos que no deben volver a usarse sin reapertura explícita

1. (R=F(R)) como identidad ontológica.
2. VA(o)=(R_i).
3. supramedium como totalidad global o source de reality.
4. ManyMany-R como categoría ontológica estable.
5. (Omega_infty) como blocker vigente.
6. F2 como premisa necesaria del argumento de maximalidad.
7. StageFactorization como paso oculto en K2.
8. fractalidad como consecuencia de branching/nesting.
9. Metaemergence como nivel ontológico sin nueva definición y tests.
10. witness/certificado como truthmaker.
11. “subsystem = non-context”.
12. “no context proliferation” como guard; el guard vigente es no-free-promotion.
13. Cluster-R como colector superior literal.
14. (Omega_i) como premisa de ContinuationProfile.
15. REC o Muro como premisas de ExistsR.

---

## 13. Política de arqueología a partir de ahora

Antes de introducir un nuevo término o declarar una vieja ruta “muerta”:

1. buscar su primera aparición y su última dependencia;
2. clasificarlo en una de las cinco categorías del encabezado;
3. registrar su descendiente si fue absorbido;
4. marcar SUPERSEDED junto al texto histórico si la formulación antigua puede inducir error;
5. no eliminar contraejemplos o teoremas negativos que sigan limitando rutas actuales;
6. actualizar simultáneamente normativo, ledger y este mapa cuando cambie el status;
7. si un concepto reaparece —como (arepsilon)— demostrar que se reutiliza **sin redefinirlo retrospectivamente** para obtener la conclusión deseada.

La función de este documento es precisamente evitar que una futura refactorización pierda de vista que gran parte de la arquitectura vigente es una **transformación de trabajo anterior, no una sustitución total**.
