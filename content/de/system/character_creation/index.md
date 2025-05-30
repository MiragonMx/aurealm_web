---
title: "Arkanthia Regelwerk - Charaktererstellung"
draft: false
math: true
publishdate: 2024-04-29T09:00:00+02:00
summary: "Hier werdet ihr einmal exemplarisch durch eine Charaktererstellung geführt."
thumbnail: img/Charaktererstellung (4_3).png
---

Hier ist natürlich grundlegend einmal wichtig, eurem Charakter einen Namen, ein Alter und eine Geschichte zu geben. Versucht euch zu überlegen, was die Ziele eures Charakters im Leben sind, was ihn bisher beeinflusst hat, welche Werte ihm wichtig sind und ob er irgendwelche Ticks oder Verhaltensmuster hat. Macht euch hier wirklich in Ruhe Gedanken und überlegt euch, welchen Charakter ihr selbst spielen und auch ausleben wollt.
Nun geht es an die Vergabe der Werte. Der hier vorgestellte Beispielscharakter soll den Namen Verlon haben, der mit 21 Jahren noch recht jung ist. Verlon ist nicht der hellste, physisch aber sehr gut aufgestellt. Charisma und Geschicklichkeit sind bei ihm leicht unterdurchschnittlich. So ergeben sich folgende Attributs-Werte:

* **Stärke:** 7
* **Geschicklichkeit:** 4
* **Konstitution:** 8
* **Intelligenz:** 2
* **Charisma:** 4

Verlon möchte keine <a class="glossary-link" href={{<ref "glossary/things/magic">}} >Magie</a> lernen, vergibt also auch keine FPs in diese Fähigkeit, kann dies später aber bei jedem Levelaufstieg nachholen. Damit ergeben sich für ihn folgende Werte:

{{<table>}}
| Wert <img width=300/> | Formel <img width=300/> | Verlons Wert <img width=300/> |
| :---: | :---: | :---: |
| Trefferpunkte | \((\frac{Stärke}{2} + \frac{Konstitution}{4}) \cdot Level + 10\) | \((\frac{7}{2} + \frac{4}{4}) \cdot 1 + 10 = 15.5\) |
| TP-Regeneration / h | \((\frac{max.\ \ TP}{10}) - X (Art\ \ der\ \ Verletzung)\) | \((\frac{15.5}{10} + \frac{4}{4}) - 0 = 1.6 (gerundet)\) |
| Mana-Punkte | \((\frac{Intelligenz \cdot Level}{2}) + Magiefähigkeit \cdot 10\) | \((\frac{2 \cdot 1}{2}) + 0 \cdot 10 = 1\) |
| Mana-Regeneration / h | \((\frac{max.\ \ Mana}{10})\) | \((\frac{1}{10}) = 0.1 \) |
| Mentale Belastbarkeit | \((\frac{Charisma \cdot Level}{2}) + 50 \) | \((\frac{4 \cdot 1}{2}) + 50 = 52\) |
| MB-Regeneration / h | \((\frac{max.\ \ MB}{10}) - X (Art\ \ der\ \ Verstörung)\) | \((\frac{52}{10}) = 5.2 \) |
| Initiative | \((\frac{Stärke + 20}{Geschicklichkeit})\) | \((\frac{7 + 20}{4}) = 6.8 (gerundet) \) |
| Reichweite | \((\frac{Konstitution + Geschicklichkeit}{2})\) | \((\frac{8 + 4}{2}) = 6 \) |
| Ausweichen | \((\frac{Geschicklichkeit}{2})\) | \((\frac{4}{2}) = 2 \) |
{{</table>}}

Damit hat Verlon schon mal viele wichtige Werte berechnet. Nun will er seine anfänglichen 150 Fähigkeitspunkte verteilen. Er entscheidet sich dazu *Einhändig 14* (29 FP), *Faustkampf 5* (6 FP) und *Jagen 9* (14 FP) in der Begabung *Handeln* zu leveln. Somit hat er insgesamt 49 FP in der Begabung vergeben. Um den Begabungswert von *Handeln* nun zu berechnen, muss er \(Begabungswert = \frac{\sum Fähigkeitsspunkte}{10} \le 8\) berechnen. In Verlons Fall wäre dies also: \(Begabungswert = \frac{49}{10} = 4.9 \leq 8\). Sein Begabungswert für *Handeln* wird nun auf 5 aufgerundet. Auf diesen kann er nun immer würfeln, wenn er eine Handlung ausführen möchte, die richtige Fähigkeit aber nicht gelernt hat. Außerdem werden alle seine Fähigkeiten in der Begabung *Handeln* durch sein Attribut **Konstitution** verbessert. Hierzu muss der Attributwert (Verlon hat **Konstitution 8**) durch vier geteilt werden (\(+ \frac{8}{4} = +2\)). Somit werden alle *Handeln*-Fähigkeiten um +2 verbessert, weshalb er nun *Einhändig 16*, *Faustkampf 7* und *Jagen 11* hat.

In *Soziales* lernt Verlon folgende Fähigkeiten: *Flirten 10* (17 FP), *Begeistern 6* (8 FP), *Humor 12* (23 FP) und *Überzeugen 8* (12 FP). Insgesamt hat er in *Soziales* somit 60 FP vergeben, woraus ein Begabungswert von 6 resultiert. Durch seinen Attributswert **Charisma** von 4 erhält Verlon auch hier +1 auf alle seine Fähigkeiten der Begabung *Soziales*.

Jetzt hat Verlon noch 41 FPs, die er in der Begabung *Wissen* vergeben kann. Er entscheidet sich dazu, 26 FP in Religion zu investieren (*Religion 11*). Außerdem levelt er *Holzbearbeitung 8* (12 FP) und *Medizin 3* (3 FP). Dafür ergibt sich ein Begabungswert von 4.1, also 4. Durch das Attribut **Intelligenz** von 2 berechnet sich eine Verbesserung der Begabung von 0.5, welche auf 1 gerundet wird und ihm +1 auf alle *Wissens*-Fähigkeiten gibt.

Außerdem kann Verlon jetzt die fünf Standardfähigkeiten ergänzen, dann ist er mit seiner Charaktererstellung fertig.
