"""
Script pour générer des données de campagnes publicitaires
Future Interns - Task 2: Social Media Campaign Performance Tracker
Author: KHALID AG MOHAMED ALY
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configuration
np.random.seed(42)
random.seed(42)

# Nombre de campagnes
n_campaigns = 100

# Listes de données
campaign_types = ['Awareness', 'Engagement', 'Conversion']
platforms = ['Facebook', 'Instagram']

# Templates de noms de campagne
campaign_templates = {
    'Awareness': [
        'Brand Awareness Q{}', 'Product Launch {}', 'New Collection {}',
        'Seasonal Campaign {}', 'Brand Story {}'
    ],
    'Engagement': [
        'Engagement Boost {}', 'Community Building {}', 'Interactive Contest {}',
        'User Generated Content {}', 'Poll Campaign {}'
    ],
    'Conversion': [
        'Flash Sale {}', 'Limited Offer {}', 'Retargeting Campaign {}',
        'Holiday Promotion {}', 'Black Friday {}'
    ]
}

# Générer les dates (derniers 6 mois)
end_date = datetime.now()
start_date = end_date - timedelta(days=180)

# Fonction pour générer des métriques réalistes
def generate_campaign_metrics(campaign_type, platform, budget):
    """Génère des métriques réalistes basées sur le type et la plateforme"""
    
    # Facteurs d'influence
    type_factors = {
        'Awareness': {'ctr': 0.008, 'engagement': 0.02, 'conversion': 0.01},
        'Engagement': {'ctr': 0.015, 'engagement': 0.05, 'conversion': 0.015},
        'Conversion': {'ctr': 0.02, 'engagement': 0.03, 'conversion': 0.03}
    }
    
    platform_multipliers = {
        'Facebook': {'reach': 1.2, 'ctr': 1.0, 'cpc': 1.0},
        'Instagram': {'reach': 1.0, 'ctr': 1.3, 'cpc': 1.15}
    }
    
    # Récupérer les facteurs
    factors = type_factors[campaign_type]
    multipliers = platform_multipliers[platform]
    
    # Calculer les métriques de base
    # CPM entre $5 et $15
    cpm = random.uniform(5, 15)
    impressions = int((budget / cpm) * 1000)
    
    # Reach (80-95% des impressions)
    reach = int(impressions * random.uniform(0.80, 0.95) * multipliers['reach'])
    
    # Clicks basés sur CTR
    base_ctr = factors['ctr'] * multipliers['ctr']
    ctr_variation = random.uniform(0.7, 1.3)  # Variation ±30%
    actual_ctr = base_ctr * ctr_variation
    clicks = int(impressions * actual_ctr)
    
    # Engagement
    base_engagement_rate = factors['engagement']
    engagement_variation = random.uniform(0.8, 1.4)
    actual_engagement_rate = base_engagement_rate * engagement_variation
    engagement = int(reach * actual_engagement_rate)
    
    # Conversions
    base_conversion_rate = factors['conversion']
    conversion_variation = random.uniform(0.6, 1.5)
    actual_conversion_rate = base_conversion_rate * conversion_variation
    conversions = int(clicks * actual_conversion_rate)
    
    # Revenue (basé sur une valeur moyenne de conversion)
    avg_order_value = random.uniform(30, 150)
    revenue = conversions * avg_order_value
    
    return {
        'Impressions': impressions,
        'Reach': reach,
        'Clicks': clicks,
        'Engagement': engagement,
        'Conversions': conversions,
        'Revenue': round(revenue, 2)
    }

# Créer le dataset
data = []

for i in range(n_campaigns):
    # Générer Campaign ID
    campaign_id = f"CMP{str(i+1).zfill(4)}"
    
    # Sélectionner type et plateforme
    campaign_type = random.choice(campaign_types)
    platform = random.choice(platforms)
    
    # Générer nom de campagne
    template = random.choice(campaign_templates[campaign_type])
    campaign_name = template.format(random.randint(1, 10))
    
    # Générer dates
    days_ago = random.randint(0, 180)
    campaign_start = (end_date - timedelta(days=days_ago)).date()
    duration = random.randint(7, 30)  # Campagnes de 7 à 30 jours
    campaign_end = (campaign_start + timedelta(days=duration))
    
    # Générer budget (distribution réaliste)
    if random.random() < 0.6:  # 60% petits budgets
        budget = round(random.uniform(500, 2000), 2)
    elif random.random() < 0.9:  # 30% budgets moyens
        budget = round(random.uniform(2000, 5000), 2)
    else:  # 10% gros budgets
        budget = round(random.uniform(5000, 15000), 2)
    
    # Générer les métriques
    metrics = generate_campaign_metrics(campaign_type, platform, budget)
    
    # Ajouter l'enregistrement
    data.append({
        'Campaign ID': campaign_id,
        'Campaign Name': campaign_name,
        'Platform': platform,
        'Campaign Type': campaign_type,
        'Start Date': campaign_start,
        'End Date': campaign_end,
        'Budget': budget,
        'Impressions': metrics['Impressions'],
        'Reach': metrics['Reach'],
        'Clicks': metrics['Clicks'],
        'Engagement': metrics['Engagement'],
        'Conversions': metrics['Conversions'],
        'Revenue': metrics['Revenue']
    })

# Créer le DataFrame
df = pd.DataFrame(data)

# Calculer les métriques supplémentaires
df['Duration'] = (pd.to_datetime(df['End Date']) - pd.to_datetime(df['Start Date'])).dt.days
df['CTR'] = (df['Clicks'] / df['Impressions'] * 100).round(3)
df['Engagement Rate'] = (df['Engagement'] / df['Reach'] * 100).round(3)
df['Conversion Rate'] = (df['Conversions'] / df['Clicks'] * 100).round(3)
df['CPC'] = (df['Budget'] / df['Clicks']).round(3)
df['CPM'] = (df['Budget'] / df['Impressions'] * 1000).round(3)
df['Cost Per Conversion'] = (df['Budget'] / df['Conversions']).round(3)
df['ROAS'] = (df['Revenue'] / df['Budget']).round(3)
df['ROI'] = ((df['Revenue'] - df['Budget']) / df['Budget'] * 100).round(2)
df['Frequency'] = (df['Impressions'] / df['Reach']).round(2)

# Gérer les valeurs infinies (division par zéro)
df = df.replace([np.inf, -np.inf], 0)

# Sauvegarder le dataset
output_path = '../data/campaign_data.csv'
df.to_csv(output_path, index=False)

print("✅ Dataset de campagnes publicitaires généré avec succès!")
print(f"📊 Nombre de campagnes: {len(df)}")
print(f"📁 Fichier sauvegardé: {output_path}")

print(f"\n📋 Aperçu des données:")
print(df.head(10))

print(f"\n📊 STATISTIQUES GLOBALES")
print("="*70)
print(f"💰 Budget Total: ${df['Budget'].sum():,.2f}")
print(f"💵 Revenu Total: ${df['Revenue'].sum():,.2f}")
print(f"📈 ROI Moyen: {df['ROI'].mean():.2f}%")
print(f"🎯 CTR Moyen: {df['CTR'].mean():.3f}%")
print(f"🔄 Taux de Conversion Moyen: {df['Conversion Rate'].mean():.3f}%")
print(f"👁️  Impressions Totales: {df['Impressions'].sum():,}")
print(f"👥 Reach Total: {df['Reach'].sum():,}")
print(f"🖱️  Clicks Totaux: {df['Clicks'].sum():,}")
print(f"🎉 Conversions Totales: {df['Conversions'].sum():,}")

print(f"\n📊 RÉPARTITION")
print("="*70)
print("\n🔷 Par Plateforme:")
print(df.groupby('Platform').agg({
    'Budget': 'sum',
    'Revenue': 'sum',
    'ROI': 'mean'
}).round(2))

print("\n🔶 Par Type de Campagne:")
print(df.groupby('Campaign Type').agg({
    'Budget': 'sum',
    'Revenue': 'sum',
    'ROI': 'mean',
    'CTR': 'mean'
}).round(2))

print("\n🏆 TOP 5 CAMPAGNES PAR ROI:")
top_campaigns = df.nlargest(5, 'ROI')[['Campaign Name', 'Platform', 'Campaign Type', 'Budget', 'Revenue', 'ROI']]
print(top_campaigns)

print("\n⚠️  BOTTOM 5 CAMPAGNES PAR ROI:")
bottom_campaigns = df.nsmallest(5, 'ROI')[['Campaign Name', 'Platform', 'Campaign Type', 'Budget', 'Revenue', 'ROI']]
print(bottom_campaigns)

# Créer un fichier d'information
info_text = f"""
# Dataset Information - Social Media Campaign Performance

