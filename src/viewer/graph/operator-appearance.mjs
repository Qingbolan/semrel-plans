// Algebra glyphs where established; execution-only operators retain their names.
const entries = {
  FILTER:['σ','filter'], DROP_NULL:['σ','filter'], PROJECT:['π','project'],
  JOIN:['⋈','join'], LEFT_JOIN:['⟕','join'], SEMI_JOIN:['⋉','join'], ANTI_JOIN:['▷','join'], CROSS_JOIN:['×','cross'],
  AGGREGATE:['γ','aggregate'], DISTINCT:['δ','distinct'], SORT:['τ','sort'],
  UNION_ALL:['⊎','union'], UNION_DISTINCT:['∪','union'], INTERSECT:['∩','intersect'],
  SEM_FILTER:['σ','filter'], SEM_JOIN:['⋈','join'], SEM_LEFT_JOIN:['⟕','join'], SEM_AGG:['γ','aggregate'],
  SCAN:['','scan'], LIMIT:['','limit'], TAKE_FIRST:['','limit'], ARGMIN:['','sort'],
  COMPUTE:['','compute'], CTE:['','reference'], CTE_REF:['','reference'], UNNEST:['','unnest'],
  SEM_MAP:['','compute'], SEM_CLASSIFY:['','classify'], SEM_TOPK:['','sort']
};
export function operatorAppearance(type){
  const [symbol,pattern]=entries[type]||['','compute'];
  return {symbol,pattern};
}
