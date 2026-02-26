name: Hourly DNS Update
on:
  schedule:
    - cron: '0 * * * *'
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3
        with:
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install requests

      - name: Run Script
        run: python main.py

      - name: Commit and Push Changes
        run: |
          git config --global user.name "net-node-manager"
          git config --global user.email "bot@net-node-manager.studio"
          git add list.txt
          git commit -m "Automated IP update" || exit 0
          git push
