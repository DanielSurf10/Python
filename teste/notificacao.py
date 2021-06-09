from win10toast import ToastNotifier

notificacao = ToastNotifier()

notificacao.show_toast("Atenção!",
                       "Falta 1 minuto",
                       icon_path="livro.ico")
