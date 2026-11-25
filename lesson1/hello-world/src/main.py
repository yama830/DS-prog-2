import flet as ft


def main(page: ft.Page):

    #hello-world
    hello_world = ft.Text("Hello World" , size=50)

    #カウンター表示用のオブジェクト
    counter = ft.Text("0", size=50, data=0)

    #+ボタンがクリックされたときに呼び出される関数
    def increment_click(e: ft.Event[ft.FloatingActionButton]):
        counter.data += 1
        counter.value = str(counter.data)

    #-ボタンがクリックされたときに呼び出される関数
    def decrement_click(e: ft.Event[ft.FloatingActionButton]):
            counter.data -= 1
            counter.value = str(counter.data)

    #+ボタンを描画エリアに追加
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, key="increment", on_click=increment_click
    )

    #コンテンツを描画エリアに追加
    page.add(
        #実行環境に表示エリアを合わせるためのオブジェクト
        ft.SafeArea(
            expand=True,
            #パーツをまとめるオブジェクト
            content=ft.Container(
                #content = counter,
                content=ft.Column(controls=[hello_world, counter],alignment=ft.MainAxisAlignment.CENTER),
                alignment=ft.Alignment.CENTER,
            ),
        ),
    ft.FloatingActionButton(icon=ft.Icons.REMOVE, key="decrement", on_click=decrement_click),
    )


if __name__ == "__main__":
    ft.run(main)
