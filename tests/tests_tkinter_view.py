import unittest


class MyTestCase(unittest.TestCase):

    def test_add_widgets(self):
        from src.view_tkinter.tk_interface import widget_model as wm
        from src.view_tkinter import tk_interface as intf
        from src.view_tkinter.view import View

        view = View()

        row_col_configuration1 = (((0,), (1,)), ((1,), (1,)))
        row_col_configuration2 = (((3,), (1,)), ((1,), (1,)))
        view_model = [
            wm('root', 0, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*row_col_configuration1)),
            wm(0, 1, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*row_col_configuration2)),
            wm(0, 2, 'canvas', 0, 0, 1, 1, 'nsew', bg='light yellow'),
            wm(1, 3, 'button', 0, 0, 0, 0, 'nsew', **intf.button_options('Button1', lambda *_: print('Button1'))),
            wm(1, 4, 'button', 0, 0, 1, 1, 'nsew', **intf.button_options('Button2', lambda *_: print('Button2'))),
            wm(1, 5, 'button', 0, 0, 2, 2, 'nsew', **intf.button_options('Button3', lambda *_: print('Button3'))),
            wm(1, 6, 'button', 1, 1, 0, 0, 'nsew', **intf.button_options('Button4', lambda *_: print('Button4'))),
            wm(1, 7, 'button', 1, 1, 1, 1, 'nsew', **intf.button_options('Button5', lambda *_: print('Button5'))),
            wm(1, 8, 'button', 1, 1, 2, 2, 'nsew', **intf.button_options('Button6', lambda *_: print('Button6'))),
            wm(1, 8, 'button', 2, 2, 0, 2, 'nsew', **intf.button_options('Button7', lambda *_: print('Button7'))),
        ]

        view.add_widgets(view_model)
        # view.launch_app()

    def test_search_filter(self):
        from src.view_tkinter.ViewModels import create_view_model_search_popup
        from src.view_tkinter.view import View

        all_groups_and_names = (
            ('Transactions', 'Tr_Revenue'),
            ('Transactions', 'Tr_COGS'),
            ('Transactions', 'Tr_AR'),
            ('Transactions', 'Tr_AP'),
            ('Transactions', 'Tr_Inventory'),
            ('Macro', 'Add Tr_Revenue'),
            ('Macro', 'Add Tr_COGS'),
            ('Command', 'Export as Excel'),
        )

        view = View()
        entry = 'entry_0'
        tree = 'tree_0'
        view_model = create_view_model_search_popup('toplevel', entry, tree)
        view.add_widgets(view_model)

        # Entry operations
        view.focus(entry)

        # Tree operations
        view.switch_tree(tree)

        # view.launch_app()


def get_view_model_slider(origin, slider_wh: tuple, handle_wh: tuple, min_max_wh: tuple, min_max_x, colors: dict):
    so = origin
    width, height = slider_wh
    handle_width, handle_height = handle_wh
    min_max_width, min_max_height = min_max_wh
    color_fill_handle = colors['fill_handle']
    color_fill_max = colors['fill_max']
    color_fill_min = colors['fill_min']
    color_fill_slider = colors['fill_slider']
    color_line_handle = colors['line_handle']
    color_line_max = colors['line_max']
    color_line_min = colors['line_min']
    color_line_slider = colors['line_slider']
    view_model_slider = {
        'slider': {
            'coordinate_from': origin,
            'coordinate_to': (so[0] + width, so[1] + height),
            'line_color': color_line_slider,
            'line_width': 1,
            'tags': '',
            'fill': ('%s' % color_fill_slider),
        },
        'max': {
            'coordinate_from': (so[0] + min_max_x, so[1] - min_max_height / 2),
            'coordinate_to': (so[0] + min_max_x + min_max_width, so[1] + min_max_height / 2),
            'line_color': color_line_max,
            'line_width': 1,
            'tags': '',
            'fill': color_fill_max,
        },
        'min': {
            'coordinate_from': (so[0] + min_max_x, so[1] + height - handle_height / 2),
            'coordinate_to': (so[0] + min_max_x + min_max_width, so[1] + height + handle_height / 2),
            'line_color': color_line_min,
            'line_width': 1,
            'tags': '',
            'fill': color_fill_min,
        },
        'handle': {
            'coordinate_from': (so[0], so[1] + height - handle_height),
            'coordinate_to': (so[0] + handle_width, so[1] + height),
            'line_color': color_line_handle,
            'line_width': 1,
            'tags': '',
            'fill': color_fill_handle,
        }
    }
    return view_model_slider


