py_escape_chars = "\"'\\{}"
re_escape_chars = '\'"\\{}()[]~$^%&*=+|:.'
bash_escape_chars = '" $&%!*?()[]{}:'
html_escape_chars = {'\'':'&rsquo;', '&':'&amp;'}

def py_escape_string(string):
	for i in py_escape_chars:
		string = string.replace(i, r'\{0}'.format(i))
	return string

def re_escape_string(string):
	for i in re_escape_chars:
		string = string.replace(i, r'\{0}'.format(i))
	return string

def bash_escape_string(string):
	for i in bash_escape_chars:
		string = string.replace(i, r'\{0}'.format(i))
	return string

def html_escape_string(string):
    for i in html_escape_chars.keys():
        if i in string:
            string = string.replace(i, html_escape_chars[i])
    return string

def escape_string(string, mode):
    if mode == 'py':
        string = py_escape_string(string)
    if mode == 're':
        string = re_escape_string(string)
    if mode == 'bash':
        string = bash_escape_string(string)
    if mode == 'html':
        string = html_escape_string(string)
    return string
