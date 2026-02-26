name: Hourly DNS Update
on:
  schedule:
    - cron: '0 * * * *'
  workflow_dispatch:

jobs:
  run-updater:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install requests

      - name: Run IP Scanner
        run: python main.py

      - name: Commit and Push Changes
        run: |
          git config --global user.name "net-node-manager"
          git config --global user.email "bot@net-node-manager.studio"
          git add list.txt
          git commit -m "Automated IP update" || exit 0
          git push
