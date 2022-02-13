import tkinter as tk
from tkinter import ttk
from typing import Callable
from typing import Type

widget_tree_view = ttk.Treeview


def update_tree(tree: ttk.Treeview, view_model):
    tree_initial_settings(tree, view_model)

    tree.delete(*get_all_tree_children(tree))
    tree.selection_clear()
    for tree_data in view_model['tree_datas']:
        parent: str = tree_data['parent']
        index_: str = tree_data.get('index', 'end')
        text: str = tree_data['text']
        values: tuple = tree_data['values']
        tags: tuple = tree_data['tags']
        select_this_item: bool = tree_data['select_this_item']
        iid = tree_data.get('id', None)
        if iid is not None:
            item = tree.insert(parent, index_, text=text, iid=iid, values=values, tags=tags)
        else:
            item = tree.insert(parent, index_, text=text, values=values, tags=tags)
        if select_this_item:
            tree.selection_add(item)
            tree.focus(item)


def tree_initial_settings(tree: ttk.Treeview, view_model):
    if is_first_time_updating_the_tree(tree):
        headings: tuple = view_model['headings']
        widths: tuple = view_model['widths']
        stretches: tuple = view_model['stretches']
        need_scroll_v: bool = view_model['scroll_v']
        need_scroll_h: bool = view_model['scroll_h']

        tree['show'] = 'tree headings'
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
        flat_order_children += (child, )
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
    tree.bind(f'<ButtonRelease-{1}>', lambda e: command())
    tree.bind(f'<ButtonRelease-{2}>', lambda e: command())
    tree.bind(f'<ButtonRelease-{3}>', lambda e: command())


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
