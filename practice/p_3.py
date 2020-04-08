from p_2 import Graph, Vertex

path = ['A', 'B', 'D', 'E', 'F', 'C']


def knight_tour(n, path, u, limit):
    u.set_color('gray')
    path.append(u)
    if n < limit:
        nbr_list = list(u.get_connections())
        i = 0
        done = False
        while i < len(nbr_list) and not done:
            if nbr_list[i].getColor() == 'white':
                done = knight_tour(n + 1, path, nbr_list[i], limit)
            i = i + 1
        if not done:  # prepare to backtrack
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done


knight_tour(0, path, 'A', 6)
# def knight_graph(bd_size):
#     kt_graph = Graph()
#     for row in range(bd_size):
#         for col in range(bd_size):
#             node_id = pos_to_nod_id(row, col, bd_size)
#             new_positions = gen_legal_moves(row, col, bd_size)
#             for e in new_positions:
#                 nid = pos_to_node_id(e[0], e[1], bd_size)
#                 kt_graph.add_edge(node_id, nid)
#
#     return kt_graph
#
#
# def gen_legal_moves(x, y, bd_size):
#     new_moves = []
#     move_off_sets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
#                      (1, -2), (1, 2), (2, -1), (2, 1)]
#
#     for i in move_off_sets:
#         new_x = x + i[0]
#         new_y = y + i[1]
#         if legal_coord(new_x, bd_size) and legal_coord(new_y, bd_size):
#             new_moves.append((new_x, new_y))
#
#     return new_moves
#
#
# def legal_coord(x, bd_size):
#     if 0 <= x < bd_size:
#         return True
#     else:
#         return False
