def make_plural(s):
    if (s.endswith(('s', 'o', 'sh'))):
        return s + "es"
    elif (s.endswith('y')):
        return s[0:len(s) - 1] + "ies"
    return s + "s"


def get_hash_tag(s):
    open_pos = s.find('{')
    close_pos = s.find('}', open_pos)
    if (open_pos != -1 and close_pos != -1):
        return s[open_pos + 1:close_pos]
    return s


def tokenize(s):
    ans = []
    while (s.find('<') >= 0):
        open_pos = max(s.rfind(' ', 0, s.find('<')), 0)
        close_pos = s.find(' ', s.find('>'))
        if (close_pos <= 0):
            close_pos = len(s)
        if (open_pos != 0):
            ans += s[:open_pos].split(' ')
        substr = s[open_pos + 1:close_pos]
        ans.append((substr.replace('<', '')).replace('>', ''))
        s = s[close_pos + 1:]
    if (len(s) != 0):
        ans += s.split(' ')
    return ans
