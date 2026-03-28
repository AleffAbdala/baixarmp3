# Extrair e Converter Audio para MP3

Script simples em Python para extrair e converter o audio de um video para `mp3` usando `yt-dlp` e `ffmpeg`.

## Requisitos

- Python 3.10 ou superior
- `ffmpeg` instalado no sistema

## Instalação

1. Clone ou acesse a pasta do projeto.
2. Crie um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Instalar o ffmpeg

Ubuntu/Debian:

```bash
sudo apt install ffmpeg
```

macOS com Homebrew:

```bash
brew install ffmpeg
```

Windows com winget:

```powershell
winget install Gyan.FFmpeg
```

## Como usar

Execute o script:

```bash
python3 baixar_mp3.py
```

Depois:

1. Escolha a opção `1`
2. Cole o link do video
3. Escolha o bitrate ou pressione `Enter` para usar `192`
4. Aguarde a extração e a conversão

O arquivo sera salvo em `~/Downloads`.

## Uso por linha de comando

Tambem e possivel informar os dados diretamente pela linha de comando:

```bash
python3 baixar_mp3.py "LINK_DO_VIDEO"
```

Definindo o bitrate:

```bash
python3 baixar_mp3.py "LINK_DO_VIDEO" --bitrate 320
```

## Dependências

- `yt-dlp`: processa o link informado e extrai o audio
- `ffmpeg`: converte o áudio para `mp3`

## Observações

- O nome do arquivo é sanitizado com `restrictfilenames=True`
- A saida e gerada em `mp3` com bitrate configuravel: `128`, `192`, `256` ou `320`
- A conversão usa `44.1 kHz` e áudio estéreo
