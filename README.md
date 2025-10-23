
# 📱 Social Media Campaign Performance Tracker

**Future Interns - Data Science & Analytics Internship**  
**Task 2 | Track Code: DS**  
**Intern: KHALID AG MOHAMED ALY**  
**Internship Period: October 16 - November 16, 2025**

---

## 🎯 Objectif du Projet

Analyser les performances des campagnes publicitaires sur les réseaux sociaux (Facebook/Instagram) pour évaluer :
- L'engagement des publications
- Le taux de clics (CTR - Click-Through Rate)
- Le retour sur investissement (ROI)
- Les meilleures pratiques marketing
- L'optimisation des campagnes

---

## 🛠️ Technologies Utilisées

- **Python** : Analyse et traitement des données
- **Pandas & NumPy** : Manipulation de données
- **Matplotlib & Seaborn** : Visualisations
- **Power BI / Google Looker Studio** : Dashboard interactif
- **Excel/Google Sheets** : Analyse complémentaire
- **Canva** (optionnel) : Présentation visuelle

---

## 📁 Structure du Projet

```
FUTURE_DS_02/
│
├── README.md
├── data/
│   ├── campaign_data.csv
│   └── data_cleaned.csv
│
├── notebooks/
│   └── campaign_analysis.ipynb
│
├── scripts/
│   ├── data_generator.py
│   └── performance_analyzer.py
│
├── dashboards/
│   ├── campaign_dashboard.pbix
│   ├── looker_studio_dashboard.pdf
│   └── screenshots/
│
├── reports/
│   ├── campaign_insights.md
│   └── roi_analysis.pdf
│
└── visuals/
    └── charts/
```

---

## 📊 Dataset - Métriques de Campagne

Le dataset contient les informations suivantes :

### Colonnes Principales :
- **Campaign ID** : Identifiant unique de campagne
- **Campaign Name** : Nom de la campagne
- **Platform** : Plateforme (Facebook/Instagram)
- **Campaign Type** : Type (Awareness/Engagement/Conversion)
- **Start Date** : Date de début
- **End Date** : Date de fin
- **Budget** : Budget alloué ($)
- **Impressions** : Nombre d'impressions
- **Reach** : Portée (utilisateurs uniques)
- **Clicks** : Nombre de clics
- **Engagement** : Interactions totales (likes, comments, shares)
- **Conversions** : Nombre de conversions
- **Revenue** : Revenu généré ($)

---

## 🔍 Métriques Calculées (KPIs)

### 1. Métriques d'Engagement
```
• CTR (Click-Through Rate) = (Clicks / Impressions) × 100
• Engagement Rate = (Engagement / Reach) × 100
• CPC (Cost Per Click) = Budget / Clicks
• CPM (Cost Per Mille) = (Budget / Impressions) × 1000
```

### 2. Métriques de Conversion
```
• Conversion Rate = (Conversions / Clicks) × 100
• Cost Per Conversion = Budget / Conversions
• ROAS (Return on Ad Spend) = Revenue / Budget
• ROI = ((Revenue - Budget) / Budget) × 100
```

### 3. Métriques d'Efficacité
```
• Frequency = Impressions / Reach
• Cost Per Engagement = Budget / Engagement
• Revenue Per Click = Revenue / Clicks
```

---

## 📈 Analyses Effectuées

### 1. Analyse de Performance Globale
- Vue d'ensemble des campagnes
- KPIs agrégés
- Comparaison entre plateformes

### 2. Analyse par Type de Campagne
- Performance Awareness vs Engagement vs Conversion
- Budget allocation optimal
- ROI par type

### 3. Analyse Temporelle
- Tendances des performances
- Meilleurs jours/heures de publication
- Saisonnalité des campagnes

### 4. Analyse Comparative
- Facebook vs Instagram
- Campagnes gagnantes vs perdantes
- Benchmarking des métriques

### 5. Optimisation Budget
- Recommandations d'allocation
- Campagnes sous-performantes à arrêter
- Opportunités de scaling

---

## 💡 Insights Principaux

### Performance Globale
- **Budget Total Investi** : $XXX,XXX
- **Revenu Total Généré** : $XXX,XXX
- **ROI Moyen** : XX%
- **CTR Moyen** : X.XX%
- **Taux de Conversion** : X.XX%

