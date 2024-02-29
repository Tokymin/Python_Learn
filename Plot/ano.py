import matplotlib.pyplot as plt
import pandas as pd

# Recreating the DataFrame after reset
data = {
    'Model': ['CIAGAN', 'DeepPrivacy', 'FALCO', 'Ours'],
    'Inner face': [0.7277, 0.7658, 0.7817, 0.7923],
    'Outer face': [0.8372, 0.8511, 0.8518, 0.8523],
    'Combined': [0.7852, 0.8135, 0.8181, 0.8197]
}
color = ['b', 'g', 'y', 'r']
df = pd.DataFrame(data)

# Adjusting the DataFrame for the new structure
# Transposing the DataFrame to have models as columns and metrics as rows
df_transposed = df.set_index('Model').T

# Plotting the new bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Set position of bar on X axis
models = df_transposed.columns
barWidth = 0.2
positions = range(len(df_transposed))

# Create bars for each model in each metric
for i, model in enumerate(models):
    ax.bar([p + barWidth * i for p in positions], df_transposed[model], width=barWidth, label=model, color=color[i])

# Add xticks on the middle of the group bars
ax.set_xlabel('Metrics', fontweight='bold')
ax.set_xticks([r + barWidth * (len(models) - 1) / 2 for r in positions])
ax.set_xticklabels(df_transposed.index)
ax.set_ylabel('Scores')
ax.set_title('Model Comparison Across Different Metrics')

# Create legend & Show graphic
ax.legend()

# Save the figure
plt.savefig('model_comparison_bar_chart_adjusted.png')
plt.show()
