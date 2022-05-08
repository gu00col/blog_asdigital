#!/bin/bash
echo "Adicionando agente"
./ssh-add.sh
echo "Iniciando push"
git add .
echo "Arquivos adicionados"
git commit -a -m "Push Automatizado"
echo "Iniciando o push"
git push
echo "Fim do script"