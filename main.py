import ast


def print_collector(source):
    collected_print = []
    ast_object = ast.parse(source)
    for child in ast.iter_child_nodes(ast_object):
        if isinstance(child, ast.Expr):
            if(child.value.func.id == 'print'):
                collected_print.append(child.value.func.id)
                print('print文あるけどいいの?')
    return collected_print