### Top Performers
1. **Meilleure Campagne** : [Nom] - ROI de XXX%
2. **Meilleure Plateforme** : [Facebook/Instagram]
3. **Meilleur Type** : [Awareness/Engagement/Conversion]

### Recommandations
✅ Augmenter le budget sur les campagnes à ROI > 200%  
✅ Optimiser le CTR des campagnes sous la moyenne  
✅ Tester de nouveaux formats sur Instagram  
✅ Réduire les dépenses sur les campagnes à ROI < 50%

---

## 🎨 Dashboard Interactif

Le dashboard inclut :

### Page 1 : Vue d'Ensemble
- KPIs principaux (Budget, ROI, CTR, Conversions)
- Graphique de tendance ROI
- Comparaison Facebook vs Instagram
- Top 5 campagnes

### Page 2 : Analyse Détaillée
- Performance par type de campagne
- Analyse temporelle
- Distribution du budget
- Funnel de conversion

### Page 3 : Optimisation
- Matrice performance-budget
- Recommandations automatiques
- Prédictions de ROI
- Allocation budget optimale

**Voir les captures d'écran dans** : `dashboards/screenshots/`

---

## 🚀 Comment Utiliser ce Projet

### Prérequis
```bash
pip install pandas numpy matplotlib seaborn jupyter scikit-learn
```

### Étapes d'Exécution

1. **Générer le Dataset**
```bash
python scripts/data_generator.py
```

2. **Lancer l'Analyse**
```bash
jupyter notebook notebooks/campaign_analysis.ipynb
```

3. **Créer le Dashboard**
- Ouvrir Power BI Desktop
- Importer `data/data_cleaned.csv`
- Suivre le guide dans `dashboards/powerbi_guide.md`

4. **Alternative Google Looker Studio**
- Importer dans Google Sheets
- Connecter à Looker Studio
- Utiliser les templates fournis

---

## 📊 Visualisations Clés

### Graphiques Inclus :
1. **Line Chart** : Évolution du ROI dans le temps
2. **Bar Chart** : Comparaison performances par plateforme
3. **Scatter Plot** : Budget vs ROI
4. **Heatmap** : Performance par jour/heure
5. **Funnel Chart** : Parcours de conversion
6. **Bubble Chart** : Budget vs Engagement vs Conversions
7. **Pie Chart** : Distribution du budget
8. **Waterfall Chart** : Contribution au revenu total

---

## 📝 Compétences Développées

✅ Marketing Analytics  
✅ Calcul de KPIs publicitaires  
✅ Analyse ROI et ROAS  
✅ Optimisation de campagnes  
✅ A/B Testing conceptuel  
✅ Data Storytelling  
✅ Dashboard Design  
✅ Business Intelligence  

---

## 🔗 Ressources Complémentaires

### Documentation
- [Facebook Ads Reporting](https://www.facebook.com/business/help)
- [Instagram Insights Guide](https://business.instagram.com)
- [Google Analytics 4](https://analytics.google.com)

### Benchmarks Industrie
- CTR moyen : 0.5% - 2%
- Taux de conversion moyen : 2% - 5%
- ROI cible : > 200%
- Cost Per Click : $0.50 - $2.00

---

## 📧 Contact

**Intern** : KHALID AG MOHAMED ALY  
**LinkedIn** : [https://www.linkedin.com/in/khalid-ag-mohamed-aly/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BOTy5sIGKRLSuhk48ofeccg%3D%3D]  
**Email** : [alansarymohamed38@gmail.com]  

---

## 📜 License

Ce projet fait partie du programme de stage Future Interns - Data Science & Analytics Track.

**Internship ID** : FIT/OCT25/DS8272

---

## 🏆 Résultats et Impact

### Métriques de Succès :
- ✅ XX campagnes analysées
- ✅ $XXX,XXX de budget optimisé
- ✅ XX% d'amélioration du ROI potentiel
- ✅ XX recommandations actionnables

### Cas d'Usage Réels :
Ce type d'analyse permet aux entreprises de :
- Économiser 20-30% du budget marketing
- Augmenter le ROI de 50-100%
- Identifier rapidement les campagnes inefficaces
- Prendre des décisions data-driven

---

*Dernière mise à jour : [Date]*  
*Version : 1.0*
