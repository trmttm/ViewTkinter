from .. import tk_interface as intf
from ..tk_interface import widget_model as wm


def create_configuration_setting(frame, **kwargs):
    rc_0_1 = ((0,), (1,)), ((1,), (1,))
    fr = 'fr_setting_top'

    entry_project = kwargs['entry_project']
    entry_nop = kwargs['entry_nop']
    btn_setting_ok = kwargs['btn_setting_ok']
    check_btn_cleaner = kwargs['check_btn_cleaner'] if 'check_btn_cleaner' in kwargs else 'check_btn_cleaner'
    check_btn_live_calc = kwargs['check_btn_live_calc'] if 'check_btn_live_calc' in kwargs else 'check_btn_live_calc'
    check_btn_auto_relay_to_right_end = kwargs.get('check_btn_relay_right_end', 'check_btn_relay_right_end')
    btn_project = kwargs.get('btn_project', 'btn_project')

    entry_account_w = kwargs.get('account_w')
    entry_account_h = kwargs.get('account_h')
    entry_account_font_size = kwargs.get('account_font_size')
    entry_operator_w = kwargs.get('operator_w')
    entry_operator_h = kwargs.get('operator_h')
    entry_operator_font_size = kwargs.get('operator_font_size')
    entry_constant_w = kwargs.get('constant_w')
    entry_constant_h = kwargs.get('constant_h')
    entry_constant_font_size = kwargs.get('constant_font_size')
    entry_bb_w = kwargs.get('bb_w')
    entry_bb_h = kwargs.get('bb_h')
    entry_bb_font_size = kwargs.get('bb_font_size')
    frame_account = 'account_frame'

    view_model = [
        wm(frame, fr, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(*rc_0_1)),
        wm(fr, 'project_folder', 'label', 0, 0, 0, 0, 'nsew', **{'text': 'Project Folder'}),
        wm(fr, entry_project, 'entry', 0, 0, 1, 1, 'e', **{'width': 60}),
        wm(fr, btn_project, 'button', 0, 0, 2, 2, 'e', **{'text': 'Folder', }),

        wm(fr, 'nop', 'label', 1, 1, 0, 0, 'nsew', **{'text': 'Number of Periods'}),
        wm(fr, entry_nop, 'entry', 1, 1, 1, 1, 'e', **{'width': 10}),
        wm(fr, btn_setting_ok, 'button', 1, 1, 2, 2, 'e', **{'text': 'Apply'}),

        wm(fr, 'clean_state', 'label', 2, 2, 0, 0, 'nsew', **{'text': 'Clean states upon save'}),
        wm(fr, check_btn_cleaner, 'check_button', 2, 2, 1, 1, 'w', ),

        wm(fr, 'live_calculation', 'label', 3, 3, 0, 0, 'nsew', **{'text': 'Live Calculation'}),
        wm(fr, check_btn_live_calc, 'check_button', 3, 3, 1, 1, 'w', **{'value': True}),

        wm(fr, frame_account, 'frame', 4, 4, 0, 2, 'nsew', ),
        wm(frame_account, 'account', 'label', 0, 0, 0, 0, 'nsew', **{'text': 'Account'}),
        wm(frame_account, entry_account_w, 'entry', 0, 0, 1, 1, 'nsew', **{'width': 3}),
        wm(frame_account, entry_account_h, 'entry', 0, 0, 2, 2, 'nsew', **{'width': 3}),
        wm(frame_account, entry_account_font_size, 'entry', 0, 0, 3, 3, 'nsew', **{'width': 3}),

        wm(frame_account, 'operator', 'label', 1, 1, 0, 0, 'nsew', **{'text': 'Operator'}),
        wm(frame_account, entry_operator_w, 'entry', 1, 1, 1, 1, 'nsew', **{'width': 3}),
        wm(frame_account, entry_operator_h, 'entry', 1, 1, 2, 2, 'nsew', **{'width': 3}),
        wm(frame_account, entry_operator_font_size, 'entry', 1, 1, 3, 3, 'nsew', **{'width': 3}),

        wm(frame_account, 'constant', 'label', 2, 2, 0, 0, 'nsew', **{'text': 'Constant'}),
        wm(frame_account, entry_constant_w, 'entry', 2, 2, 1, 1, 'nsew', **{'width': 3}),
        wm(frame_account, entry_constant_h, 'entry', 2, 2, 2, 2, 'nsew', **{'width': 3}),
        wm(frame_account, entry_constant_font_size, 'entry', 2, 2, 3, 3, 'nsew', **{'width': 3}),

        wm(frame_account, 'bb', 'label', 3, 3, 0, 0, 'nsew', **{'text': 'BB'}),
        wm(frame_account, entry_bb_w, 'entry', 3, 3, 1, 1, 'nsew', **{'width': 3}),
        wm(frame_account, entry_bb_h, 'entry', 3, 3, 2, 2, 'nsew', **{'width': 3}),
        wm(frame_account, entry_bb_font_size, 'entry', 3, 3, 3, 3, 'nsew', **{'width': 3}),

        wm(fr, 'lbl_relay_x', 'label', 5, 5, 0, 0, 'nsew', **{'text': 'Auto relay at right end'}),
        wm(fr, check_btn_auto_relay_to_right_end, 'check_button', 5, 5, 1, 1, 'w', **{'value': True}),

    ]
    return view_model
