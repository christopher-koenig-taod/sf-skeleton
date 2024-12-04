# README
Dieses Repository beinhaltet Code für Data Science Use Cases. 

__Wichtig__:
- Für jeden Use Case muss ein separater Ordner angelegt werden
- Zur lokalen Entwicklung nutzen wir Conda als Package Manager


## Lokales Set-Up
Set-Up des Conda-Environments:
- Erstelle eine Kopie der `conda_env.yml.example` und benenne sie in `conda_env.yml`
- Ersetze Setze dort die Werte der Umgebungsvariablen `SNOWFLAKE_USER` und `SNOWFLAKE_PASSWORD` mit deinem Snowflake Login
- Erstelle das Conda-Environments über: 
    ```
    conda env create -f conda_env.yml
    ```


Update des Conda-Environments:
- Exportiere alle installierten Dependencies mit:
    ```
    conda env export --from-history > conda_env.yml.example
    ```
- Lösche das mapping "prefix" 
- WICHTIG: Lösche die Werte der Umgebungsvariablen SNOWFLAKE_PASSWORD & SNOWFLAKE_USER

## Beheben von import-Problemen mit pillow
Erst alles via Conda installieren dann '''pip install pillow==10.4.0'''.
