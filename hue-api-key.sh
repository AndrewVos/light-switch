#!/usr/bin/env bash

set -euo pipefail
IFS=$'\n\t'

HUE_IP=$(curl https://www.meethue.com/api/nupnp 2> /dev/null | cut -d '"' -f 8)

function create-hue-user() {
  curl \
    --request POST \
    --header "Accept: application/json" \
    --data '{"devicetype":"my_hue_app#andrew"}' \
    "http://$HUE_IP/api"
}

RESULT=$(create-hue-user)
if [[ "$RESULT" =~ "link button not pressed" ]]; then
  echo
  echo "Press the button on the Hue and then press ENTER..."
  read
fi
KEY=$(create-hue-user | cut -d '"' -f 6)
echo "Your Hue API key: $KEY"
