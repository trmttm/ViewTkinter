import interface_tk as intf
from interface_tk import widget_model as wm


def create_view_model_search_popup(toplevel, entry, tree):
    r1_c0 = (((1,), (1,)), ((0,), (1,)))
    r0_c0 = (((0,), (1,)), ((0,), (1,)))
    frame = 'frame_0'
    frame_tree = 'frame_tree'
    view_model = [
        wm('root', toplevel, 'toplevel', 0, 0, 0, 0, 'nsew', **intf.top_level_options('Search', (500, 300))),
        wm(toplevel, frame, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*r1_c0)),
        wm(frame, entry, 'entry', 0, 0, 0, 0, 'new', **intf.entry_options(None, True)),
        wm(frame, frame_tree, 'frame', 1, 1, 0, 0, 'nsew', **intf.frame_options(*r0_c0)),
        wm(frame_tree, tree, 'treeview', 0, 0, 0, 0, 'nsew', ),
    ]
    return view_model
