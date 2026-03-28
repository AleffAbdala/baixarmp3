import os
import yt_dlp

def baixar_mp3():
    url = input("\nCole o link do YouTube: ")

    download_path = os.path.expanduser("~/Downloads")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
        'restrictfilenames': True,  # 🔥 remove caracteres bugados
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'postprocessor_args': [
            '-ar', '44100',  # padrão universal
            '-ac', '2'
        ],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n✅ Download concluído!\n")
    except Exception as e:
        print(f"\n❌ Erro: {e}\n")


def menu():
    while True:
        print("==== MENU ====")
        print("1 - Baixar música (MP3)")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            baixar_mp3()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")


if __name__ == "__main__":
    menu()