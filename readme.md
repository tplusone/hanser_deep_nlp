## Repository zum Hanser-Buch *Deep Natural Language Processing* (2022)
### Arbeiten mit dem Repository 
Die Ordner des Repositorys sind entlang der Kapitel des Buches organisiert. 
In den Kapiteln finden Sie jeweils die Codebeispiel als *Jupyter Notebooks* (\*.ipynb-Dateien). 
Sie können das komplette Repository entweder auf ihren Rechner herunterladen oder auf die Jupyter Notebooks direkt im Internet zugreifen 
und den Code und die Resultate einsehen.<br><br>
Wenn Sie das Repository herunterladen möchten, müssen Sie *git* auf ihrem Rechner installiert haben. Die Software ist kostenlos verfügbar
zum Beispiel unter *https://git-scm.com/downloads*. Wenn Sie die Software installiert haben, können Sie das komplette Repository
aus dem Terminal-Fenster mit folgendem Befehl lokal speichern:<br>
**git clone https://github.com/tplusone/hanser_deep_nlp.git** 
<br>
### Virtuelle Umgebung
Die Datei **environmet.yml** enthält alle Python-Bibliotheken, die zur Ausführung der Codebeispiele notwendig sind. 
Wenn Sie eine virtuelle Umgebung in Anaconda anlegen möchten, die diese Bibliotheken enthält, navigieren Sie über das Anaconda-Terminalfenster
(Anaconda Prompt) einfach in den Basisordner des Repositories (*deep_nlp*) und geben dann folgenden Befehl ein:<br>
*conda env create -f environment.yml* <br>
Nach Fertigstellung der Environment lässt sich die Umgebung mit *conda activate deep_nlp* einfach aktivieren.<br>
Alternativ können Sie die notwendigen Bibliotheken natürlich auch manuell installieren. Sie benötigen im Wesentlichen folgende Module:<br>
*matplotlib, Version=3.4.2<br>
nltk, Version=3.6.2<br>
numpy, Version=1.19.2<br>
pandas, Version=1.0.3<br>
scikit-learn, Version=0.22.1<br>
tensorflow, Version=2.3.0<br>
transformers, Version=4.10.2*
