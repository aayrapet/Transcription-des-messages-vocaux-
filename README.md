# 🗣️ Transcription de messages vocaux

## 🎯 Objectif
Ce projet a pour objectif de **convertir un message vocal en texte** avec **horodatage** et **résumé automatique**.  
Il vise à faciliter l’analyse et la synthèse de conversations, réunions ou messages vocaux grâce à une interface API simple et efficace.

---

## ⚙️ Technologies utilisées
- **Flask** — Framework web pour créer l’API REST  
- **OpenAI Whisper API** / **SpeechRecognition** — Transcription vocale (speech-to-text)  
- **spaCy** — Résumé automatique du texte  
- **Pytest** — Tests unitaires  
- **Docker** — Conteneurisation et déploiement reproductible  

---

## 🧩 Fonctionnalités principales
1. **Upload d’audios** via une API Flask (`/upload`)  
2. **Transcription automatique** du fichier audio en texte  
3. **Horodatage** des segments audio pour une lecture synchronisée  
4. **Nettoyage et formatage** du texte transcrit  
5. **Résumé automatique** du texte final à l’aide de spaCy  
6. **Tests unitaires** pour valider le bon fonctionnement de chaque étape  

---

## 🚧 Défis techniques
- Traitement de **gros fichiers audio**
- Amélioration de la **précision selon le niveau de bruit**
- Gestion et **stockage efficace** des fichiers audio temporaires
- Maintien des performances de l’API sous forte charge  

---

## 🧱 Architecture du projet

