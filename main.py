import ast

input_source = """

def hoge(a,b=1):
  return a+b

a = 1

print(hoge(a))
"""

ast_object = ast.parse(input_source)
print(ast.dump(ast_object))

for child in ast.iter_child_nodes(ast_object):
    if isinstance(child, ast.Expr):
        if(child.value.func.id == 'print'):
            print('print文あるけどいいの?')
