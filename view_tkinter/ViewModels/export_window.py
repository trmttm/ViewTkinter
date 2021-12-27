from .. import tk_interface as intf


def export_window(frame_id, **kwargs) -> list:
    f = intf.widget_model

    fr_names = ('General', 'Sensitivity', 'Scenario', 'Graphs', 'Dash Board')
    fr_ids = tuple(f'fr_excel_export_tab_{n}' for n in range(len(fr_names)))

    fr_0_0 = ((0,), (1,)), ((0,), (1,))
    fr_0_1 = ((0,), (1,)), ((1,), (1,))
    fr_1_0 = ((1,), (1,)), ((0,), (1,))
    fr_1_01 = ((1,), (1,)), ((0, 1,), (1, 1,))
    fr_0_01 = ((0,), (1,)), ((0, 1,), (1, 1,))
    fr_10_0 = ((10, 0,), (1,)), ((0,), (1,))

    fr_general = 'fr_general'
    fr_general_file = 'fr_gen_file_name'
    fr_general_buttons = 'fr_gen_buttons'

    fr_sensitivity = 'fr_sensitivity'
    fr_sensitivity_target_l = 'fr_sensitivity_target_left'
    fr_sensitivity_target_r = 'fr_sensitivity_target_right'
    fr_sensitivity_variables_l = 'fr_sensitivity_variables_l'
    fr_sensitivity_variable_r = 'fr_sensitivity_variable_r'
    fr_sensitivity_btn = 'fr_sensitivity_var_button'
    fr_sens_range = 'fr_sens_range'

    fr_scenario = 'fr_scenario'
    fr_graph = 'fr_graph'

    fr_dash_board = 'fr_dash_board'
    fr_dash_board_tree = 'fr_dash_board_tree'

    graph_names = (
        'Income Statement Waterfall',
        'Cash Flow Waterfall',
        'Balance Sheet Visualize',
        'DCF Waterfall',
    )

    dash_board_names = (
        'DashBoard1',
        'DashBoard2',
    )

    entry_name = get_kwargs('entry_export_file_name', kwargs) or 'entry_export_file_name'
    entry_path = get_kwargs('entry_path', kwargs) or 'entry_path'
    entry_sens_delta = get_kwargs('entry_sensitivity_delta', kwargs) or 'entry_sensitivity_delta'
    entry_sensitivity_min = get_kwargs('entry_sensitivity_min', kwargs) or 'entry_sensitivity_min'
    entry_sensitivity_increment = get_kwargs('entry_sensitivity_increment', kwargs) or 'entry_sensitivity_increment'
    entry_sensitivity_max = get_kwargs('entry_sensitivity_max', kwargs) or 'entry_sensitivity_max'
    entry_scenario_name = get_kwargs('entry_scenario_name', kwargs) or 'entry_scenario_name'

    tree_sensitivity_account_list = get_kwargs('tree_sensitivity_account_list', kwargs) or 'tree_sens_account_list'
    tree_sensitivity_target_list = get_kwargs('tree_sensitivity_target_list', kwargs) or 'tree_sensitivity_target_list'
    tree_sensitivity_input_list = get_kwargs('tree_sensitivity_input_list', kwargs) or 'tree_sensitivity_input_list'
    tree_sensitivity_variable_list = get_kwargs('tree_sensitivity_variable_list', kwargs) or 'tree_sens_variable_list'
    tree_dash_board = get_kwargs('tree_dash_board', kwargs) or 'tree_dash_board'
    tree_scenario = get_kwargs('tree_scenario', kwargs) or 'tree_scenario'
    tree_graph = get_kwargs('tree_graph', kwargs) or 'tree_graph'

    btn_path = get_kwargs('btn_path', kwargs) or 'btn_path'
    btn_sensitivity_target_add = get_kwargs('btn_sensitivity_target_add', kwargs) or 'btn_sensitivity_target_add'
    btn_sensitivity_target_remove = get_kwargs('btn_sensitivity_target_remove', kwargs) or 'btn_sens_target_remove'
    btn_sensitivity_target_up = get_kwargs('btn_sensitivity_target_up', kwargs) or 'btn_sens_target_up'
    btn_sensitivity_target_down = get_kwargs('btn_sensitivity_target_down', kwargs) or 'btn_sens_target_down'
    btn_sensitivity_variable_add = get_kwargs('btn_sensitivity_variable_add', kwargs) or 'btn_sens_var_add'
    btn_sensitivity_variable_remove = get_kwargs('btn_sensitivity_variable_remove', kwargs) or 'btn_sens_var_remove'
    btn_sensitivity_delta = get_kwargs('btn_sensitivity_delta', kwargs) or 'btn_sensitivity_delta'
    btn_scenario_name = get_kwargs('btn_scenario_name', kwargs) or 'btn_scenario_name'
    btn_fr_scenario_up = get_kwargs('btn_fr_scenario_up', kwargs) or 'btn_fr_scenario_up'
    btn_fr_scenario_down = get_kwargs('btn_fr_scenario_down', kwargs) or 'btn_fr_scenario_down'
    btn_fr_scenario_delete = get_kwargs('btn_fr_scenario_delete', kwargs) or 'btn_fr_scenario_delete'
    btn_graph_name = get_kwargs('btn_graph_name', kwargs) or 'btn_graph_name'
    btn_fr_graph_up = get_kwargs('btn_fr_graph_up', kwargs) or 'btn_fr_graph_up'
    btn_fr_graph_down = get_kwargs('btn_fr_graph_down', kwargs) or 'btn_fr_graph_down'
    btn_fr_graph_delete = get_kwargs('btn_fr_graph_delete', kwargs) or 'btn_fr_graph_delete'
    btn_dash_board_name = get_kwargs('btn_dash_board_name', kwargs) or 'btn_dash_board_name'
    btn_fr_dash_board_up = get_kwargs('btn_fr_dash_board_up', kwargs) or 'btn_fr_dash_board_up'
    btn_fr_dash_board_down = get_kwargs('btn_fr_dash_board_down', kwargs) or 'btn_fr_dash_board_down'
    btn_fr_dash_board_delete = get_kwargs('btn_fr_dash_board_delete', kwargs) or 'btn_fr_dash_board_delete'
    btn_export = get_kwargs('btn_export', kwargs) or 'btn_export'

    check_btn_input_sheet = get_kwargs('check_btn_input_sheet', kwargs) or 'check_btn_input_sheet'

    options_fr_selected_acs = intf.frame_options(*fr_1_0, propagate=False)

    view_model = [
        f(frame_id, 'export_notebook', 'notebook', 0, 0, 0, 0, 'nsew', **intf.notebook_options(fr_ids, fr_names)),

        # General
        f(fr_ids[0], fr_general, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*fr_10_0)),
        # General File Name
        f(fr_general, fr_general_file, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*fr_0_01)),
        f(fr_general_file, 'label_name', 'label', 0, 0, 0, 0, 'nsew', **{'text': 'File Name:'}),
        f(fr_general_file, entry_name, 'entry', 0, 0, 1, 1, 'nsew', **{'default_value': 'Excel'}),
        f(fr_general_file, 'label_extension', 'label', 0, 0, 2, 2, 'nsew', **{'text': '.xlsx'}),
        # General Folder Path
        f(fr_general_file, 'label_name', 'label', 1, 1, 0, 0, 'nsew', **{'text': 'Folder Path:'}),
        f(fr_general_file, entry_path, 'entry', 1, 1, 1, 1, 'nsew', **{'default_value': 'Path'}),
        f(fr_general_file, btn_path, 'button', 1, 1, 2, 2, 'nsew', **{'text': 'Folder', 'width': 2}),
        # General Input Sheet
        f(fr_general_file, '_', 'label', 2, 2, 0, 0, 'nsew', **{'text': 'Insert Sheet Names in Input Sheet:'}),
        f(fr_general_file, check_btn_input_sheet, 'check_button', 2, 2, 1, 1, 'nsw'),

        # Sensitivity
        f(fr_ids[1], fr_sensitivity, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*fr_1_01)),
        # Sensitivity - Target
        # ----Left Account List
        f(fr_sensitivity, fr_sensitivity_target_l, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*fr_1_0)),
        f(fr_sensitivity_target_l, 'sens_account_list_label', 'label', 0, 0, 0, 0, 'nsew', **{'text': 'Account List'}),
        f(fr_sensitivity_target_l, tree_sensitivity_account_list, 'treeview', 1, 1, 0, 0, 'nsew', ),
        # ----Middle Button
        f(fr_sensitivity_target_l, 'fr_sensitivity_button', 'frame', 1, 1, 1, 1, 'ew', **intf.frame_options(*fr_0_0)),
        f('fr_sensitivity_button', btn_sensitivity_target_add, 'button', 0, 0, 0, 0, '', **{'text': '->'}),
        f('fr_sensitivity_button', btn_sensitivity_target_remove, 'button', 1, 1, 0, 0, '', **{'text': '<-'}),
        f('fr_sensitivity_button', btn_sensitivity_target_up, 'button', 2, 2, 0, 0, '', **{'text': '⬆️'}),
        f('fr_sensitivity_button', btn_sensitivity_target_down, 'button', 3, 3, 0, 0, '', **{'text': '⬇️'}),
        # ----Right Target List
        f(fr_sensitivity, fr_sensitivity_target_r, 'frame', 0, 0, 1, 1, 'nsew', **intf.frame_options(*fr_1_0)),
        f(fr_sensitivity_target_r, 'sens_target_list_label', 'label', 0, 0, 0, 0, 'nsew', **{'text': 'Target(s)'}),
        f(fr_sensitivity_target_r, tree_sensitivity_target_list, 'treeview', 1, 1, 0, 0, 'nsew', ),

        # Sensitivity - Variables
        # ----Left Input List
        f(fr_sensitivity, fr_sensitivity_variables_l, 'frame', 1, 1, 0, 0, 'nsew', **intf.frame_options(*fr_1_0)),
        f(fr_sensitivity_variables_l, 'sens_input_list_label', 'label', 0, 0, 0, 0, 'nsew', **{'text': 'Inputs'}),
        f(fr_sensitivity_variables_l, tree_sensitivity_input_list, 'treeview', 1, 1, 0, 0, 'nsew', ),
        # ----Middle Button
        f(fr_sensitivity_variables_l, fr_sensitivity_btn, 'frame', 1, 1, 1, 1, 'ew', **intf.frame_options(*fr_0_0)),
        f(fr_sensitivity_btn, btn_sensitivity_variable_add, 'button', 0, 0, 0, 0, 'ew', **{'text': '->'}),
        f(fr_sensitivity_btn, btn_sensitivity_variable_remove, 'button', 1, 1, 0, 0, 'ew', **{'text': '<-'}),
        f(fr_sensitivity_btn, 'fr_sensitivity_delta', 'frame', 2, 2, 0, 0, 'ew', **intf.frame_options(*fr_0_1)),
        f('fr_sensitivity_delta', 'label_delta_blank', 'label', 0, 0, 0, 1, '', **{'text': ''}),
        f('fr_sensitivity_delta', entry_sens_delta, 'entry', 1, 1, 0, 0, 'we', **{'default_value': 10, 'width': 5}),
        f('fr_sensitivity_delta', 'sensitivity_delta_uom', 'label', 1, 1, 1, 1, 'we', **{'text': '%'}),
        f('fr_sensitivity_delta', btn_sensitivity_delta, 'button', 2, 2, 0, 1, 'we', **{'text': 'Set Delta'}),
        # ----Right Variable List
        # Compare frame options with fr_sensitivity_variables_l (this prevents window from expanding when data added)
        f(fr_sensitivity, fr_sensitivity_variable_r, 'frame', 1, 1, 1, 1, 'nsew', **options_fr_selected_acs),
        f(fr_sensitivity_variable_r, 'sens_variable_list_label', 'label', 0, 0, 0, 0, 'nsew', **{'text': 'Variables'}),
        f(fr_sensitivity_variable_r, tree_sensitivity_variable_list, 'treeview', 1, 1, 0, 0, 'nsew', ),

        # Sensitivity - Range
        f(fr_sensitivity, fr_sens_range, 'frame', 2, 2, 0, 1, 'nsew', **intf.frame_options(*fr_0_0)),
        f(fr_sens_range, 'sensitivity_min_label', 'label', 0, 0, 0, 0, 'nse', **{'text': 'Range Minimum'}),
        f(fr_sens_range, entry_sensitivity_min, 'entry', 0, 0, 1, 1, 'nse', **{'default_value': -120, 'width': 5}),
        f(fr_sens_range, 'sens_increment_label', 'label', 0, 0, 2, 2, 'nsew', **{'text': '%    Increment'}),
        f(fr_sens_range, entry_sensitivity_increment, 'entry', 0, 0, 3, 3, 'nsew', **{'default_value': 10, 'width': 5}),
        f(fr_sens_range, 'sensitivity_max_label', 'label', 0, 0, 4, 4, 'nsew', **{'text': '%    Range Maximum'}),
        f(fr_sens_range, entry_sensitivity_max, 'entry', 0, 0, 5, 5, 'nsew', **{'default_value': 120, 'width': 5}),

        # Scenario
        f(fr_ids[2], fr_scenario, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*fr_10_0)),
        f(fr_scenario, 'fr_scenario_name', 'frame', 0, 0, 0, 0, 'nswe', **intf.frame_options(*fr_0_1)),
        f('fr_scenario_name', 'scenario_name_label', 'label', 0, 0, 0, 0, 'nsew', **{'text': 'Scenario Name:'}),
        f('fr_scenario_name', entry_scenario_name, 'entry', 0, 0, 1, 1, 'nsew', **{'default_value': 'Base Case'}),
        f('fr_scenario_name', btn_scenario_name, 'button', 0, 0, 2, 2, 'nsew', **{'text': 'Add'}),

        f(fr_scenario, 'fr_scenario_tree', 'frame', 1, 1, 0, 0, 'nswe', **intf.frame_options(*fr_0_0)),
        f(fr_scenario, tree_scenario, 'treeview', 1, 1, 0, 0, 'nsew', ),
        f(fr_scenario, 'fr_scenario_tree_btn', 'frame', 1, 1, 1, 1, 'swe', **intf.frame_options(*fr_0_0)),
        f('fr_scenario_tree_btn', btn_fr_scenario_up, 'button', 0, 0, 0, 0, 'nswe', **{'text': '⬆️', 'width': 2}),
        f('fr_scenario_tree_btn', btn_fr_scenario_down, 'button', 1, 1, 0, 0, 'nswe', **{'text': '⬇️', 'width': 2}),
        f('fr_scenario_tree_btn', btn_fr_scenario_delete, 'button', 2, 2, 0, 0, 'nswe', **{'text': '❌', 'width': 2}),

        # Graphs
        f(fr_ids[3], fr_graph, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*fr_10_0)),
        f(fr_graph, 'fr_graph_name', 'frame', 0, 0, 0, 0, 'nswe', **intf.frame_options(*fr_0_1)),
        f('fr_graph_name', 'graph_name_label', 'label', 0, 0, 0, 0, 'nsew', **{'text': 'Graph Name:'}),
        f('fr_graph_name', 'graph_name_entry', 'combo_box', 0, 0, 1, 1, 'nsew', **{'values': graph_names}),
        f('fr_graph_name', btn_graph_name, 'button', 0, 0, 2, 2, 'nsew', **{'text': 'Add'}),

        f(fr_graph, 'fr_graph_tree', 'frame', 1, 1, 0, 0, 'nswe', **intf.frame_options(*fr_0_0)),
        f(fr_graph, tree_graph, 'treeview', 1, 1, 0, 0, 'nsew', ),
        f(fr_graph, 'fr_graph_tree_btn', 'frame', 1, 1, 1, 1, 'swe', **intf.frame_options(*fr_0_0)),
        f('fr_graph_tree_btn', btn_fr_graph_up, 'button', 0, 0, 0, 0, 'nswe', **{'text': '⬆️', 'width': 2}),
        f('fr_graph_tree_btn', btn_fr_graph_down, 'button', 1, 1, 0, 0, 'nswe', **{'text': '⬇️', 'width': 2}),
        f('fr_graph_tree_btn', btn_fr_graph_delete, 'button', 2, 2, 0, 0, 'nswe', **{'text': '❌', 'width': 2}),

        # DashBoard
        f(fr_ids[4], fr_dash_board, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*fr_10_0)),
        f(fr_dash_board, 'fr_db_name', 'frame', 0, 0, 0, 0, 'nswe', **intf.frame_options(*fr_0_1)),
        f('fr_db_name', 'dash_board_name_label', 'label', 0, 0, 0, 0, 'nsew', **{'text': 'Dash Board Name:'}),
        f('fr_db_name', 'dash_board_name_entry', 'combo_box', 0, 0, 1, 1, 'nsew', **{'values': dash_board_names}),
        f('fr_db_name', btn_dash_board_name, 'button', 0, 0, 2, 2, 'nsew', **{'text': 'Add'}),

        f(fr_dash_board, fr_dash_board_tree, 'frame', 1, 1, 0, 0, 'nswe', **intf.frame_options(*fr_0_0)),
        f(fr_dash_board_tree, tree_dash_board, 'treeview', 1, 1, 0, 0, 'nsew', ),
        f(fr_dash_board_tree, 'fr_db_tree_btn', 'frame', 1, 1, 1, 1, 'swe', **intf.frame_options(*fr_0_0)),
        f('fr_db_tree_btn', btn_fr_dash_board_up, 'button', 0, 0, 0, 0, 'nswe', **{'text': '⬆️', 'width': 2}),
        f('fr_db_tree_btn', btn_fr_dash_board_down, 'button', 1, 1, 0, 0, 'nswe', **{'text': '⬇️', 'width': 2}),
        f('fr_db_tree_btn', btn_fr_dash_board_delete, 'button', 2, 2, 0, 0, 'nswe', **{'text': '❌', 'width': 2}),

        # Bottom Buttons
        f(frame_id, fr_general_buttons, 'frame', 1, 1, 0, 0, 'nsew', **intf.frame_options(*fr_0_0)),
        f(fr_general_buttons, btn_export, 'button', 0, 0, 0, 0, 'swe', **{'text': 'Export'}),

    ]
    return view_model


def get_kwargs(key, kwargs: dict):
    return kwargs[key] if key in kwargs else None
