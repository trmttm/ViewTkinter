import tkinter as tk
from tkinter import font
from tkinter import ttk
from typing import Callable
from typing import Type

widget_tree_view = ttk.Treeview


def update_tree(tree: ttk.Treeview, view_model):
    tree_initial_settings(tree, view_model)

    tree.delete(*get_all_tree_children(tree))
    tree.selection_clear()
    queue = list(view_model['tree_datas'])
    item_counter = 0
    while len(queue) > 0:
        tree_data = queue.pop(0)
        parent: str = tree_data['parent']
        index_: str = tree_data.get('index', 'end')
        text: str = tree_data['text']
        values: tuple = tree_data['values']
        select_this_item: bool = tree_data['select_this_item']
        iid = tree_data.get('id', None)
        item_unique_tag = f'item_unique_tag_{item_counter}'
        tags: tuple = tree_data['tags'] + (item_unique_tag,)
        try:
            if iid is not None:
                item = tree.insert(parent, index_, text=text, iid=iid, values=values, tags=tags, open=True)
            else:
                item = tree.insert(parent, index_, text=text, values=values, tags=tags, open=True)
        except:
            queue.append(tree_data)  # put it back in the queue it needs parent to be first inserted
            continue
        if tree_data.get('background_color', None):
            tree.tag_configure(item_unique_tag, background=True)
        if tree_data.get('foreground_color', None):
            tree.tag_configure(item_unique_tag, foreground=True)
        overstrike = tree_data.get('strikethrough', False)
        underline = tree_data.get('underline', False)
        weight = tree_data.get('weight', 'normal')
        tree.tag_configure(item_unique_tag, font=font.Font(overstrike=overstrike, underline=underline, weight=weight))
        if select_this_item:
            tree.selection_add(item)
            tree.focus(item)
        item_counter += 1


def tree_initial_settings(tree: ttk.Treeview, view_model):
    if is_first_time_updating_the_tree(tree):
        headings: tuple = view_model['headings']
        widths: tuple = view_model['widths']
        stretches: tuple = view_model['stretches']
        need_scroll_v: bool = view_model['scroll_v']
        need_scroll_h: bool = view_model['scroll_h']
        text_width: bool = view_model.get('text_width', 0)

        tree['show'] = 'tree headings' if text_width > 0 else 'headings'
        if text_width > 0:
            tree.column('#0', width=text_width)
        tree['columns'] = tuple(n for n in range(len(headings)))
        for n, column_name in enumerate(headings):
            tree.heading(f'{n}', text=column_name)
        for n, (width, stretch) in enumerate(zip(widths, stretches)):
            tree.column(f'{n}', width=width, stretch=stretch)

        if need_scroll_v:
            parent = tree.master
            scroll = ttk.Scrollbar(parent, orient=tk.VERTICAL)
            scroll.configure(command=tree.yview)
            tree.configure(yscrollcommand=scroll.set)
            scroll.grid(row=0, column=1, sticky='ns')
        if need_scroll_h:
            parent = tree.master
            scroll = ttk.Scrollbar(parent, orient=tk.HORIZONTAL)
            scroll.configure(command=tree.xview)
            tree.configure(xscrollcommand=scroll.set)
            scroll.grid(row=1, column=0, sticky='we')


def is_first_time_updating_the_tree(tree: ttk.Treeview):
    return tree['columns'] == ''


def get_tree_selection_text(tree: ttk.Treeview) -> str:
    id_ = tree.focus()
    return tree.item(id_)['text']


def get_all_tree_children(tree: ttk.Treeview, item="") -> tuple:
    # recursively get all of the children of a tree
    children = tree.get_children(item)
    flat_order_children = ()
    for child in children:
        flat_order_children += (child,)
        flat_order_children += get_all_tree_children(tree, child)
    return tuple(flat_order_children)


def get_tree_values(tree: ttk.Treeview) -> dict:
    all_ids = get_all_tree_children(tree)
    selected_ids = tree.selection()
    focused_id = get_tree_focused_id(tree)

    tree_values = {'all_values': []}
    for tree_item_id in all_ids:
        values_ = tree.item(tree_item_id)['values']
        tree_values[tree_item_id] = {
            'is_selected': tree_item_id in selected_ids,
            'is_focused': tree_item_id == focused_id,
            'values': values_,
        }
        tree_values['all_values'].append(values_)
    tree_values['selected_ids'] = selected_ids
    tree_values['focused_id'] = focused_id

    return tree_values