## Overview
- **Total Campaigns**: {len(df)}
- **Date Range**: {df['Start Date'].min()} to {df['End Date'].max()}
- **Platforms**: {df['Platform'].nunique()} (Facebook, Instagram)
- **Campaign Types**: {df['Campaign Type'].nunique()} (Awareness, Engagement, Conversion)

## Financial Metrics
- **Total Budget**: ${df['Budget'].sum():,.2f}
- **Total Revenue**: ${df['Revenue'].sum():,.2f}
- **Overall ROI**: {((df['Revenue'].sum() - df['Budget'].sum()) / df['Budget'].sum() * 100):.2f}%
- **Average ROAS**: {df['ROAS'].mean():.2f}

## Performance Metrics
- **Average CTR**: {df['CTR'].mean():.3f}%
- **Average Conversion Rate**: {df['Conversion Rate'].mean():.3f}%
- **Average CPC**: ${df['CPC'].mean():.2f}
- **Average CPM**: ${df['CPM'].mean():.2f}
- **Total Impressions**: {df['Impressions'].sum():,}
- **Total Conversions**: {df['Conversions'].sum():,}

## Columns Description
1. **Campaign ID**: Unique identifier
2. **Campaign Name**: Name of the campaign
3. **Platform**: Facebook or Instagram
4. **Campaign Type**: Awareness, Engagement, or Conversion
5. **Start Date**: Campaign start date
6. **End Date**: Campaign end date
7. **Budget**: Total budget allocated ($)
8. **Impressions**: Number of times ad was displayed
9. **Reach**: Number of unique users reached
10. **Clicks**: Number of clicks on ad
11. **Engagement**: Total interactions (likes, comments, shares)
12. **Conversions**: Number of conversions/purchases
13. **Revenue**: Total revenue generated ($)
14. **CTR**: Click-Through Rate (%)
15. **Engagement Rate**: Percentage of reach that engaged
16. **Conversion Rate**: Percentage of clicks that converted
17. **CPC**: Cost Per Click ($)
18. **CPM**: Cost Per Mille/1000 Impressions ($)
19. **Cost Per Conversion**: Average cost to get one conversion ($)
20. **ROAS**: Return on Ad Spend (Revenue/Budget)
21. **ROI**: Return on Investment (%)

## Usage
Perfect for:
- Marketing analytics practice
- ROI optimization
- Campaign performance comparison
- A/B testing analysis
- Budget allocation strategies
"""

with open('../data/campaign_dataset_info.txt', 'w') as f:
    f.write(info_text)

print("\n📄 Informations du dataset sauvegardées: ../data/campaign_dataset_info.txt")
print("\n🎉 PROCESSUS TERMINÉ!")
