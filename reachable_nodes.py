def reachables(adj_list, start_node):
    return get_reachable_nodes(adj_list, adj_list[start_node])
    
def get_reachable_nodes(adj_list, node, result = set()):
    for i in node:
        if (i in result): break
    
        result.add(i)
        result.update(get_reachable_nodes(adj_list, adj_list[i], result))
    return result
