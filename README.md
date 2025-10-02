# 仮想環境の構築

- バージョンの環境によって動かない場合，仮想環境に作って対処する方法を記す
    - 仮想環境の生成(myenvのところはすきな名前で)
      ```
      python -m venv venv
      ```
    - 仮想環境のアクティベート(macOSの場合)
      ```
      source venv/bin/activate
      ```
    - 仮想環境のアクティベート(Windowsの場合)
      ```
      venv\Scripts\activate
      ```
    - 必要なパッケージをインストール(requirements.txtにもう記述してます)
      ```
      pip install -r requirements.txt
      ```
    - 出る時
      ```
      deactivate
      ```