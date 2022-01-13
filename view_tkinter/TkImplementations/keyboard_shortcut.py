import os_identifier

shift = 'shift'
function = 'function'
control = 'control'
option = 'alt_option'
command = 'command'

space = 'Space'
return_ = 'Return'
back_space = 'BackSpace'
delete = 'Delete'
escape = 'Escape'

up = 'Up'
down = 'Down'
left = 'Left'
right = 'Right'

if os_identifier.is_mac:
    tk_n_none = 0
    tk_none_special = 96
    tk_n_shift = 1
    tk_n_function = 64
    tk_n_control = 4
    tk_n_option = 16
    tk_n_command = 8
else:
    tk_n_none = 8
    tk_none_special = 262144
    tk_n_shift = 1
    tk_n_function = 64
    tk_n_control = 4
    tk_n_option = 131072
    tk_n_command = 8
tk_n_all = tk_n_shift + tk_n_function + tk_n_control + tk_n_option + tk_n_command

n_none = 0
n_shift = 1
n_function = 64
n_control = 4
n_option = 16
n_command = 8
n_all = n_shift + n_function + n_control + n_option + n_command

tk_modifier_interpreter = {
    # No Modifier
    tk_n_none: n_none,

    # One Modifier
    tk_n_none + tk_n_shift: n_shift,
    tk_n_none + tk_n_function: n_function,
    tk_n_none + tk_n_control: n_control,
    tk_n_none + tk_n_option: n_option,
    tk_n_none + tk_n_command: n_command,

    # Two Modifiers
    tk_n_none + tk_n_shift + tk_n_function: n_shift + n_function,
    tk_n_none + tk_n_shift + tk_n_control: n_shift + n_control,
    tk_n_none + tk_n_shift + tk_n_option: n_shift + n_option,
    tk_n_none + tk_n_shift + tk_n_command: n_shift + n_command,
    tk_n_none + tk_n_control + tk_n_function: n_control + n_function,
    tk_n_none + tk_n_control + tk_n_option: n_control + n_option,
    tk_n_none + tk_n_control + tk_n_command: n_control + n_command,
    tk_n_none + tk_n_command + tk_n_function: n_command + n_function,
    tk_n_none + tk_n_command + tk_n_option: n_command + n_option,
    tk_n_none + tk_n_function + tk_n_option: n_function + n_option,

    # Three Modifiers
    tk_n_none + tk_n_all - (tk_n_shift + tk_n_function): n_all - (n_shift + n_function),
    tk_n_none + tk_n_all - (tk_n_shift + tk_n_control): n_all - (n_shift + n_control),
    tk_n_none + tk_n_all - (tk_n_shift + tk_n_option): n_all - (n_shift + n_option),
    tk_n_none + tk_n_all - (tk_n_shift + tk_n_command): n_all - (n_shift + n_command),
    tk_n_none + tk_n_all - (tk_n_control + tk_n_function): n_all - (n_control + n_function),
    tk_n_none + tk_n_all - (tk_n_control + tk_n_option): n_all - (n_control + n_option),
    tk_n_none + tk_n_all - (tk_n_control + tk_n_command): n_all - (n_control + n_command),
    tk_n_none + tk_n_all - (tk_n_command + tk_n_function): n_all - (n_command + n_function),
    tk_n_none + tk_n_all - (tk_n_command + tk_n_option): n_all - (n_command + n_option),
    tk_n_none + tk_n_all - (tk_n_function + tk_n_option): n_all - (n_function + n_option),

    # Four Modifiers
    tk_n_none + tk_n_all - tk_n_shift: n_all - n_shift,
    tk_n_none + tk_n_all - tk_n_function: n_all - n_function,
    tk_n_none + tk_n_all - tk_n_control: n_all - n_control,
    tk_n_none + tk_n_all - tk_n_option: n_all - n_option,
    tk_n_none + tk_n_all - tk_n_command: n_all - n_command,

    # All Modifiers
    tk_n_none + tk_n_all: n_all,
}

