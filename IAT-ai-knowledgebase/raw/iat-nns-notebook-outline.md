<!-- Raw source: the Markdown cells of iat_demo.ipynb (IAT-nns-for-students), extracted in order on 2026-11-13. Language: German. Code cells and outputs are not included. -->

### Drehbuch 1.5h Einleitung neuronale Netze

1) Lineare Regression als Modell mit einem Parameter
2) Summe der Residuen als Fehlerfunktion
3) Ableitung als Richtung zum Minimum
4) Micrograd für lineare Regression mit einem Parameter
5) Visuelle Darstellung des Berechnungsgraphen bei linearer Regression
6) Micrograd für lineare Regression mit zwei Parametern
7) Klassifikationsdemo mit nur einem Neuron
8) Klassifikationsdemo mit neuronalem Netz
9) MNIST Klassifikation (eigenes Skript)

#### Lineare Regression mit einem Parameter (Steigung der Geraden)

Animierte Darstellung nur Gerade

Animierte Darstellung mit Residuen

#### Summe der Residuenquadrate als Fehlerfunktion

Animierte Darstellung Modell neben Fehlerfunktion

#### Ableitung als Richtung zum Minimum

Animation zur Veranschaulichung des Begriffs _Ableitung_

#### Micrograd für lineare Regression mit einem Parameter

Das Modell

Veränderung des Parameters $beta_1$ in Richtung der negativen Ableitung (Gradienten)

Animation erstellen

#### Visuelle Darstellung des Berechnungsgraphen bei linearer Regression

Mit nur einem Datenpunkt, um die Struktur zu zeigen. Zuerst die Hilfsfunktionen zur Darstellung.

Ein konkretes Beispiel angeben

Händische Berechnung zur Verifikation, dass Gradientenabstieg funktioniert

Komplizierterer Graph für lineare Regression mit drei Datenpunkten

Gleich wie oben: Händische Berechnung zur Verifikation, dass Gradientenabstieg funktioniert

#### Micrograd für lineare Regression mit zwei Parametern

Das Modell

Fehlerminimierung durch Gradientenabstieg

Visuelle Darstellung

#### Klassifikationsdemo mit nur einem Neuron

Das Netz und die Daten

Trainieren des einzelnen Neurons, wiederum durch Gradientenabstieg

Darstellung des Trainingsfortschritts

#### Klassifikationsdemo mit einem ganzen neuronalen Netz (adaptiert nach Vorlage von Andrej Karpathy)

Die Daten

Das Modell

Die Fehlerfunktion

Vorbereitung der visuellen Darstellung

Trainieren des neuronalen Netzes

Berechnung der Animation

#### MNIST Klassifikation (eigenes Skript)

weiter mit /opt/pytorch-env/IAT-MNIST/mnist-pytorch.py
