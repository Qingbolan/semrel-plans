/** Escaped, lossless EAL highlighting; compilation remains the reader's responsibility. */
const EalCode = (() => {
  const escape = text => text.replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const rules = [
    ['comment', /\/\/[^\r\n]*/y],
    ['string', /"(?:\\[\s\S]|[^"\\])*"/y],
    ['keyword', /\b(?:mission|call|emit|on|with|let|timeout|retries|on_failure|optional|kind|value|abort|skip|retry|continue)\b/y],
    ['boolean', /\b(?:true|false)\b/y],
    ['number', /\b\d+(?:\.\d+)?\b/y],
    ['type', /\b[A-Za-z_][\w]*\.output\b/y],
    ['property', /\b[A-Za-z_][\w]*(?=\s*=)/y],
    ['punctuation', /[{}()[\],.=]/y],
    ['', /\s+|[A-Za-z_][\w]*/y],
  ];
  function highlight(source,selectedLine=-1){
    const lines=[''];let offset=0;
    while(offset<source.length){
      let value=source[offset],type='';
      for(const [name,pattern] of rules){pattern.lastIndex=offset;const match=pattern.exec(source);if(match){value=match[0];type=name;break;}}
      value.split('\n').forEach((part,i)=>{if(i)lines.push('');lines[lines.length-1]+=type&&part?`<span class="token ${type}">${escape(part)}</span>`:escape(part);});offset+=value.length;
    }
    return lines.map((line,i)=>`<span class="source-line${i===selectedLine?' highlight':''}"${i===selectedLine?' id="source-target"':''}>${line}</span>`).join('\n');
  }
  return {highlight};
})();
