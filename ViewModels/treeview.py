import interface_tk as intf


def tree_view(frame_id, tree_id='tree_id') -> list:
    f = intf.widget_model
    view_model = [
        f(frame_id, tree_id, 'treeview', 0, 0, 0, 0, 'nsew', ),
    ]
    return view_model