tk_key_interpreter = {
    # General
    ' ': (space, 0),
    '\uf704': ('F1', -n_function),
    '\uf705': ('F2', -n_function),
    '\uf706': ('F3', -n_function),
    '\uf707': ('F4', -n_function),
    '\uf708': ('F5', -n_function),
    '\uf709': ('F6', -n_function),
    '\uf70a': ('F7', -n_function),
    '\uf70b': ('F8', -n_function),
    '\uf70c': ('F9', -n_function),
    '\uf70d': ('F10', -n_function),
    '\uf70e': ('F11', -n_function),
    '\uf70f': ('F12', -n_function),

    # alt_option
    'å': ('a', n_option),
    '∫': ('b', n_option),
    'ç': ('c', n_option),
    '∂': ('d', n_option),
    '´': ('e', n_option),
    'ƒ': ('f', n_option),
    '©': ('g', n_option),
    '˙': ('h', n_option),
    'ˆ': ('i', n_option),
    '∆': ('j', n_option),
    '˚': ('k', n_option),
    '¬': ('l', n_option),
    'µ': ('m', n_option),
    '˜': ('n', n_option),
    'ø': ('o', n_option),
    'π': ('p', n_option),
    'œ': ('q', n_option),
    '®': ('r', n_option),
    'ß': ('s', n_option),
    '†': ('t', n_option),
    '¨': ('u', n_option),
    '√': ('v', n_option),
    '∑': ('w', n_option),
    '≈': ('x', n_option),
    '¥': ('y', n_option),
    'Ω': ('z', n_option),
    '¡': ('1', n_option),
    '™': ('2', n_option),
    '£': ('3', n_option),
    '¢': ('4', n_option),
    '∞': ('5', n_option),
    '§': ('6', n_option),
    '¶': ('7', n_option),
    '•': ('8', n_option),
    'ª': ('9', n_option),
    'º': ('0', n_option),
    '–': ('-', n_option),
    '≠': ('=', n_option),
    '\x7f': (back_space, n_option),
    ' ': (space, n_option),

    # Shift
    'A': ('a', 1),
    'B': ('b', 1),
    'C': ('c', 1),
    'D': ('d', 1),
    'E': ('e', 1),
    'F': ('f', 1),
    'G': ('g', 1),
    'H': ('h', 1),
    'I': ('i', 1),
    'J': ('j', 1),
    'K': ('k', 1),
    'L': ('l', 1),
    'M': ('m', 1),
    'N': ('n', 1),
    'O': ('o', 1),
    'P': ('p', 1),
    'Q': ('q', 1),
    'R': ('r', 1),
    'S': ('s', 1),
    'T': ('t', 1),
    'U': ('u', 1),
    'V': ('v', 1),
    'W': ('w', 1),
    'X': ('x', 1),
    'Y': ('y', 1),
    'Z': ('z', 1),
    '+': ('=', 1),

    # Control
    '\x01': ('a', 0),
    '\x02': ('b', 0),
    '\x03': ('c', 0),
    '\x04': ('d', 0),
    '\x05': ('e', 0),
    '\x06': ('f', 0),
    '\x07': ('g', 0),
    '\x08': ('h', 0),
    '\x09': ('i', 0),
    '\n': ('j', 0),
    '\x0b': ('k', 0),
    '\x0c': ('l', 0),
    '\r': ('m', 0),
    '\x0e': ('n', 0),
    '\x0f': ('o', 0),
    '\x10': ('p', 0),
    '\x11': ('q', 0),
    '\x12': ('r', 0),
    '\x13': ('s', 0),
    '\x14': ('t', 0),
    '\x15': ('u', 0),
    '\x16': ('v', 0),
    '\x17': ('w', 0),
    '\x18': ('x', 0),
    '\x19': ('y', 0),
    '\x1a': ('z', 0),
    '\x1f': ('-', 0),

    # Command Option
    '^': ('i', 0),
    '~': ('n', 0),
}

keys_that_require_adjustments = (
    '\uf704',
    '\uf705',
    '\uf706',
    '\uf707',
    '\uf708',
    '\uf709',
    '\uf70a',
    '\uf70b',
    '\uf70c',
    '\uf70d',
    '\uf70e',
    '\uf70f',
)
state_that_require_adjustments = (0,)
keysym_that_require_adjustments = ('KP_Enter', delete, up, down, left, right)


def tk_interpret_state(environment_dependent_state) -> int:
    state = environment_dependent_state
    return tk_modifier_interpreter[state] if state in tk_modifier_interpreter else state


def interpret_key(key, keysym, state) -> tuple:
    is_windows = os_identifier.is_windows

    if keysym == 'space':
        return space, 0
    elif keysym == 'Return':
        return return_, 0
    elif keysym == 'Escape':
        return escape, 0
    elif keysym == 'KP_Enter':
        return return_, -32
    elif keysym == 'BackSpace':
        return back_space, 0
    elif keysym == 'Delete':
        return delete, convert_special_modifier_to_global_modifier(state)
    elif keysym == 'Up':
        return up, convert_special_modifier_to_global_modifier(state)
    elif keysym == 'Down':
        return down, convert_special_modifier_to_global_modifier(state)
    elif keysym == 'Left':
        return left, convert_special_modifier_to_global_modifier(state)
    elif keysym == 'Right':
        return right, convert_special_modifier_to_global_modifier(state)
    elif keysym == 'minus':
        return '-', 0
    elif keysym == 'equal':
        return '=', 0
    elif is_windows and keysym in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        return keysym, 0
    elif is_windows and keysym in ('F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',):
        return keysym, 0
    else:
        return tk_key_interpreter[key] if key in tk_key_interpreter else (key, 0)


def convert_special_modifier_to_global_modifier(state):
    adjustment_to_local_modifier = -tk_none_special
    local_modifier = state + adjustment_to_local_modifier
    global_modifier = tk_interpret_state(local_modifier)
    adjustment_from_local_to_global = (global_modifier - local_modifier)
    adjustment_to_global_modifier = adjustment_to_local_modifier + adjustment_from_local_to_global
    return adjustment_to_global_modifier


def tk_state_adjustment(key: str, state: int, adjustment: int, keysym) -> int:
    if key in keys_that_require_adjustments:
        return state + adjustment
    elif state in state_that_require_adjustments:
        return state + adjustment
    elif keysym in keysym_that_require_adjustments:
        return state + adjustment
    else:
        return state
