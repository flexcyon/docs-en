export function highlightJson(str) {
  var s = str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  return s.replace(/("(?:[^"\\]|\\.)*")|(-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?)|(\b(?:true|false|null)\b)/g,
    function(m, str, num, kw) {
      if (str !== undefined) return '<span class="s2">' + str + '</span>';
      if (num !== undefined) return '<span class="mi">' + num + '</span>';
      if (kw !== undefined) return '<span class="kc">' + kw + '</span>';
      return m;
    }
  );
}
