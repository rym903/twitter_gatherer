# poetry.lockからrequirements.txtを作成
poetry export -f requirements.txt --output requirements.txt
gcloud functions deploy crawler \
    --gen2 \
    --region asia-east2 \
    # chromeのversionにより、3.9以上だとバグが発生する....
    --runtime python38  \
    --allow-unauthenticated  \
    --trigger-http