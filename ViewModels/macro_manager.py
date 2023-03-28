import interface_tk as intf
from interface_tk import widget_model as wm


def create_macro_manager_view_model(frame, **kwargs) -> list:
    rc_0_0 = (((0,), (1,)), ((0,), (1,)))
    rc_0_1 = (((0,), (1,)), ((1,), (1,)))
    rc_0_2 = (((0,), (1,)), ((2,), (1,)))
    rc_1_0 = (((1,), (1,)), ((0,), (1,)))
    rc_0_2345 = (((0,), (1,)), ((2, 3, 4, 5), (1, 1, 1, 3)))
    fr_0 = 'fr_main_macro'

    fr_tree1 = 'tree_frame1'
    frame_middle = 'frame_middle'
    fr_tree2 = 'tree_frame2'
    fr_m_btn = 'frame_m_btn'
    btn_del_macro = kwargs['btn_del_macro']
    btn_load_macro = kwargs['btn_merge_macro']
    btn_save_macro = kwargs['btn_save_macro']
    btn_run_commands = kwargs['btn_run_commands']
    btn_run_commands_fast = kwargs['btn_run_commands_fast']
    btn_clear_commands = kwargs['btn_clear_commands']
    btn_del_commands = kwargs['btn_del_commands']
    btn_copy_commands = kwargs['btn_copy_commands']
    btn_down_command = kwargs['btn_down_command']
    btn_up_command = kwargs['btn_up_command']
    btn_set_cmd_name = kwargs['btn_set_command_name']
    btn_set_args = kwargs['btn_set_args']
    btn_set_kwargs = kwargs['btn_set_kwargs']
    btn_replace_args = kwargs['btn_replace_args']
    tree_cmds = kwargs['tree_commands']
    tree_macros = kwargs['tree_macros']
    cb_macro_mode = kwargs['check_btn_macro_mode']
    entry_macro_name = kwargs['entry_macro_name']
    btn_w = kwargs['btn_width'] if 'btn_width' in kwargs else 5
    options = intf.frame_options(*rc_0_0, propagate=False)  # Prevent treeview to change frame size
    options.update({'width': 400})  # Manually set the frame size

    fr_pw = 'frame_macro_paned_window'
    fr1 = 'fr_macro_left'
    fr2 = 'fr_macro_right'
    paned_window_options = intf.paned_window_options(False, (fr1, fr2), (3, 1))

    fr_pane_right = 'fr_pane_right'
    view_model = [
        wm(frame, fr_0, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*rc_1_0)),

        wm(fr_0, 'fr_top', 'frame', 0, 0, 0, 0, 'nswe', **intf.frame_options(*rc_0_2)),
        wm('fr_top', 'Mode', 'label', 0, 0, 0, 0, 'nw', **{'text': 'Record Macro:'}),
        wm('fr_top', cb_macro_mode, 'check_button', 0, 0, 1, 1, 'nw'),
        wm('fr_top', entry_macro_name, 'entry', 0, 0, 2, 2, 'nwe', **{'default_value': 'New Macro Name'}),
        wm('fr_top', btn_set_cmd_name, 'button', 0, 0, 3, 3, 'nsew', **{'text': 'set name', 'width': btn_w}),
        wm('fr_top', btn_set_args, 'button', 0, 0, 4, 4, 'nsew', **{'text': 'set args', 'width': btn_w}),
        wm('fr_top', btn_set_kwargs, 'button', 0, 0, 5, 5, 'nsew', **{'text': 'set kwargs', 'width': btn_w}),
        wm('fr_top', btn_replace_args, 'button', 0, 0, 6, 6, 'nsew', **{'text': 'replace args', 'width': btn_w}),

        wm(fr_0, fr_pw, 'paned_window', 1, 1, 0, 0, 'nsew', **paned_window_options),

        wm(fr1, fr_tree1, 'frame', 0, 0, 0, 0, 'nsew', **options),
        wm(fr_tree1, tree_cmds, 'treeview', 0, 0, 0, 0, 'nsew', ),
        wm(fr_tree1, 'tree_btn_frame', 'frame', 1, 1, 0, 0, 'nse', **intf.frame_options(*rc_0_2345)),
        wm('tree_btn_frame', btn_up_command, 'button', 0, 0, 0, 0, 'nsew', **{'text': '↑', 'width': 2}),
        wm('tree_btn_frame', btn_down_command, 'button', 0, 0, 1, 1, 'nsew', **{'text': '↓', 'width': 2}),
        wm('tree_btn_frame', btn_copy_commands, 'button', 0, 0, 2, 2, 'nsew', **{'text': 'Copy', 'width': btn_w}),
        wm('tree_btn_frame', btn_del_commands, 'button', 0, 0, 3, 3, 'nsew', **{'text': 'Delete', 'width': btn_w}),
        wm('tree_btn_frame', btn_clear_commands, 'button', 0, 0, 4, 4, 'nsew', **{'text': 'Clear', 'width': btn_w}),
        wm('tree_btn_frame', btn_run_commands, 'button', 0, 0, 5, 5, 'nsew', **{'text': 'Run.S', 'width': btn_w}),
        wm('tree_btn_frame', btn_run_commands_fast, 'button', 0, 0, 6, 6, 'nsew', **{'text': 'Run.F', 'width': btn_w}),

        wm(fr2, fr_pane_right, 'frame', 0, 0, 0, 0, 'nswe', **intf.frame_options(*rc_0_1)),
        wm(fr_pane_right, frame_middle, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*rc_0_1)),
        wm(frame_middle, fr_m_btn, 'frame', 0, 0, 0, 0, 'ew', **intf.frame_options(*rc_0_1)),
        wm(fr_m_btn, btn_save_macro, 'button', 0, 0, 0, 0, 'ew', **{'text': '->', 'width': 5}),
        wm(fr_m_btn, btn_load_macro, 'button', 1, 1, 0, 0, 'ew', **{'text': '<-', 'width': 5}),

        wm(fr_pane_right, fr_tree2, 'frame', 0, 0, 1, 1, 'nsew', **intf.frame_options(*rc_0_0)),
        wm(fr_tree2, tree_macros, 'treeview', 0, 0, 0, 0, 'nsew', ),

        wm(fr_tree2, 'tree_btn_frame', 'frame', 1, 1, 0, 0, 'nse', **intf.frame_options(*rc_0_2)),
        wm('tree_btn_frame', btn_del_macro, 'button', 0, 0, 0, 0, 'nsew', **{'text': 'Delete', 'width': btn_w}),

    ]
    return view_model
