#!/bin/bash
echo "⚡ Instalando StormScan..."
pip3 install -r requirements.txt
chmod +x main.py
sudo ln -s $(pwd)/main.py /usr/local/bin/stormscan
echo "✅ Instalación completa. Usa 'stormscan <target>'"
