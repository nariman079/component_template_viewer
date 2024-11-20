#!/bin/bash

# Проверка, что передано два аргумента
if [ "$#" -ne 2 ]; then
  echo "Использование: ./action.sh <environment> <action>"
  echo "Пример: ./action.sh prod run"
  exit 1
fi

# Аргументы
ENVIRONMENT=$1
ACTION=$2

# Проверка аргумента среды
case $ENVIRONMENT in
  local)
    case $ACTION in
      run)
        docker compose -f database.yaml -f docker-compose.local.yaml up
        ;;
      build)
        docker compose -f database.yaml -f docker-compose.local.yaml up --build
        ;;
      down)
        docker compose -f database.yaml -f docker-compose.local.yaml down
        ;;
      *)
        echo "Неизвестное действие: $ACTION. Доступные действия для PROD: run, down"
        exit 1
        ;;
    esac
    ;;
  *)
    echo "Неизвестная среда: $ENVIRONMENT. Доступные среды: prod"
    exit 1
    ;;
esac
