function Div(elem)
  --print("## Inside custom filter ##")
  --print("Attributes: ", elem.attributes)
  --print("Elem: ", pandoc.utils.stringify(elem))

  if elem.attributes['custom']=="table" then
    print("Found custom attribute!") 
    local content = pandoc.utils.stringify(elem.content)
    local options = elem.attributes['options']
    -- Workaround from https://tex.stackexchange.com/a/224096    
    return {
      pandoc.RawBlock('latex', '\\begin{figure}[' .. options .. ']\\begin{minipage}{0.5\\textwidth}\\onecolumn'),
      elem,
      pandoc.RawBlock('latex', '\\end{minipage}\\twocolumn\\end{figure}')}
  end

end