class MyConcreteViews(unittest.TestCase):

    def test_pre_defined_view_models(self):
        from src.view_tkinter import tk_interface as intf
        f = intf.widget_model
        frame_root_id = 1
        parent_id = 'root'
        # row_col_configuration = ((0,), (1,)), ((0, 1, 2, 3), (1, 1, 1, 1))
        row_col_configuration = ((0,), (1,)), ((0,), (1,))
        frame = [f(parent_id, frame_root_id, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*row_col_configuration))]

        # Select model creator
        from src.view_tkinter.ViewModels import input_entry as model_creator
        view_model = frame + model_creator(frame_root_id)

        from src.view_tkinter import View
        view = View()
        view.add_widgets(view_model)

        # view.launch_app()

    def test_view_status_bar(self):
        from src.view_tkinter import tk_interface as intf
        f = intf.widget_model
        frame_root_id = 1
        parent_id = 'root'
        row_col_configuration = ((1,), (1,)), ((0, 1, 2, 3), (1, 1, 1, 1))
        frame = [f(parent_id, frame_root_id, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*row_col_configuration))]

        n = 0

        def update_status_bar():
            nonlocal n
            view.update_status_bar({'text': f'Status bar is successfully updated {n}.'})
            n += 1

        status_bar_id = 'status bar'
        view_model = frame
        view_model += [
            f(frame_root_id, status_bar_id, 'label', 0, 0, 0, 0, 'nsew', **{'text': 'Status Bar'}),
            f(frame_root_id, 'button', 'button', 0, 0, 1, 1, 'nsew',
              **{'text': 'Update', 'command': update_status_bar}),
        ]

        from src.view_tkinter import View
        view = View()
        view.add_widgets(view_model)
        view.switch_status_bar(status_bar_id)
        # view.launch_app()

    def test_frame_switcher(self):
        from src.view_tkinter import tk_interface as intf
        f = intf.widget_model
        frame_root_id = 1
        parent_id = 'root'
        rc_config0 = ((0,), (1,)), ((1,), (1,))
        frame = [f(parent_id, frame_root_id, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*rc_config0))]

        rc_config1 = ((0,), (1,)), ((0,), (1,))
        rc_config2 = ((1,), (1,)), ((0,), (1,))
        view_model = frame
        fr1 = 'frame1'
        fr2 = 'frame2'
        fr3 = 'frame3'
        fr4 = 'frame4'
        fr_l = 'fr_l'
        fr_r = 'fr_r'
        view_model += [
            f(frame_root_id, fr_l, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*rc_config1)),
            f(fr_l, 'btn1', 'button', 0, 0, 0, 0, 'nsew', **{'text': 'Switch 1'}),
            f(fr_l, 'btn2', 'button', 1, 1, 0, 0, 'nsew', **{'text': 'Switch 2'}),
            f(fr_l, 'btn3', 'button', 2, 2, 0, 0, 'nsew', **{'text': 'Switch 3'}),
            f(fr_l, 'btn4', 'button', 3, 3, 0, 0, 'nsew', **{'text': 'Switch 4'}),
            f(frame_root_id, fr_r, 'frame', 0, 0, 1, 1, 'nsew', **intf.frame_options(*rc_config1)),
            f(fr_r, fr1, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*rc_config2)),
            f(fr_r, fr2, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*rc_config2)),
            f(fr_r, fr3, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*rc_config2)),
            f(fr_r, fr4, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*rc_config2)),
            f(fr1, 'label1', 'label', 0, 0, 0, 0, 'nsew', **{'text': 'This is frame 1'}),
            f(fr2, 'label2', 'label', 0, 0, 0, 0, 'nsew', **{'text': 'This is frame 2'}),
            f(fr3, 'label3', 'label', 0, 0, 0, 0, 'nsew', **{'text': 'This is frame 3'}),
            f(fr4, 'label4', 'label', 0, 0, 0, 0, 'nsew', **{'text': 'This is frame 4'}),
            f(fr1, 'entry', 'entry', 1, 1, 0, 0, 'nsew', **{}),
            f(fr2, 'canvas', 'canvas', 1, 1, 0, 0, 'nsew', **{'bg': 'orange'}),

        ]

        from src.view_tkinter import View
        view = View()
        view.add_widgets(view_model)

        view.bind_command_to_widget('btn1', lambda: view.switch_frame(fr1))
        view.bind_command_to_widget('btn2', lambda: view.switch_frame(fr2))
        view.bind_command_to_widget('btn3', lambda: view.switch_frame(fr3))
        view.bind_command_to_widget('btn4', lambda: view.switch_frame(fr4))

        # view.launch_app()

    def test_macro_manager(self):
        from src.view_tkinter.view import View
        from src.view_tkinter.ViewModels import create_macro_manager_view_model
        view = View()

        kwargs = {'btn_del_macro': 'btn_del_macro',
                  'btn_merge_macro': 'btn_merge_macro',
                  'btn_save_macro': 'btn_save_macro',
                  'btn_run_commands': 'btn_run_commands',
                  'btn_clear_commands': 'btn_clear_commands',
                  'btn_del_commands': 'btn_del_commands',
                  'btn_copy_commands': 'btn_copy_commands',
                  'btn_down_command': 'btn_down_command',
                  'btn_up_command': 'btn_up_command',
                  'tree_commands': 'tree_commands',
                  'tree_macros': 'tree_macros',
                  'check_btn_macro_mode': 'check_btn_macro_mode',
                  'entry_macro_name': 'entry_macro_name',
                  'btn_set_command_name': 'btn_set_command_name',
                  'btn_set_args': 'btn_set_args',
                  'btn_set_kwargs': 'btn_set_kwargs',
                  }

        view_model = create_macro_manager_view_model('root', **kwargs)

        view.add_widgets(view_model)
        # view.launch_app()

    def test_configuration_setting(self):
        from src.view_tkinter.view import View
        from src.view_tkinter.ViewModels import create_configuration_setting
        view = View()
        kwargs = {
            'entry_nop': 'entry_nop',
            'btn_setting_ok': 'btn_setting_ok',
        }
        view_model = create_configuration_setting('root', **kwargs)

        view.add_widgets(view_model)
        # view.launch_app()

    def test_export_window(self):
        from src.view_tkinter.view import View
        from src.view_tkinter.ViewModels import export_window
        view = View()

        view_model = export_window('root', )

        view.add_widgets(view_model)
        # view.launch_app()

    def test_canvas_save_setting(self):
        from src.view_tkinter.view import View
        from src.view_tkinter.ViewModels import canvas_save_setting
        view = View()
        view_model = canvas_save_setting('root', 'entry_total_frames', 'entry_height', 'btn_canvas_save', 50)

        view.add_widgets(view_model)
        view.launch_app()

    def test_graph(self):
        from src.view_tkinter.view import View
        from src.view_tkinter import tk_interface as intf
        view = View()
        f = intf.widget_model
        view_model = [
            f('root', 'canvas', 'canvas', 0, 0, 0, 0, 'nsew', (1, 1), **{'bg': 'light yellow'}),
        ]

        view.add_widgets(view_model)
        view.switch_canvas('canvas')

        dx = 100
        dy = 100

        origin = (200 + dx, 210 + dy)
        x_axis_length = 400
        y_axis_length = 300

        so = (10 + dx, 10 + dy)
        sw = 25
        sh = 200

        hh = 25
        hw = 25

        mmw = 45
        mmh = 20
        mmx = -60
        slider_wh = (sw, sh)
        handle_wh = (hw, hh)
        min_max_wh = (mmw, mmh)
        colors = {
            'fill_handle': 'yellow',
            'fill_max': None,
            'fill_min': None,
            'fill_slider': 'light grey',
            'line_handle': 'black',
            'line_max': 'black',
            'line_min': 'black',
            'line_slider': 'black',
        }
        cl_mx_sl = 'black'
        xl_mn_sl = 'black'
        cl_y = 'blue'
        cl_x = 'blue'
        view_model = {
            'max_line': {
                'coordinate_from': (so[0] + mmx + mmw, so[1]),
                'coordinate_to': (so[0], so[1]),
                'line_color': cl_mx_sl,
                'line_width': 1,
                'arrow': None,
            },
            'min_line': {
                'coordinate_from': (so[0] + mmx + mmw, so[1] + sh),
                'coordinate_to': (so[0], so[1] + sh),
                'line_color': xl_mn_sl,
                'line_width': 1,
                'arrow': None,
            },
            'y_axis': {
                'coordinate_from': origin,
                'coordinate_to': (origin[0], origin[1] - y_axis_length),
                'line_color': cl_y,
                'line_width': 2,
                'arrow': 'to',
            },
            'x_axis': {
                'coordinate_from': origin,
                'coordinate_to': (origin[0] + x_axis_length, origin[1]),
                'line_color': cl_x,
                'line_width': 2,
                'arrow': 'to',
            },
        }

        view_model_slider = get_view_model_slider(so, slider_wh, handle_wh, min_max_wh, mmx, colors)
        color_fill_bar1 = 'blue'
        color_fill_bar2 = 'orange'
        color_line_bar1 = 'black'
        color_line_bar2 = 'black'

        gap1 = 10
        gap2 = 10
        width1 = 20
        width2 = 20
        height1 = 150
        height2 = -250

        x1_from = origin[0] + gap1
        x1_to = x1_from + width1
        x2_from = x1_to + gap2
        x2_to = x2_from + width2

        y1_fom = origin[1]
        y1_to = origin[1] - height1
        y2_from = y1_to
        y2_to = y1_to - height2
        view_model_bars = {
            'bar1': {
                'coordinate_from': (x1_from, y1_fom),
                'coordinate_to': (x1_to, y1_to),
                'line_color': color_line_bar1,
                'line_width': 1,
                'tags': '',
                'fill': color_fill_bar1,
            },
            'bar2': {
                'coordinate_from': (x2_from, y2_from),
                'coordinate_to': (x2_to, y2_to),
                'line_color': color_line_bar2,
                'line_width': 1,
                'tags': '',
                'fill': color_fill_bar2,
            },
        }
        view_model_slider.update(view_model_bars)
        view.draw_rectangle(view_model_slider)
        view.draw_line(view_model)

        view.launch_app()

    def test_scrollable_frame(self):
        from view_tkinter.view import View
        from view_tkinter import tk_interface as intf
        view = View()
        f = intf.widget_model
        view_model = [
            f('root', 'sf', 'scrollable_frame', 0, 0, 0, 0, 'nsew', ),
            f('sf', 'label1', 'label', 1, 1, 0, 0, 'nsew', **{'text': 'Lable1'}),
            f('sf', 'label2', 'label', 2, 2, 0, 0, 'nsew', **{'text': 'Lable2'}),
            f('sf', 'label3', 'label', 3, 3, 0, 0, 'nsew', **{'text': 'Lable3'}),
            f('sf', 'label4', 'label', 4, 4, 0, 0, 'nsew', **{'text': 'Lable4'}),
            f('sf', 'label5', 'label', 5, 5, 0, 0, 'nsew', **{'text': 'Lable5'}),
            f('sf', 'label6', 'label', 6, 6, 0, 0, 'nsew', **{'text': 'Lable6'}),
            f('sf', 'label7', 'label', 7, 7, 0, 0, 'nsew', **{'text': 'Lable7'}),
            f('sf', 'label8', 'label', 8, 8, 0, 0, 'nsew', **{'text': 'Lable8'}),
            f('sf', 'label9', 'label', 9, 9, 0, 0, 'nsew', **{'text': 'Lable9'}),
            f('sf', 'label10', 'label', 10, 10, 0, 0, 'nsew', **{'text': 'Lable10'}),
            f('sf', 'label11', 'label', 11, 11, 0, 0, 'nsew', **{'text': 'Lable11'}),
            f('sf', 'label12', 'label', 12, 12, 0, 0, 'nsew', **{'text': 'Lable12'}),
            f('sf', 'label13', 'label', 13, 13, 0, 0, 'nsew', **{'text': 'Lable13'}),
            f('sf', 'label14', 'label', 14, 14, 0, 0, 'nsew', **{'text': 'Lable14'}),
            f('sf', 'label15', 'label', 15, 15, 0, 0, 'nsew', **{'text': 'Lable15'}),
            f('sf', 'label1', 'label', 1, 1, 1, 1, 'nsew', **{'text': 'Lable1'}),
            f('sf', 'label2', 'label', 2, 2, 1, 1, 'nsew', **{'text': 'Lable2'}),
            f('sf', 'label3', 'label', 3, 3, 1, 1, 'nsew', **{'text': 'Lable3'}),
            f('sf', 'label4', 'label', 4, 4, 1, 1, 'nsew', **{'text': 'Lable4'}),
            f('sf', 'label5', 'label', 5, 5, 1, 1, 'nsew', **{'text': 'Lable5'}),
            f('sf', 'label6', 'label', 6, 6, 1, 1, 'nsew', **{'text': 'Lable6'}),
            f('sf', 'label7', 'label', 7, 7, 1, 1, 'nsew', **{'text': 'Lable7'}),
            f('sf', 'label8', 'label', 8, 8, 1, 1, 'nsew', **{'text': 'Lable8'}),
            f('sf', 'label9', 'label', 9, 9, 1, 1, 'nsew', **{'text': 'Lable9'}),
            f('sf', 'label10', 'label', 10, 10, 1, 1, 'nsew', **{'text': 'Lable10'}),
            f('sf', 'label11', 'label', 11, 11, 1, 1, 'nsew', **{'text': 'Lable11'}),
            f('sf', 'label12', 'label', 12, 12, 1, 1, 'nsew', **{'text': 'Lable12'}),
            f('sf', 'label13', 'label', 13, 13, 1, 1, 'nsew', **{'text': 'Lable13'}),
            f('sf', 'label14', 'label', 14, 14, 1, 1, 'nsew', **{'text': 'Lable14'}),
            f('sf', 'label15', 'label', 15, 15, 1, 1, 'nsew', **{'text': 'Lable15'}),
        ]

        view.add_widgets(view_model)

        # view.launch_app()


if __name__ == '__main__':
    unittest.main()
