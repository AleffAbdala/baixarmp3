# Baixar MP3 do YouTube

Script simples em Python para baixar o áudio de vídeos do YouTube e converter para `mp3` usando `yt-dlp` e `ffmpeg`.

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
2. Cole o link do YouTube
3. Aguarde o download e a conversão

O arquivo será salvo em `~/Downloads`.

## Dependências

- `yt-dlp`: faz o download do áudio do vídeo
- `ffmpeg`: converte o áudio para `mp3`

## Observações

- O nome do arquivo é sanitizado com `restrictfilenames=True`
- A saída é gerada em `mp3` com qualidade `192 kbps`
- A conversão usa `44.1 kHz` e áudio estéreo
