import argparse
from pathlib import Path

import yt_dlp
from yt_dlp.utils import DownloadError


DEFAULT_DOWNLOAD_DIR = Path.home() / "Downloads"
BITRATES_VALIDOS = ("128", "192", "256", "320")


def obter_url() -> str:
    return input("\nCole o link do video: ").strip()


def obter_bitrate() -> str:
    print("\nBitrates disponiveis:")
    print("Quanto maior o bitrate, melhor tende a ser a qualidade do audio.")
    for bitrate in BITRATES_VALIDOS:
        print(f"- {bitrate} kbps")

    bitrate = input("Escolha o bitrate [192]: ").strip()
    return bitrate or "192"


def validar_url(url: str) -> bool:
    return url.startswith(("http://", "https://"))


def validar_bitrate(bitrate: str) -> bool:
    return bitrate in BITRATES_VALIDOS


def criar_pasta_download(destino: Path) -> None:
    destino.mkdir(parents=True, exist_ok=True)


def montar_opcoes_ydl(destino: Path, bitrate: str) -> dict:
    return {
        "format": "bestaudio/best",
        "outtmpl": str(destino / "%(title)s.%(ext)s"),
        "restrictfilenames": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": bitrate,
            }
        ],
        "postprocessor_args": ["-ar", "44100", "-ac", "2"],
    }


def extrair_audio(
    url: str,
    destino: Path = DEFAULT_DOWNLOAD_DIR,
    bitrate: str = "192",
) -> None:
    if not validar_url(url):
        raise ValueError("Informe um link valido que comece com http:// ou https://.")

    if not validar_bitrate(bitrate):
        raise ValueError(
            f"Bitrate invalido. Use um destes valores: {', '.join(BITRATES_VALIDOS)}."
        )

    criar_pasta_download(destino)
    ydl_opts = montar_opcoes_ydl(destino, bitrate)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def processar_extracao(url: str, destino: Path, bitrate: str) -> None:
    try:
        extrair_audio(url, destino, bitrate)
        print(f"\nArquivo salvo em: {destino}")
        print(f"Bitrate escolhido: {bitrate} kbps")
        print("\nExtracao concluida com sucesso.\n")
    except ValueError as error:
        print(f"\nErro de validacao: {error}\n")
    except DownloadError as error:
        print(f"\nErro ao processar o link informado: {error}\n")
    except FileNotFoundError:
        print("\nErro: ffmpeg nao foi encontrado no sistema.\n")
    except Exception as error:
        print(f"\nErro inesperado: {error}\n")


def baixar_mp3_interativo() -> None:
    url = obter_url()
    bitrate = obter_bitrate()
    processar_extracao(url, DEFAULT_DOWNLOAD_DIR, bitrate)


def criar_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Extrai e converte o audio de um video para MP3."
    )
    parser.add_argument("url", nargs="?", help="Link do video")
    parser.add_argument(
        "-b",
        "--bitrate",
        default="192",
        choices=BITRATES_VALIDOS,
        help="Bitrate do arquivo MP3",
    )
    return parser


def menu() -> None:
    while True:
        print("==== MENU ====")
        print("1 - Extrair audio em MP3")
        print("0 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            baixar_mp3_interativo()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opcao invalida.\n")


def main() -> None:
    parser = criar_parser()
    args = parser.parse_args()

    if args.url:
        processar_extracao(
            url=args.url,
            destino=DEFAULT_DOWNLOAD_DIR,
            bitrate=args.bitrate,
        )
        return

    menu()


if __name__ == "__main__":
    main()