def get_all_tree_values(tree: ttk.Treeview):
    return get_tree_values(tree)['all_values']


def tree_focused_values(tree: ttk.Treeview) -> tuple:
    return tree.item(get_tree_focused_id(tree))['values']


def tree_selected_values(tree: ttk.Treeview) -> tuple:
    selected_item_ids = tree.selection()
    all_values = get_tree_values(tree)
    return tuple(all_values[id_]['values'] for id_ in selected_item_ids)


def get_selected_tree_item_orders(tree: ttk.Treeview) -> tuple:
    all_item_ids = get_all_tree_children(tree)
    selected_item_ids = tree.selection()
    return tuple(all_item_ids.index(item_id) for item_id in selected_item_ids)


def get_tree_focused_id(tree: ttk.Treeview):
    id_ = tree.focus()
    return id_


def bind_tree(command: Callable, tree: ttk.Treeview):
    tree.bind('<<TreeviewSelect>>', lambda e: command())


def bind_tree_left_click(command: Callable, tree: ttk.Treeview):
    _bind_tree_click(1, tree, command)


def bind_tree_right_click(command: Callable, tree: ttk.Treeview):
    _bind_tree_click(2, tree, command)


def bind_tree_middle_click(command: Callable, tree: ttk.Treeview):
    _bind_tree_click(3, tree, command)


def bind_tree_left_click_release(command: Callable, tree: ttk.Treeview):
    _bind_tree_click_release(1, tree, command)


def bind_tree_right_click_release(command: Callable, tree: ttk.Treeview):
    _bind_tree_click_release(2, tree, command)


def bind_tree_middle_click_release(command: Callable, tree: ttk.Treeview):
    _bind_tree_click_release(3, tree, command)


def _bind_tree_click(n: int, tree: ttk.Treeview, command: Callable):
    tree.bind(f'<Button-{n}>', lambda e: command(get_value_from_tree_click_event(tree, e)))


def _bind_tree_click_release(n: int, tree: ttk.Treeview, command: Callable):
    tree.bind(f'<ButtonRelease-{n}>', lambda e: command(get_value_from_tree_click_event(tree, e)))


def get_value_from_tree_click_event(tree: ttk.Treeview, event):
    # select row under mouse
    row_id = tree.identify_row(event.y)
    col_id = tree.identify_column(event.x)
    if row_id:
        # mouse pointer over item
        tree.selection_set(row_id)
        tree.focus(row_id)

        try:
            column = int(col_id.replace('#', '')) - 1
        except:
            column = 0
        item_id = event.widget.focus()
        item = event.widget.item(item_id)
        values = item['values']
        return tree.get_children().index(row_id), column, values[column]
    else:
        # mouse pointer not over item
        # occurs when items do not fill frame
        # no action required
        return None, None, None


def select_multiple_tree_items(tree: ttk.Treeview, indexes: tuple):
    if indexes:
        tree_item_ids = tuple(get_all_tree_children(tree)[n] for n in indexes)
        tree.focus(tree_item_ids[0])
        tree.selection_set(tree_item_ids)


def tree_number_of_items(tree: ttk.Treeview) -> int:
    return len(get_all_tree_children(tree))


def select_tree(tree: ttk.Treeview, n_th: int = None):
    tree.focus_set()
    select_nth_item_in_the_tree(tree, n_th or 0)


def select_nth_item_in_the_tree(tree: ttk.Treeview, n):
    if has_something_to_select(tree, n):
        first_item_id = get_all_tree_children(tree)[n]
        select_tree_item(tree, first_item_id)


def has_something_to_select(tree: ttk.Treeview, index_: int) -> bool:
    return len(get_all_tree_children(tree)) > index_


def select_tree_item(tree: ttk.Treeview, tree_item_id):
    tree.focus(tree_item_id)
    tree.selection_set(tree_item_id)


def get_tree_id_from_position(tree_item_position: int, tree: ttk.Treeview):
    return get_all_tree_children(tree)[tree_item_position]


def add_treeview(options, parent, widget_class: Type[ttk.Treeview]):
    tree = widget_class(parent, **options)
    return tree


def focus_tree(widget, kwargs):
    try:
        tree_item_position = kwargs['tree_item_position'] or 0
    except KeyError:
        tree_item_position = 0

    if type(tree_item_position) in (int,):
        select_tree(widget, tree_item_position)
    else:
        select_multiple_tree_items(widget, tree_item_position)
        widget.focus_set()


def deselect_tree_items(tree: ttk.Treeview):
    for item in tree.selection():
        tree.selection_remove(item)
