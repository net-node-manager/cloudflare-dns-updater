name: Hourly DNS Update
on:
  schedule:
    - cron: '0 * * * *'
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: pip install requests
      - name: Run Script
        run: python main.py
      - name: Commit and Push
        run: |
          git config --global user.name 'net-node-manager'
          git config --global user.email 'bot@net-node-manager.com'
          git add list.txt
          git commit -m "Update IP list" || exit 0
          git push
