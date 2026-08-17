# Formal model status for v0.1.0

The formal analytical model in `sistema_analitico_exergico.json` is preserved from the recovered complete pre-canonical Exergism corpus. Version `0.1.0` exposes rather than silently resolves ambiguities found during adversarial review.

## Known ambiguity: transition `a*` weights

In `modulacion_por_contexto.transicion.pesos`, the recovered values `a1..a5` sum to **0.90**, while the corresponding `a*` groups in the other recovered contexts sum to `1.00`.

The recovered corpus does not establish whether `0.90` is intentional scaling or a historical omission/typo. Therefore implementations **MUST NOT** silently renormalize the values or invent the missing `0.10`. A calculation using this profile should identify the exact recovered values and, where material, sensitivity-test plausible alternatives.

## Known ambiguity: `z1` and `z2`

The macroevent aggregation formulas use `z1` and `z2`:

- `E_i_adj_M` applies `z1 * MAX_i(P_atr_i)`;
- `M_f_M` applies `z2 * MAX_i(M_f_i * P_atr_i)`.

No canonical numerical values for `z1` or `z2` are present in the recovered corpus. Implementations **MUST NOT** silently default them. Those aggregate formulas are numerically under-specified until an explicit parameter profile supplies the values.

## Parameter discipline

More generally, contextual weights and temporal factors are analytical assumptions, not universal constants merely because suggested values exist in the corpus. Implementations should record the parameter profile, uncertainty and sensitivity relevant to a result.

These notes do not modify the recovered formulas or weights. They make their current epistemic/formal status explicit so later doctrinal work can address them through an auditable change.
