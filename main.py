import flet as ft
# from write_paths import write_paths # テキストに書き込んで保存しておく
from backup import backup_with_timestamp # バックアップ実行

target_paths = []

# -------------------- #
#      LIST BOX        #
# -------------------- #
def list_box():
    target_path_viewer = ft.Column(controls=[])

    for target_path in target_paths:
        row =ft.ListTile(
            title=ft.Text(value=target_path),
            trailing=ft.IconButton(
                icon=ft.icons.DELETE,
                icon_color=ft.colors.RED,
                on_click=delete_path
            )
        )
        target_path_viewer.controls.append(row)

    
    wrapper = ft.Container(
        content=target_path_viewer if len(target_paths) > 0 else ft.Text("バクアップするフォルダ、または、ファイルを選択してください"),
        bgcolor=ft.colors.SURFACE_VARIANT,
        padding=ft.padding.all(5),
        border_radius=ft.border_radius.all(5),
        margin=ft.margin.all(5),
    )

    return wrapper

def delete_path(e):
    target_paths.remove(e.control.parent.title.value)
    e.page.controls[2]= list_box()
    e.page.update()
    pass

# -------------------- #
#  FILE PICKER BUTTON  #
# -------------------- #
def picker_btns(page):
    def pick_file_result(e: ft.FilePickerResultEvent):
        target_paths.append(e.files[0].path)
        page.controls[2]= list_box()
        page.update()

    def pick_fldr_result(e: ft.FilePickerResultEvent):
        target_paths.append(e.path)
        page.controls[2] = list_box()
        page.update()

    pick_file_dialog = ft.FilePicker(on_result=pick_file_result)
    pick_fldr_dialog = ft.FilePicker(on_result=pick_fldr_result)
    page.overlay.extend([pick_file_dialog, pick_fldr_dialog])

    add_file_btn = ft.ElevatedButton(
        "Add Files",
        icon=ft.icons.FILE_OPEN,
        on_click=lambda\
            e: pick_file_dialog.pick_files(allow_multiple=True), 
     ) 
    add_fldr_btn = ft.ElevatedButton(
        "Add Folder",
        icon=ft.icons.FOLDER_OPEN,
        on_click=lambda\
            e: pick_fldr_dialog.get_directory_path(),
    )
    return ft.Row(
        controls=[add_file_btn, add_fldr_btn]
    )

# -------------------- #
#     EXECUTE BTN      #
# -------------------- #
def exe_btn():
    return ft.Row(
        controls=[ft.ElevatedButton(
            "Backup 実行",
            on_click=backup
        )],
        alignment=ft.MainAxisAlignment.CENTER,
    )

def backup(e): # イベントハンドラーの時は、(e)が必須! そうしないと、エラーになる
    backup_with_timestamp(target_paths)
    
# ====================== #
#     MAIN FUNCTION      #
# ====================== #
def main(page: ft.Page):
    page.title = "Backup Tool"
    page.add(picker_btns(page), ft.Divider(), list_box(), exe_btn())

ft.app(target=main)